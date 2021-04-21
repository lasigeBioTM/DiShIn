**************
Other Examples
**************


The following examples will assume the default options, i.e. the values shown are calculated using extrinsic IC and DCA.     


Gene Ontology (GO) and UniProt proteins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the latest version of the database we created:

.. code:: shell

     wget http://labs.rd.ciencias.ulisboa.pt/dishin/go202104.db.gz
     gunzip -N go202104.db.gz

Now to calculate the similarity between *maltose biosynthetic process*
and *maltose catabolic process*, first we need to obtain the semantic base IDs of those concepts:

.. code:: python

    ssmpy.semantic_base("go.db")
    e1 = ssmpy.get_id("GO_0000023")
    e2 = ssmpy.get_id("GO_0000025")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    4.315813746201754
    0.38793452313030363
    0.06840605034663635

Now to calculate the similarity between proteins
`Q12345 <http://www.uniprot.org/uniprot/Q12345>`__ and
`Q12346 <http://www.uniprot.org/uniprot/Q12346>`__, first we retrieve the GO terms associated with each one:

.. code-block:: python

    e1 = ssmpy.get_uniprot_annotations("Q12345")
    e2 = ssmpy.get_uniprot_annotations("Q12346")

Next we use the ``ssm_multiple`` to calculate the average maximum semantic similarity, using the resnik measure

.. code:: python

    ssmpy.ssm_multiple(ssmpy.ssm_resnik, e1, e2)
    ssmpy.ssm_multiple(ssmpy.ssm_lin, e1, e2)
    ssmpy.ssm_multiple(ssmpy.ssm_jiang_conrath, e1, e2)

Output:

.. code:: python

  0.6015115682274214
  0.12201023476842265
  0.09317326288224918


To create an updated version of the database, download the ontology and annotations:

.. code:: shell
     
    wget http://purl.obolibrary.org/obo/go.owl
    wget http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
    gunzip goa_uniprot_all_noiea.gaf.gz 

The annotations will be used to calculate the extrinsic information content.

Next create the semantic base:

.. code:: python

    ssmpy.create_semantic_base("go.owl", "go.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", "goa_uniprot_all_noiea.gaf)

This is stored in the form of a sqlite database on the same directory of your project.

    
Chemical Entities of Biological Interest (ChEBI) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell
          
     wget http://labs.rd.ciencias.ulisboa.pt/dishin/chebi202104.db.gz
     gunzip -N chebi202104.db.gz


Now to calculate the similarity between *aripiprazole* and *bithionol*
execute:

.. code:: python

    ssmpy.semantic_base("chebi.db")
    e1 = ssmpy.get_id("CHEBI_31236")
    e2 = ssmpy.get_id("CHEBI_3131")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)


Output:

.. code:: python

     1.4393842298350599
     0.12935491517581163
     0.049077257018319796

To create an updated version of the database, download the ontology:

.. code:: shell

    wget http://purl.obolibrary.org/obo/chebi/chebi_lite.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("chebi_lite.owl", "chebi.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

    
Human Phenotype (HP) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     wget http://labs.rd.ciencias.ulisboa.pt/dishin/hp202104.db.gz
     gunzip -N hp202104.db.gz

Now to calculate the similarity between *Optic nerve coloboma* and
*Optic nerve dysplasia* execute:

.. code:: python

    ssmpy.semantic_base("hp.db")
    e1 = ssmpy.get_id("HP_0000588")
    e2 = ssmpy.get_id("HP_0001093")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    4.593979372426621
    0.5118244533189668
    0.10242304162282165


To create an updated version of the database, download the ontology:

.. code:: shell

    wget http://purl.obolibrary.org/obo/hp.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("hp.owl", "hp.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

    
Human Disease Ontology (HDO) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     wget http://labs.rd.ciencias.ulisboa.pt/dishin/doid202104.db.gz
     gunzip -N doid202104.db.gz

Now to calculate the similarity between *Asthma* and *Lung cancer*
execute:

.. code:: python

    ssmpy.semantic_base("doid.db")
    e1 = ssmpy.get_id("DOID_2841")
    e2 = ssmpy.get_id("DOID_1324")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    2.3627836143597176
    0.4328907089097581
    0.13906777879867938

To create an updated version of the database, download the ontology:

.. code:: shell

     wget http://purl.obolibrary.org/obo/doid.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("doid.owl", "doid.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

Medical Subject Headings (MeSH) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     wget http://labs.rd.ciencias.ulisboa.pt/dishin/mesh202104.db.gz
     gunzip -N mesh202104.db.gz

Now to calculate the similarity between *Malignant Hyperthermia* and *Fever*
execute:

.. code:: python

    ssmpy.semantic_base("mesh.db")
    e1 = ssmpy.get_id("D008305")
    e2 = ssmpy.get_id("D005334")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    1.2582571367910345
    0.17390901691859173
    0.07719755683816652

To create an updated version of the database, download the _NT_ version from ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/mesh.nt.gz and unzip it:

.. code:: shell

     wget ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/mesh.nt.gz
     gunzip mesh.nt.gz

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("mesh.nt", "mesh.db", "http://id.nlm.nih.gov/mesh/", "http://id.nlm.nih.gov/mesh/vocab#broaderDescriptor", '')
    
Radiology Lexicon (RadLex) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     wget http://labs.rd.ciencias.ulisboa.pt/dishin/radlex202104.db.gz
     gunzip -N radlex202104.db.gz


Now to calculate the similarity between *nervous system of right upper
limb* and *nervous system of left upper limb* execute:

.. code:: python

    ssmpy.semantic_base("radlex.db")
    e1 = ssmpy.get_id("RID16139")
    e2 = ssmpy.get_id("RID16140")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    9.366531825151093
    0.9310964912333252
    0.41905978419640516

To create an updated version of the database, download the *RDF/XML* version from http://bioportal.bioontology.org/ontologies/RADLEX and save it as *radlex.rdf*

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("radlex.rdf", "radlex.db", "http://www.radlex.org/RID/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')


WordNet Example
~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     wget http://labs.rd.ciencias.ulisboa.pt/dishin/wordnet202104.db.gz
     gunzip -N wordnet202104.db.gz


Now to calculate the similarity between the nouns *ambulance* and
*motorcycle* execute:

.. code:: python

    ssmpy.semantic_base("wordnet.db")
    e1 = ssmpy.get_id("ambulance-noun-1")
    e2 = ssmpy.get_id("motorcycle-noun-1")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    6.331085809208157
    0.6792379292396559
    0.14327549414725688

To create an updated version of the database, download the ontology:

.. code:: shell

    wget http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("wordnet-hyponym.rdf", "wordnet.db", "http://www.w3.org/2006/03/wn/wn20/instances/synset-", "http://www.w3.org/2006/03/wn/wn20/schema/hyponymOf", '')
