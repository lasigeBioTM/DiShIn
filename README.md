# DiShIn: Semantic Similarity Measures using Disjunctive Shared Information

This software package provides the basic functions to start using semantic similarity measures directly from a rdf or owl file. 

A web tool using this package is available at: http://labs.fc.ul.pt/dishin/

### INSTALLATION

Either clone this repository or install from pypi:

```
pip install ssmpy
```

## USAGE: 

```shell
python dishin.py <semanticbase>.db <term1> <term2>
python dishin.py <semanticbase>.[owl|rdf] <semanticbase>.db <name_prefix> <relation> <annotation_file>
```
or use the python functions directly

```python
>>> import ssmpy
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
Resnik 	 DiShIn 	 intrinsic 	0.293893332451
Resnik 	 MICA 	 	 intrinsic 	0.587786664902
Lin 	 DiShIn 	 intrinsic 	0.195397745542
Lin 	 MICA 	 	 intrinsic 	0.390795491084
JC 	 DiShIn 	 intrinsic 	0.413160290851
JC 	 MICA 	 	 intrinsic 	0.545678333969
Resnik 	 DiShIn 	 extrinsic 	0.225992561872
Resnik 	 MICA 	 	 extrinsic 	0.451985123743
Lin 	 DiShIn 	 extrinsic 	0.15045953662
Lin 	 MICA 	 	 extrinsic 	0.30091907324
JC 	 DiShIn 	 extrinsic 	0.391842474063
JC 	 MICA 	 	 extrinsic 	0.476176683193

```

Using the python function directly (first download metals.db and metals.txt from this repository):
```python
>>> ssmpy.create_semantic_base("metals.owl", "metals.db", "https://raw.githubusercontent.com/lasigeBioTM/ssm/master/metals.owl#", "http://www.w3.org/2000/01/rdf-schema#subClassOf", "metals.txt")
>>> ssmpy.semantic_base("metals.db")
>>> e1 = ssmpy.get_id("copper")
>>> e2 = ssmpy.get_id("gold")
>>> ssmpy.ssm_resnik (e1,e2)
```

### Gene Ontology (GO) and UniProt proteins Example

Download the ontology and annotations:
```shell
wget http://purl.obolibrary.org/obo/go.owl
wget http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
gunzip goa_uniprot_all_noiea.gaf.gz 
```

Create the semantic base:
```shell
python dishin.py go.owl go.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf goa_uniprot_all_noiea.gaf
```

Now to calculate the similarity between _maltose biosynthetic process_ and _maltose catabolic process_ execute:
```shell
python dishin.py go.db GO_0000023 GO_0000025
```

Output:
```txt

Resnik   DiShIn          intrinsic      3.77628827887
Resnik   MICA            intrinsic      8.90977567369
Lin      DiShIn          intrinsic      0.407967349889
Lin      MICA            intrinsic      0.962558285087
JC       DiShIn          intrinsic      0.0912398605342
JC       MICA            intrinsic      1.44269504089
Resnik   DiShIn          extrinsic      3.90322051564
Resnik   MICA            extrinsic      10.8429770989
Lin      DiShIn          extrinsic      0.335106659477
Lin      MICA            extrinsic      0.930911748348
JC       DiShIn          extrinsic      0.0645621511038
JC       MICA            extrinsic      0.62133493456
```

Now to calculate the similarity between proteins [Q12345](http://www.uniprot.org/uniprot/Q12345) and [Q12346](http://www.uniprot.org/uniprot/Q12346) execute:

```shell
python dishin.py go.db Q12345 Q12346
```

Output:
```txt
Resnik   DiShIn          intrinsic      0.71245987296
Resnik   MICA            intrinsic      0.86114182192
Lin      DiShIn          intrinsic      0.0815862437434
Lin      MICA            intrinsic      0.0986072045826
JC       DiShIn          intrinsic      0.0746193683317
JC       MICA            intrinsic      0.0747498775484
Resnik   DiShIn          extrinsic      0.263180891661
Resnik   MICA            extrinsic      0.479787642163
Lin      DiShIn          extrinsic      0.0407370976359
Lin      MICA            extrinsic      0.0744385765602
JC       DiShIn          extrinsic      0.0963202202036
JC       MICA            extrinsic      0.0977061369628
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
Resnik   DiShIn          intrinsic      1.35348538334
Resnik   MICA            intrinsic      5.36203900206
Lin      DiShIn          intrinsic      0.124157709369
Lin      MICA            intrinsic      0.491869722596
JC       DiShIn          intrinsic      0.0523677861211
JC       MICA            intrinsic      0.0902640991714
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
Resnik   DiShIn          intrinsic      3.05120683059
Resnik   MICA            intrinsic      6.08995149382
Lin      DiShIn          intrinsic      0.346806801862
Lin      MICA            intrinsic      0.692197126688
JC       DiShIn          intrinsic      0.0870050196333
JC       MICA            intrinsic      0.184634686534
```

### Human Disease Ontology (HDO) Example

Download the ontology:
```shell
wget https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid.owl
```

Create the semantic base:
```shell
python dishin.py doid.owl doid.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

Now to calculate the similarity between _Asthma_ and _Lung cancer_ execute:
```shell
python dishin.py doid.db DOID_2841 DOID_1324
```

Output:
```txt
Resnik   DiShIn          intrinsic      2.29931853312
Resnik   MICA            intrinsic      3.70394398358
Lin      DiShIn          intrinsic      0.409564492804
Lin      MICA            intrinsic      0.659762410974
JC       DiShIn          intrinsic      0.150841449132
JC       MICA            intrinsic      0.261764573924
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
Resnik   MICA            intrinsic      9.35897587112
Lin      MICA            intrinsic      0.931044698021
JC       MICA            intrinsic      0.721347520444
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
Resnik   MICA            intrinsic      6.33108580921
Lin      MICA            intrinsic      0.67923792924
JC       MICA            intrinsic      0.167236367313
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

- F. Couto and A. Lamurias, “Semantic similarity definition,” in Encyclopedia of Bioinformatics and Computational Biology (S. Ranganathan, K. Nakai, C. Schönbach, and M. Gribskov, eds.), vol. 1, pp. 870–876, Oxford: Elsevier, 2019
[https://doi.org/10.1016/B978-0-12-809633-8.20401-9]
[https://www.researchgate.net/publication/323219905_Semantic_Similarity_Definition]

