#### To build:
## docker build github.com/lasigeBioTM/DiShIn -t fjmc/dishin-image
#### To test it:
## docker run -it --rm --name dishin-container fjmc/dishin-image ./example1.py

#### To build with databases:
## curl -O -L https://github.com/lasigeBioTM/DiShIn/archive/master.zip
## unzip master.zip
## cd DiShIn-master
## cat Dockerfile-Databases >> Dockerfile
## docker build . -t fjmc/dishin-image:databases202104
#### To test it:
## docker run -it --rm --name dishin-container fjmc/dishin-image ./example2.py


FROM ubuntu:18.04
LABEL maintainer="fcouto@di.fc.ul.pt"

RUN apt-get update 
RUN apt-get install -y \
    curl \
    python3 \
    python3-pip

RUN pip3 install ssmpy 
        
# Labels
LABEL org.label-schema.description="DiShIn (Semantic Similarity Measures using Disjunctive Shared Information)"
LABEL org.label-schema.url="http://labs.rd.ciencias.ulisboa.pt/dishin/"
LABEL org.label-schema.vcs-url="https://github.com/lasigeBioTM/DiShIn"
LABEL org.label-schema.docker.cmd="docker run -it --rm --name mer-container fjmc/dishin-image"

WORKDIR /DiShIn

COPY metals.owl ./
COPY metals.txt ./

COPY example*.py ./

RUN apt-get autoremove
RUN apt-get clean


