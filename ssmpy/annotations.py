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

import ssmpy.ssm
import sys


if sys.version_info > (3, 0):
    # Python 3 code in this block
    import urllib.request
else:
    # Python 2 code in this block
    import urllib2


def get_uniprot_annotations(protein_acc):
    """Retrieve GO annotations for a UniProt ID using UniProt API
    
    :param protein_acc: UniProt protein ID
    :type protein_acc: string
    :return: list of GO terms
    :rtype: list


    :Example:

    >>> import ssmpy
    >>> import urllib.request
    >>> import gzip
    >>> import shutil
    >>> urllib.request.urlretrieve("http://labs.rd.ciencias.ulisboa.pt/dishin/go201907.db.gz", "go.db.gz")[0]
        'go.db.gz'
        >>> with gzip.open('go.db.gz', 'rb') as f_in:
        ...    with open('go.db', 'wb') as f_out:
        ...        shutil.copyfileobj(f_in, f_out)
        >>> ssmpy.semantic_base("go.db")
        >>> l = sorted(ssmpy.get_uniprot_annotations("Q12345"))
        >>> l
        [1746, 9044, 17053, 21566, 24341, 57621, 95359]
    """

    url = "http://www.uniprot.org/uniprot/" + protein_acc + ".txt"

    if sys.version_info > (3, 0):
        # Python 3 code in this block
        response = urllib.request.urlopen(url)
        data = response.read().decode("ascii")
    else:
        # Python 2 code in this block
        response = urllib2.urlopen(url)
        data = response.read()

    lines = str.split(data, "\n")
    entries = []
    for l in lines:
        tag = "DR   GO;"
        if l.startswith(tag):
            t = l[len(tag) + 1 : l.find(";", len(tag))].replace(":", "_")
            e = ssmpy.get_id(t)
            entries.append(e)

    return entries
