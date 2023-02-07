# DiShIn: Semantic Similarity Measures using Disjunctive Shared Information

[![Downloads](https://pepy.tech/badge/ssmpy)](https://pepy.tech/project/ssmpy)

This software package provides the basic functions to start using semantic similarity measures directly from a rdf or owl file. 

A web tool using this package is available at: http://labs.fc.ul.pt/dishin/

Package documentation: https://dishin.readthedocs.io/en/latest/

** **NEW** **
- New examples addes, namely the ontologies: OSCI, CL, ECTO, and ENVO
- Databases updated: 202302
- Docker image available: https://hub.docker.com/r/fjmc/dishin-image

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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/go202302.db.gz
gunzip -N go202302.db.gz
```

Now to calculate the similarity between _maltose biosynthetic process_ and _maltose catabolic process_ execute:
```shell
python dishin.py go.db GO_0000023 GO_0000025
```

Output:
```txt
Resnik    DiShIn   intrinsic        3.78921500847647
Resnik    MICA     intrinsic        8.851627638869019
Lin       DiShIn   intrinsic        0.41195174078911123
Lin       MICA     intrinsic        0.9623215907495385
JC        DiShIn   intrinsic        0.08461688373053834
JC        MICA     intrinsic        0.5906161091496406
Resnik    DiShIn   extrinsic        4.310175268311233
Resnik    MICA     extrinsic        10.13641508423437
Lin       DiShIn   extrinsic        0.39394227804683757
Lin       MICA     extrinsic        0.9264501327520663
JC        DiShIn   extrinsic        0.07011679859284012
JC        MICA     extrinsic        0.3832242933372551
```

Now to calculate the similarity between proteins [Q12345](http://www.uniprot.org/uniprot/Q12345) and [Q12346](http://www.uniprot.org/uniprot/Q12346) execute:

```shell
python dishin.py go.db Q12345 Q12346
```

Output:
```txt
Resnik    DiShIn   intrinsic        1.0570711021304315
Resnik    MICA     intrinsic        1.0570711021304315
Lin       DiShIn   intrinsic        0.12958973249230304
Lin       MICA     intrinsic        0.12958973249230304
JC        DiShIn   intrinsic        0.07363762393108407
JC        MICA     intrinsic        0.07363762393108407
Resnik    DiShIn   extrinsic        0.47838902966531843
Resnik    MICA     extrinsic        0.47838902966531843
Lin       DiShIn   extrinsic        0.09255485176480098
Lin       MICA     extrinsic        0.09255485176480098
JC        DiShIn   extrinsic        0.09036345699860157
JC        MICA     extrinsic        0.09036345699860157
```

To create an updated version of the database, download the ontology and annotations:
```shell
curl -L -O http://purl.obolibrary.org/obo/go.owl
curl -L -O http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
gunzip goa_uniprot_all_noiea.gaf.gz 
```

And then create the new database:
```shell
python dishin.py go.owl go.db http://purl.obolibrary.org/obo/ http://www.w3.org/2000/01/rdf-schema#subClassOf goa_uniprot_all_noiea.gaf
```

###  Chemical Entities of Biological Interest (ChEBI) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/chebi202302.db.gz
gunzip -N chebi202302.db.gz
```

Now to calculate the similarity between _aripiprazole_ and _bithionol_ execute:
```shell
python dishin.py chebi.db CHEBI_31236 CHEBI_3131
```

Output:
```txt
Resnik    DiShIn   intrinsic        1.476632415671022
Resnik    MICA     intrinsic        5.641314851207291
Lin       DiShIn   intrinsic        0.13064609500712546
Lin       MICA     intrinsic        0.4991193124261839
JC        DiShIn   intrinsic        0.048421904489541145
JC        MICA     intrinsic        0.08115272103316418
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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/hp202302.db.gz
gunzip -N hp202302.db.gz
```

Now to calculate the similarity between _Optic nerve coloboma_ and _Optic nerve dysplasia_ execute:
```shell
python dishin.py hp.db HP_0000588 HP_0001093
```

Output:
```txt
Resnik    DiShIn   intrinsic        4.617876786673204
Resnik    MICA     intrinsic        5.995918897457362
Lin       DiShIn   intrinsic        0.5108021406767812
Lin       MICA     intrinsic        0.6632329855539579
JC        DiShIn   intrinsic        0.10157307132754399
JC        MICA     intrinsic        0.14106272672409434
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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/doid202302.db.gz
gunzip -N doid202302.db.gz
```

Now to calculate the similarity between _Asthma_ and _Lung cancer_ execute:
```shell
python dishin.py doid.db DOID_2841 DOID_1324
```

Output:
```txt
Resnik    DiShIn   intrinsic        2.4006601711893345
Resnik    MICA     intrinsic        3.8437441646748516
Lin       DiShIn   intrinsic        0.4363310773119593
Lin       MICA     intrinsic        0.6986182602651521
JC        DiShIn   intrinsic        0.13884016970564805
JC        MICA     intrinsic        0.23167677096337774
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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/osci202302.db.gz
gunzip -N osci202302.db.gz
```

Now to calculate the similarity between _neuronal stem cell_ and _sensory neuron_ execute:
```shell
python dishin.py osci.db CL_0000047 CL_0000101
```

Output:
```txt
Resnik    DiShIn   intrinsic        3.1560550137337486
Resnik    MICA     intrinsic        4.1255971057262055
Lin       DiShIn   intrinsic        0.6369806275261506
Lin       MICA     intrinsic        0.8326614782980606
JC        DiShIn   intrinsic        0.21751839842873807
JC        MICA     intrinsic        0.3761904438530041
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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/cl202302.db.gz
gunzip -N cl202302.db.gz
```

Now to calculate the similarity between _neuronal stem cell_ and _sensory neuron_ execute:
```shell
python dishin.py cl.db CL_0000047 CL_0000101
```

Output:
```txt
Resnik    DiShIn   intrinsic        1.9063375764548978
Resnik    MICA     intrinsic        2.6866433997198857
Lin       DiShIn   intrinsic        0.3272258822885516
Lin       MICA     intrinsic        0.4611666200814948
JC        DiShIn   intrinsic        0.11313710298029131
JC        MICA     intrinsic        0.1373961991624287
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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/ecto202302.db.gz
gunzip -N ecto202302.db.gz
```

Now to calculate the similarity between _water vapour saturated air_ and _pressure of air_ execute:
```shell
python dishin.py ecto.db ENVO_01000829 ENVO_09200011
```

Output:
```txt
Resnik    DiShIn   intrinsic        0.4783673341124399
Resnik    MICA     intrinsic        0.4783673341124399
Lin       DiShIn   intrinsic        0.052996013929053794
Lin       MICA     intrinsic        0.052996013929053794
JC        DiShIn   intrinsic        0.05526015750810917
JC        MICA     intrinsic        0.05526015750810917
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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/envo202302.db.gz
gunzip -N envo202302.db.gz
```

Now to calculate the similarity between _water vapour saturated air_ and _pressure of air_ execute:
```shell
python dishin.py envo.db ENVO_01000829 ENVO_09200011
```

Output:
```txt
Resnik    DiShIn   intrinsic        0.10095128489526445
Resnik    MICA     intrinsic        0.10095128489526445
Lin       DiShIn   intrinsic        0.012723633698085534
Lin       MICA     intrinsic        0.012723633698085534
JC        DiShIn   intrinsic        0.06000093158424831
JC        MICA     intrinsic        0.06000093158424831
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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/mesh202302.db.gz
gunzip -N mesh202302.db.gz
```

Now to calculate the similarity between _Malignant Hyperthermia_ and _Fever_ execute:
```shell
python dishin.py mesh.db D008305 D005334
```

Output:
```txt
Resnik    DiShIn   intrinsic        3.652230798230297
Resnik    MICA     intrinsic        6.113436328571005
Lin       DiShIn   intrinsic        0.510133103212917
Lin       MICA     intrinsic        0.8539072194176971
JC        DiShIn   intrinsic        0.1247773485102854
JC        MICA     intrinsic        0.3234294846252581
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

###  Radiology Lexicon (RadLex) Example

Download the lastest version of the database we created:
```shell
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/radlex202302.db.gz
gunzip -N radlex202302.db.gz
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
curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/wordnet202302.db.gz
gunzip -N wordnet202302.db.gz
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

