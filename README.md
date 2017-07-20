# DiShIn: Semantic Similarity Measures using Disjunctive Shared Information

This software package provides the basic functions to start using semantic similarity measures directly from a rdf or owl file. 

- semanticbase.py : provides a function to produce the semantic-base as a SQLite database 

- ssm.py : provides the functions to calculate semantic similarity based on teh SQLite database

- metals.py : provides examples of semantric similarity for the metals.owl 

- chebi.py : provides examples for the ChEBI ontology; OWL file:  ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/

- go.py : provides examples for the Gene Ontology (GO) ontology; OWL file: http://geneontology.org/page/download-ontology#go.obo_and_go.owl; Annotation files (extrinsic): http://www.geneontology.org/page/download-annotations

- hpo.py : provides examples for the Human Phenotype ontology (HPO); OWL file: http://human-phenotype-ontology.github.io/downloads.html

- wordnet.py : provides examples for the WordNet; OWL file: <http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf>

Notice that we should comment the semanticbase.create call after the .db file has been created, and only uncomment it when a new version of the owl file is available.

A web tool using this package is available at: http://labs.fc.ul.pt/dishin/

## References: 

- F. Couto and H. Pinto, The next generation of similarity measures that fully explore the semantics in biomedical ontologies, Journal of Bioinformatics and Computational Biology, vol. 11, no. 1371001, pp. 1-12, 2013 (http://dx.doi.org/10.1142/S0219720013710017)

- F. Couto and M. Silva, Disjunctive shared information between ontology concepts: application to Gene Ontology, Journal of Biomedical Semantics, vol. 2, no. 5, pp. 1-16, 2011 (http://dx.doi.org/10.1186/2041-1480-2-5)
