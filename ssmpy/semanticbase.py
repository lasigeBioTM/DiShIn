###############################################################################
#                                                                             #
# Licensed under the Apache License, Version 2.0 (the "License"); you may     #
# not use this file except in compliance with the License. You may obtain a   #
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0           #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS,           #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
# See the License for the specific language governing permissions and         #
# limitations under the License.                                              #
#                                                                             #
###############################################################################
#                                                                             #
# Software developed based on the work published in the following articles:   #
# - F. Couto and A. Lamurias, "Semantic similarity definition," in Reference  #
#   Module in Life Sciences (Encyclopedia of Bioinformatics and Computational #
#   Biology), pp. 1--17, Elsevier, 2018                                       #
#   https://doi.org/10.1016/B978-0-12-809633-8.20401-9,                       #
#   https://www.researchgate.net/publication/323219905                        #
#                                                                             #
# @author Francisco M. Couto                                                  #
###############################################################################

import rdflib
import sqlite3

memory_db = True

def open_db (sb_file):

    global connection
    
    if memory_db :
        connection = sqlite3.connect(':memory:')
        connection.execute('PRAGMA temp_store = 2') # temporary tables and indices kept in memory
    else:
        connection = sqlite3.connect(sb_file)
    connection.isolation_level = None #auto_commit
    

def close_db (sb_file):

    global connection

    if memory_db :
        script = ''.join(connection.iterdump())
        connection_disk = sqlite3.connect(sb_file)
        connection_disk.execute('DROP TABLE IF EXISTS relation')
        connection_disk.execute('DROP TABLE IF EXISTS entry')
        connection_disk.execute('DROP TABLE IF EXISTS transitive')
        connection_disk.executescript(script)
        connection_disk.commit()
        connection_disk.execute('''VACUUM''')
        connection_disk.close()
        connection.close()
    else:
        connection.execute('VACUUM')   
        connection.close()
        

def create (owl_file, sb_file, name_prefix, relation, annotation_file):

    global memory_db 
    # memory_db = not(sb_file.endswith('go.db') or sb_file.endswith('chebi.db'))     # gene ontology and chebi maybe too large to calculate the transitive closure in a memory database

    open_db(sb_file)
    
    connection.execute('DROP TABLE IF EXISTS relation')

    connection.execute('''
          CREATE TABLE relation (
          id     INTEGER PRIMARY KEY AUTOINCREMENT,
          entry1        INTEGER,
          entry2        INTEGER,
          UNIQUE (entry1,entry2)
          )''')
    
    connection.execute('DROP TABLE IF EXISTS entry')

    connection.execute('''
            CREATE TABLE entry (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name  VARCHAR(255) UNIQUE,
            refs  MEDIUMINT UNSIGNED,
            freq  MEDIUMINT UNSIGNED,
            desc  MEDIUMINT UNSIGNED
            )''')


    #loading the ontology
    print ("loading the ontology " + owl_file)
    g=rdflib.Graph()
    g.load(owl_file)

    for s,p,o in g:
        if str(p) == relation :
            s = str(s)
            o = str(o)
            if s.startswith(name_prefix) and o.startswith(name_prefix):
                 s = s[len(name_prefix):]
                 o = o[len(name_prefix):]
                 #print (s,p,o)
                 connection.execute('''  
                    INSERT OR IGNORE INTO entry (name) VALUES (?)
                 ''', (s,))
                 rows = connection.execute('SELECT id FROM entry WHERE name = ?', (s,))
                 entry1 = rows.fetchone()[0]
                 rows = connection.execute('''  
                    INSERT OR IGNORE INTO entry (name) VALUES (?)
                 ''', (o,))
                 rows = connection.execute('SELECT id FROM entry WHERE name = ?', (o,))
                 entry2 = rows.fetchone()[0]
                 #print (str(entry1) + ":" + str(entry2))
                 rows = connection.execute('''  
                    INSERT OR IGNORE INTO relation (entry1,entry2) VALUES (?,?)
                 ''', (entry1,entry2,))

    g.close()
    
    connection.execute('DROP TABLE IF EXISTS transitive')

    connection.execute('''
    CREATE TABLE transitive (
      id     INTEGER PRIMARY KEY AUTOINCREMENT,
      entry1 INTEGER,
      entry2 INTEGER,
      distance SMALLINT UNSIGNED
    )
    ''')


    connection.execute('CREATE INDEX re1 ON relation(entry1)')
    connection.execute('CREATE INDEX te2d ON transitive(entry2, distance)')
    
    connection.execute('''
    INSERT INTO transitive (entry1, entry2, distance)
      SELECT id, id, 0 FROM entry
    ''')
 
 
    connection.execute('''
    INSERT INTO transitive (entry1, entry2, distance)
      SELECT entry1, entry2, 1 FROM relation
    ''')
 
    changes = 1
    i = 1
       
    while changes > 0 and i < 255:
        print ("calculating transitive closure at distance: " +  str(i))
        rows = connection.execute('''
         INSERT INTO transitive (entry1, entry2, distance)
            SELECT tc.entry1, r.entry2, tc.distance + 1
            FROM relation AS r,
                transitive AS tc
            WHERE r.entry1 = tc.entry2 AND tc.distance=?
        ''',(i,))
        rows=connection.execute('''SELECT changes()''')
        changes = rows.fetchone()[0]      
        i = i + 1


    # Calculate the frequency of each entry based on the number of references
    if annotation_file != '' :
        print ("calculating the frequency from file " + annotation_file)
        file  = open(annotation_file, 'r').read()
        rows=connection.execute('''SELECT id, name FROM entry''')
        for row in rows:
            id = row[0]
            name = row[1]
            count = file.count(name.replace('_',':',1))
            #print("frequency of " + name + " - " + str(count))
            connection.execute('''UPDATE entry SET refs = ? WHERE id=?''',(count,id,))            
    else:
        connection.execute('''UPDATE entry SET refs = 1''')
    
    
    print ("calculating the descendents")
    # Calculate the number of descendents 
    connection.execute('''UPDATE entry SET desc = 
                               (SELECT COUNT(DISTINCT t.entry1)
                                FROM transitive t
                                WHERE t.entry2=entry.id)''')


    print ("calculating the hierarchical frequency")
    connection.execute('''
      UPDATE entry SET freq =
       (SELECT SUM(a.refs) 
        FROM entry a
        WHERE a.id IN
            (SELECT t.entry1
             FROM transitive t 
             WHERE entry.id=t.entry2))
    ''')

    connection.execute('CREATE INDEX te ON transitive(entry2,entry1)')

    print ("the end")
    close_db(sb_file)


