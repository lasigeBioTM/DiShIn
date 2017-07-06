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

print ('       resnik mica extrinsic similarity platinum gold = ' + str(ssm.ssm_resnik (platinum, gold)))
print ('                                 mathematical formula = ' + str(-math.log(6.0/9.0)))

print ('          lin mica extrinsic similarity platinum gold = ' + str(ssm.ssm_lin (platinum, gold)))
print ('                                 mathematical formula = ' + str((2*-math.log(6.0/9.0))/(-math.log(2.0/9.0)-math.log(2.0/9.0))))

print ('jiang-conrath mica extrinsic similarity platinum gold = ' + str(ssm.ssm_jiang_conrath (platinum, gold)))
print ('                                 mathematical formula = ' + str(1 / ( -math.log(2.0/9.0) -math.log(2.0/9.0) - 2*-math.log(6.0/9.0)) ))

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
