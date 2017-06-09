import rdflib
import sqlite3

def create (owl_file, sb_file, name_prefix):
	connection = sqlite3.connect(sb_file)
	
	connection.isolation_level = None #auto_commit
	
	
	connection.execute('''
		  DROP TABLE IF EXISTS relation
		  ''')

	connection.execute('''
		  CREATE TABLE relation (
		  id	 INTEGER PRIMARY KEY AUTOINCREMENT,
		  entry1		 INTEGER,
		  entry2		  INTEGER,
		  UNIQUE (entry1,entry2)
		  )''')
	  
	connection.execute('CREATE INDEX r1 ON relation(entry1);')
	
	connection.execute('''
		  DROP TABLE IF EXISTS entry
		  ''')

	connection.execute('''
			CREATE TABLE entry (
			id	 INTEGER PRIMARY KEY AUTOINCREMENT,
			name  VARCHAR(255) UNIQUE,
			refs  INTEGER,
			freq  INTEGER
			)''')

				
	g=rdflib.Graph()
	g.load(owl_file)

	for s,p,o in g:
		if str(p) == 'http://www.w3.org/2000/01/rdf-schema#subClassOf':
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
	id	 INTEGER PRIMARY KEY AUTOINCREMENT,
	entry1 INTEGER,
	entry2 INTEGER,
	distance INTEGER	
	)
	''')

	connection.execute('CREATE INDEX t1 ON transitive(entry1,entry2);')
	connection.execute('CREATE INDEX t2 ON transitive(entry2,distance);')
	
	connection.execute('''
	INSERT INTO transitive (entry1, entry2, distance)
	  SELECT id, id, 0 FROM entry
	''')


	connection.execute('''
	INSERT INTO transitive (entry1, entry2, distance)
	  SELECT entry1, entry2, 1 FROM relation
	''')

	n_entries = 0
	rows=connection.execute('''SELECT * FROM entry''')
	for row in rows:
		n_entries = row[0]

	for i in range(1,n_entries):	
	  connection.execute('''
		 INSERT INTO transitive (entry1, entry2, distance)
			SELECT tc.entry1, r.entry2, tc.distance + 1
			FROM relation AS r,
				transitive AS tc
			WHERE r.entry1 = tc.entry2 AND tc.distance=?
	  ''',(i,))
	  #print i
	  
	# Calculate the frequency of each entry based on the number of references

	connection.execute('''
	  UPDATE entry SET refs = 1;
	''')

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
   
