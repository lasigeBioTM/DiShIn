import sqlite3
import math
import ssm
import semanticbase

semanticbase.create('chebi_lite.owl', 'chebi_lite.db', 'http://purl.obolibrary.org/obo/')

ssm.semantic_base('chebi_lite.db')

ssm.intrinsic = False

ssm.mica = False

e1 = ssm.get_id('CHEBI_22160')
e2 = ssm.get_id('CHEBI_22712')

print ssm.ssm_resnik (e1, e2)

ssm.mica = True

print ssm.ssm_resnik (e1, e2)

print ssm.ssm_lin (e1, e2)

