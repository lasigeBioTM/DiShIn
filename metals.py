import sqlite3
import math
import ssm
import semanticbase

semanticbase.create('metals.owl', 'metals.db', 'https://raw.githubusercontent.com/lasigeBioTM/ssm/master/metals.owl#', 'http://www.w3.org/2000/01/rdf-schema#subClassOf','metals.txt')

ssm.semantic_base('metals.db')

ssm.intrinsic = False

ssm.mica = False

platinum = ssm.get_id('platinum')

gold = ssm.get_id('gold')

silver = ssm.get_id('silver')

copper = ssm.get_id('copper')

palladium = ssm.get_id('palladium')

print ('resnik dishin extrinsic similarity platinum gold = ' + str(ssm.ssm_resnik (platinum, gold)))
print ('                            mathematical formula = ' + str((-math.log(6.0/9.0)-math.log(9.0/9.0))/2))

ssm.mica = True

print ('  resnik mica extrinsic similarity platinum gold = ' + str(ssm.ssm_resnik (platinum, gold)))
print ('                            mathematical formula = ' + str(-math.log(6.0/9.0)))

print ('     lin mica extrinsic similarity platinum gold = ' + str(ssm.ssm_lin (platinum, gold)))
print ('                            mathematical formula = ' + str((2*-math.log(6.0/9.0))/(-math.log(2.0/9.0)-math.log(2.0/9.0))))


print ('resnik **mica** extrinsic similarity:')
print ('   platinum copper    = ' + str(ssm.ssm_resnik (platinum, copper)))
print ('   platinum gold      = ' + str(ssm.ssm_resnik (platinum, gold)))
print ('   copper gold        = ' + str(ssm.ssm_resnik (copper, gold)))
print ('   platinum palladium = ' + str(ssm.ssm_resnik (platinum, palladium)))
print ('   silver gold        = ' + str(ssm.ssm_resnik (silver, gold)))

ssm.mica = False
print ('resnik **dishin** extrinsic similarity:')
print ('   platinum copper    = ' + str(ssm.ssm_resnik (platinum, copper)))
print ('   platinum gold      = ' + str(ssm.ssm_resnik (platinum, gold)))
print ('   copper gold        = ' + str(ssm.ssm_resnik (copper, gold)))
print ('   platinum palladium = ' + str(ssm.ssm_resnik (platinum, palladium)))
print ('   silver gold        = ' + str(ssm.ssm_resnik (silver, gold)))
