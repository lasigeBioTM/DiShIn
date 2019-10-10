
****************
Getting started
****************


Installation
=============

Either clone this repository or install from pypi:

::

    pip install ssmpy

Quick start
============

.. code::

    import ssmpy

Metals Example
~~~~~~~~~~~~~~




To create the semantic base file (*metals.db*) from the `metals.owl  <https://github.com/lasigeBioTM/DiShIn/blob/master/metals.owl>`_
file:

.. code-block:: python

    ssmpy.create_semantic_base("metals.owl", "metals.db", "https://raw.githubusercontent.com/lasigeBioTM/ssm/master/metals.owl#", "http://www.w3.org/2000/01/rdf-schema#subClassOf", "metals.txt")
    ssmpy.semantic_base("metals.db")


The *metals.txt* contains the a list of occurrences. For example, the
following contents has one occurrence for each term, except gold and
silver with two occurrences.
::  

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

Now to calculate the similarity between *copper* and *gold* execute

.. code-block:: python

    e1 = ssmpy.get_id("copper")
    e2 = ssmpy.get_id("gold")
    ssmpy.ssm_resnik (e1,e2)

Output:

.. code-block:: python

    0.22599256187152864





