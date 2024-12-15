# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os


os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    # Skip the header row
    header = next(reader)