import os
import re

def scan_directory_for_sql(directory_path):
    sql_queries = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.py'):  # Check for Python files
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    for line_num, line in enumerate(lines, start=1):
                        matches = re.findall(r"[\'\"](SELECT\s.*?|INSERT\s.*?|UPDATE\s.*?|DELETE\s.*?|CREATE\s.*?|DROP\s.*?|ALTER\s.*?|FROM\s.*?|INTO\s.*?|VALUES\s.*?|WHERE\s.*?|AND\s.*?|OR\s.*?|JOIN\s.*?|LEFT\s.*?|RIGHT\s.*?|INNER\s.*?|OUTER\s.*?|ON\s.*?|SET\s.*?)['\"](.{1,500})", line, re.IGNORECASE)
                        if matches:
                            for match in matches:
                                sql_queries.append({'file': file_path, 'line': line_num, 'query': match[0].strip(),'next_characters': match[1]})
    return sql_queries

# Usage: Provide the directory path you want to scan for Python files containing SQL queries
directory_to_scan = r'C:\Users'
results = scan_directory_for_sql(directory_to_scan)

if results:
    print(f"Potential SQL queries found in files within '{directory_to_scan}':")
    for result in results:
        print(f"File: {result['file']}, Line {result['line']}: Query {result['query']}{result['next_characters']}")
else:
    print(f"No potential SQL queries found in files within '{directory_to_scan}'")
