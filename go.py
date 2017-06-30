import sqlite3
import math
import ssm
import semanticbase

#semanticbase.create('go.owl', 'go.db', 'http://purl.obolibrary.org/obo/')

ssm.semantic_base('go.db')

t1 = ssm.get_id('GO_0000024') # maltose biosynthetic process
t2 = ssm.get_id('GO_0000025') # maltose catabolic process

print ('The id of t1 is ' + str(t1))
print ('The id of t2 is ' + str(t2))

ssm.intrinsic = True

ssm.mica = False

print ('resnik dishin intrinsic similarity = ' + str(ssm.ssm_resnik (t1,t2)))

ssm.mica = True

print ('resnink mica intrinsic similarity = ' + str(ssm.ssm_resnik (t1,t2)))

print ('lin mica intrinsic similarity = ' + str(ssm.ssm_lin (t1,t2)))

