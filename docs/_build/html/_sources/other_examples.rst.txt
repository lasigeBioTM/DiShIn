**************
Other Examples
**************


The following examples will assume the default options, i.e. the values shown are calculated using extrinsic IC and DCA.     


Gene Ontology (GO) and UniProt proteins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the latest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/go202302.db.gz
     gunzip -N go202302.db.gz

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

    4.310175268311233
    0.39394227804683757
    0.07011679859284012

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

   0.47838902966531843
   0.09255485176480098
   0.09036345699860157

To create an updated version of the database, download the ontology and annotations:

.. code:: shell
     
    curl -L -O http://purl.obolibrary.org/obo/go.owl
    curl -L -O http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
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
          
     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/chebi202302.db.gz
     gunzip -N chebi202302.db.gz


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

     1.476632415671022
     0.13064609500712546
     0.048421904489541145

To create an updated version of the database, download the ontology:

.. code:: shell

    curl -L -O http://purl.obolibrary.org/obo/chebi/chebi_lite.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("chebi_lite.owl", "chebi.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

    
Human Phenotype (HP) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/hp202302.db.gz
     gunzip -N hp202302.db.gz

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

    4.617876786673204
    0.5108021406767812
    0.10157307132754399

To create an updated version of the database, download the ontology:

.. code:: shell

    curl -L -O http://purl.obolibrary.org/obo/hp.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("hp.owl", "hp.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

    
Human Disease Ontology (HDO) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/doid202302.db.gz
     gunzip -N doid202302.db.gz

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

    2.4006601711893345
    0.4363310773119593
    0.13884016970564805

To create an updated version of the database, download the ontology:

.. code:: shell

     curl -L -O http://purl.obolibrary.org/obo/doid.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("doid.owl", "doid.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

Ontology for Stem Cell Investigations (OSCI) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/osci202302.db.gz
     gunzip -N osci202302.db.gz

Now to calculate the similarity between *neuronal stem cell* and *sensory neuron*
execute:

.. code:: python

    ssmpy.semantic_base("osci.db")
    e1 = ssmpy.get_id("CL_0000047")
    e2 = ssmpy.get_id("CL_0000101")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    3.1560550137337486
    0.6369806275261506
    0.21751839842873807

To create an updated version of the database, download the ontology:

.. code:: shell

     curl -L -O https://raw.githubusercontent.com/stemcellontologyresource/OSCI/master/src/ontology/osci.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("osci.owl", "osci.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

Cell Ontology (CL)
~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/cl202302.db.gz
     gunzip -N cl202302.db.gz

Now to calculate the similarity between *neuronal stem cell* and *sensory neuron*
execute:

.. code:: python

    ssmpy.semantic_base("cl.db")
    e1 = ssmpy.get_id("CL_0000047")
    e2 = ssmpy.get_id("CL_0000101")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    1.9063375764548978
    0.3272258822885516
    0.11313710298029131

To create an updated version of the database, download the ontology:

.. code:: shell

     curl -L -O http://purl.obolibrary.org/obo/cl.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("cl.owl", "cl.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

Environmental conditions, treatments and exposures ontology (ECTO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/ecto202302.db.gz
     gunzip -N ecto202302.db.gz

Now to calculate the similarity between *water vapour saturated air* and *pressure of air*
execute:

.. code:: python

    ssmpy.semantic_base("ecto.db")
    e1 = ssmpy.get_id("ENVO:01000829")
    e2 = ssmpy.get_id("ENVO:09200011")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    0.4783673341124399
    0.052996013929053794
    0.05526015750810917

To create an updated version of the database, download the ontology:

.. code:: shell

     curl -L -O http://purl.obolibrary.org/obo/ecto.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("ecto.owl", "ecto.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')

Environment Ontology (ENVO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/envo202302.db.gz
     gunzip -N envo202302.db.gz

Now to calculate the similarity between *water vapour saturated air* and *pressure of air*
execute:

.. code:: python

    ssmpy.semantic_base("envo.db")
    e1 = ssmpy.get_id("ENVO:01000829")
    e2 = ssmpy.get_id("ENVO:09200011")
    ssmpy.ssm_resnik(e1,e2)
    ssmpy.ssm_lin(e1,e2)
    ssmpy.ssm_jiang_conrath(e1,e2)

Output:

.. code:: python

    0.10095128489526445
    0.012723633698085534
    0.06000093158424831

To create an updated version of the database, download the ontology:

.. code:: shell

     curl -L -O http://purl.obolibrary.org/obo/envo.owl

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("envo.owl", "envo.db", "http://purl.obolibrary.org/obo/", "http://www.w3.org/2000/01/rdf-schema#subClassOf", '')


Medical Subject Headings (MeSH) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/mesh202302.db.gz
     gunzip -N mesh202302.db.gz

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

    3.652230798230297
    0.510133103212917
    0.1247773485102854


To create an updated version of the database, download the _NT_ version from ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/mesh.nt.gz and unzip it:

.. code:: shell

     curl -L -O ftp://nlmpubs.nlm.nih.gov/online/mesh/rdf/mesh.nt.gz
     gunzip mesh.nt.gz

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("mesh.nt", "mesh.db", "http://id.nlm.nih.gov/mesh/", "http://id.nlm.nih.gov/mesh/vocab#broaderDescriptor", '')
    
Radiology Lexicon (RadLex) Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the lastest version of the database we created:

.. code:: shell

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/radlex202302.db.gz
     gunzip -N radlex202302.db.gz


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

     curl -L -O http://labs.rd.ciencias.ulisboa.pt/dishin/wordnet202302.db.gz
     gunzip -N wordnet202302.db.gz


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

    curl -L -O http://www.w3.org/2006/03/wn/wn20/rdf/wordnet-hyponym.rdf

And then create the new database:

.. code:: python

    ssmpy.create_semantic_base("wordnet-hyponym.rdf", "wordnet.db", "http://www.w3.org/2006/03/wn/wn20/instances/synset-", "http://www.w3.org/2006/03/wn/wn20/schema/hyponymOf", '')
