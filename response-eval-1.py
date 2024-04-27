import os
import sys
import re

def count_matches_and_lines(file_path, search_string):
    matches = 0
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            matches += len(re.findall(search_string, line))
    return line_count, matches

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <search_string> <directory_path>")
        sys.exit(1)

    search_string = sys.argv[1]
    directory = sys.argv[2]

    with open("report.txt", 'w') as report_file:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                line_count, matches = count_matches_and_lines(file_path, search_string)
                if line_count > 0:
                    match_ratio = matches / line_count
                else:
                    match_ratio = 0
                report_file.write(f"File: {filename}\n")
                report_file.write(f"Line count: {line_count}\n")
                report_file.write(f"Matches for '{search_string}': {matches}\n")
                report_file.write(f"Match ratio: {match_ratio:.6f}\n\n")

if __name__ == "__main__":
    main()
