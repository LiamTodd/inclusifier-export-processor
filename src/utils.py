import csv
import os
from src.constants import OUTPUT_PATH

def process_csv_file(file_path, file_name):
    # Initialize a dictionary to store sums for each column
    column_sums = {}

    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Extract and store the header row
        header = next(csv_reader)

        # Initialize column sums with zeros
        for col_name in header[2:]:
            column_sums[col_name] = 0

        # Iterate through the rows
        for row in csv_reader:
            for col_name, value in zip(header, row):
                try:
                    value = int(value)
                except ValueError:
                    continue  # Skip if the value is not a valid number

                # Update the sum for the current column
                column_sums[col_name] += value

    # Write the results to a text file
    processed_file_path = f"{OUTPUT_PATH}{file_name[:-4]}.txt"
    with open(processed_file_path, mode="w") as processed_file:
        processed_file.write(f"File: {file_name}\n\n")
        processed_file.write("\n".join([f"{col}: {sum}" for col, sum in column_sums.items() if sum > 0]))

    print(f"Results saved to: {processed_file_path}")
