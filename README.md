# DiShIn: Semantic Similarity Measures using Disjunctive Shared Information

This software package provides the basic functions to start using semantic similarity measures directly from a rdf or owl file. 

A web tool using this package is available at: http://labs.fc.ul.pt/dishin/


## USAGE: 

```shell
python dishin.py <semanticbase>.db <term1> <term2>
python dishin.py <semanticbase>.[owl|rdf] <semanticbase>.db <name_prefix> <relation> <annotation_file>
```

### Metals Example

To create the semantic base file (_metals.db_) from the _metals.owl_ file:
```shell
python dishin.py metals.owl metals.db https://raw.githubusercontent.com/lasigeBioTM/ssm/master/metals.owl# http://www.w3.org/2000/01/rdf-schema#subClassOf metals.txt
```

The _metals.txt_ contains the a list of occurrences. For example, the following contents has one occurrence for each term, except gold and silver with two occurrences.
```txt
gold
silver
gold
silver
copper
platinum
palladium
metal
coinage
precious
```

Now to calculate the similarity between _copper_ and _gold_ execute:

```shell
python dishin.py metals.db copper gold
```

Output:
```txt
Resnik 	 DiShIn 	 intrinsic 	0.2938933324510595
Resnik 	 MICA 	 	 intrinsic 	0.587786664902119
Lin 	 DiShIn 	 intrinsic 	0.19539774554219633
Lin 	 MICA 	 	 intrinsic 	0.39079549108439265
JC 	 DiShIn 	 intrinsic 	0.41316029085112316
JC 	 MICA 	 	 intrinsic 	0.5456783339686456
Resnik 	 DiShIn 	 extrinsic 	0.22599256187152864
Resnik 	 MICA 	 	 extrinsic 	0.45198512374305727
Lin 	 DiShIn 	 extrinsic 	0.1504595366201814
Lin 	 MICA 	 	 extrinsic 	0.3009190732403628
JC 	 DiShIn 	 extrinsic 	0.3918424740632774
JC 	 MICA 	 	 extrinsic 	0.47617668319259754
```

### Gene Ontology (GO) and UniProt proteins Example

Download the ontology and annotations:
```shell
wget http://archive.geneontology.org/latest-termdb/go_daily-termdb.owl.gz
wget http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
gunzip go_daily-termdb.owl.gz 
gunzip goa_uniprot_all_noiea.gaf.gz 
```

Create the semantic base:
```shell
python dishin.py go_daily-termdb.owl go.db http://purl.org/obo/owl/GO# http://www.w3.org/2000/01/rdf-schema#subClassOf goa_uniprot_all_noiea.gaf
```

Now to calculate the similarity between _maltose biosynthetic process_ and _maltose catabolic process_ execute:
```shell
python dishin.py go.db GO_0000024 GO_0000025
```

Output:
```txt
Resnik 	 DiShIn 	 intrinsic 	3.27686491515
Resnik 	 MICA 	 	 intrinsic 	8.91092304331
Lin 	 DiShIn 	 intrinsic 	0.341195434724
Lin 	 MICA 	 	 intrinsic 	0.927827768394
JC 	 DiShIn 	 intrinsic 	0.0790238305229
JC 	 MICA 	 	 intrinsic 	0.721347520444
Resnik 	 DiShIn 	 extrinsic 	6.24018392019
Resnik 	 MICA 	 	 extrinsic 	13.4448298467
Lin 	 DiShIn 	 extrinsic 	0.405184611581
Lin 	 MICA 	 	 extrinsic 	0.87299320483
JC 	 DiShIn 	 extrinsic 	0.0545812354476
JC 	 MICA 	 	 extrinsic 	0.255622218635
```

Now to calculate the similarity between proteins [Q12345](http://www.uniprot.org/uniprot/Q12345) and [Q12346](http://www.uniprot.org/uniprot/Q12346) execute:

```shell
python dishin.py go.db Q12345 Q12346
```

Output:
```txt
Resnik 	 DiShIn 	 intrinsic 	0.716191626804
Resnik 	 MICA 	 	 intrinsic 	0.864432485011
Lin 	 DiShIn 	 intrinsic 	0.0820024443277
Lin 	 MICA 	 	 intrinsic 	0.0989710020485
JC 	 DiShIn 	 intrinsic 	0.0744612781029
JC 	 MICA 	 	 intrinsic 	0.0746817790648
Resnik 	 DiShIn 	 extrinsic 	0.983006979289
Resnik 	 MICA 	 	 extrinsic 	1.2045858634
Lin 	 DiShIn 	 extrinsic 	0.109395081314
Lin 	 MICA 	 	 extrinsic 	0.134114260655
JC 	 DiShIn 	 extrinsic 	0.073703048577
JC 	 MICA 	 	 extrinsic 	0.0753867503734
```


###  Chemical Entities of Biological Interest (ChEBI) Example

Download the ontology:
```shell
wget ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/chebi_lite.owl
```

Create the semantic base:
```shell
python dishin.py chebi_lite.owl chebi.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

Now to calculate the similarity between _aripiprazole_ and _bithionol_ execute:
```shell
python dishin.py chebi.db CHEBI_31236 CHEBI_3131
```

Output:
```txt
Resnik 	 DiShIn 	 intrinsic 	1.34864156948
Resnik 	 MICA 	 	 intrinsic 	5.34912740927
Lin 	 DiShIn 	 intrinsic 	0.123972474646
Lin 	 MICA 	 	 intrinsic 	0.491712977807
JC 	 DiShIn 	 intrinsic 	0.0524663655252
JC 	 MICA 	 	 intrinsic 	0.0904252486264
```

### Human Phenotype (HP) Example

Download the ontology:
```shell
wget http://purl.obolibrary.org/obo/hp.owl
```

Create the semantic base:
```shell
python dishin.py hp.owl hp.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

Now to calculate the similarity between _Optic nerve coloboma_ and _Optic nerve dysplasia_ execute:
```shell
python dishin.py hp.db HP_0000588 HP_0001093
```

Output:
```txt
Resnik 	 DiShIn 	 intrinsic 	3.05120683059
Resnik 	 MICA 	 	 intrinsic 	6.08995149382
Lin 	 DiShIn 	 intrinsic 	0.346806801862
Lin 	 MICA 	 	 intrinsic 	0.692197126688
JC 	 DiShIn 	 intrinsic 	0.0870050196333
JC 	 MICA 	 	 intrinsic 	0.184634686534
```

### Human Disease Ontology (HDO) Example

Download the ontology:
```shell
wget https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid-simple.owl
```

Create the semantic base:
```shell
python dishin.py doid-simple.owl doid.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

Now to calculate the similarity between _Asthma_ and _Lung cancer_ execute:
```shell
python dishin.py doid.db DOID_2841 DOID_1324
```

Output:
```txt
Resnik 	 DiShIn 	 intrinsic 	2.01382659386
Resnik 	 MICA 	 	 intrinsic 	4.02765318772
Lin 	 DiShIn 	 intrinsic 	0.323283569128
Lin 	 MICA 	 	 intrinsic 	0.646567138257
JC 	 DiShIn 	 intrinsic 	0.118610966131
JC 	 MICA 	 	 intrinsic 	0.227103923688
```

###  Radiology Lexicon (RadLex) Example

Download the _RDF/XML_ version from http://bioportal.bioontology.org/ontologies/RADLEX and save it as _radlex.rdf_

Create the semantic base:
```shell
python dishin.py radlex.rdf radlex.db http://www.radlex.org/RID/# http://www.radlex.org/RID/#Is_A ''
```

Now to calculate the similarity between _nervous system of right upper limb_ and _nervous system of left upper limb_ execute:
```shell
python dishin.py radlex.db RID16139 RID16140
```

Output:
```txt
Resnik 	 MICA 	 intrinsic 	9.35897587112
Lin 	 MICA 	 intrinsic 	0.931044698021
JC 	 MICA 	 intrinsic 	0.721347520444
```

### WordNet Example

Download the ontology:
```shell
wget http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf
```

Create the semantic base:
```shell
python dishin.py wordnet-hyponym.rdf wordnet.db http://www.w3.org/2006/03/wn/wn20/instances/synset- http://www.w3.org/2006/03/wn/wn20/schema/hyponymOf ''
```

Now to calculate the similarity between the nouns _ambulance_ and _motorcycle_ execute:
```shell
python dishin.py wordnet.db ambulance-noun-1 motorcycle-noun-1
```

Output:
```txt
Resnik 	 MICA 	 intrinsic 	6.33108580921
Lin 	 MICA 	 intrinsic 	0.67923792924
JC 	 MICA 	 intrinsic 	0.167236367313
```

## Data Sources 

### Gene Ontology (GO) 
- Ontology: http://geneontology.org/page/download-ontology#go.obo_and_go.owl; 
- Annotation files (extrinsic): http://www.geneontology.org/page/download-annotations
- SemanticBase: http://labs.rd.ciencias.ulisboa.pt/dishin/go.db

### ChEBI 
- Ontology: ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/
- SemanticBase: http://labs.rd.ciencias.ulisboa.pt/dishin/chebi.db

### Human Phenotype ontology (HPO)
- Ontology: http://human-phenotype-ontology.github.io/downloads.html
- SemanticBase: http://labs.rd.ciencias.ulisboa.pt/dishin/hp.db

### Human Disease Ontology (DO)
- Ontology: https://github.com/DiseaseOntology/HumanDiseaseOntology/tree/master/src/ontology
- SemanticBase: http://labs.rd.ciencias.ulisboa.pt/dishin/doid.db

### RadLex
- Ontology: http://bioportal.bioontology.org/ontologies/RADLEX
- SemanticBase: http://labs.rd.ciencias.ulisboa.pt/dishin/radlex.db

### WordNet
- Ontology: http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf
- SemanticBase: http://labs.rd.ciencias.ulisboa.pt/dishin/wordnet.db

## Source Code 

- semanticbase.py : provides a function to produce the semantic-base as a SQLite database 

- ssm.py : provides the functions to calculate semantic similarity based on the SQLite database

- annotations.py :  provides the functions to get the annotations for the given proteins 

- dishin.py :  executes the functions according to the input given

## Reference: 

- F. Couto and A. Lamurias, “Semantic similarity definition,” in Reference Module in Life Sciences (Encyclopedia of Bioinformatics and Computational Biology), pp. 1--17, Elsevier, 2018 (https://doi.org/10.1016/B978-0-12-809633-8.20401-9, https://www.researchgate.net/publication/323219905_Semantic_Similarity_Definition)


