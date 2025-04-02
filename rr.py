import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

# Function to calculate Round Robin scheduling
def calculate_rr(processes, quantum):
    n = len(processes)
    remaining_burst = [p[2] for p in processes]
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    queue = deque()
    time = 0
    executed = []

    # Sort processes by arrival time and add the first process to the queue
    processes.sort(key=lambda x: x[1])
    queue.append(0)
    visited = [False] * n
    visited[0] = True

    while queue:
        i = queue.popleft()
        pid, arrival, burst = processes[i]

        # Process executes for the time quantum or until it finishes
        execution_time = min(quantum, remaining_burst[i])
        executed.append((pid, time, execution_time))
        time += execution_time
        remaining_burst[i] -= execution_time

        # Add new arrivals to the queue
        for j in range(n):
            if not visited[j] and processes[j][1] <= time and remaining_burst[j] > 0:
                queue.append(j)
                visited[j] = True

        # If process is not yet complete, put it back in queue
        if remaining_burst[i] > 0:
            queue.append(i)
        else:
            completion_time[i] = time
            turnaround_time[i] = completion_time[i] - arrival
            waiting_time[i] = turnaround_time[i] - burst

    return waiting_time, turnaround_time, completion_time, executed

# Function to draw Gantt chart
def draw_gantt_chart(executed):
    fig, ax = plt.subplots(figsize=(8, 2))
    for pid, start, duration in executed:
        ax.broken_barh([(start, duration)], (10, 5), facecolors='orange')
        ax.text(start + duration / 2, 12, f'P{pid}', ha='center', va='center', color='black')

    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart for Round Robin Scheduling")
    plt.show()

# Example Process List (Process ID, Arrival Time, Burst Time)
processes = [(1, 0, 8), (2, 1, 4), (3, 2, 9), (4, 3, 5)]
quantum = 3  # Time slice
waiting_time, turnaround_time, completion_time, executed = calculate_rr(processes, quantum)

# Convert to DataFrame for easy viewing
df = pd.DataFrame(processes, columns=["Process ID", "Arrival Time", "Burst Time"])
df["Completion Time"] = completion_time
df["Turnaround Time"] = turnaround_time
df["Waiting Time"] = waiting_time

print(df)
draw_gantt_chart(executed)
