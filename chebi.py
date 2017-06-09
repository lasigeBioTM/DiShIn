import sqlite3
import math
import ssm
import semanticbase

#semanticbase.create('chebi_lite.owl', 'chebi_lite.db', 'http://purl.obolibrary.org/obo/')

ssm.semantic_base('chebi_lite.db')

ssm.intrinsic = False

ssm.mica = False

gold = ssm.get_id('CHEBI_29287')
silver = ssm.get_id('CHEBI_30512')

print gold
print silver

print ssm.ssm_resnik (gold, silver)

ssm.mica = True

print ssm.ssm_resnik (gold, silver)

print ssm.ssm_lin (gold, silver)

