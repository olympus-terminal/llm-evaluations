import re

def count_matches_and_lines(file_path, search_string):
    matches = 0
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            matches += len(re.findall(search_string, line))
    return line_count, matches
