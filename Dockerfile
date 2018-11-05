FROM ubuntu:18.04

RUN apt-get update -qqq &&\
    apt-get install --no-install-recommends -y python3.6 python3-pip &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip3 install --no-cache-dir numpy scipy pandas statsmodels

WORKDIR /home

COPY 1-longitudinal-minimal-data-set-V2.csv /home/1-longitudinal-minimal-data-set-V2.csv
COPY hie_analysis.py /home/hie_analysis.py

ENTRYPOINT ["python3", "/home/hie_analysis.py"]
