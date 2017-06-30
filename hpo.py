import sqlite3
import math
import ssm
import semanticbase

#semanticbase.create('hpo.owl', 'hpo.db', 'http://purl.obolibrary.org/obo/')

ssm.semantic_base('hpo.db')


t1 = ssm.get_id('HP_0000588') # Optic nerve coloboma
t2 = ssm.get_id('HP_0001093') # Optic nerve dysplasia

print ('The id of t1 is ' + str(t1))
print ('The id of t2 is ' + str(t2))

ssm.intrinsic = True

ssm.mica = False

print ('resnik dishin intrinsic similarity = ' + str(ssm.ssm_resnik (t1,t2)))

ssm.mica = True

print ('resnink mica intrinsic similarity = ' + str(ssm.ssm_resnik (t1,t2)))

print ('lin mica intrinsic similarity = ' + str(ssm.ssm_lin (t1,t2)))


