[![CI](https://github.com/nogibjj/mini_project_2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mini_project_2/actions/workflows/cicd.yml)

## mini project 2: Pandas Descriptive Statistics 

This repo contains: 
- .devcontainer     
- .github   
- .gitignore    
- Makefile  
- README.md     
- requirements.txt      
- main.py   
- test_main.py

## Overview
- The purpose of this project is to build descriptive statistic template by using `Pandas` and its associated attributes (e.g.`DataFrame.describe()`). 
- Functions wrote by the authors are `findMin`, `findMax` and `calcMean`.
- Visualizations are produced to demonstrate the relationship between features. 


## Check and test
<img width="1728" alt="Screenshot 2023-09-10 at 12 43 15" src="https://github.com/nogibjj/mini_project_2/assets/141781876/4e8796e4-21ae-4a02-8f46-c55dfb7e32ab">
test successfully passed 

## Automation CICD
We have implemented automation practices and tools to enhance efficiency and maintain code quality:

Devcontainer: Inside the .devcontainer folder, you'll find two crucial files:

Dockerfile: This file defines environment variables to ensure a consistent development environment for all collaborators, mitigating potential conflicts and version mismatches.
devcontainer.json: A JSON file specifying environment variables and installed extensions within the virtual environment.
Makefile: Our Makefile contains instructions for several tasks, including:

Installing required packages (specified in requirements.txt).
Enforcing code formatting using the black formatter.
Running tests for functions (files starting with "Check...").
Linting the code with pylint.
GitHub Actions: We've integrated GitHub Actions using the main.yml file, enabling automated tasks based on events such as pushes and pull requests. The workflow covers installing packages, code formatting, linting, and testing.

Requirements.txt: The requirements.txt file enumerates the essential Python packages for the project. While it currently comprises generic Python packages, it can be tailored to include specific dependencies as required for future project scopes.

This project is aimed at demonstrating efficient data analysis using the Pandas library while emphasizing code quality through automation and testing.

## statistical results of the data 
### 1. general outlook of the data from head
<img width="699" alt="Screenshot 2023-09-10 at 18 29 27" src="https://github.com/nogibjj/mini_project_2/assets/141781876/34311d34-da55-4744-89e1-2f94036c1779">

### 2. statistical summary
<img width="1038" alt="Screenshot 2023-09-10 at 18 29 03" src="https://github.com/nogibjj/mini_project_2/assets/141781876/9fe61268-e137-465c-b2f8-242b8a09a1a4">


## A glimpse of the data visualization 
![Figure_1](https://github.com/nogibjj/mini_project_2/assets/141781876/fd2ab311-baf7-43a6-95ec-6bcf1e8504f4)






