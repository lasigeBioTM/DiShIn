# DiShIn: Semantic Similarity Measures using Disjunctive Shared Information

[![Downloads](https://pepy.tech/badge/ssmpy)](https://pepy.tech/project/ssmpy)

This software package provides the basic functions to start using semantic similarity measures directly from a rdf or owl file. 

A web tool using this package is available at: http://labs.fc.ul.pt/dishin/

Package documentation: https://dishin.readthedocs.io/en/latest/

## Reference: 

- F. Couto and A. Lamurias, “Semantic similarity definition,” in Encyclopedia of Bioinformatics and Computational Biology (S. Ranganathan, K. Nakai, C. Schönbach, and M. Gribskov, eds.), vol. 1, pp. 870–876, Oxford: Elsevier, 2019
[https://doi.org/10.1016/B978-0-12-809633-8.20401-9]
[https://www.researchgate.net/publication/323219905_Semantic_Similarity_Definition]

### INSTALLATION

Either clone this repository or install from pypi:

```
pip install ssmpy
```

## USAGE: 

You can use DiShIn as a command line tool with the dishin.py script of this repository:

```shell
python dishin.py <semanticbase>.db <term1> <term2>
python dishin.py <semanticbase>.[owl|rdf] <semanticbase>.db <name_prefix> <relation> <annotation_file>
```

or use the python functions directly:

```python
>>> import ssmpy
```

You can find more usage examples at https://dishin.readthedocs.io/en/latest/other_examples.html.

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
Resnik     DiShIn    intrinsic          0.2938933324510595
Resnik     MICA      intrinsic          0.587786664902119
Lin        DiShIn    intrinsic          0.19539774554219633
Lin        MICA      intrinsic          0.39079549108439265
JC         DiShIn    intrinsic          0.41316029085112316
JC         MICA      intrinsic          0.5456783339686456
Resnik     DiShIn    extrinsic          0.22599256187152864
Resnik     MICA      extrinsic          0.45198512374305727
Lin        DiShIn    extrinsic          0.1504595366201814
Lin        MICA      extrinsic          0.3009190732403628
JC         DiShIn    extrinsic          0.3918424740632774
JC         MICA      extrinsic          0.47617668319259754
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

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/go201907.db.gz
gunzip -N go201907.db.gz
```

Now to calculate the similarity between _maltose biosynthetic process_ and _maltose catabolic process_ execute:
```shell
python dishin.py go.db GO_0000023 GO_0000025
```

Output:
```txt
Resnik     DiShIn    intrinsic          3.7851272458782113
Resnik     MICA      intrinsic          8.911024218626034
Lin        DiShIn    intrinsic          0.4088671082942098
Lin        MICA      intrinsic          0.9625633347404052
JC         DiShIn    intrinsic          0.09136641197816901
JC         MICA      intrinsic          1.442695040888967
Resnik     DiShIn    extrinsic          4.273448119532465
Resnik     MICA      extrinsic          10.354796690276364
Lin        DiShIn    extrinsic          0.3919119421698985
Lin        MICA      extrinsic          0.9496239027945961
JC         DiShIn    extrinsic          0.0754073347935026
JC         MICA      extrinsic          0.9102392266268364
```

Now to calculate the similarity between proteins [Q12345](http://www.uniprot.org/uniprot/Q12345) and [Q12346](http://www.uniprot.org/uniprot/Q12346) execute:

```shell
python dishin.py go.db Q12345 Q12346
```

Output:
```txt
Resnik     DiShIn    intrinsic          1.3730675314939769
Resnik     MICA      intrinsic          1.653493583942882
Lin        DiShIn    intrinsic          0.16453282374961184
Lin        MICA      intrinsic          0.19975479444590458
JC         DiShIn    intrinsic          0.081825490673384
JC         MICA      intrinsic          0.09503231097236876
Resnik     DiShIn    extrinsic          0.9309878004221438
Resnik     MICA      extrinsic          1.143670161919403
Lin        DiShIn    extrinsic          0.15280642004118333
Lin        MICA      extrinsic          0.19273825637513847
JC         DiShIn    extrinsic          0.1013441951183969
JC         MICA      extrinsic          0.11970943511723715
```

To create an updated version of the database, download the ontology and annotations:
```shell
wget http://purl.obolibrary.org/obo/go.owl
wget http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
gunzip goa_uniprot_all_noiea.gaf.gz 
```

And then create the new database:
```shell
python dishin.py go.owl go.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf goa_uniprot_all_noiea.gaf
```

###  Chemical Entities of Biological Interest (ChEBI) Example

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/chebi201907.db.gz
gunzip -N chebi201907.db.gz
```

Now to calculate the similarity between _aripiprazole_ and _bithionol_ execute:
```shell
python dishin.py chebi.db CHEBI_31236 CHEBI_3131
```

Output:
```txt
Resnik     DiShIn    intrinsic          1.3532341094444025
Resnik     MICA      intrinsic          5.3808132551673
Lin        DiShIn    intrinsic          0.12372266288871554
Lin        MICA      intrinsic          0.49195371280548356
JC         DiShIn    intrinsic          0.05216806727627202
JC         MICA      intrinsic          0.08997939012118301
```
To create an updated version of the database, download the ontology:
```shell
wget ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/chebi_lite.owl
```

And then create the new database:
```shell
python dishin.py chebi_lite.owl chebi.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

### Human Phenotype (HP) Example

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/hp201907.db.gz
gunzip -N hp201907.db.gz
```

Now to calculate the similarity between _Optic nerve coloboma_ and _Optic nerve dysplasia_ execute:
```shell
python dishin.py hp.db HP_0000588 HP_0001093
```

Output:
```txt
Resnik     DiShIn    intrinsic          4.514739038358012
Resnik     MICA      intrinsic          5.917583373691076
Lin        DiShIn    intrinsic          0.5079590611976912
Lin        MICA      intrinsic          0.665794870870856
JC         DiShIn    intrinsic          0.11433121677975834
JC         MICA      intrinsic          0.16832667824491762
```

To create an updated version of the database, download the ontology:
```shell
wget http://purl.obolibrary.org/obo/hp.owl
```

And then create the new database:
```shell
python dishin.py hp.owl hp.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

### Human Disease Ontology (HDO) Example

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/doid201907.db.gz
gunzip -N doid201907.db.gz
```

Now to calculate the similarity between _Asthma_ and _Lung cancer_ execute:
```shell
python dishin.py doid.db DOID_2841 DOID_1324
```

Output:
```txt
Resnik     DiShIn    intrinsic          2.316903156622129
Resnik     MICA      intrinsic          3.730767546816189
Lin        DiShIn    intrinsic          0.40974430023007496
Lin        MICA      intrinsic          0.6597862035890811
JC         DiShIn    intrinsic          0.14980794775373127
JC         MICA      intrinsic          0.2599100799712222
```
To create an updated version of the database, download the ontology:
```shell
wget http://purl.obolibrary.org/obo/doid.owl
```

And then create the new database:
```shell
python dishin.py doid.owl doid.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

###  Medical Subject Headings (MeSH) Example

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/mesh201911.db.gz
gunzip -N mesh201911.db.gz
```

Now to calculate the similarity between _Malignant Hyperthermia_ and _Fever_ execute:
```shell
python dishin.py mesh.db D008305 D005334
```

Output:
```txt
Resnik 	 MICA 	 intrinsic 	1.33556794556
Lin 	 MICA 	 intrinsic 	0.18486943136
JC 	 MICA 	 intrinsic 	0.0849066961975
```

To create an updated version of the database, download the _NT_ version from ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/mesh.nt.gz and unzip it:
```shell
wget ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/mesh.nt.gz
gunzip mesh.nt.gz
```
And then create the new database:
```shell
python dishin.py mesh.nt mesh.db http://id.nlm.nih.gov/mesh/ http://id.nlm.nih.gov/mesh/vocab#broaderDescriptor ''
```

###  Radiology Lexicon (RadLex) Example

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/radlex201907.db.gz
gunzip -N radlex201907.db.gz
```

Now to calculate the similarity between _nervous system of right upper limb_ and _nervous system of left upper limb_ execute:
```shell
python dishin.py radlex.db RID16139 RID16140
```

Output:
```txt
Resnik   MICA    intrinsic      9.363855135365721
Lin      MICA    intrinsic      0.9310781524369027
JC       MICA    intrinsic      0.7213475204444816
```

To create an updated version of the database, download the _RDF/XML_ version from http://bioportal.bioontology.org/ontologies/RADLEX and save it as _radlex.rdf_

And then create the new database:
```shell
python dishin.py radlex.rdf radlex.db http://radlex.org/RID/ http://www.w3.org/2000/01/rdf-schema#subClassOf '' 
```

### WordNet Example

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/wordnet201907.db.gz
gunzip wordnet201907.db.gz
```

Now to calculate the similarity between the nouns _ambulance_ and _motorcycle_ execute:
```shell
python dishin.py wordnet.db ambulance-noun-1 motorcycle-noun-1
```

Output:
```txt
Resnik   MICA    intrinsic      6.331085809208157
Lin      MICA    intrinsic      0.6792379292396559
JC       MICA    intrinsic      0.1672363673134892
```

To create an updated version of the database, download the ontology:
```shell
wget http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf
```

And then create the new database:
```shell
python dishin.py wordnet-hyponym.rdf wordnet.db http://www.w3.org/2006/03/wn/wn20/instances/synset- http://www.w3.org/2006/03/wn/wn20/schema/hyponymOf ''
```
## Source Code 

- ssmpy/semanticbase.py : provides a function to produce the semantic-base as a SQLite database 

- ssmpy/ssm.py : provides the functions to calculate semantic similarity based on the SQLite database

- ssmpy/annotations.py :  provides the functions to get the annotations for the given proteins 

- dishin.py :  executes the functions according to the input given

