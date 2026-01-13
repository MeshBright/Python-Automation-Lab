# Python Automation Tools 🛠️🐍

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Automation%20%26%20Data-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-orange?style=for-the-badge)

## 📖 About The Project

Welcome to **Python Automation Tools**. This repository serves as a central lab for my experiments in software efficiency, algorithmic logic, and data processing. 

As a **Mechatronics Engineering student**, I often encounter problems that require more than just hardware solutions. This collection represents my journey into mastering the software side of engineering—specifically using **Python** to automate repetitive workflows, structure data using **Object-Oriented Programming (OOP)**, and solve complex algorithmic challenges.

### 🎯 Objectives
* **Automation:** Reducing manual friction in daily tasks through scripting.
* **Data Processing:** Implementing robust classes and methods using **NumPy** and **Pandas** to handle datasets efficiently.
* **Algorithmic Proficiency:** continuous practice of logic and efficiency (inspired by Kaggle coursework).

---

## 📂 Repository Structure

The projects here are categorized by their core function.

### 1. 📊 Foundational Data Logic
*A collection of scripts focused on the core building blocks of data manipulation.*

Rather than complex frameworks, this section focuses on mastering the fundamental logic required for engineering software. These scripts demonstrate:

* **Data Organization**: Using **Dictionaries** and **Lists** to map and store hardware/component information (like sensor costs or batch logs).
* **Logical Flow**: Implementing **Conditional Statements** and **Iteration** to process messy datasets into clean, usable information.
* **Algorithm Basics**: Solving problems through step-by-step logical procedures, ensuring the code is readable and efficient for future scaling.

### 2. 🤖 Task Automation
*Scripts designed to save time, reduce error, and handle file operations.*

* **`FactorBatchProcessor.py`**: A data cleaning utility designed to handle inconsistent "machine logs." It sanitizes raw text strings (removing messy delimiters), parses unique batch codes, and calculates cumulative manufacturing costs using a component dictionary. It includes logic for conditional pricing (e.g., handling 'x' component surcharges).
* **`ThoughtStorer.py`**: A CLI-based logging tool that captures dynamic user input and persistently stores it to a local text file. It demonstrates Python's File I/O capabilities, managing write (`w`), append (`a`), and read (`r`) modes to maintain a sequential history of entries.

### 3. 🧠 Algorithm Practice
*Logic building and problem solving.*
* **`Kaggle_Drills/`**: Solutions and refactored code from data science courses and challenges.
* **`Math_Utils.py`**: Helper functions for engineering calculations (matrices, vectors).

### 4. 🌐 Versatility Proof (JavaScript)
*Demonstrating logic adaptability and environment setup.*

This project showcases the ability to apply engineering logic within a JavaScript environment, specifically focusing on user input handling and manual calculation priority.

* **`Multi-Operand Calculator`**: A script that manually parses three numbers and two operators. 
    * **Logic**: Uses a nested decision-matrix to handle arithmetic priority (BODMAS).
    * **Dependency Management**: Utilizes `npm` and the `prompt-sync` library for CLI-based user interaction.
    * **Safety**: Implements `if/else` guard clauses to prevent division-by-zero errors.
    * **[🔗 View Code on GitHub Gist](https://gist.github.com/MeshBright/7520d8de2f79740c0090246409f304e4)**

---

## 🛠️ Tech Stack & Concepts

* **Language:** Python 3.10+
* **Libraries:** `pandas`, `numpy`, `os`, `sys`
* **Concepts:**
    * Object-Oriented Programming (Classes, Inheritance)
    * File I/O and Path Management
    * Data Vectorization

---

## 🚀 Getting Started

To run these scripts on your local machine:

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/YourUsername/Python-Automation-Tools.git](https://github.com/YourUsername/Python-Automation-Tools.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd Python-Automation-Tools
    ```
3.  **Install dependencies (if applicable):**
    ```bash
    pip install numpy pandas
    ```
4.  **Run a script:**
    ```bash
    python path/to/script_name.py
    ```

---

## 🔮 Future Roadmap

* Integration of **Flutter** backend logic for mobile data handling.
* Connecting automation scripts to microcontroller serial data (Arduino).
* Expanding the OOP module for more complex data visualization.

---

*Created by [Methushael Bright] - Mechatronics Engineering Student @ FUTMINNA*
