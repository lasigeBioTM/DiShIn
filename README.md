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

If you use it from the shell, you need to install python3, sqlite3, rdflib and pandas:
```shell
sudo apt-get update
sudo apt-get install python3 python3-rdflib python3-pandas sqlite3
```

and then clone and enter the folder:
```shell
git clone https://github.com/lasigeBioTM/DiShIn.git
cd DiShIn
```

If you just have python2 or you cannot install packages,
then create and use a lighter version of DiShIn:  
```shell
curl https://raw.githubusercontent.com/lasigeBioTM/DiShIn/master/dishin.py | sed -e 's/import ssmpy/import ssm\nimport annotations/; s/ssmpy\.ssm\./ssm./g; s/ssmpy\./ssm./g; s/ssm.get_uniprot_annotations/annotations.get_uniprot_annotations/g' > dishin.py
curl https://raw.githubusercontent.com/lasigeBioTM/DiShIn/master/ssmpy/ssm.py | sed 's/from ssmpy./# from ssmpy./' > ssm.py
curl https://raw.githubusercontent.com/lasigeBioTM/DiShIn/master/ssmpy/annotations.py | sed 's/import ssmpy./import /; s/ssmpy./ssm./' > annotations.py
```
Note, this light version cannot create new databases.

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
JC         DiShIn    intrinsic          0.29236619053475066
JC         MICA      intrinsic          0.35303485982596094
Resnik     DiShIn    extrinsic          0.22599256187152864
Resnik     MICA      extrinsic          0.45198512374305727
Lin        DiShIn    extrinsic          0.1504595366201814
Lin        MICA      extrinsic          0.3009190732403628
JC         DiShIn    extrinsic          0.281527889373394
JC         MICA      extrinsic          0.322574315537045
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

Download the latest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/go202104.db.gz
gunzip -N go202104.db.gz
```

Now to calculate the similarity between _maltose biosynthetic process_ and _maltose catabolic process_ execute:
```shell
python dishin.py go.db GO_0000023 GO_0000025
```

Output:
```txt
Resnik     DiShIn    intrinsic          3.775439615001474
Resnik     MICA      intrinsic          8.880063901891981
Lin        DiShIn    intrinsic          0.4091891133909429
Lin        MICA      intrinsic          0.9624377146523844
JC         DiShIn    intrinsic          0.08401669887638269
JC         MICA      intrinsic          0.5906161091496418
Resnik     DiShIn    extrinsic          4.315813746201754
Resnik     MICA      extrinsic          10.575802576015931
Lin        DiShIn    extrinsic          0.38793452313030363
Lin        MICA      extrinsic          0.950624649327762
JC         DiShIn    extrinsic          0.06840605034663635
JC         MICA      extrinsic          0.4765053580405049
```

Now to calculate the similarity between proteins [Q12345](http://www.uniprot.org/uniprot/Q12345) and [Q12346](http://www.uniprot.org/uniprot/Q12346) execute:

```shell
python dishin.py go.db Q12345 Q12346
```

Output:
```txt
Resnik     DiShIn    intrinsic          1.4462923030269426
Resnik     MICA      intrinsic          1.4462923030269426
Lin        DiShIn    intrinsic          0.18745282441602068
Lin        MICA      intrinsic          0.18745282441602068
JC         DiShIn    intrinsic          0.08633506268285998
JC         MICA      intrinsic          0.08633506268285998
Resnik     DiShIn    extrinsic          0.6015115682274214
Resnik     MICA      extrinsic          0.6015115682274214
Lin        DiShIn    extrinsic          0.12201023476842265
Lin        MICA      extrinsic          0.12201023476842265
JC         DiShIn    extrinsic          0.09317326288224918
JC         MICA      extrinsic          0.09317326288224918
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
wget http://labs.rd.ciencias.ulisboa.pt/dishin/chebi202104.db.gz
gunzip -N chebi202104.db.gz
```

Now to calculate the similarity between _aripiprazole_ and _bithionol_ execute:
```shell
python dishin.py chebi.db CHEBI_31236 CHEBI_3131
```

Output:
```txt
Resnik     DiShIn    intrinsic          1.4393842298350599
Resnik     MICA      intrinsic          5.5106315826160674
Lin        DiShIn    intrinsic          0.12935491517581163
Lin        MICA      intrinsic          0.4952307147453835
JC         DiShIn    intrinsic          0.049077257018319796
JC         MICA      intrinsic          0.0817424736051902
```
To create an updated version of the database, download the ontology:
```shell
wget http://purl.obolibrary.org/obo/chebi/chebi_lite.owl
```

And then create the new database:
```shell
python dishin.py chebi_lite.owl chebi.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

### Human Phenotype (HP) Example

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/hp202104.db.gz
gunzip -N hp202104.db.gz
```

Now to calculate the similarity between _Optic nerve coloboma_ and _Optic nerve dysplasia_ execute:
```shell
python dishin.py hp.db HP_0000588 HP_0001093
```

Output:
```txt
Resnik     DiShIn    intrinsic          4.593979372426621
Resnik     MICA      intrinsic          6.005278943833842
Lin        DiShIn    intrinsic          0.5118244533189668
Lin        MICA      intrinsic          0.6690601683812312
JC         DiShIn    intrinsic          0.10242304162282165
JC         MICA      intrinsic          0.14407501033681872
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
wget http://labs.rd.ciencias.ulisboa.pt/dishin/doid202104.db.gz
gunzip -N doid202104.db.gz
```

Now to calculate the similarity between _Asthma_ and _Lung cancer_ execute:
```shell
python dishin.py doid.db DOID_2841 DOID_1324
```

Output:
```txt
Resnik     DiShIn    intrinsic          2.3627836143597176
Resnik     MICA      intrinsic          3.791674698804828
Lin        DiShIn    intrinsic          0.4328907089097581
Lin        MICA      intrinsic          0.6946809425735787
JC         DiShIn    intrinsic          0.13906777879867938
JC         MICA      intrinsic          0.2307893214756218
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
wget http://labs.rd.ciencias.ulisboa.pt/dishin/mesh202104.db.gz
gunzip -N mesh202104.db.gz
```

Now to calculate the similarity between _Malignant Hyperthermia_ and _Fever_ execute:
```shell
python dishin.py mesh.db D008305 D005334
```

Output:
```txt
Resnik     DiShIn    intrinsic          1.2582571367910345
Resnik     MICA      intrinsic          1.2582571367910345
Lin        DiShIn    intrinsic          0.17390901691859173
Lin        MICA      intrinsic          0.17390901691859173
JC         DiShIn    intrinsic          0.07719755683816652
JC         MICA      intrinsic          0.07719755683816652
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
wget http://labs.rd.ciencias.ulisboa.pt/dishin/radlex202104.db.gz
gunzip -N radlex202104.db.gz
```

Now to calculate the similarity between _nervous system of right upper limb_ and _nervous system of left upper limb_ execute:
```shell
python dishin.py radlex.db RID16139 RID16140
```

Output:
```txt
Resnik     MICA      intrinsic          9.366531825151093
Lin        MICA      intrinsic          0.9310964912333252
JC         MICA      intrinsic          0.41905978419640516
```

To create an updated version of the database, download the _RDF/XML_ version from http://bioportal.bioontology.org/ontologies/RADLEX and save it as _radlex.rdf_

And then create the new database:
```shell
python dishin.py radlex.rdf radlex.db http://radlex.org/RID/ http://www.w3.org/2000/01/rdf-schema#subClassOf '' 
```

### WordNet Example

Download the lastest version of the database we created:
```shell
wget http://labs.rd.ciencias.ulisboa.pt/dishin/wordnet202104.db.gz
gunzip -N wordnet202104.db.gz
```

Now to calculate the similarity between the nouns _ambulance_ and _motorcycle_ execute:
```shell
python dishin.py wordnet.db ambulance-noun-1 motorcycle-noun-1
```

Output:
```txt
Resnik     MICA      intrinsic          6.331085809208157
Lin        MICA      intrinsic          0.6792379292396559
JC         MICA      intrinsic          0.14327549414725688
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

