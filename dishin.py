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

import ssmpy
import sys

sb_file = sys.argv[1]

# Create a new semantic base
if len(sys.argv) == 6 and not (sb_file.endswith(".db")):

    db_file = sys.argv[2]
    name_prefix = sys.argv[3]
    relation = sys.argv[4]
    annotation_file = sys.argv[5]

    ssmpy.create_semantic_base(sb_file, db_file, name_prefix, relation, annotation_file)

# Calculate the similarity

elif len(sys.argv) == 4 and sb_file.endswith(".db"):

    ssmpy.semantic_base(sb_file)

    name1 = sys.argv[2]
    name2 = sys.argv[3]

    # Similarity between proteins
    if sb_file.endswith("go.db") and not (name1.startswith("GO")):
        import annotations

        e1 = ssmpy.get_uniprot_annotations(name1)
        e2 = ssmpy.get_uniprot_annotations(name2)

        ssmpy.intrinsic = True

        ssmpy.mica = False
        print(
            "Resnik \t DiShIn \t intrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_resnik, e1, e2))
        )
        ssmpy.mica = True
        print(
            "Resnik \t MICA \t intrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_resnik, e1, e2))
        )
        ssmpy.mica = False
        print(
            "Lin \t DiShIn \t intrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_lin, e1, e2))
        )
        ssmpy.mica = True
        print(
            "Lin \t MICA \t intrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_lin, e1, e2))
        )
        ssmpy.mica = False
        print(
            "JC \t DiShIn \t intrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_jiang_conrath, e1, e2))
        )
        ssmpy.mica = True
        print(
            "JC \t MICA \t intrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_jiang_conrath, e1, e2))
        )

        ssmpy.intrinsic = False

        ssmpy.mica = False
        print(
            "Resnik \t DiShIn \t extrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_resnik, e1, e2))
        )
        ssmpy.mica = True
        print(
            "Resnik \t MICA \t extrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_resnik, e1, e2))
        )
        ssmpy.mica = False
        print(
            "Lin \t DiShIn \t extrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_lin, e1, e2))
        )
        ssmpy.mica = True
        print(
            "Lin \t MICA \t extrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_lin, e1, e2))
        )
        ssmpy.mica = False
        print(
            "JC \t DiShIn \t extrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_jiang_conrath, e1, e2))
        )
        ssmpy.mica = True
        print(
            "JC \t MICA \t extrinsic \t"
            + str(ssmpy.ssm_multiple(ssmpy.ssm_jiang_conrath, e1, e2))
        )

    else:
        # Similarity between terms

        e1 = ssmpy.get_id(name1)
        e2 = ssmpy.get_id(name2)

        if e1 > 0 and e2 > 0:
            ssmpy.intrinsic = True

            # ontology with multiple inheritance
            if not (sb_file.endswith("wordnet.db") or sb_file.endswith("radlex.db")):
                ssmpy.mica = False
                print(
                    "Resnik \t DiShIn \t intrinsic \t" + str(ssmpy.ssm_resnik(e1, e2))
                )

            ssmpy.mica = True
            print("Resnik \t MICA \t intrinsic \t" + str(ssmpy.ssm_resnik(e1, e2)))

            if not (sb_file.endswith("wordnet.db") or sb_file.endswith("radlex.db")):
                ssmpy.mica = False
                print("Lin \t DiShIn \t intrinsic \t" + str(ssmpy.ssm_lin(e1, e2)))

            ssmpy.mica = True
            print("Lin \t MICA \t intrinsic \t" + str(ssmpy.ssm_lin(e1, e2)))

            if not (sb_file.endswith("wordnet.db") or sb_file.endswith("radlex.db")):
                ssmpy.mica = False
                print(
                    "JC \t DiShIn \t intrinsic \t"
                    + str(ssmpy.ssm_jiang_conrath(e1, e2))
                )

            ssmpy.mica = True
            print("JC \t MICA \t intrinsic \t" + str(ssmpy.ssm_jiang_conrath(e1, e2)))

            if sb_file.endswith("go.db") or sb_file.endswith("metals.db"):

                ssmpy.intrinsic = False
                ssmpy.mica = False
                print(
                    "Resnik \t DiShIn \t extrinsic \t" + str(ssmpy.ssm_resnik(e1, e2))
                )
                ssmpy.mica = True
                print("Resnik \t MICA \t extrinsic \t" + str(ssmpy.ssm_resnik(e1, e2)))
                ssmpy.mica = False
                print("Lin \t DiShIn \t extrinsic \t" + str(ssmpy.ssm_lin(e1, e2)))
                ssmpy.mica = True
                print("Lin \t MICA \t extrinsic \t" + str(ssmpy.ssm_lin(e1, e2)))
                ssmpy.mica = False
                print(
                    "JC \t DiShIn \t extrinsic \t"
                    + str(ssmpy.ssm_jiang_conrath(e1, e2))
                )
                ssmpy.mica = True
                print(
                    "JC \t MICA \t extrinsic \t" + str(ssmpy.ssm_jiang_conrath(e1, e2))
                )

        else:

            print("Error: entry unknown")

else:

    print("ERROR: wrong parameters")
    print("Usage:   python dishin.py <semanticbase>.db <term1> <term2>")
    print("Example: python dishin.py metals.db gold copper")
    print(
        "Usage:   python dishin.py <semanticbase>.[owl|rdf] <semanticbase>.db <name_prefix> <relation> <annotation_file>"
    )
    print(
        "Example: python dishin.py metals.owl metals.db https://raw.githubusercontent.com/lasigeBioTM/ssm/master/metals.owl# http://www.w3.org/2000/01/rdf-schema#subClassOf metals.txt"
    )
