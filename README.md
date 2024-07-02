[![Downloads](https://pepy.tech/badge/ssmpy)](https://pepy.tech/project/ssmpy)

# DiShIn: Semantic Similarity Measures using Disjunctive Shared Information

This software package offers essential functions for utilizing semantic similarity measures directly from RDF or OWL files.

Access the web tool utilizing this package here: [DiShIn Demo](https://labs.rd.ciencias.ulisboa.pt/dishin/)

Package documentation: https://dishin.readthedocs.io/en/latest/

## New Stuff

### 2024
- **DATABASES**: Databases updated: 202407

### 2023
- **ONTOLOGIES**: New examples added, namely the ontologies: OSCI, CL, ENVO, and ECTO.

### 2021
- **DOCKER**: Image available: [fjmc/dishin-image](https://hub.docker.com/r/fjmc/dishin-image)

## References: 
- **Semantic similarity definition**  
  F. Couto and A. Lamurias  
  in *Encyclopedia of Bioinformatics and Computational Biology* (S. Ranganathan, K. Nakai, C. Schönbach, and M. Gribskov, eds.), vol. 1, pp. 870–876, Oxford: Elsevier, 2019  
  [DOI: 10.1016/B978-0-12-809633-8.20401-9](https://doi.org/10.1016/B978-0-12-809633-8.20401-9)  
  [ResearchGate](https://www.researchgate.net/publication/323219905_Semantic_Similarity_Definition)

## System Requirements

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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/go202407.db.gz
gunzip -N go202407.db.gz
```

Now to calculate the similarity between _maltose biosynthetic process_ and _maltose catabolic process_ execute:
```shell
python dishin.py go.db GO_0000023 GO_0000025
```

Output:
```txt
Resnik       DiShIn      intrinsic  5.425897125338367
Resnik       MICA        intrinsic  8.817112581532497
Lin          DiShIn      intrinsic  0.592108571115022
Lin          MICA        intrinsic  0.9621796748838876
JC           DiShIn      intrinsic  0.11798605228261819
JC           MICA        intrinsic  0.5906161091496418
Resnik       DiShIn      extrinsic  5.996307081288803
Resnik       MICA        extrinsic  10.06498546096925
Lin          DiShIn      extrinsic  0.5516531867976029
Lin          MICA        extrinsic  0.9259668041253548
JC           DiShIn      extrinsic  0.09305100083697551
JC           MICA        extrinsic  0.3832242933372551
```

Now to calculate the similarity between proteins [Q12345](http://www.uniprot.org/uniprot/Q12345) and [Q12346](http://www.uniprot.org/uniprot/Q12346) execute:

```shell
python dishin.py go.db Q12345 Q12346
```

Output:
```txt
Resnik       DiShIn      intrinsic  1.0460749575571253
Resnik       MICA        intrinsic  1.0460749575571253
Lin          DiShIn      intrinsic  0.12881766476333187
Lin          MICA        intrinsic  0.12881766476333187
JC           DiShIn      intrinsic  0.07376784927866546
JC           MICA        intrinsic  0.07376784927866546
Resnik       DiShIn      extrinsic  0.4593770683280119
Resnik       MICA        extrinsic  0.4593770683280119
Lin          DiShIn      extrinsic  0.09032548949936249
Lin          MICA        extrinsic  0.09032548949936249
JC           DiShIn      extrinsic  0.09082772814721791
JC           MICA        extrinsic  0.09082772814721791
```

To create an updated version of the database, download the ontology and annotations:
```shell
curl -L -O http://purl.obolibrary.org/obo/go.owl
curl -L -O https://release.geneontology.org/2024-06-17/annotations/filtered_goa_uniprot_all_noiea.gaf.gz
gunzip filtered_goa_uniprot_all_noiea.gaf.gz
```

And then create the new database:
```shell
python dishin.py go.owl go.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf filtered_goa_uniprot_all_noiea.gaf
```

###  Chemical Entities of Biological Interest (ChEBI) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/chebi202407.db.gz
gunzip -N chebi202407.db.gz
```

Now to calculate the similarity between _aripiprazole_ and _bithionol_ execute:
```shell
python dishin.py chebi.db CHEBI_31236 CHEBI_3131
```

Output:
```txt
Resnik       DiShIn      intrinsic  1.5055300158880238
Resnik       MICA        intrinsic  5.806757844273615
Lin          DiShIn      intrinsic  0.13081472985683726
Lin          MICA        intrinsic  0.5045462068019113
JC           DiShIn      intrinsic  0.04760389486434374
JC           MICA        intrinsic  0.08061766783674874
```
To create an updated version of the database, download the ontology:
```shell
curl -L -O http://purl.obolibrary.org/obo/chebi/chebi_lite.owl
```

And then create the new database:
```shell
python dishin.py chebi_lite.owl chebi.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

### Human Phenotype (HP) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/hp202407.db.gz
gunzip -N hp202407.db.gz
```

Now to calculate the similarity between _Optic nerve coloboma_ and _Optic nerve dysplasia_ execute:
```shell
python dishin.py hp.db HP_0000588 HP_0001093
```

Output:
```txt
Resnik       DiShIn      intrinsic  4.670874222643114
Resnik       MICA        intrinsic  6.024899323194219
Lin          DiShIn      intrinsic  0.5111252236334636
Lin          MICA        intrinsic  0.6592937140135965
JC           DiShIn      intrinsic  0.10065343384373353
JC           MICA        intrinsic  0.13836941515802242
```

To create an updated version of the database, download the ontology:
```shell
curl -L -O http://purl.obolibrary.org/obo/hp.owl
```

And then create the new database:
```shell
python dishin.py hp.owl hp.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

### Human Disease Ontology (HDO) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/doid202407.db.gz
gunzip -N doid202407.db.gz
```

Now to calculate the similarity between _Asthma_ and _Lung cancer_ execute:
```shell
python dishin.py doid.db DOID_2841 DOID_1324
```

Output:
```txt
Resnik       DiShIn      intrinsic  2.432559719491104
Resnik       MICA        intrinsic  3.894842361456266
Lin          DiShIn      intrinsic  0.4393904394647951
Lin          MICA        intrinsic  0.7035208562955191
JC           DiShIn      intrinsic  0.13874802978811976
JC           MICA        intrinsic  0.23349514659345028
```
To create an updated version of the database, download the ontology:
```shell
curl -L -O http://purl.obolibrary.org/obo/doid.owl
```

And then create the new database:
```shell
python dishin.py doid.owl doid.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

###  Ontology for Stem Cell Investigations (OSCI) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/osci202407.db.gz
gunzip -N osci202407.db.gz
```

Now to calculate the similarity between _neuronal stem cell_ and _sensory neuron_ execute:
```shell
python dishin.py osci.db CL_0000047 CL_0000101
```

Output:
```txt
Resnik       DiShIn      intrinsic  3.1560550137337486
Resnik       MICA        intrinsic  4.1255971057262055
Lin          DiShIn      intrinsic  0.6369806275261506
Lin          MICA        intrinsic  0.8326614782980606
JC           DiShIn      intrinsic  0.21751839842873807
JC           MICA        intrinsic  0.3761904438530041
```

To create an updated version of the database, download the ontology:
```shell
curl -L -O https://raw.githubusercontent.com/stemcellontologyresource/OSCI/master/src/ontology/osci.owl
```

And then create the new database:
```shell
python dishin.py osci.owl osci.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```


###  Cell Ontology (CL) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/cl202407.db.gz
gunzip -N cl202407.db.gz
```

Now to calculate the similarity between _neuronal stem cell_ and _sensory neuron_ execute:
```shell
python dishin.py cl.db CL_0000047 CL_0000101
```

Output:
```txt
Resnik       DiShIn      intrinsic  1.7731416175429349
Resnik       MICA        intrinsic  2.504915112519477
Lin          DiShIn      intrinsic  0.3003331215124555
Lin          MICA        intrinsic  0.4242802534346819
JC           DiShIn      intrinsic  0.10797329434564479
JC           MICA        intrinsic  0.12823797003111145
```

To create an updated version of the database, download the ontology:
```shell
curl -L -O http://purl.obolibrary.org/obo/cl.owl
```

And then create the new database:
```shell
python dishin.py cl.owl cl.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```


###  Environmental conditions, treatments and exposures ontology (ECTO) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/ecto202407.db.gz
gunzip -N ecto202407.db.gz
```

Now to calculate the similarity between _water vapour saturated air_ and _pressure of air_ execute:
```shell
python dishin.py ecto.db ENVO_01000829 ENVO_09200011
```

Output:
```txt
Resnik       DiShIn      intrinsic  0.3741060286214311
Resnik       MICA        intrinsic  0.3741060286214311
Lin          DiShIn      intrinsic  0.0435162446031204
Lin          MICA        intrinsic  0.0435162446031204
JC           DiShIn      intrinsic  0.057320898271413026
JC           MICA        intrinsic  0.057320898271413026
```

To create an updated version of the database, download the ontology:
```shell
curl -L -O http://purl.obolibrary.org/obo/ecto.owl
```

And then create the new database:
```shell
python dishin.py ecto.owl ecto.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

###  Environment Ontology (ENVO) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/envo202407.db.gz
gunzip -N envo202407.db.gz
```

Now to calculate the similarity between _water vapour saturated air_ and _pressure of air_ execute:
```shell
python dishin.py envo.db ENVO_01000829 ENVO_09200011
```

Output:
```txt
Resnik       DiShIn      intrinsic  0.09259857636092807
Resnik       MICA        intrinsic  0.09259857636092807
Lin          DiShIn      intrinsic  0.011463181071745975
Lin          MICA        intrinsic  0.011463181071745975
JC           DiShIn      intrinsic  0.05892533743160689
JC           MICA        intrinsic  0.05892533743160689
```

To create an updated version of the database, download the ontology:
```shell
curl -L -O http://purl.obolibrary.org/obo/envo.owl
```

And then create the new database:
```shell
python dishin.py envo.owl envo.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf ''
```

###  Medical Subject Headings (MeSH) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/mesh202407.db.gz
gunzip -N mesh202407.db.gz
```

Now to calculate the similarity between _Malignant Hyperthermia_ and _Fever_ execute:
```shell
python dishin.py mesh.db D008305 D005334
```

Output:
```txt
Resnik       DiShIn      intrinsic  3.6682439022751536
Resnik       MICA        intrinsic  6.131468006209348
Lin          DiShIn      intrinsic  0.5110825484632721
Lin          MICA        intrinsic  0.8542742461838173
JC           DiShIn      intrinsic  0.12471452425193749
JC           MICA        intrinsic  0.3234294846252581
```

To create an updated version of the database, download the _NT_ version from ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/mesh.nt.gz and unzip it:
```shell
curl -L -O ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/mesh.nt.gz
gunzip mesh.nt.gz
```
And then create the new database:
```shell
python dishin.py mesh.nt mesh.db http://id.nlm.nih.gov/mesh/ http://id.nlm.nih.gov/mesh/vocab#broaderDescriptor ''
```

### WordNet Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/wordnet202407.db.gz
gunzip -N wordnet202407.db.gz
```

Now to calculate the similarity between the nouns _ambulance_ and _motorcycle_ execute:
```shell
python dishin.py wordnet.db ambulance-noun-1 motorcycle-noun-1
```

Output:
```txt
Resnik       MICA        intrinsic  6.331085809208157
Lin          MICA        intrinsic  0.6792379292396559
JC           MICA        intrinsic  0.14327549414725688
```

To create an updated version of the database, download the ontology:
```shell
curl -L -O http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf
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

