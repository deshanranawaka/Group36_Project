# Group 36: Reddit Word Frequency Analysis
Scalable Data Engineering Solution Design & Implementation

This project performs large-scale text analysis on Reddit data using a distributed Spark cluster. It identifies the top 10 most frequent words (excluding NLTK stopwords) and conducts performance benchmarks across different scaling scenarios.

## Architecture Diagram
The system is deployed on the Swedish Science Cloud (OpenStack) using a Master-Worker architecture.

graph TD
    subgraph Local_Machine
        A[Project Repo] --> B[scripts/deploy.sh]
    end

    subgraph Cluster_Master_192.168.5.177
        B -- SSH/Rsync --> C[src/analysis_job.py]
        C -- spark-submit --> D[Spark Master Process]
    end

    subgraph HDFS_Storage
        E[(corpus-webis-tldr-17.json)] -- Data Stream --> D
    end

    subgraph Worker_Nodes
        D -- Tasks --> F[Worker 1: 192.168.5.97]
        D -- Tasks --> G[Worker 2: 192.168.5.28]
        D -- Tasks --> H[Worker 3: 192.168.5.181]
    end

- Master Node: Coordinates job scheduling and hosts the Spark UI on port 4040.
- Worker Nodes: Three ALIVE workers providing a total of 6 cores for parallel processing.
- Storage: HDFS handles the large Reddit JSON corpus.


## Project Structure

| Folder / File | Description |
| --- | --- |
| `README.md` | Setup instructions, architecture diagrams, and usage guides. |
| `data/` | Contains `sample_reddit.json` for local testing and exploration. |
| `src/config.py` | Centralized configuration for network IPs, HDFS paths, and NLTK stopwords. |
| `src/etl_job.py` | Data ingestion and cleaning logic, including JSON parsing and text preprocessing. |
| `src/analysis_job.py` | The main Spark entry point containing the core MapReduce word count logic. |
| `scripts/deploy.sh` | Bash script to sync the local `src/` directory to the remote master node via rsync. |
| `scripts/run_benchmark.sh` | Orchestrates the horizontal and vertical scaling tests across the cluster. |
| `scripts/parse_results.py` | Python helper to extract runtimes from `scaling_report.txt` for performance analysis. |
| `notebooks/` | Jupyter notebooks used for initial data exploration and prototyping. |
| `docs/` | Project documentation, including contribution statements |


## Setup Instructions
1. Prerequisites
- Python 3.10+ installed locally
- SSH access to the cluster at 192.168.5.177.
- 'rsync' installed for deployment

2. Environment Configuration
- Update src/config.py with your current Master IP and HDFS paths.

3. Deploying Code
- Run the deployment script from your project root to push the src/ directory to the cluster.
'chmod +x scripts/deploy.sh
./scripts/deploy.sh'

4. Running Benchmarks \
The project is designed to measure performance across three distinct scaling scenarios.
- Horizontal Scaling: 1 Worker vs. 2 Workers vs. 3 Workers
- Vertical Compute: 1 Core vs. 2 Cores on a single worker
- Vertical Memory: 0.5GB vs. 1.0GB vs. 2.5GB executor memory
Execute the full suite using:
'chmod +x scripts/run_benchmark.sh
./scripts/run_benchmark.sh'
Results will be logged to scaling_report.txt for analysis.

5. Analyzing Benchmark Results
To quickly extract the runtimes for your performance analysis, use the specialized parser script.
Execute the script from the project root after the benchmark completes.
'python3 scripts/parse_results.py'
The parser will scan the logs and display a clean summary table in your terminal: