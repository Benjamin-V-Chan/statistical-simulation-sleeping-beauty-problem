# statistical-simulation-sleeping-beauty-problem

## Project Overview

This project simulates the Sleeping Beauty problem, a well-known thought experiment in probability theory. The simulation models multiple trials where Sleeping Beauty is awakened under different conditions based on the outcome of a fair coin flip. The experiment is used to evaluate the probability that she assigns to the event that the coin landed on Heads when she is awakened.

## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_trials.py    # Generates trials for simulation
│   ├── 02_run_simulation.py     # Runs the core Sleeping Beauty experiment
│   ├── 03_analyze_results.py    # Computes Bayesian probabilities and other statistics
│   ├── 04_visualize_results.py  # Generates plots and visualizations
├── outputs/
│   ├── results.csv              # Stores simulation results
│   ├── plots/                   # Folder for visualizations
│   ├── summary.txt              # Summary of statistical findings
├── config.json                  # Configuration file for trial settings
├── requirements.txt              # Required dependencies
├── README.md                    # Documentation
```

## Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```sh
pip install -r requirements.txt
```

### 2. Generate Trials:
```
python scripts/01_generate_trials.py
```
This script generates the trial data where each trial corresponds to a single instance of the Sleeping Beauty experiment.

### 3. Run the Simulation:
```
python scripts/02_run_simulation.py
```
This script simulates the experiment by counting the number of awakenings for Heads and Tails and computing empirical probabilities.

### 4. Analyze the Results:
```
python scripts/03_analyze_results.py
```
This script applies Bayesian analysis to compute theoretical probabilities and compares them with empirical results.

### 5. Visualize Results:
```
python scripts/04_visualize_results.py
```
This script generates visualizations of the simulation results, such as bar charts of awakening distributions.

## Requirements

- Python 3.8+
- Matplotlib