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
# - F. Couto and M. Silva, Disjunctive shared information between ontology    #
#   concepts: application to Gene Ontology, Journal of Biomedical Semantics,  #
#   vol. 2, no. 5, pp. 1-16, 2011                                             #
#   http://dx.doi.org/10.1142/S0219720013710017                               #
# - F. Couto and H. Pinto, The next generation of similarity measures that    # 
#   fully explore the semantics in biomedical ontologies, Journal of          # 
#   Bioinformatics and Computational Biology, vol. 11, no. 1371001,           # 
#   pp. 1-12, 2013                                                            #
#   http://dx.doi.org/10.1186/2041-1480-2-5                                   #
#                                                                             #
# @author Francisco M. Couto                                                  #
###############################################################################

import rdflib
import sqlite3

def create (owl_file, sb_file, name_prefix, relation, annotation_file):
    connection = sqlite3.connect(sb_file)
    
    connection.isolation_level = None #auto_commit
    
    
    connection.execute('''
          DROP TABLE IF EXISTS relation
          ''')

    connection.execute('''
          CREATE TABLE relation (
          id     INTEGER PRIMARY KEY AUTOINCREMENT,
          entry1         INTEGER,
          entry2          INTEGER,
          UNIQUE (entry1,entry2)
          )''')
      
    connection.execute('CREATE INDEX r1 ON relation(entry1);')
    
    connection.execute('''
          DROP TABLE IF EXISTS entry
          ''')

    connection.execute('''
            CREATE TABLE entry (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name  VARCHAR(255) UNIQUE,
            refs  INTEGER,
            freq  INTEGER,
            desc  INTEGER
            )''')

                
    g=rdflib.Graph()
    g.load(owl_file)

    for s,p,o in g:
        if str(p) == relation : 
            s = str(s)
            o = str(o)
            if len(s)>len(name_prefix) and len(o)>len(name_prefix):
                 s = s[len(name_prefix):]
                 o = o[len(name_prefix):]
                 #print (s,p,o)
                 connection.execute('''  
                    INSERT OR IGNORE INTO entry (name) VALUES (?)
                 ''', (s,))
                 rows = connection.execute('SELECT id FROM entry WHERE name = ?', (s,))
                 for row in rows:
                    entry1 = row[0]
                 rows = connection.execute('''  
                    INSERT OR IGNORE INTO entry (name) VALUES (?)
                 ''', (o,))
                 rows = connection.execute('SELECT id FROM entry WHERE name = ?', (o,))
                 for row in rows:
                    entry2 = row[0]
                 #print (str(entry1) + ":" + str(entry2))
                 rows = connection.execute('''  
                    INSERT OR IGNORE INTO relation (entry1,entry2) VALUES (?,?)
                 ''', (entry1,entry2,))
                 connection.commit()

    connection.execute('''
         DROP TABLE IF EXISTS transitive;
    ''')

    connection.execute('''
    CREATE TABLE transitive (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    entry1 INTEGER,
    entry2 INTEGER,
    distance INTEGER    
    )
    ''')

    connection.execute('CREATE INDEX t2 ON transitive(entry2,distance);')

    connection.execute('CREATE INDEX tt ON transitive(entry1,entry2);')
    
    connection.execute('''
    INSERT INTO transitive (entry1, entry2, distance)
      SELECT id, id, 0 FROM entry
    ''')


    connection.execute('''
    INSERT INTO transitive (entry1, entry2, distance)
      SELECT entry1, entry2, 1 FROM relation
    ''')

    n_entries = 0
    previous_n_entries = -1
    i = 1
      
    while n_entries > previous_n_entries:   
      connection.execute('''
         INSERT INTO transitive (entry1, entry2, distance)
            SELECT tc.entry1, r.entry2, tc.distance + 1
            FROM relation AS r,
                transitive AS tc
            WHERE r.entry1 = tc.entry2 AND tc.distance=?
      ''',(i,))
      i = i + 1
      print ("distance " +  str(i))
      previous_n_entries = n_entries
      rows=connection.execute('''SELECT COUNT(*) FROM transitive''')
      for row in rows:
        n_entries = row[0]
      
    # Calculate the frequency of each entry based on the number of references
    if annotation_file != '' :
        file  = open(annotation_file, 'r').read()
        rows=connection.execute('''SELECT id, name FROM entry''')
        for row in rows:
            id = row[0]
            name = row[1]
            count = file.count(name.replace('_',':',1))
            # print(name + " - " + str(count))
            connection.execute('''UPDATE entry SET refs = ? WHERE id=?''',(count,id,))            
    else:
        connection.execute('''UPDATE entry SET refs = 1''')

    connection.commit()

    # Calculate the number of descendents 
    connection.execute('''UPDATE entry SET desc = 
                               (SELECT COUNT(DISTINCT t.entry1)
                                FROM transitive t
                                WHERE t.entry2=entry.id)''')
        
    connection.commit()

    connection.execute('''
      UPDATE entry SET freq =
      (SELECT SUM(e2.refs) 
      FROM entry e2
      WHERE e2.id IN
            (SELECT t.entry1
             FROM transitive t 
             WHERE entry.id=t.entry2))
    ''')

    connection.commit()
    connection.close()
   
