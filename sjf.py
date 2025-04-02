import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate SJF (Non-preemptive)
def calculate_sjf(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival, then burst time
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    remaining_processes = processes.copy()
    time = 0
    executed = []

    while remaining_processes:
        # Get processes that have arrived
        available = [p for p in remaining_processes if p[1] <= time]
        if not available:
            time += 1
            continue

        # Select the process with the shortest burst time
        available.sort(key=lambda x: x[2])
        process = available.pop(0)
        remaining_processes.remove(process)

        pid, arrival, burst = process
        start_time = max(time, arrival)
        end_time = start_time + burst
        time = end_time

        executed.append((pid, start_time, burst))

        index = processes.index(process)
        completion_time[index] = end_time
        turnaround_time[index] = end_time - arrival
        waiting_time[index] = turnaround_time[index] - burst

    return waiting_time, turnaround_time, completion_time, executed

# Function to draw Gantt chart
def draw_gantt_chart(executed):
    fig, ax = plt.subplots(figsize=(8, 2))
    for pid, start, burst in executed:
        ax.broken_barh([(start, burst)], (10, 5), facecolors='green')
        ax.text(start + burst / 2, 12, f'P{pid}', ha='center', va='center', color='white')

    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart for SJF Scheduling")
    plt.show()

# Example Process List (Process ID, Arrival Time, Burst Time)
processes = [(1, 0, 6), (2, 2, 8), (3, 4, 7), (4, 5, 3)]
waiting_time, turnaround_time, completion_time, executed = calculate_sjf(processes)

# Convert to DataFrame for easy viewing
df = pd.DataFrame(processes, columns=["Process ID", "Arrival Time", "Burst Time"])
df["Completion Time"] = completion_time
df["Turnaround Time"] = turnaround_time
df["Waiting Time"] = waiting_time

print(df)
draw_gantt_chart(executed)
