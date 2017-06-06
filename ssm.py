import sqlite3
import math

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
    #return information_content_intrinsic (entry)
    return information_content_extrinsic (entry)

def shared_ic_mica (entry1, entry2):

    ic = 0 

    ancestors = common_ancestors(entry1, entry2)

    for anc in ancestors:
        ic = max(information_content(anc),ic)

    return ic

def shared_ic (entry1, entry2):
    #return shared_ic_dca (entry1, entry2)
    return shared_ic_mica (entry1, entry2)

def ssm_resnik (entry1, entry2):

    return shared_ic(entry1, entry2)

def ssm_lin (entry1, entry2):

    return 2*shared_ic(entry1, entry2) / (information_content(entry1) + information_content(entry2))


print ssm_resnik (6, 7)

print ssm_lin (6, 7)



