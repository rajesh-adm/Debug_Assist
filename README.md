Read ME:

1.Its python based tool that helps to add and maintain the database of customer/critical/any internal issues with solutions.
2.Its helps quickly retrieve the known solutions while debugging/stuck with issues not present in public domain.
3.Reduces debug time by identifying the engineers to reach out who already fixed the similar issues on specific tech areas.
4.It helps in retrieving no. of solutions given by engineers in the team and in assessing the engineers debugging ability in an area.
5.Helps align the work items/NPIs according to the debugging skill.
6.It assists to constantly update the solutions based on new platforms or tech areas introduced.

Usage:
./Debug_Assist_Manager.py
Debug Assist Manager
1. Add new entry in Issue Repository
2. Query Solution
3. Query Team Stats
4. Report Solution is Not working
5. Fetch all Reported Solutions
6. Modify/Update the existing solution
7. Fetch All Solutions
8. Exit


Enter your choice (1-10): 1
Enter the problem/error message: BGP stats is stuck in idle state
Enter the solution: Verify if the interfaces or cabling is proper or tcp handshake is complete
Enter the author name: sailaja
Enter Tech Area (def:Generic) :BGP
Enter Documentation Link/PR/GLO  (def:NA):
Entry saved successfully!

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
Enter your choice (1-10): 2
Enter the problem to search for (multiple words allowed): ospf
No matching problems found.
Enter the full problem statement: unable to find LSAs in firewall filter accept term from the ospf session
Enter the author name: sanapalar
Enter Tech Area (def:Generic) :ospf
Entry saved successfully!
Problem will be reported to the lead

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
Enter your choice (1-10): 3
+-------------+-----------------------+---------------+
|| Engineer ID | TechArea              | No.of Entries ||
+-------------+-----------------------+---------------+
|| sanapalar   | Spirent (1), ixia (1) | 2             ||
+-------------+-----------------------+---------------+
|| sailaja     | BGP (2), DHCP (1)     | 3             ||
+-------------+-----------------------+---------------+

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
Enter your choice (1-10): 4
+----------+---------------+---------------+
|| TechArea | Engineer ID   | No.of Entries ||
+----------+---------------+---------------+
|| Spirent  | sanapalar (1) | 1             ||
+----------+---------------+---------------+
|| ixia     | sanapalar (1) | 1             ||
+----------+---------------+---------------+
|| BGP      | sailaja (2)   | 2             ||
+----------+---------------+---------------+
|| DHCP     | sailaja (1)   | 1             ||
+----------+---------------+---------------+

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
Enter your choice (1-10): 5
Enter the solution id which is not working: 3
['3', 'BGP Peers down in evpn vxlan spine', '', 'sailaja', 'BGP', 'NA']
Entry logged in report successfully! It will be re-verified and updated after review


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
Enter your choice (1-10): 6
Enter the solution ID to be modified:3
Please find the problem statement: BGP Peers down in evpn vxlan spine
Enter the new solution for the above problem: Please check if the interfaces are down or tcp port 179 is in listening state
Successfully updated row with ID 3: column 2 set to ' Please check if the interfaces are down or tcp port 179 is in listening state'.

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
Enter your choice (1-10): 7
+-------------+------------------------------------+----------+---------+----------+------+
|| Solution ID | Problem                            | Solution | Author  | TechArea | Link ||
+-------------+------------------------------------+----------+---------+----------+------+
|| 3           | BGP Peers down in evpn vxlan spine |          | sailaja | BGP      | NA   ||
+-------------+------------------------------------+----------+---------+----------+------+

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
Enter your choice (1-10): 8
+------------+--------------------------------------------------------------------------+-------------+----------+
|| Problem ID | Problem                                                                 | Reported by | TechArea ||
+------------+--------------------------------------------------------------------------+-------------+----------+
|| 1         | unable to find LSAs in firewall filter accept term from the ospf session | sanapalar   | ospf     ||
+------------+--------------------------------------------------------------------------+-------------+----------+


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
Enter your choice (1-10): 9
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
|| ID | Problem                                                                                      | Solution                                             | Author    | TechArea |  Link                                 ||
+----+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+-----------+---------------------------+
|| 1  | Unable to add dhcp clients on spirent ""undersubscription detected as Average gap            | update pps with higher value and verify              | sanapalar | Spire nt | https://spirent.com/documentation     ||
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
|| 2  | Unable to add dhcp clients on ixia as ports are locked                                       | please unlock the ports in settings-->ports-->unlock | sanapalar | ixi  a   | https://ixia.com/documentation/ports  ||
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+
|| 3  | BGP Peers down in evpn vxlan spine                                                           | please chekc tcp conenction                          | sailaja   | BGP      | NA                                    ||
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------+-----------+----------+---------------------------------------+


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
Enter your choice (1-10): 10
Exiting program.
