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

import ssm
import semanticbase
import sys

if  len(sys.argv) == 4:

	semantic_base = sys.argv[1]

	ssm.semantic_base(semantic_base)

	name1 = sys.argv[2]
	name2 = sys.argv[3]

	if semantic_base == 'go.db' and not(name1.startswith('GO')) :
	
		e1 = semanticbase.get_uniprot_annotations(name1)
		e2 = semanticbase.get_uniprot_annotations(name2)

		ssm.intrinsic = False

		ssm.mica = False

		print("Resnik \t DiShIn \t extrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_resnik,e1,e2)))

		ssm.mica = True

		print("Resnik \t MICA \t extrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_resnik,e1,e2)))

		ssm.mica = False

		print("Lin \t DiShIn \t extrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_lin,e1,e2)))

		ssm.mica = True

		print("Lin \t MICA \t extrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_lin,e1,e2)))

		ssm.mica = False

		print("Jiang&Conrath \t DiShIn \t extrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_jiang_conrath,e1,e2)))

		ssm.mica = True

		print("Jiang&Conrath \t MICA \t extrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_jiang_conrath,e1,e2)))
	
	else:
	
		e1 = ssm.get_id(name1)
		e2 = ssm.get_id(name2)

		if e1>0 and e2>0:
			ssm.intrinsic = True

			if semantic_base != 'wordnet.db' :
			
				ssm.mica = False

				print("Resnik \t DiShIn \t intrinsic \t"+ str(ssm.ssm_resnik (e1,e2)))

			ssm.mica = True

			print("Resnik \t MICA \t intrinsic \t"+ str(ssm.ssm_resnik (e1,e2)))
			
			if semantic_base != 'wordnet.db' :
			
				ssm.mica = False

				print("Lin \t DiShIn \t intrinsic \t"+ str(ssm.ssm_lin (e1,e2)))

			ssm.mica = True

			print("Lin \t MICA \t intrinsic \t"+ str(ssm.ssm_lin (e1,e2)))

			if semantic_base != 'wordnet.db' :
				
				ssm.mica = False

				print("Jiang&Conrath \t DiShIn \t intrinsic \t"+ str(ssm.ssm_jiang_conrath (e1,e2)))

			ssm.mica = True

			print("Jiang&Conrath \t MICA \t intrinsic \t"+ str(ssm.ssm_jiang_conrath (e1,e2)))

			if semantic_base == 'go.db' :
				
				ssm.intrinsic = False

				ssm.mica = False

				print("Resnik \t DiShIn \t extrinsic \t"+ str(ssm.ssm_resnik (e1,e2)))

				ssm.mica = True

				print("Resnik \t MICA \t extrinsic \t"+ str(ssm.ssm_resnik (e1,e2)))

				ssm.mica = False

				print("Lin \t DiShIn \t extrinsic \t"+ str(ssm.ssm_lin (e1,e2)))

				ssm.mica = True

				print("Lin \t MICA \t extrinsic \t"+ str(ssm.ssm_lin (e1,e2)))

				ssm.mica = False

				print("Jiang&Conrath \t DiShIn \t extrinsic \t"+ str(ssm.ssm_jiang_conrath (e1,e2)))

				ssm.mica = True

				print("Jiang&Conrath \t MICA \t extrinsic \t"+ str(ssm.ssm_jiang_conrath (e1,e2)))
				
		else:

			print ('Error: entry unknown')
			
		   
else:

	print ('Sorry, wrong parameters')
   


