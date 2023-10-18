import csv
from src.constants import OUTPUT_PATH, NON_INCLUSIVE_LANGUAGE_TERMS, CSV_HEADERS


def get_language_category(input_term):
    for category, terms in NON_INCLUSIVE_LANGUAGE_TERMS.items():
        if any(term.lower() == input_term.lower() for term in terms):
            return category
    return "Category not found"


def process_csv_file(file_path, file_name):
    # Initialize a dictionary to store sums for each column
    term_data = {}

    with open(file_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile)

        # Extract and store the header row
        header = next(csv_reader)

        # Initialize column sums with zeros
        for term in header[2:]:
            term_data[term] = {}
            term_data[term]["total"] = 0
            term_data[term]["files"] = 0
            term_data[term]["category"] = get_language_category(term)

        # Iterate through the rows
        for row in csv_reader:
            for term, value in zip(header, row):
                try:
                    value = int(value)
                except ValueError:
                    continue  # Skip if the value is not a valid number

                # Update the sum and file count for the current column
                term_data[term]["total"] += value
                if value > 0:
                    term_data[term]["files"] += 1

    # Write the results to a csv file
    processed_file_path = f"{OUTPUT_PATH}{file_name[:-4]}.csv"
    with open(processed_file_path, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADERS)
        writer.writeheader()
        for col, entry in term_data.items():
            if entry["total"] > 0:
                writer.writerow(
                    {
                        "Term": col,
                        "Occurrences": entry["total"],
                        "Files": entry["files"],
                        "Category": entry["category"],
                    }
                )

    print(f"Results saved to: {processed_file_path}")
