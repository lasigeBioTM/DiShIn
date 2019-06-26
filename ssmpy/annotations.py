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
