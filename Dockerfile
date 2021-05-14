#### To build:
## docker build github.com/lasigeBioTM/DiShIn -t fjmc/dishin-image
#### To test it:
## docker run -it --rm --name dishin-container -v "$PWD":/usr/src/myapp -w /usr/src/myapp fjmc/dishin-image python example1.py

#### To build with databases:
## curl -O -L https://github.com/lasigeBioTM/DiShIn/archive/master.zip
## unzip master.zip
## cd DiShIn-master 
## curl -O http://labs.rd.ciencias.ulisboa.pt/dishin/chebi202104.db.gz; gunzip -N chebi202104.db.gz; curl -O http://labs.rd.ciencias.ulisboa.pt/dishin/go202104.db.gz; gunzip -N go202104.db.gz; curl -O http://labs.rd.ciencias.ulisboa.pt/dishin/hp202104.db.gz; gunzip -N hp202104.db.gz; curl -O http://labs.rd.ciencias.ulisboa.pt/dishin/doid202104.db.gz; gunzip -N doid202104.db.gz; curl -O http://labs.rd.ciencias.ulisboa.pt/dishin/mesh202104.db.gz; gunzip -N mesh202104.db.gz; curl -O http://labs.rd.ciencias.ulisboa.pt/dishin/radlex202104.db.gz; gunzip -N radlex202104.db.gz; curl -O http://labs.rd.ciencias.ulisboa.pt/dishin/wordnet202104.db.gz; gunzip -N wordnet202104.db.gz
## docker build . -t fjmc/dishin-image:databases202104
#### To test it:
## docker run -it --rm --name dishin-container -v "$PWD":/usr/src/myapp -w /usr/src/myapp fjmc/dishin-image:databases202104 python example2.py


FROM python:3.7.5-slim
LABEL maintainer="fcouto@di.fc.ul.pt"

RUN python -m pip install ssmpy 
        
# Labels
LABEL org.label-schema.description="DiShIn (Semantic Similarity Measures using Disjunctive Shared Information)"
LABEL org.label-schema.url="http://labs.rd.ciencias.ulisboa.pt/dishin/"
LABEL org.label-schema.vcs-url="https://github.com/lasigeBioTM/DiShIn"
LABEL org.label-schema.docker.cmd="docker run -it --rm --name mer-container fjmc/dishin-image"

COPY metals.owl /usr/src/myapp/
COPY metals.txt /usr/src/myapp/

COPY *.db /usr/src/myapp/

