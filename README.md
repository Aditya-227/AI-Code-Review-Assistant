# AI Code Review & Bug Prediction Assistant

An AI-powered software analysis tool that evaluates Git repositories to identify potential bug risks, code complexity issues, and overall repository health.

The system combines **static code analysis, repository mining, and machine learning-based risk estimation** to provide developers with actionable insights about their codebase.



# Overview

Software defects often arise from complex code, large files, and frequently modified components.
This project automatically analyzes a repository and highlights:

• Files with high bug risk
• Code complexity issues
• Repository health score
• Code quality insights

The results are presented through an **interactive Streamlit dashboard**.



# Features

### Repository Analysis

* Reads a local Git repository
* Extracts commit history
* Calculates file change frequency

### Code Parsing

* Parses Python files
* Extracts functions and classes

### Feature Extraction

Computes metrics such as:

* Lines of Code
* Cyclomatic Complexity
* Function Count
* Change Frequency

### Bug Risk Estimation

Predicts bug probability for each file based on code complexity and repository activity.

### Code Review Engine

Detects common issues such as:

* High complexity functions
* Long methods
* Potential maintainability problems

### Repository Health Score

Calculates an overall health score based on:

* Complexity
* Bug risk
* Code issues

### Interactive Dashboard

Provides visual insights including:

* Health score gauge
* Bug probability charts
* Complexity visualizations
* High-risk file detection
* AI repository summary



# Tech Stack

**Language**

* Python

**Libraries**

* Streamlit
* Plotly
* GitPython
* Radon
* Pandas
* NumPy
* Scikit-learn



# Project Structure


AI-Code-Review-Assistant
│
├── app.py
├── repo_loader.py
├── parser.py
├── feature_extractor.py
├── bug_predictor.py
├── code_review.py
├── health_score.py
│
├── models/
├── embeddings/
│
├── screenshots/
└── README.md



# Architecture

The system processes repositories through multiple stages:

1. Repository Loader – Extract Git history
2. Code Parser – Analyze Python files
3. Feature Extractor – Generate complexity metrics
4. Bug Predictor – Estimate defect probability
5. Code Review Engine – Detect maintainability issues
6. Health Score Calculator – Compute repository health
7. Streamlit Dashboard – Display insights visually

---

# Installation

Clone the repository:


git clone https://github.com/Aditya-227/AI-Code-Review-Assistant.git


Navigate into the project:

cd AI-Code-Review-Assistant


Install dependencies:


pip install -r requirements.txt




# Run the Application

Start the Streamlit dashboard:


streamlit run app.py


Then open the browser and enter the path of a local Git repository to analyze.


# Example Output

Repository Health Score: **83%**

Top Risk Files

| File                 | Bug Probability |
| -------------------- | --------------- |
| parser.py            | 0.54            |
| feature_extractor.py | 0.52            |
| repo_loader.py       | 0.49            |



# Screenshots




(screenshots/Main.png)
(screenshots/2.png))
(screenshots/3.png)
(screenshots/4.png)
(screenshots/5.png)
(screenshots/6.png)




# Future Improvements

* LLM-based code review suggestions
* Function-level bug prediction
* Commit activity visualization
* Duplicate code detection across repositories





Project Architecture Diagram

                +----------------------+
                |   Git Repository     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Repository Loader   |
                |   (GitPython)        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     Code Parser      |
                |   (Python AST)       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Feature Extraction  |
                | LOC / Complexity     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Bug Predictor      |
                |  Risk Estimation     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Code Review Engine  |
                | Complexity / Issues  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Repository Health    |
                |     Score            |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Streamlit Dashboard  |
                | Interactive Charts   |
                +----------------------+

# Author

Aditya Verma
