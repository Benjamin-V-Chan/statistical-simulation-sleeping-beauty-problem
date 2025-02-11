# statistical-simulation-sleeping-beauty-problem

## Project Overview

This project simulates the Sleeping Beauty problem, a well-known thought experiment in probability theory. The simulation models multiple trials where Sleeping Beauty is awakened under different conditions based on the outcome of a fair coin flip. The experiment is used to evaluate the probability that she assigns to the event that the coin landed on Heads when she is awakened.

### Mathematical Background

#### The Basic Setup
Sleeping Beauty is put to sleep on Sunday. A fair coin is flipped:
- If **Heads**, she is awakened once (on Monday).
- If **Tails**, she is awakened twice (on Monday and Tuesday), but she will not remember previous awakenings.

Each time she wakes up, she is asked: *What is the probability that the coin landed on Heads?*

#### Bayesian Analysis
Define the following probabilities:
- $\( P(H) = \frac{1}{2} \)$ (the probability of flipping Heads)
- $\( P(T) = \frac{1}{2} \)$ (the probability of flipping Tails)
- $\( P(A | H) = 1 \)$ (the probability that Sleeping Beauty awakens given Heads)
- $\( P(A | T) = 2 \)$ (the probability that Sleeping Beauty awakens given Tails)

By the law of total probability, the probability of awakening on any given day is:
$$P(A) = P(H) P(A | H) + P(T) P(A | T)$$
Substituting the values:
$$P(A) = \left( \frac{1}{2} \times 1 \right) + \left( \frac{1}{2} \times 2 \right) = \frac{1}{2} + 1 = \frac{3}{2}$$

By Bayes' Theorem, the probability that the coin landed on Heads given that she is awakened is:
$$P(H | A) = \frac{P(A | H) P(H)}{P(A)}$$
Substituting the known values:
$$P(H | A) = \frac{(1 \times \frac{1}{2})}{\frac{3}{2}} = \frac{1}{3}$$
Thus, when awakened, Sleeping Beauty should assign a probability of **1/3** to the event that the coin landed on Heads.

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