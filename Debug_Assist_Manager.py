#!/usr/bin/python3

import csv
import os
import re
#from tabulate import tabulate

def add_entry():
    """Add a new problem, solution, and author entry to the CSV file."""
    problem = input("Enter the problem/error message: ").strip()
    solution = input("Enter the solution: ").strip()
    author = input("Enter the author name: ").strip()
    TechArea = input("Enter Tech Area (def:Generic) :").strip()  or  "Generic"
    Link= input("Enter Documentation Link/PR/GLO  (def:NA):")  or  "NA"
    # Define CSV file name
    filename = "problem_solutions.csv"

    # Check if file exists to determine if headers are needed
    file_exists = os.path.isfile(filename)
    last_id = get_last_id(filename)
    new_id = last_id + 1
    data=[str(new_id), problem , solution , author , TechArea , Link]
    # Write to CSV
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header if file is new
        if not file_exists:
            writer.writerow(['ID', 'Problem', 'Solution', 'Author', 'TechArea', 'Link'])
        writer.writerow(data)
    print("Entry saved successfully!")

def query_solution():
    """Query the CSV file for a problem with partial word matching, supporting multiple words."""
    search_problem = input("Enter the problem to search for (multiple words allowed): ").strip()
    filename = "problem_solutions.csv"

    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header
            found = False
            match_count = 0
            table_data = []
            # Split search query into words and create regex pattern for each
            search_words = [word.strip() for word in search_problem.split() if word.strip()]
            if not search_words:
                print("Please enter at least one search word.")
                return
            # Create a pattern that matches each word partially within word boundaries
            patterns = [rf'\b\w*{re.escape(word)}\w*\b' for word in search_words]
            for row in reader:
                # Check if all patterns match the problem field
                if all(re.search(pattern, row[1], re.IGNORECASE) for pattern in patterns):
                    match_count += 1
                    table_data.append([row[0],row[1],row[2],row[3],row[4],row[5]])
                    found = True
            if table_data:
                    headers = [ "ID", "Problem", "Solution", "Author", "TechArea", "Link"]
                    print(tabulate(table_data, headers=headers))

            if not found:
                print("No matching problems found.")
                """Add full problem statement,  author entry to report in the CSV file."""
                Nosolution = input("Enter the full problem statement: ").strip()
                reportedauthor = input("Enter the author name: ").strip()
                TechArea2 = input("Enter Tech Area (def:Generic) :").strip()  or  "Generic"
                # Define CSV file name
                filename2 = "No_solutions.csv"

                # Check if file exists to determine if headers are needed
                file_exists2 = os.path.isfile(filename2)
                last_id2 = get_last_id(filename2)
                new_id2 = last_id2 + 1
                data2=[str(new_id2), Nosolution , reportedauthor , TechArea2]
                # Write to CSV
                with open(filename2, mode='a', newline='', encoding='utf-8') as file2:
                       writer = csv.writer(file2)
                       # Write header if file is new
                       if not file_exists2:
                            writer.writerow(['Problem ID', 'Problem', 'Reported by', 'TechArea'])
                       writer.writerow(data2)
                       print("Entry saved successfully!")
                       print("Problem will be reported to the lead")
            else:
                print(f"\nTotal matches found: {match_count}")
    except FileNotFoundError:
        print("No data file found. Please add entries first.")

def get_last_id(csv_file):
    """Read the CSV file and return the highest ID, or 0 if empty."""
    last_id = 0
    if os.path.exists(csv_file):
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            try:
                header = next(csv_reader)  # Skip header
                for row in csv_reader:
                    if row and row[0].isdigit():  # Ensure valid ID
                        last_id = max(last_id, int(row[0]))
            except StopIteration:
                pass  # File is empty
    return last_id


def query_stats(data):
    filename = "problem_solutions.csv"
    occurrences = {}
    '''If data requested is based on Tech Area or else Engineer ID'''
    if  data=="TechArea":
        target_column = 4
        search_column = 3
    else:
        target_column = 3
        search_column = 4
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header

            for row in reader:
                if len(row) > max(target_column, search_column):  # Ensure columns exist
                    target_value = row[target_column]
                    search_value = row[search_column]
                    if target_value not in occurrences:
                        occurrences[target_value] = {}
                    occurrences[target_value][search_value] = occurrences[target_value].get(search_value, 0) + 1
        table_data = []

        for target_value, search_counts in occurrences.items():
             search_value_combined = ", ".join(f"{search_val} ({count})" for search_val, count in search_counts.items())
             # Sum the counts for the Count column
             total_count = sum(search_counts.values())
             table_data.append([target_value, search_value_combined, total_count])

        # Step 3: Display as a table
        if  data=="TechArea" and table_data:
                headers = [ "TechArea", "Engineer ID", "No.of Entries"]
                #print(tabulate(table_data, headers=headers, tablefmt="grid"))
                print(tabulate(table_data, headers=headers))
        elif  data=="Engineer_ID" and table_data:
                headers = [ "Engineer ID", "TechArea", "No.of Entries"]
                #print(tabulate(table_data, headers=headers, tablefmt="grid"))
                print(tabulate(table_data, headers=headers))
        else:
            print("No matches found in the CSV.")

    except FileNotFoundError:
        print("No data file found. Please add entries first.")

def report_solution():
       solution_id = input("Enter the solution id which is not working: ").strip()
       # Define CSV file name
       filename = "problem_solutions.csv"
       report= "reported_solutions.csv"

       # Check if file exists to determine if headers are needed
       file_exists = os.path.isfile(report)
def report_solution():
       solution_id = input("Enter the solution id which is not working: ").strip()
       # Define CSV file name
       filename = "problem_solutions.csv"
       report= "reported_solutions.csv"

       # Check if file exists to determine if headers are needed
       file_exists = os.path.isfile(report)

       row=fetch_row_by_id(filename, solution_id)
       print(row)
       if row:
            # Write to CSV
            with open(report, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write header if file is new
                if not file_exists:
                    writer.writerow(['Solution ID', 'Problem', 'Solution', 'Author', 'TechArea', 'Link'])
                    writer.writerow(row)
                    print("Entry logged in report successfully! It will be re-verified and updated after review")
                else:
                    old_row=fetch_row_by_id(report, solution_id)
                    if old_row is None:
                        writer.writerow(row)
                        print("New Entry logged in report successfully! It will be re-verified and updated after review")
                    elif type(old_row) is list:
                        print("Issue already reported, we are working on it to rectify")
                    else:
                        print("Invalid Solution ID provided")

def fetch_row_by_id(csv_file, target_id):
    """Fetch a row from the CSV file based on the given ID."""
    found =False
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader, None)  # Skip header
            if header is None:
                print("Error: CSV file is empty.")
                return None

            for row in csv_reader:
                if len(row) > 0 and row[0] == str(target_id):  # Check if id matches
                    found= True
                    return row
        if not found:
            print(f"No row found with ID {target_id} in {csv_file}.")
            return None

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected issue occurred: {e}")
        return None


def modify_solution():
    # Example usage
    csv_file = 'problem_solutions.csv'  #CSV file path
    target_id = input("Enter the solution ID to be modified:")  # ID of the row to modify
    column_index = 1  # Column to modify (0-based index)

    problem= fetch_column_by_id(csv_file, target_id, column_index)
    print(f'Please find the problem statement: {problem}')

    new_solution = input("Enter the new solution for the above problem:")  # New value for the column
    column_index = 2  # Column to modify (0-based index)
    modify_row_by_id(csv_file, target_id, column_index, new_solution)

def fetch_column_by_id(csv_file, target_id, column_index):
    """Fetch a specific column value from the row with the given ID."""
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader, None)  # Skip header
            if header is None:
                print("Error: CSV file is empty.")
                return None

            if column_index >= len(header):
                print(f"Error: Column index {column_index} is out of range. Max index is {len(header)-1}.")
                return None

            for row in csv_reader:
                if len(row) > max(0, column_index) and row[0] == str(target_id):  # Check if id matches
                    found = True
                    return row[column_index]
           
        if not found: 
             print(f"No row found with ID {target_id}.")
             return None

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected issue occurred: {e}")
        return None

def modify_row_by_id(csv_file, target_id, column_index, new_value):
    """Modify a specific column in the row with the given ID."""
    try:
        # Temporary list to store CSV data
        rows = []
        header = None
        found = False

        # Step 1: Read the CSV file
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader, None)  # Read header
            if header is None:
                print("Error: CSV file is empty.")
                return False

            # Read and modify the matching row
            for row in csv_reader:
                if len(row) > max(0, column_index) and row[0] == str(target_id):
                    row[column_index] = new_value  # Update the specified column
                    found = True
                rows.append(row)

        if not found:
            print(f"No row found with ID {target_id}.")
            return False

        # Step 2: Write the modified data back to the CSV
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)  # Write header
            csv_writer.writerows(rows)  # Write all rows

        print(f"Successfully updated row with ID {target_id}: column {column_index} set to '{new_value}'.")
        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return False
    except Exception as e:
        print(f"Error: An unexpected issue occurred: {e}")
        return False


def tabulate(table_data, headers=None):
    """
    Custom tabulate function to display tabular data in a grid format.

    Args:
        table_data: List of lists/tuples, where each inner list is a row.
        headers: List/tuple of column headers (optional).

    Returns:
        String containing the formatted table.
    """
    # Handle empty data
    if not table_data and not headers:
        return "No data to display."

    # Convert all data to strings and ensure valid rows
    data = [[str(cell) for cell in row] for row in table_data if isinstance(row, (list, tuple))]
    if not data and headers:
        data = [[] for _ in range(1)]  # Placeholder for headers-only table
    if not data:
        return "No valid rows to display."

    # Include headers in data if provided
    if headers:
        headers = [str(h) for h in headers]
        data = [headers] + data
    else:
        headers = ['' for _ in range(len(data[0]))] if data[0] else []

    # Calculate maximum width for each column
    if not data[0]:  # Handle empty first row
        return "No valid columns to display."

    col_widths = []
    for i in range(len(data[0])):  # Iterate over columns
        max_width = max(len(row[i]) for row in data if i < len(row))
        col_widths.append(max_width)

    if not col_widths:
        return "No valid columns to display."

    # Build table components
    separator = '+' + '+'.join('-' * (w + 2) for w in col_widths) + '+'
    # Fix: Create format string with individual width for each column
    row_format = '||' + '|'.join(' {{:<{}}} '.format(w) for w in col_widths) + '||'

    # Construct the table
    table_lines = [separator]
    for row in data:
        # Pad row with empty strings if shorter than expected
        row = row + [''] * (len(col_widths) - len(row))
        table_lines.append(row_format.format(*row))
        table_lines.append(separator)

    # Return the table string
    return '\n'.join(table_lines)

def fetch_all_entries(data):
        try:
            if  data== "allsolutions":  
                report= "problem_solutions.csv"
            elif  data== "problems":
                report= "No_solutions.csv"
            else:
                report= "reported_solutions.csv"

            # Read the CSV file
            with open(report, 'r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                # Extract header
                header = next(csv_reader, None)
                if header is None:
                    print("Error: CSV file is empty.")
                    return

                # Read all rows
                rows = [row for row in csv_reader]

                # Display table using tabulate
                #print(tabulate(rows, headers=header, tablefmt='grid'))
                print(tabulate(rows, headers=header))

        except FileNotFoundError:
            print(f"Error: File '{csv_file}' not found.")
        except Exception as e:
            print(f"Error: An unexpected issue occurred: {e}")


def main():
    while True:
        print("\nDebug Assist Manager")
        print("1. Add new entry in Issue Repository")
        print("2. Query Solution")
        print("3. Query Team Stats")
        print("4. Query TechArea Stats")
        print("5. Report Solution is Not working")
        print("6. Modify/Update the existing solution")
        print("7. Fetch all Non working/Reported Solutions")
        print("8. Fetch all Reported Problems with no Solutions")
        print("9. Fetch all Solutions")
        print("10. Exit")
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            query_solution()
        elif choice == '3':
            query_stats("Engineer_ID")
        elif choice == '4':
            query_stats("TechArea")
        elif choice == '5':
            report_solution()
        elif choice == '6':
            modify_solution()
        elif choice == '7':
            fetch_all_entries("reported_solutions")
        elif choice == '8':
            fetch_all_entries("problems")
        elif choice == '9':
            fetch_all_entries("allsolutions")
        elif choice == '10':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 - 10.")

if __name__ == "__main__":
    main()

