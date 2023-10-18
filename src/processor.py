import sys
import os
from src.constants import SINGLE_TYPE, ALL_TYPE, EXPORTS_DIR
from src.utils import process_csv_file


def main():
    if len(sys.argv) < 2:
        print("Error: Incorrect number of args.")
        return
    run_type = sys.argv[1]

    if run_type == SINGLE_TYPE:
        if len(sys.argv) != 3:
            print("Error: Incorrect number of args.")
        run_root = sys.argv[2]
        file_path = f"{EXPORTS_DIR}/{run_root}"
        if not os.path.exists(file_path):
            print("Error: File not found.")
            return
        if not file_path.endswith(".csv"):
            print("Error: Invalid file type.")
            return
        with open(file_path, newline="") as csvfile:
            process_csv_file(file_path, run_root)

    elif run_type == ALL_TYPE:
        for file in os.listdir(EXPORTS_DIR):
            if file.endswith(".csv"):
                process_csv_file(f"{EXPORTS_DIR}/{file}", file)

    else:
        print("Error: Invalid run type.")
        return


if __name__ == "__main__":
    main()
