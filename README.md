CPU Scheduler Simulator

A Python-based CPU scheduling simulator that helps visualize different scheduling algorithms. The program simulates the execution of processes and generates Gantt charts for better understanding. Additionally, it calculates performance metrics such as waiting time, turnaround time, and response time.

Features
--------
✅ Supports multiple scheduling algorithms:

First-Come, First-Served (FCFS)

Shortest Job First (SJF - Non-preemptive & Preemptive)

Round Robin (RR)

Priority Scheduling (Non-preemptive & Preemptive)

✅ Process Visualization using Gantt Charts

✅ Performance Metrics Calculation:

Waiting Time

Turnaround Time

Response Time

✅ User-friendly GUI using Tkinter

✅ Real-time simulation of CPU scheduling

How It Works
------------
1. Process Input
   
The user enters process details such as process ID, arrival time, burst time, and priority (for priority scheduling).

For Round Robin scheduling, the user must also specify the time quantum.

2. CPU Scheduling Algorithm Execution
   
Based on the selected scheduling algorithm, the CPU scheduler executes the processes.

The program simulates how the CPU executes each process and records the start and finish times.

3. Gantt Chart Generation
   
After scheduling, the program generates a Gantt chart to visually represent the execution order of processes.

5. Performance Metrics Calculation
   
The program calculates waiting time, turnaround time, and response time for each process.

It also calculates average waiting time and average turnaround time and displays them.

Installation and Setup:
-----------------------
Prerequisites:


Ensure you have Python 3 installed on your system. If you don't have it, download it from Python Official Website.

Install Required Libraries:

Run the following command in the terminal to install dependencies:

pip install matplotlib pandas

Run the Simulator

Navigate to the project directory and execute:

python scheduler_gui.py

Example Output:
---------------

Gantt Chart Example:

The Gantt chart visually represents the scheduling order of processes.


| P1 | P2 | P3 | P4 |

0    2    5    9   12

Performance Metrics Example:


After execution, the program displays the following:


Process | Arrival Time | Burst Time | Waiting Time | Turnaround Time  
 
P1      | 0           | 2         | 0           | 2  
P2      | 1           | 3         | 1           | 4  
P3      | 2           | 4         | 3           | 7  
P4      | 3           | 3         | 6           | 9  
Average Waiting Time: 2.5
Average Turnaround Time: 5.5

A pop-up message will also display the average waiting time and turnaround time.
