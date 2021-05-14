import ssmpy

ssmpy.semantic_base("go.db")
e1 = ssmpy.get_id("GO_0000023")
e2 = ssmpy.get_id("GO_0000025")
print(ssmpy.ssm_resnik(e1,e2))
print(ssmpy.ssm_lin(e1,e2))
print(ssmpy.ssm_jiang_conrath(e1,e2))

e1 = ssmpy.get_uniprot_annotations("Q12345")
e2 = ssmpy.get_uniprot_annotations("Q12346")
print(ssmpy.ssm_multiple(ssmpy.ssm_resnik, e1, e2))
print(ssmpy.ssm_multiple(ssmpy.ssm_lin, e1, e2))
print(ssmpy.ssm_multiple(ssmpy.ssm_jiang_conrath, e1, e2))
