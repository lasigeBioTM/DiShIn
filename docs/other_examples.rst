**************
Other Examples
**************

Semantic Similarity options
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can choose to calculate the measures using either the extrinsic or intrinsic Information Content (IC), and using the Most Informative Common Ancestors (MICA) or Disjunctive Common Ancestors (DCA). By default, the measures are calculated using extrinsic IC and DCA.

.. code-block:: python

     ssmpy.mica = False # determines if it uses MICA or DCA
     ssmpy.intrinsic = False # determines if it uses extrinsic or intrinsic IC



Gene Ontology (GO) and UniProt proteins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First download GO and annotations to your project directory:

.. code:: shell

    wget http://purl.obolibrary.org/obo/go.owl
    wget http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
    gunzip goa_uniprot_all_noiea.gaf.gz 

The annotations will be used to calculate the extrinsic information content.

Next create the semantic base:

.. code-block:: python

    ssmpy.create_semantic_base("go.owl", "go.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", "goa_uniprot_all_noiea.gaf

This is stored in the form of a sqlite database on the same directory of your project.

Now to calculate the similarity between *maltose biosynthetic process*
and *maltose catabolic process*, first we need to obtain the semantic base IDs of those concepts:


.. code:: shell

    ssmpy.semantic_base("go.db")
    e1 = ssmpy.get_id("GO_0000023")
    e2 = ssmpy.get_id("GO_0000025")
    ssmpy.ssm_resnik(e1,e2)

Output:

.. code:: python

    3.903220515643575

Now to calculate the similarity between proteins
`Q12345 <http://www.uniprot.org/uniprot/Q12345>`__ and
`Q12346 <http://www.uniprot.org/uniprot/Q12346>`__, first we retrieve the GO terms associated with each one:

.. code-block:: python

    e1 = ssmpy.get_uniprot_annotations("Q12345")
    e2 = ssmpy.get_uniprot_annotations("Q12346")

Next we use the ``ssm_multiple`` to calculate the average maximum semantic similarity, using the resnik measure

.. code:: python

    ssmpy.ssm_multiple(ssmpy.ssm_resnik, e1, e2)

Output:

.. code:: python

  0.4627295852212107

Chemical Entities of Biological Interest (ChEBI) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the ontology:

.. code:: shell

    wget ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/chebi_lite.owl

Create the semantic base:

.. code:: python

    ssmpy.create_semantic_base("chebi_lite.owl", "chebi.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

Now to calculate the similarity between *aripiprazole* and *bithionol*
execute:

.. code:: python

    ssmpy.semantic_base("chebi.db")
    e1 = ssmpy.get_id("CHEBI_31236")
    e2 = ssmpy.get_id("CHEBI_3131")
    ssmpy.ssm_resnik(e1,e2)

Output:

.. code:: python

    1.3534853833420923


Human Phenotype (HP) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the ontology:

.. code:: shell

    wget http://purl.obolibrary.org/obo/hp.owl

Create the semantic base:

.. code:: python

    ssmpy.create_semantic_base("hp.owl", "hp.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

Now to calculate the similarity between *Optic nerve coloboma* and
*Optic nerve dysplasia* execute:

.. code:: python

    ssmpy.semantic_base("hp.db")
    e1 = ssmpy.get_id("HP_0000588")
    e2 = ssmpy.get_id("HP_0001093")
    ssmpy.ssm_resnik(e1,e2)

Output:

.. code:: python

    3.0512068305931033

Human Disease Ontology (HDO) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the ontology:

.. code:: shell

    wget https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid.owl

Create the semantic base:

.. code:: python

    ssmpy.create_semantic_base("doid.owl", "doid.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

Now to calculate the similarity between *Asthma* and *Lung cancer*
execute:

.. code:: python

    ssmpy.semantic_base("doid.db")
    e1 = ssmpy.get_id("DOID_2841")
    e2 = ssmpy.get_id("DOID_1324")
    ssmpy.ssm_resnik(e1,e2)

Output:

.. code:: python

    2.29931853312


Radiology Lexicon (RadLex) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the *RDF/XML* version from
http://bioportal.bioontology.org/ontologies/RADLEX and save it as
*radlex.rdf*

Create the semantic base:

.. code:: python

    ssmpy.create_semantic_base("radlex.rdf", "radlex.db", "http://www.radlex.org/RID/#", "http://www.radlex.org/RID/#Is_A", '')

Now to calculate the similarity between *nervous system of right upper
limb* and *nervous system of left upper limb* execute:

.. code:: python

    ssmpy.semantic_base("radlex.db")
    e1 = ssmpy.get_id("RID16139")
    e2 = ssmpy.get_id("RID16140")
    ssmpy.ssm_resnik(e1,e2)

Output:

.. code:: python

    9.35897587112


WordNet Example
~~~~~~~~~~~~~~~

Download the ontology:

.. code:: shell

    wget http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf

Create the semantic base:

.. code:: python

    ssmpy.create_semantic_base("wordnet-hyponym.rdf", "wordnet.db", "http://www.w3.org/2006/03/wn/wn20/instances/synset-", "http://www.w3.org/2006/03/wn/wn20/schema/hyponymOf", '')

Now to calculate the similarity between the nouns *ambulance* and
*motorcycle* execute:

.. code:: python

    ssmpy.semantic_base("wordnet.db")
    e1 = ssmpy.get_id("ambulance-noun-1")
    e2 = ssmpy.get_id("motorcycle-noun-1")
    ssmpy.ssm_resnik(e1,e2)

Output:

.. code:: python

    6.33108580921
