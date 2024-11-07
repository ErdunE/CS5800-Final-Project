## Timeline and Status of Project Milestones

| Task                                     | Start Date   | End Date     | Status                                                                 |
|------------------------------------------|--------------|--------------|------------------------------------------------------------------------|
| Project Start                            | Oct 21, 2024 | -            | ![Completed](https://img.shields.io/badge/Status-Completed-brightgreen) |
| Confirm Team Members and Team Name       | Oct 21, 2024 | Nov 08, 2024 | ![Completed](https://img.shields.io/badge/Status-Completed-brightgreen) |
| Select Algorithm                         | Nov 08, 2024 | Nov 22, 2024 | ![Completed](https://img.shields.io/badge/Status-Completed-brightgreen) |
| Brainstorm and Research Materials        | Oct 21, 2024 | Nov 06, 2024 | ![Completed](https://img.shields.io/badge/Status-Completed-brightgreen) |
| Confirm Plan and Assign Tasks            | Nov 06, 2024 | Nov 07, 2024 | ![Completed](https://img.shields.io/badge/Status-Completed-brightgreen) |
| Complete Individual Coding Tasks         | Nov 07, 2024 | Nov 15, 2024 | ![In Progress](https://img.shields.io/badge/Status-In%20Progress-yellow) |
| Code Integration, Testing, and Debugging | Nov 16, 2024 | Nov 20, 2024 | ![Planned](https://img.shields.io/badge/Status-Planned-lightgrey)       |
| Discuss and Divide Paper Tasks           | Nov 20, 2024 | Nov 21, 2024 | ![Planned](https://img.shields.io/badge/Status-Planned-lightgrey)       |
| Complete Individual Paper Sections       | Nov 21, 2024 | Nov 23, 2024 | ![Planned](https://img.shields.io/badge/Status-Planned-lightgrey)       |
| Merge and Refine Paper                   | Nov 23, 2024 | Nov 25, 2024 | ![Planned](https://img.shields.io/badge/Status-Planned-lightgrey)       |
| Discuss and Plan Presentation            | Nov 25, 2024 | Nov 25, 2024 | ![Planned](https://img.shields.io/badge/Status-Planned-lightgrey)       |
| Complete Individual Presentation Tasks   | Nov 25, 2024 | Dec 02, 2024 | ![Planned](https://img.shields.io/badge/Status-Planned-lightgrey)       |
| Merge Presentation and Practice          | Dec 02, 2024 | Dec 09, 2024 | ![Planned](https://img.shields.io/badge/Status-Planned-lightgrey)       |
| Project End                              | -            | Dec 09, 2024 | ![Planned](https://img.shields.io/badge/Status-Planned-lightgrey)       |

## CS5800 Final Project - Team 3Cs Project

### Table of Contents

1. [Project Overview](#project-overview)
2. [Team Name: 3Cs](#team-name-3cs)
3. [Team Members](#team-members)
4. [Basic Information](#basic-information)
5. [Project Structure](#project-structure)
6. [Dataset](#dataset)
7. [Branching Strategy](#branching-strategy)
8. [Commit and Pull Request Guidelines](#commit-and-pull-request-guidelines)
9. [Collaboration Workflow](#collaboration-workflow)
   - [Clone the Repository](#1-clone-the-repository)
   - [Create a Feature Branch](#2-create-a-feature-branch)
   - [Commit and Push Your Changes](#3-commit-and-push-your-changes)
   - [Create a Pull Request (PR)](#4-create-a-pull-request-pr)
   - [Merge Changes](#5-merge-changes)
   
### Project Overview
This is the team project of CS5800 Algorithms. In this project, we aim to implement algorithms k-Nearest Neighbors for continuous variables with tested program and GUI. The project will be divided into multiple modules, with each team member responsible for specific tasks.
### Team Name: 3Cs
* **Chinese** — all of us are from China.
* **Collaboration** — We value teamwork to achieve our goals.
* **Creativity** — Innovation and problem is the core of how we approach challenges.
### Team Members
* **Erdun E**
* **Hailee Wang**
* **Fengkai Liu**
### Basic Information
* **Author:** Erdun E, Hailee Wang, Fengkai Liu
* **Course:** CS5800 Algorithm
* **Program:** CS5800 Final Project
* **Professor:** Dr. Alan Jamieson

### Project Structure
```aiignore
* Main                  [Kai]
* Controller            [Kai]      
* Visualizer            [Kai]
* KnnAlgorithmModule    [Hailee]
* DataProcessorModule   [Erdun]
```
### Dataset
[iris.csv](https://github.com/ErdunE/CS5800-Final-Project/blob/main/iris.csv)

### Branching Strategy
* Main Branch: main
* Feature Branch Naming Convention: workspace-[workspace-name] (e.g., workspace-erdun)
* All development should be done on workspace branches, and changes will only be merged into the team-project branch after review.
### Commit and Pull Request Guidelines
* Create a workspace branch for each member specific task.
* Push your changes to the workspace branch and open a Pull Request (PR) to merge into the team-project branch.
* Code Review: At least one team member must review and approve the PR before merging.
* Ensure tests pass before merging into the main project branch.
### Collaboration Workflow
1. Clone the Repository:
```
git clone https://github.com/ErdunE/CS5800-Final-Project.git
cd CS5800-Final-Project
```
example
```aiignore
erdune@ErdundeMBP CS5800-Final-Project % pwd
/Users/erdune/Desktop/CS5800-Final-Project
```
2. Create a Feature Branch:
```
git checkout -b workspace-erdun team-project
```
example
```
erdune@ErdundeMacBook-Pro CS5800_Final_Project % git checkout -b workspace-erdun team-project
M       .DS_Store
M       CS5010ProgrammingDesignParadigm/.DS_Store
M       CS5800Algorithm/.DS_Store
Switched to a new branch ‘workspace-erdun’
erdune@ErdundeMacBook-Pro CS5800_Final_Project % git branch
  feature-improvement
  main
  team-project
* workspace-erdun
erdune@ErdundeMacBook-Pro CS5800_Final_Project % 

```
3. Commit and Push Your Changes:
```
git add .
git commit -m “Implemented Algorithms Logic”
git push origin workspace-erdun
```
4. Create a Pull Request (PR):
    * Open a PR on GitHub to merge your feature branch into the team-project branch.
    * Request at least one other team member to review your PR.
5. Merge Changes:
    * Once the review is approved, and all tests pass, merge the PR.