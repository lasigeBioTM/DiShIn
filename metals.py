import sqlite3
import math
import ssm
import semanticbase

semanticbase.create('metals.owl', 'metals.db', 'https://raw.githubusercontent.com/lasigeBioTM/ssm/master/metals.owl#')

ssm.semantic_base('metals.db')

ssm.intrinsic = False

ssm.mica = False

platinum = ssm.get_id('platinum')

gold = ssm.get_id('gold')

silver = ssm.get_id('silver')

copper = ssm.get_id('copper')

palladium = ssm.get_id('palladium')

print ssm.ssm_resnik (platinum, gold)

print (-math.log(6.0/9.0)-math.log(9.0/9.0))/2

ssm.mica = True

print ssm.ssm_resnik (platinum, gold)

print -math.log(6.0/9.0)

print ssm.ssm_lin (platinum, gold)

print (2*-math.log(6.0/9.0))/(-math.log(2.0/9.0)-math.log(2.0/9.0))

print ssm.ssm_resnik (platinum, copper)
print ssm.ssm_resnik (platinum, gold)
print ssm.ssm_resnik (copper, gold)
print ssm.ssm_resnik (platinum, palladium)
print ssm.ssm_resnik (silver, gold)

ssm.mica = False

print ssm.ssm_resnik (platinum, copper)
print ssm.ssm_resnik (platinum, gold)
print ssm.ssm_resnik (copper, gold)
print ssm.ssm_resnik (platinum, palladium)
print ssm.ssm_resnik (silver, gold)
