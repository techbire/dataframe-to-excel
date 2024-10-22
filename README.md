# Python DataFrame to Excel File Project
![](ss.png)

[Watch the project demo on YouTube](https://www.youtube.com/watch?v=h4zc1_noLh4)


This repository demonstrates how to convert a Python DataFrame into an Excel file using the `pandas` and `openpyxl` libraries. The project includes a sample dataset representing a 50 Days Summer Challenge schedule, but the code can be adapted for any DataFrame.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project provides a simple yet powerful example of how to use Python to manipulate data and save it in an Excel format. The sample dataset is a structured schedule for a 50 Days Summer Challenge, covering various topics in DSA (Data Structures and Algorithms) and Development.

## Features
- Create and manipulate data using pandas DataFrames.
- Export data from a DataFrame to an Excel file using openpyxl.
- Sample dataset included for demonstration purposes.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/techbire/dataframe-to-excel.git
    cd dataframe-to-excel
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install pandas openpyxl
    ```

## Usage
To generate the Excel file, simply run the `main.py` script:

```bash
python main.py
```

This will create an Excel file named `dsa_and_development_schedule_corrected.xlsx` in the project directory.

## Code Explanation

### Script: `generate_schedule.py`
This script creates a DataFrame with the sample data and exports it to an Excel file.

```python
import pandas as pd

# Sample data
data = {
    "Date": [
        "06-06-24", "07-06-24", "08-06-24", "09-06-24", "10-06-24", "11-06-24", "12-06-24", "13-06-24", "14-06-24",
        "15-06-24", "16-06-24", "17-06-24", "18-06-24", "19-06-24", "20-06-24", "21-06-24", "22-06-24", "23-06-24",
        "24-06-24", "25-06-24", "26-06-24", "27-06-24", "28-06-24", "29-06-24", "30-06-24", "01-07-24", "02-07-24",
        "03-07-24", "04-07-24", "05-07-24", "06-07-24", "07-07-24", "08-07-24", "09-07-24", "10-07-24", "11-07-24",
        "12-07-24", "13-07-24", "14-07-24", "15-07-24", "16-07-24", "17-07-24", "18-07-24", "19-07-24", "20-07-24",
        "21-07-24", "22-07-24", "23-07-24", "24-07-24", "25-07-24"
    ],
    "DSA Topic": [
        "Step 1: Learn the basics", "", "", "Step 2: Sorting Techniques", "", "", "Step 3: Arrays", "", "",
        "Step 4: Binary Search", "", "", "Step 5: Strings", "", "Step 6: LinkedList", "", "", "", "Step 7: Recursion",
        "", "", "Step 8: Bit Manipulation", "", "Step 9: Stack and Queues", "", "", "Step 10: Sliding Window & Two Pointer",
        "", "Step 11: Heaps", "", "", "Step 12: Greedy Algorithms", "", "Step 13: Binary Trees", "", "", 
        "Step 14: Binary Search Trees", "", "Step 15: Graphs", "", "", "Step 16: Dynamic Programming", "", "", 
        "Step 17: Tries", "", "Step 18: Strings", "", "", ""
    ],
    "Subtopics/Tasks": [
        "C++ Syntax, Data Types, Operators, Control Flow", "Functions, Pointers, References", "STL Overview, Arrays",
        "Bubble Sort, Selection Sort", "Insertion Sort, Merge Sort", "Quick Sort, Heap Sort", "Easy Problems on Arrays",
        "Medium Problems on Arrays", "Hard Problems on Arrays", "Basic String Problems", "Binary Search in 1D and 2D Arrays",
        "Search Space Problems", "Basic String Problems", "Medium String Problems", "Single LinkedList", "Double LinkedList",
        "Medium Problems on LinkedList", "Hard Problems on LinkedList", "Basic Recursion Problems", "Medium Recursion Problems",
        "Hard Recursion Problems", "Concepts of Bit Manipulation", "Problems on Bit Manipulation", "Learning Stack and Queue",
        "Pre-In-Post-fix Notations", "Monotonic Stack, Implementation", "Sliding Window Problems", "Two Pointer Problems",
        "Learning Heaps", "Medium Problems on Heaps", "Hard Problems on Heaps", "Easy Greedy Problems", "Medium/Hard Greedy Problems",
        "Binary Tree Traversals", "Medium Problems on Binary Trees", "Hard Problems on Binary Trees", "Concepts of BST",
        "Problems on BST", "Graph Concepts", "Basic Graph Problems", "Medium Graph Problems", "Hard Graph Problems", 
        "DP Patterns", "Basic DP Problems", "Medium DP Problems", "Hard DP Problems", "Tries Concepts", "Problems on Tries",
        "Advanced String Problems", "Final Revision of All Topics"
    ],
    "Development": [
        "HTML Basics: Structure, Tags, Attributes", "CSS Basics: Selectors, Properties, Box Model", "Tailwind CSS: Setup, Utility Classes",
        "Tailwind CSS: Layout, Responsive Design", "JavaScript Basics: Syntax, Variables, Data Types", "JavaScript Basics: Functions, Scope",
        "JavaScript DOM Manipulation", "JavaScript ES6: Let, Const, Arrow Functions", "JavaScript ES6: Promises, Async/Await",
        "JavaScript ES6: Classes, Modules", "JavaScript: Callbacks, Closures", "JavaScript: Array Methods, Higher Order Functions",
        "JavaScript: Objects, Prototypes", "JavaScript: Async Patterns (Callbacks, Promises)", "JavaScript: Async Patterns (Async/Await)",
        "JavaScript: Fetch API, Axios", "JavaScript: Error Handling", "JavaScript: Event Loop, Event Handling", "JavaScript: DOM Manipulation",
        "JavaScript: Form Validation", "JavaScript: Local Storage, Session Storage", "JavaScript: Regular Expressions", "JavaScript: ES6 Features",
        "JavaScript: ES6 Features Continued", "JavaScript: ES6 Features Continued", "JavaScript: ES6 Features Continued", "ReactJS: Introduction, JSX",
        "ReactJS: Components, Props, State", "ReactJS: Lifecycle Methods", "ReactJS: Handling Events", "ReactJS: Conditional Rendering",
        "ReactJS: Lists and Keys", "ReactJS: Forms and Form Validation", "ReactJS: Context API", "ReactJS: Hooks", "ReactJS: Custom Hooks",
        "ReactJS: Performance Optimization", "NodeJS: Introduction, NPM", "NodeJS: Modules, File System", "NodeJS: HTTP Module, ExpressJS Basics",
        "NodeJS: REST APIs with ExpressJS", "NodeJS: Middleware, Routing", "NodeJS: CRUD Operations", "NodeJS: Authentication with JWT",
        "NodeJS: Testing with Jest", "NodeJS: Deployment", "NodeJS: Full-Stack Project", "NodeJS: Full-Stack Project", "NodeJS: Full-Stack Project",
        "NodeJS: Full-Stack Project"
    ]
}

# Ensure all lists have the same length
max_length = max(len(data["Date"]), len(data["DSA Topic"]), len(data["Subtopics/Tasks"]), len(data["Development"]))
for key in data:
    while len(data[key]) < max_length:
        data[key].append("")

# Create the DataFrame
df_corrected = pd.DataFrame(data)

# Save the corrected DataFrame to an Excel file
file_path_corrected = 'dsa_and_development_schedule_corrected.xlsx'
df_corrected.to_excel(file_path_corrected, index=False)

print(f"Data saved to {file_path_corrected}")
```

### Explanation
1. **Import pandas**: The script starts by importing the pandas library.
2. **Sample Data**: A dictionary `data` is defined, containing four lists representing dates, DSA topics, subtopics/tasks, and development topics.
3. **Ensure Equal Length**: The script ensures all lists in the dictionary have the same length by appending empty strings where necessary.
4. **Create DataFrame**: The data is converted into a pandas
