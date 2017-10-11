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

ssm.semantic_base('go.db')

proteins = ['Q12345', 'Q12346', 'Q12347']

prot_entries = {}
for p in proteins :
 prot_entries[p]=semanticbase.get_uniprot_annotations(p)

for p1 in proteins :
	for p2 in proteins[proteins.index(p1)+1:] :
		e1 = prot_entries[p1]
		e2 = prot_entries[p2]
		print ('Similarity between '+ p1 + ' and ' + p2)
		
		ssm.intrinsic = True
		ssm.mica = False
		print ('resnik dishin intrinsic similarity = ' + str(ssm.ssm_multiple(ssm.ssm_resnik,e1,e2)))

		ssm.mica = True

		print ('resnik mica intrinsic similarity = ' + str(ssm.ssm_multiple(ssm.ssm_resnik,e1,e2)))

		print ('lin mica intrinsic similarity = ' + str(ssm.ssm_multiple(ssm.ssm_lin,e1,e2)))

		ssm.intrinsic = False

		ssm.mica = False

		print ('resnik dishin extrinsic similarity = ' + str(ssm.ssm_multiple(ssm.ssm_resnik,e1,e2)))


		ssm.mica = True

		print ('resnik mica extrinsic similarity = ' + str(ssm.ssm_multiple(ssm.ssm_resnik,e1,e2)))

		print ('lin mica extrinsic similarity = ' + str(ssm.ssm_multiple(ssm.ssm_lin,e1,e2)))

