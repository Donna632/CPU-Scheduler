import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate waiting time and turnaround time
def calculate_fcfs(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    completion_time[0] = processes[0][1] + processes[0][2]  # Arrival + Burst Time
    turnaround_time[0] = completion_time[0] - processes[0][1]
    waiting_time[0] = turnaround_time[0] - processes[0][2]

    for i in range(1, n):
        completion_time[i] = max(completion_time[i - 1], processes[i][1]) + processes[i][2]
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

    return waiting_time, turnaround_time, completion_time

# Function to draw Gantt chart
def draw_gantt_chart(processes, completion_time):
    fig, ax = plt.subplots(figsize=(8, 2))
    start_time = 0

    for i, (pid, arrival, burst) in enumerate(processes):
        ax.broken_barh([(start_time, burst)], (10, 5), facecolors='blue')
        ax.text(start_time + burst / 2, 12, f'P{pid}', ha='center', va='center', color='white')
        start_time = completion_time[i]

    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_xticks(completion_time)
    ax.set_title("Gantt Chart for FCFS Scheduling")
    plt.show()

# Example Process List (Process ID, Arrival Time, Burst Time)
processes = [(1, 0, 5), (2, 1, 3), (3, 2, 8), (4, 3, 6)]
waiting_time, turnaround_time, completion_time = calculate_fcfs(processes)

# Convert to DataFrame for easy viewing
df = pd.DataFrame(processes, columns=["Process ID", "Arrival Time", "Burst Time"])
df["Completion Time"] = completion_time
df["Turnaround Time"] = turnaround_time
df["Waiting Time"] = waiting_time

print(df)
draw_gantt_chart(processes, completion_time)
