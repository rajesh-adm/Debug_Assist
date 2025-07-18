Below is a `README.md` file for the **Debug Assist Manager**, a Python-based tool described in your content. The README is structured to provide an overview, features, usage instructions, and sample interactions based on the provided details. It uses Markdown formatting for clarity and includes tables to reflect the output format shown in your examples.



# Debug Assist Manager

## Overview

Debug Assist Manager is a Python-based tool designed to streamline the management and resolution of customer, critical, or internal issues by maintaining a database of problems and their solutions. It helps engineers quickly retrieve known solutions, identify relevant team members with expertise, and track debugging performance. The tool is particularly useful for reducing debug time and aligning work items or New Product Introductions (NPIs) based on debugging skills.

## Features

1. **Issue Repository Management**:
   - Add and maintain a database of issues with corresponding solutions, authors, and technology areas.
2. **Quick Solution Retrieval**:
   - Query known solutions for issues not available in the public domain, speeding up debugging.
3. **Team Expertise Identification**:
   - Identify engineers who have previously resolved similar issues in specific technology areas.
4. **Performance Tracking**:
   - Retrieve statistics on the number of solutions contributed by engineers to assess debugging capabilities.
5. **Work Alignment**:
   - Align tasks or NPIs based on engineers' debugging expertise in specific areas.
6. **Dynamic Updates**:
   - Update solutions as new platforms or technology areas are introduced.

## Installation

1. **Prerequisites**:
   - Python 3.6 or higher.
   - Required libraries: `tabulate` (for table formatting).
   - Install dependencies:
     ```bash
     pip install tabulate
     ```

2. **Clone or Download**:
   - Clone the repository or download the `Debug_Assist_Manager.py` script.
     ```bash
     git clone <repository_url>
     ```

3. **Run the Script**:
   - Execute the script from the command line:
     ```bash
     python Debug_Assist_Manager.py
     ```

## Usage

Run the script to access the interactive menu:

```bash
./Debug_Assist_Manager.py
```

### Menu Options

The tool provides the following options:

1. **Add new entry in Issue Repository**: Add a new issue with its solution, author, and tech area.
2. **Query Solution**: Search for a solution by problem description.
3. **Query Team Stats**: Display statistics on engineers' contributions by tech area.
4. **Query TechArea Stats**: Show issue counts by technology area and engineer.
5. **Report Solution is Not Working**: Log a solution as ineffective for review.
6. **Modify/Update the existing solution**: Update the solution for an existing issue.
7. **Fetch all Non working/Reported Solutions**: List solutions reported as not working.
8. **Fetch all Reported Problems with no Solutions**: List problems without solutions.
9. **Fetch all Solutions**: Display all stored issues and solutions.
10. **Exit**: Exit the program.

### Sample Interactions

#### 1. Add New Entry
```
Debug Assist Manager

1. Add new entry in Issue Repository
2. Query Solution
3. Query Team Stats
4. Query TechArea Stats
5. Report Solution is Not working
6. Modify/Update the existing solution
7. Fetch all Non working/Reported Solutions
8. Fetch all Reported Problems with no Solutions
9. Fetch all Solutions
10. Exit
-> Enter your choice (1-10): 1
-> Enter the problem/error message: BGP stats is stuck in idle state
Enter the solution: Verify if the interfaces or cabling is proper or tcp handshake is complete
Enter the author name: sailaja
Enter Tech Area (def:Generic): BGP
Enter Documentation Link/PR/GLO (def:NA): NA
Entry saved successfully!
```

#### 2. Query Solution (No Match, Add New Problem)
```
-> Enter your choice (1-10): 2
Enter the problem to search for (multiple words allowed): ospf
No matching problems found.
Enter the full problem statement: unable to find LSAs in firewall filter accept term from the ospf session
Enter the author name: sanapalar
Enter Tech Area (def:Generic): ospf
Entry saved successfully! Problem will be reported to the lead
```
```
-> Enter your choice (1-10): 2
Enter the problem to search for (multiple words allowed): dhcp clients
+----+-----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
|| ID | Problem                                                                                                                     | Solution                                             | Author    | TechArea | Link                                  ||
+----+-----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
|| 1  | Unable to add dhcp clients on spirent ""undersubscription detected as Average gap (IFG and IBG) (1.25e+10 bytes) is greater | update pps with higher value and verify              | sanapalar | Spirent  | https://spirent.com/documentation     ||
+----+-----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
|| 2  | Unable to add dhcp clients on ixia as ports are locked                                                                      | please unlock the ports in settings-->ports-->unlock | sanapalar | ixia     |  https://ixia.com/documentation/ports ||
+----+-----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
```
#### 3. Query Team Stats
```
-> Enter your choice (1-10): 3
+-------------+-----------------------+---------------+
| Engineer ID | TechArea              | No.of Entries |
+-------------+-----------------------+---------------+
| sanapalar   | Spirent (1), ixia (1) | 2             |
| sailaja     | BGP (2), DHCP (1)     | 3             |
+-------------+-----------------------+---------------+
```

#### 4. Query TechArea Stats
```
-> Enter your choice (1-10): 4
+----------+---------------+---------------+
| TechArea | Engineer ID   | No.of Entries |
+----------+---------------+---------------+
| Spirent  | sanapalar (1) | 1             |
| ixia     | sanapalar (1) | 1             |
| BGP      | sailaja (2)   | 2             |
| DHCP     | sailaja (1)   | 1             |
+----------+---------------+---------------+
```

#### 5. Report Solution Not Working
```
-> Enter your choice (1-10): 5
Enter the solution id which is not working: 3
Entry logged in report successfully! It will be re-verified and updated after review
```

#### 6. Modify/Update Solution
```
-> Enter your choice (1-10): 6
Enter the solution ID to be modified: 3
Please find the problem statement: BGP Peers down in evpn vxlan spine
Enter the new solution for the above problem: Please check if the interfaces are down or tcp port 179 is in listening state
Successfully updated row with ID 3: column 2 set to 'Please check if the interfaces are down or tcp port 179 is in listening state'.
```

#### 7. Fetch Non-working/Reported Solutions
```
-> Enter your choice (1-10): 7
+-------------+------------------------------------+----------+---------+----------+------+
| Solution ID | Problem                           | Solution | Author  | TechArea | Link |
+-------------+------------------------------------+----------+---------+----------+------+
| 3           | BGP Peers down in evpn vxlan spine |          | sailaja | BGP      | NA   |
+-------------+------------------------------------+----------+---------+----------+------+
```

#### 8. Fetch Reported Problems with No Solutions
```
-> Enter your choice (1-10): 8
+------------+--------------------------------------------------------------------------+-------------+----------+
| Problem ID | Problem                                                                  | Reported by | TechArea |
+------------+--------------------------------------------------------------------------+-------------+----------+
| 1          | unable to find LSAs in firewall filter accept term from the ospf session | sanapalar   | ospf     |
+------------+--------------------------------------------------------------------------+-------------+----------+
```

#### 9. Fetch All Solutions
```
-> Enter your choice (1-10): 9
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
| ID | Problem                                                                                       | Solution                                             | Author    | TechArea | Link                                  |
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
| 1  | Unable to add dhcp clients on spirent "undersubscription detected as Average gap               | update pps with higher value and verify              | sanapalar | Spirent  | https://spirent.com/documentation     |
| 2  | Unable to add dhcp clients on ixia as ports are locked                                         | please unlock the ports in settings-->ports-->unlock | sanapalar | ixia     | https://ixia.com/documentation/ports  |
| 3  | BGP Peers down in evpn vxlan spine                                                            | please chekc tcp conenction                          | sailaja   | BGP      | NA                                    |
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
```

#### 10. Exit
```
-> Enter your choice (1-10): 10
Exiting program.
```

## Configuration

- **Database**: The tool likely uses a local database (e.g., SQLite, CSV) to store issues, solutions, authors, and tech areas. Ensure the database file is in the correct path as specified in the script.
- **Dependencies**: Requires the `tabulate` library for table formatting. Install it using:
  ```bash
  pip install tabulate
  ```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For issues or feature requests, please contact the repository maintainer or open an issue on GitHub.

