import sqlite3
import math

intrinsic = False
mica = False

connection = sqlite3.connect('semanticbase.db')

def descendents (entry):

    descendents = []
    
    rows = connection.execute('''
        SELECT DISTINCT t.entry1
        FROM transitive t
        WHERE t.entry2=? 
        ''', (entry, ))

    for row in rows:
       descendents.append(row[0])

    return descendents

def get_id (name):

    iden = 0
    
    rows = connection.execute('''
        SELECT id
        FROM entry
        WHERE name = ?
    ''', (name,))

    for row in rows:
       iden = row[0]

    return iden

def num_entries ():

    num = 0
    
    rows = connection.execute('''
        SELECT id
        FROM entry
    ''')

    for row in rows:
       num = row[0]

    return num

def common_ancestors (entry1, entry2):

    ancestors = []
    
    rows = connection.execute('''
        SELECT DISTINCT t1.entry2
        FROM transitive t1, transitive t2
        WHERE t1.entry1=? AND t2.entry1=? AND t1.entry2=t2.entry2
        ''', (entry1, entry2, ))

    for row in rows:
       ancestors.append(row[0])

    return ancestors


def information_content_extrinsic (entry):

    rows = connection.execute('''
        SELECT e.freq
        FROM entry e
        WHERE e.id = ?
        ''', (entry,))
    for row in rows:
        freq = row[0] + 1.0 
    
    rows = connection.execute('''
        SELECT MAX(e.freq)
        FROM entry e
        ''')
    for row in rows:
        maxfreq = row[0] + 1.0 

    return -math.log(freq/maxfreq)

def information_content_intrinsic (entry):

    freq = len(descendents(entry)) + 1.0

    maxfreq = num_entries ()

    return -math.log(freq/maxfreq)

def information_content (entry):
    if intrinsic:
        return information_content_intrinsic (entry)
    else: 
        return information_content_extrinsic (entry)

def num_paths (entry1, ancestor):
    
    rows = connection.execute('''
        SELECT npaths
        FROM num_paths p
        WHERE p.entry1=? AND p.entry2=? 
        ''', (entry1, ancestor, ))

    for row in rows:
        npaths = row[0] + 1.0 

    return npaths

def shared_ic_dca (entry1, entry2):

    ancestors = common_ancestors(entry1, entry2)
    dca = {}

    for anc in ancestors:        
        pd = abs(num_paths(entry1, anc) - num_paths(entry2, anc))
        ic = information_content(anc)
        dca[pd] = max(information_content(anc),dca.get(pd,0));
        
    values = dca.values()

    return (float(sum(values)) / float(len(values)))
    
def shared_ic_mica (entry1, entry2):

    ic = 0 

    ancestors = common_ancestors(entry1, entry2)

    for anc in ancestors:
        ic = max(information_content(anc),ic)

    return ic


def shared_ic (entry1, entry2):
    if mica:
        return shared_ic_mica (entry1, entry2)
    else:
        return shared_ic_dca (entry1, entry2)

def ssm_resnik (entry1, entry2):

    return shared_ic(entry1, entry2)

def ssm_lin (entry1, entry2):

    return 2*shared_ic(entry1, entry2) / (information_content(entry1) + information_content(entry2))

#################################
# Examples
#################################

intrinsic = False

mica = False

print ssm_resnik (get_id('palatium'), get_id('gold'))

print (-math.log(6.0/9.0)-math.log(9.0/9.0))/2

mica = True

print ssm_resnik (get_id('palatium'), get_id('gold'))

print -math.log(6.0/9.0)

print ssm_lin (get_id('palatium'), get_id('gold'))

print (2*-math.log(6.0/9.0))/(-math.log(2.0/9.0)-math.log(2.0/9.0))
