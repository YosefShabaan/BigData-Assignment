
FROM quay.io/jupyter/scipy-notebook:latest

USER root

WORKDIR /home/jovyan/bd-a1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY data/dataset.csv ./data/dataset.csv
COPY notebook/analysis.ipynb ./notebook/analysis.ipynb

RUN mkdir -p output/figures screenshots && chown -R jovyan:users /home/jovyan/bd-a1

USER jovyan
