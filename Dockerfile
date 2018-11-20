FROM ubuntu:18.04

RUN apt-get update -qqq &&\
    apt-get install --no-install-recommends -y python3.6 python3-pip &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip3 install --no-cache-dir numpy scipy pandas statsmodels

COPY hie_analysis.py /home/hie_analysis.py

ENTRYPOINT ["python3", "/home/hie_analysis.py"]
