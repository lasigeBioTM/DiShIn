# DiShIn: Semantic Similarity Measures using Disjunctive Shared Information

This software package provides the basic functions to start using semantic similarity measures directly from a rdf or owl file. 

A web tool using this package is available at: http://labs.fc.ul.pt/dishin/


## USAGE: 

### Metals Example

```
$ python3 metals.py

copper http://www.w3.org/2000/01/rdf-schema#subClassOf coinage
gold http://www.w3.org/2000/01/rdf-schema#subClassOf precious
silver http://www.w3.org/2000/01/rdf-schema#subClassOf coinage
coinage http://www.w3.org/2000/01/rdf-schema#subClassOf metal
gold http://www.w3.org/2000/01/rdf-schema#subClassOf coinage
silver http://www.w3.org/2000/01/rdf-schema#subClassOf precious
platinum http://www.w3.org/2000/01/rdf-schema#subClassOf precious
precious http://www.w3.org/2000/01/rdf-schema#subClassOf metal
palladium http://www.w3.org/2000/01/rdf-schema#subClassOf precious
distance 2
distance 3
resnik dishin extrinsic similarity platinum gold = 0.20273255405408222
                            mathematical formula = 0.20273255405408222
       resnik mica extrinsic similarity platinum gold = 0.40546510810816444
                                 mathematical formula = 0.40546510810816444
          lin mica extrinsic similarity platinum gold = 0.2695772896908149
                                 mathematical formula = 0.2695772896908149
jiang-conrath mica extrinsic similarity platinum gold = 0.45511961331341866
                                 mathematical formula = 0.45511961331341866
resnik **mica** extrinsic similarity:
   platinum copper    = -0.0
   platinum gold      = 0.40546510810816444
   copper gold        = 0.587786664902119
   platinum palladium = 0.40546510810816444
   silver gold        = 0.587786664902119
resnik **dishin** extrinsic similarity:
   platinum copper    = 0.0
   platinum gold      = 0.20273255405408222
   copper gold        = 0.2938933324510595
   platinum palladium = 0.40546510810816444
   silver gold        = 0.587786664902119
```

### Disease Ontology Example


- download owl file

```
$ wget https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid-simple.owl
```

- in file disease.py uncomment the line:
```
 semanticbase.create('doid-simple.owl', 'disease.db', 'http://purl.obolibrary.org/obo/', 'http://www.w3.org/2000/01/rdf-schema#subClassOf', '')
```

- run the example (it takes some time to create the disease.db for the first time)

```
$ python3 disease.py

The id of Asthma is 161
The id of Pneumonia is 604
resnik dishin intrinsic similarity = 3.9933387877484807
resnik mica intrinsic similarity = 3.9933387877484807
lin mica intrinsic similarity = 0.60218242131915
```
- do not forget to comment line semanticbase.create after the first execution


### Add a new ontology named newonto

- create a new py file
```
cp disease.py newonto.py
```
- in file newonto.py uncomment the line, and edit the parameters accordingly:
```
 semanticbase.create('newonto.owl', 'newonto.db', 'http://purl.obolibrary.org/obo/', 'http://www.w3.org/2000/01/rdf-schema#subClassOf', '')
```

- find some id's of the ontology to test and replace them in the lines
```
e1 = ssm.get_id('DOID_2841') # Asthma
e2 = ssm.get_id('DOID_552') # Pneumonia
```
- finally execute the example
```
$ python3 newonto.py
```

## Files

- semanticbase.py : provides a function to produce the semantic-base as a SQLite database (to work in python v2 please check the comments in the get_uniprot_annotations function)

- ssm.py : provides the functions to calculate semantic similarity based on the SQLite database

- metals.py : provides examples of semantric similarity for the metals.owl 

- chebi.py : provides examples for the ChEBI ontology; OWL file:  ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/

- go.py : provides examples for the Gene Ontology (GO) ontology; OWL file: http://geneontology.org/page/download-ontology#go.obo_and_go.owl; Annotation files (extrinsic): http://www.geneontology.org/page/download-annotations

- uniprot.py : provides examples of using GO annotations to calculate the semantic similarity between a list of proteins in UniProt: http://www.uniprot.org/

- hpo.py : provides examples for the Human Phenotype ontology (HPO); OWL file: http://human-phenotype-ontology.github.io/downloads.html

- disease.py : provides examples for the Human Disease Ontology (DO); OWL file: https://github.com/DiseaseOntology/HumanDiseaseOntology/tree/master/src/ontology

- radlex.py : provides examples for the RadLex; RDF file: https://bioportal.bioontology.org/ontologies/RADLEX

- wordnet.py : provides examples for the WordNet; OWL file: http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf

Notice that we should comment the semanticbase.create call after the .db file has been created, and only uncomment it when a new version of the owl file is available.


## References: 

- F. Couto and A. Lamurias, “Semantic similarity definition,” in Reference Module in Life Sciences (Encyclopedia of Bioinformatics and Computational Biology), pp. 1--17, Elsevier, 2018 (https://doi.org/10.1016/B978-0-12-809633-8.20401-9, https://www.researchgate.net/publication/323219905_Semantic_Similarity_Definition)

- F. Couto and H. Pinto, The next generation of similarity measures that fully explore the semantics in biomedical ontologies, Journal of Bioinformatics and Computational Biology, vol. 11, no. 1371001, pp. 1-12, 2013 (http://dx.doi.org/10.1142/S0219720013710017)

- F. Couto and M. Silva, Disjunctive shared information between ontology concepts: application to Gene Ontology, Journal of Biomedical Semantics, vol. 2, no. 5, pp. 1-16, 2011 (http://dx.doi.org/10.1186/2041-1480-2-5)
