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
# - F. Couto and A. Lamurias, "Semantic similarity definition," in Reference  #
#   Module in Life Sciences (Encyclopedia of Bioinformatics and Computational #
#   Biology), pp. 1--17, Elsevier, 2018                                       #
#   https://doi.org/10.1016/B978-0-12-809633-8.20401-9,                       #
#   https://www.researchgate.net/publication/323219905                        #
#                                                                             #
# @author Francisco M. Couto                                                  #
###############################################################################

import ssm
import sys

sb_file = sys.argv[1]
        
# Create a new semantic base
if  len(sys.argv) == 6 and not(sb_file.endswith('.db')):
        import semanticbase

        db_file = sys.argv[2]
        name_prefix = sys.argv[3]
        relation = sys.argv[4]
        annotation_file = sys.argv[5]
        
        semanticbase.create(sb_file, db_file, name_prefix, relation, annotation_file)

# Calculate the similarity 

elif  len(sys.argv) == 4 and sb_file.endswith('.db'):
                
        ssm.semantic_base(sb_file)


        name1 = sys.argv[2]
        name2 = sys.argv[3]
                
        # Similarity between proteins
        if sb_file == 'geneontology.db' and not(name1.startswith('GO')) :
                import annotations
                
                e1 = annotations.get_uniprot_annotations(name1)
                e2 = annotations.get_uniprot_annotations(name2)
                
                ssm.intrinsic = True

                ssm.mica = False
                print("Resnik \t DiShIn \t intrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_resnik,e1,e2)))
                ssm.mica = True
                print("Resnik \t MICA \t intrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_resnik,e1,e2)))
                ssm.mica = False
                print("Lin \t DiShIn \t intrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_lin,e1,e2)))
                ssm.mica = True
                print("Lin \t MICA \t intrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_lin,e1,e2)))
                ssm.mica = False
                print("JC \t DiShIn \t intrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_jiang_conrath,e1,e2)))
                ssm.mica = True
                print("JC \t MICA \t intrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_jiang_conrath,e1,e2)))

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
                print("JC \t DiShIn \t extrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_jiang_conrath,e1,e2)))
                ssm.mica = True
                print("JC \t MICA \t extrinsic \t"+ str(ssm.ssm_multiple(ssm.ssm_jiang_conrath,e1,e2)))
                
        else :
        # Similarity between terms
                
                e1 = ssm.get_id(name1)
                e2 = ssm.get_id(name2)

                if e1>0 and e2>0:
                        ssm.intrinsic = True
                                
                        # ontology with multiple inheritance 
                        if sb_file != 'wordnet.db' and sb_file != 'radiology.db':
                                        
                                ssm.mica = False
                                print("Resnik \t DiShIn \t intrinsic \t"+ str(ssm.ssm_resnik (e1,e2)))
                                
                        ssm.mica = True
                        print("Resnik \t MICA \t intrinsic \t"+ str(ssm.ssm_resnik (e1,e2)))
                                
                        if sb_file != 'wordnet.db' and sb_file != 'radiology.db':
                                        
                                ssm.mica = False
                                print("Lin \t DiShIn \t intrinsic \t"+ str(ssm.ssm_lin (e1,e2)))
                
                        ssm.mica = True
                        print("Lin \t MICA \t intrinsic \t"+ str(ssm.ssm_lin (e1,e2)))

                        if sb_file != 'wordnet.db' and sb_file != 'radiology.db':
                                
                                ssm.mica = False
                                print("JC \t DiShIn \t intrinsic \t"+ str(ssm.ssm_jiang_conrath (e1,e2)))
                                        
                        ssm.mica = True
                        print("JC \t MICA \t intrinsic \t"+ str(ssm.ssm_jiang_conrath (e1,e2)))

                        if sb_file == 'geneontology.db' or sb_file == 'metals.db':
                                
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
                                print("JC \t DiShIn \t extrinsic \t"+ str(ssm.ssm_jiang_conrath (e1,e2)))
                                ssm.mica = True
                                print("JC \t MICA \t extrinsic \t"+ str(ssm.ssm_jiang_conrath (e1,e2)))
                                
                else:

                        print ('Error: entry unknown')
                        
else:
        
        print ('ERROR: wrong parameters')
        print ('Usage:   python dishin.py <semanticbase>.db <term1> <term2>')
        print ('Example: python dishin.py metals.db gold copper')
        print ('Usage:   python dishin.py <semanticbase>.[owl|rdf] <semanticbase>.db <name_prefix> <relation> <annotation_file>')
        print ('Example: python dishin.py metals.owl metals.db https://raw.githubusercontent.com/lasigeBioTM/ssm/master/metals.owl# http://www.w3.org/2000/01/rdf-schema#subClassOf metals.txt')
