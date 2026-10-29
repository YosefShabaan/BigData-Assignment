# CSCI461 Assignment 1 - SMS Spam Classification

## Project Overview
This project uses the SMS Spam Collection dataset to analyze messages and classify them as **ham** or **spam**. The analysis runs in a Jupyter Notebook inside a Docker container.

## Dataset
- Source: https://archive.ics.uci.edu/dataset/228/sms+spam+collection
- File: `data/dataset.csv`
- `text`: SMS message
- `label`: ham or spam
- Original dataset: 5,574 messages. After removing duplicate rows: 5,171 messages.

## What We Did
1. **Data preprocessing:** checked columns, data types, missing values and duplicates; used `loc`, `iloc`, `np.r_`, data transformations and three sampling methods (random, stratified and cluster sampling).
2. **Data analysis:** created numerical text features and a correlation heatmap.
3. **Text analysis:** cleaned text, counted tokens, plotted most frequent words and compared spam with ham.
4. **Classification:** converted text to TF-IDF features and trained Logistic Regression. Naive Bayes was also used for comparison.
5. **Clustering:** used K-Means and analyzed cluster sizes, quality and main words.

## Project Files
```text
bd-a1/
├── Dockerfile
├── requirements.txt
├── README.md
├── data/dataset.csv
├── notebook/analysis.ipynb
├── output/
│   ├── cleaned_data.csv
│   ├── model_metrics.txt
│   ├── cluster_summary.txt
│   └── figures/
└── screenshots/
```

## Docker Explanation
- **Dockerfile:** instructions used to build a Docker image.
- **Image:** contains the software and project files needed to run the project.
- **Container:** a running instance of an image.
- **Layers:** parts of an image built from instructions such as `FROM`, `RUN`, and `COPY`. Docker can reuse unchanged layers.
- **Port mapping:** `-p 8888:8888` means `HOST_PORT:CONTAINER_PORT`. Port 8888 on the computer connects to port 8888 in the container.
- **Bind mount:** `-v "${PWD}:/home/jovyan/bd-a1"` links the local project folder with the container so generated files stay on the computer.
- **Volume vs. bind mount:** Docker manages a volume; a bind mount links to a specific folder on the computer.

## Build and Run (Windows PowerShell)
Install Docker Desktop and open a terminal inside the `bd-a1` folder.

```powershell
docker build -t bd-a1:latest .
docker images
docker run -d --name bd-a1-container -p 8888:8888 -v "${PWD}:/home/jovyan/bd-a1" bd-a1:latest start-notebook.py --ServerApp.root_dir=/home/jovyan/bd-a1
docker ps
docker ps -a
docker logs bd-a1-container
docker inspect bd-a1-container
```

Open the Jupyter URL shown in `docker logs` (use its token if requested). Open `notebook/analysis.ipynb` and choose **Kernel > Restart Kernel and Run All Cells**. The result files will be saved under `output/`.

If the container exists but is stopped, run `docker start bd-a1-container`. If you need to replace it, run `docker rm -f bd-a1-container` before `docker run`.

## Docker Hub
- Repository: https://hub.docker.com/r/yosefshabaan/bd-a1
- Image: `yosefshabaan/bd-a1:latest`

Commands used to publish the image:
```powershell
docker login
docker tag bd-a1:latest yosefshabaan/bd-a1:latest
docker push yosefshabaan/bd-a1:latest
```

## Test on Another Computer (Team Verification)
A second team member should install Docker Desktop and run:

```powershell
docker pull yosefshabaan/bd-a1:latest
mkdir bd-a1-test
cd bd-a1-test
mkdir output
docker run -d --name bd-a1-verify -p 8889:8888 -v "${PWD}/output:/home/jovyan/bd-a1/output" yosefshabaan/bd-a1:latest start-notebook.py --ServerApp.root_dir=/home/jovyan/bd-a1
docker logs bd-a1-verify
```

Open Jupyter at `http://localhost:8889/lab` using the token from the logs. Run the notebook from top to bottom and check that `output/` contains the generated files. This team verification still needs to be completed.

## Outputs and Evidence
The `output/` folder contains cleaned data, classification metrics, clustering results and saved charts such as a correlation heatmap, word frequency plot, group comparison and confusion matrix. The `screenshots/` folder should contain evidence of a successful Docker build, Docker commands, the running container and JupyterLab.

## Note
The dataset is imbalanced (more ham than spam), so accuracy alone does not describe all model performance. Precision, recall, F1-score and the confusion matrix are also reported in `output/model_metrics.txt`.
