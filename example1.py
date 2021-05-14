#!/usr/bin/python3

import ssmpy

ssmpy.create_semantic_base("metals.owl", "metals.db", "https://raw.githubusercontent.com/lasigeBioTM/ssm/master/metals.owl#", "http://www.w3.org/2000/01/rdf-schema#subClassOf", "metals.txt")
ssmpy.semantic_base("metals.db")
e1 = ssmpy.get_id("copper")
e2 = ssmpy.get_id("gold")

print (ssmpy.ssm_resnik(e1,e2))
print (ssmpy.ssm_lin(e1,e2))
print (ssmpy.ssm_jiang_conrath(e1,e2))
