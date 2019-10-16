###############################################################################
#                                                                             #
# Licensed under the Apache License, Version 2.0 (the "License"); you may     #
# not use this file except in compliance with the License. You may obtain a   #
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0           #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS,           #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
# See the License for the specific language governing permissions and         #
# limitations under the License.                                              #
#                                                                             #
###############################################################################
#                                                                             #
# Software developed based on the work published in the following articles:   #
# - F. Couto and A. Lamurias, "Semantic similarity definition," in Reference  #
#   Module in Life Sciences (Encyclopedia of Bioinformatics and Computational #
#   Biology), pp. 1--17, Elsevier, 2018                                       #
#   https://doi.org/10.1016/B978-0-12-809633-8.20401-9,                       #
#   https://www.researchgate.net/publication/323219905                        #
#                                                                             #
# @author Francisco M. Couto                                                  #
###############################################################################

import sqlite3
import math

intrinsic = False
mica = False


def semantic_base(sb_file, **kwargs):
    """Initialize global connection object.
    
    You can also pass other arguments to be given to the sqlite3.connect method, for example ``check_same_thread``.
    After this method is called, the other methods will be applied to the semantic base.

    :param sb_file: sqlite database filename
    :type sb_file: string

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")

    """
    global connection

    connection = sqlite3.connect(sb_file, **kwargs)


def run_query(query, params):
    """Run any query on the semantic base.

    :param query: query to run on the semantic base
    :type query: string
    :param params: query parameters
    :type params: tuple
    :returns: query result
    :rtype: sqlite3.Cursor

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> query = "SELECT id FROM entry WHERE name = ?"
        >>> ssmpy.run_query(query, ("gold",)).fetchone()
        (3,)
    """
    rows = connection.execute(query, params)
    return rows


def get_id(name):
    """Get semantic base ID of ontolgy concept by its original label (name).
    
    :param name: ontology label (depends on the ontolgy)
    :type name: string
    :return: semantic base ID or -1 if not found
    :rtype: int

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> ssmpy.get_id("gold")
        3
    """

    rows = connection.execute(
        """
        SELECT id
        FROM entry
        WHERE name = ?
    """,
        (name,),
    )

    row = rows.fetchone()
    if row is None:
        iden = -1
    else:
        iden = row[0]

    return iden


def get_name(cid):
    """Get ontology label (name) for a given semantic base ID.

    :param cid: semantic base ID
    :type cid: int
    :return: ontology label (name)
    :rtype: string

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> ssmpy.get_name(3)
        'gold'
    """

    rows = connection.execute(
        """
       SELECT name
       FROM entry
       WHERE id = ?
    """,
        (cid,),
    )

    row = rows.fetchone()
    if row is None:
        iden = -1
    else:
        iden = row[0]

    return iden


def get_ancestors(entry):
    """Get ancestors of a given semantic base entry

    :param entry: semantic base ID
    :type entry: int
    :return: List of ancestors
    :rtype: list


    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> ssmpy.get_ancestors(gold)
        [3, 6, 2, 10]
    """
    ancestors = []

    rows = connection.execute(
        """
        SELECT DISTINCT t1.entry2
        FROM entry e, transitive t1
        WHERE t1.entry1=?
        AND e.id=t1.entry2
        ORDER BY e.freq
        """,
        (entry,),
    )

    for row in rows:
        ancestors.append(row[0])
    return ancestors


def common_ancestors(entry1, entry2):
    """Get common ancestors between two semantic base entries

    :param entry1: first semantic base ID
    :type entry1: int
    :param entry1: second semantic base ID
    :type entry1: int
    :return: List of common ancestors
    :rtype: list


    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> silver = ssmpy.get_id("silver")
        >>> ssmpy.common_ancestors(gold, silver)
        [6, 2, 10]
    """

    ancestors = []

    rows = connection.execute(
        """
        SELECT DISTINCT t1.entry2
        FROM entry e, transitive t1, transitive t2
        WHERE t1.entry1=? AND t2.entry1=? AND t1.entry2=t2.entry2
        AND e.id=t1.entry2
        ORDER BY e.freq
        """,
        (entry1, entry2),
    )

    for row in rows:
        ancestors.append(row[0])
    return ancestors


def information_content_extrinsic(entry):
    """Get the extrinsic information content of a semantic base entry.

    The values are precomputated at the time of creation of the semantic base according to
    the annotations file provided.

    
    :param entry: semantic base ID
    :type entry: int
    :return: extrinsic information content
    :rtype: float


    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> ssmpy.information_content_extrinsic(gold)
        1.2992829841302609
    """
    rows = connection.execute(
        """
        SELECT e.freq
        FROM entry e
        WHERE e.id = ?
        """,
        (entry,),
    )
    freq = rows.fetchone()[0] + 1.0
    # print (freq)

    rows = connection.execute(
        """
        SELECT MAX(e.freq)
        FROM entry e
        """
    )
    maxfreq = rows.fetchone()[0] + 1.0

    return -math.log(freq / maxfreq)


def information_content_intrinsic(entry):
    """Get the intrinsic information content of a semantic base entry.

    
    :param entry: semantic base ID
    :type entry: int
    :return: intrinsic information content
    :rtype: float


    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> ssmpy.information_content_intrinsic(gold)
        1.5040773967762742
    """

    # print entry
    rows = connection.execute(
        """
        SELECT e.desc
        FROM entry e
        WHERE e.id = ?
        """,
        (entry,),
    )
    freq = rows.fetchone()[0] + 1.0
    # print (freq)

    rows = connection.execute(
        """
        SELECT MAX(e.desc)
        FROM entry e
        """
    )
    maxfreq = rows.fetchone()[0] + 1.0

    return -math.log(freq / maxfreq)


def information_content(entry):
    """Get information content of a semantic base entry according to intrinsic.

    
    :param entry: semantic base ID
    :type entry: int
    :return: information content
    :rtype: float


    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> ssmpy.ssm.intrinsic = True
        >>> ssmpy.information_content(gold)
        1.5040773967762742
    """

    if intrinsic:
        return information_content_intrinsic(entry)
    else:
        return information_content_extrinsic(entry)


def num_paths(entry1, ancestor):
    """Get number of paths (edges) between two concepts.

    :param entry1: Child concept
    :type entry1: int
    :param ancestor: Parent concept
    :type ancestor: int
    :return: number of edges between the two concepts
    :rtype: int

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> metal = ssmpy.get_id("metal")
        >>> ssmpy.num_paths(gold, metal)
        5
    """

    rows = connection.execute(
        """
        SELECT COUNT(*)
        FROM transitive t
        WHERE t.entry1=? AND t.entry2=? 
        """,
        (entry1, ancestor),
    )

    npaths = rows.fetchone()[0] + 1

    return npaths


def shared_ic_dca(entry1, entry2):
    """Calculate the shared information content of two concepts using disjunctive common ancestors.

    :param entry1: First concept
    :type entry1: int
    :param ancestor: Second concept
    :type ancestor: int
    :return: Shared information content
    :rtype: float

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> silver = ssmpy.get_id("silver")
        >>> ssmpy.shared_ic_dca(gold, silver)
        0.587786664902119
    """

    ancestors = common_ancestors(entry1, entry2)
    dca = {}

    for anc in ancestors:
        pd = abs(num_paths(entry1, anc) - num_paths(entry2, anc))
        ic = information_content(anc)
        dca[pd] = max(information_content(anc), dca.get(pd, 0))

    values = dca.values()

    if len(values) > 0:
        ret = sum(values) / len(values)
    else:
        ret = 0

    return ret


def shared_ic_mica(entry1, entry2):
    """Calculate the shared information content of two concepts using the most informative common ancestor.

    :param entry1: First concept
    :type entry1: int
    :param ancestor: Second concept
    :type ancestor: int
    :return: Shared information content
    :rtype: float

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> silver = ssmpy.get_id("silver")
        >>> ssmpy.shared_ic_mica(gold, silver)
        0.587786664902119
    """

    ic = 0

    ancestors = common_ancestors(entry1, entry2)

    for anc in ancestors:
        ic = max(information_content(anc), ic)

    return ic


shared_ic_cache = {}


def shared_ic(entry1, entry2):
    """Calculate the shared information content of two concepts according to the value of ssmpy.ssm.mica

    Previously computed values are stored in memory for faster computation.

    :param entry1: First concept
    :type entry1: int
    :param ancestor: Second concept
    :type ancestor: int
    :return: Shared information content
    :rtype: float

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> silver = ssmpy.get_id("silver")
        >>> ssmpy.ssm.mica = True
        >>> ssmpy.shared_ic(gold, silver)
        0.587786664902119
    """

    value = 0
    key_cache = (
        str(mica)
        + ":"
        + str(intrinsic)
        + ":"
        + str(max(entry1, entry2))
        + ":"
        + str(min(entry1, entry2))
    )
    value = shared_ic_cache.get(key_cache, -1)

    if value == -1:
        if mica:
            value = shared_ic_mica(entry1, entry2)
        else:
            value = shared_ic_dca(entry1, entry2)
        shared_ic_cache[key_cache] = value

    return value


def ssm_resnik(entry1, entry2):
    """Calculate Resnik's semantic similarity.

    :param entry1: First concept
    :type entry1: int
    :param ancestor: Second concept
    :type ancestor: int
    :return: Semantic similarity
    :rtype: float

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> silver = ssmpy.get_id("silver")
        >>> ssmpy.ssm_resnik(gold, silver)
        0.587786664902119
    """

    return abs(shared_ic(entry1, entry2))


def ssm_lin(entry1, entry2):
    """Calculate Lin's semantic similarity.

    :param entry1: First concept
    :type entry1: int
    :param ancestor: Second concept
    :type ancestor: int
    :return: Semantic similarity
    :rtype: float

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> silver = ssmpy.get_id("silver")
        >>> ssmpy.ssm_lin(gold, silver)
        0.39079549108439265
    """
    aux = information_content(entry1) + information_content(entry2)

    if aux > 0:
        return 2 * shared_ic(entry1, entry2) / aux
    else:
        return 1.0


def ssm_jiang_conrath(entry1, entry2):
    """Calculate JC's semantic similarity.

    :param entry1: First concept
    :type entry1: int
    :param ancestor: Second concept
    :type ancestor: int
    :return: Semantic similarity
    :rtype: float

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("https://github.com/lasigeBioTM/DiShIn/raw/master/metals.db", "metals.db")[0]
        'metals.db'
        >>> ssmpy.semantic_base("metals.db")
        >>> gold = ssmpy.get_id("gold")
        >>> silver = ssmpy.get_id("silver")
        >>> ssmpy.ssm_jiang_conrath(gold, silver)
        0.5456783339686456
    """

    distance = (
        information_content(entry1)
        + information_content(entry2)
        - 2 * shared_ic(entry1, entry2)
    )
    if distance > 0:
        return 1 / distance
    else:
        return 1.0


def ssm_multiple(m, entry1_list, entry2_list):
    """Calculate semantic similarity over two lists of concepts.
    
    :param m: semantic similarity function
    :param entry1_list: First concept list
    :param entry2_list: Second concept list
    :return: Aggregate Similarity Measure
    :rtype: float

    :Example:
        >>> import ssmpy
        >>> import urllib.request
        >>> urllib.request.urlretrieve("http://labs.rd.ciencias.ulisboa.pt/dishin/go.db", "go.db")[0]
        'go.db'
        >>> ssmpy.semantic_base("go.db")
        >>> e1 = ssmpy.get_uniprot_annotations("Q12345")
        >>> e2 = ssmpy.get_uniprot_annotations("Q12346")
        >>> ssmpy.ssm_multiple(ssmpy.ssm_resnik, e1, e2)
        1.653493583942882
    """
    results = []
    for entry1 in entry1_list:
        results_entry1 = []
        for entry2 in entry2_list:
            result = m(entry1, entry2)
            results_entry1.append(result)
        # maximum of all values for entry1
        results.append(max(results_entry1))
    # average of all values for all entries
    avg = sum(results) / float(len(results))
    return avg
