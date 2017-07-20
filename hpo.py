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

import ssm
import semanticbase

semanticbase.create('hp.owl', 'hpo.db', 'http://purl.obolibrary.org/obo/', 'http://www.w3.org/2000/01/rdf-schema#subClassOf', '')

ssm.semantic_base('hpo.db')

e1 = ssm.get_id('HP_0000588') # Optic nerve coloboma
e2 = ssm.get_id('HP_0001093') # Optic nerve dysplasia

print ('The id of Optic nerve coloboma is ' + str(e1))
print ('The id of Optic nerve dysplasia is ' + str(e2))

ssm.intrinsic = True

ssm.mica = False

print ('resnik dishin intrinsic similarity = ' + str(ssm.ssm_resnik (e1,e2)))

ssm.mica = True

print ('resnik mica intrinsic similarity = ' + str(ssm.ssm_resnik (e1,e2)))

print ('lin mica intrinsic similarity = ' + str(ssm.ssm_lin (e1,e2)))


