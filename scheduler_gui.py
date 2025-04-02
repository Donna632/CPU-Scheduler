import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import random

# Function for FCFS Scheduling
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time
    completion_time, turnaround_time, waiting_time, gantt_chart = [], [], [], []
    time = 0

    for pid, arrival, burst, _ in processes:
        start_time = max(time, arrival)
        end_time = start_time + burst
        time = end_time

        completion_time.append(end_time)
        turnaround_time.append(end_time - arrival)
        waiting_time.append(turnaround_time[-1] - burst)
        gantt_chart.append((pid, start_time, burst))

    return completion_time, turnaround_time, waiting_time, gantt_chart

# Function for Shortest Job First (SJF) Scheduling
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by Arrival Time, then Burst Time
    completion_time, turnaround_time, waiting_time, gantt_chart = [], [], [], []
    time = 0

    for pid, arrival, burst, _ in sorted(processes, key=lambda x: x[2]):  # Sort by Burst Time
        start_time = max(time, arrival)
        end_time = start_time + burst
        time = end_time

        completion_time.append(end_time)
        turnaround_time.append(end_time - arrival)
        waiting_time.append(turnaround_time[-1] - burst)
        gantt_chart.append((pid, start_time, burst))

    return completion_time, turnaround_time, waiting_time, gantt_chart

# Function for Round Robin (RR) Scheduling
def round_robin(processes, quantum):
    queue, gantt_chart = [], []
    waiting_time, turnaround_time, completion_time = [0] * len(processes), [0] * len(processes), [0] * len(processes)
    remaining_burst = {pid: burst for pid, _, burst, _ in processes}
    time, i = 0, 0

    while True:
        done = True
        for pid, arrival, burst, _ in processes:
            if remaining_burst[pid] > 0:
                done = False
                if remaining_burst[pid] > quantum:
                    queue.append((pid, time, quantum))
                    time += quantum
                    remaining_burst[pid] -= quantum
                else:
                    queue.append((pid, time, remaining_burst[pid]))
                    time += remaining_burst[pid]
                    waiting_time[i] = time - burst - arrival
                    turnaround_time[i] = time - arrival
                    completion_time[i] = time
                    remaining_burst[pid] = 0
        if done:
            break

    for entry in queue:
        gantt_chart.append(entry)

    return completion_time, turnaround_time, waiting_time, gantt_chart

# Function for Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x[3], x[1]))  # Sort by Priority, then Arrival Time
    completion_time, turnaround_time, waiting_time, gantt_chart = [], [], [], []
    time = 0

    for pid, arrival, burst, priority in processes:
        start_time = max(time, arrival)
        end_time = start_time + burst
        time = end_time

        completion_time.append(end_time)
        turnaround_time.append(end_time - arrival)
        waiting_time.append(turnaround_time[-1] - burst)
        gantt_chart.append((pid, start_time, burst))

    return completion_time, turnaround_time, waiting_time, gantt_chart

# Function to draw Gantt Chart with different colors for each process
def draw_gantt_chart(gantt_chart):
    fig, ax = plt.subplots(figsize=(8, 2))
    
    colors = {}  # Store unique colors for each process
    for pid, start, burst in gantt_chart:
        if pid not in colors:
            colors[pid] = (random.random(), random.random(), random.random())  # Generate a random color
        ax.broken_barh([(start, burst)], (10, 5), facecolors=colors[pid])
        ax.text(start + burst / 2, 12, f'P{pid}', ha='center', va='center', color='white')

    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.set_title("Gantt Chart")
    plt.show()

# Function to run the selected algorithm
def run_scheduler():
    try:
        processes = []
        for i in range(len(entry_list)):
            pid = i + 1
            arrival = int(entry_list[i][0].get())
            burst = int(entry_list[i][1].get())
            priority = int(entry_list[i][2].get()) if entry_list[i][2].get() else 0
            processes.append((pid, arrival, burst, priority))

        selected_algorithm = algo_var.get()
        quantum = int(quantum_entry.get()) if selected_algorithm == "Round Robin" else None

        if selected_algorithm == "FCFS":
            completion_time, turnaround_time, waiting_time, gantt_chart = fcfs_scheduling(processes)
        elif selected_algorithm == "SJF":
            completion_time, turnaround_time, waiting_time, gantt_chart = sjf_scheduling(processes)
        elif selected_algorithm == "Round Robin":
            completion_time, turnaround_time, waiting_time, gantt_chart = round_robin(processes, quantum)
        elif selected_algorithm == "Priority":
            completion_time, turnaround_time, waiting_time, gantt_chart = priority_scheduling(processes)
        else:
            messagebox.showerror("Error", "Invalid algorithm selected!")
            return

        # Calculate Performance Metrics
        avg_waiting_time = sum(waiting_time) / len(waiting_time)
        avg_turnaround_time = sum(turnaround_time) / len(turnaround_time)

        # Display performance metrics
        messagebox.showinfo("Performance Metrics",
                            f"Average Waiting Time: {avg_waiting_time:.2f}\n"
                            f"Average Turnaround Time: {avg_turnaround_time:.2f}")

        # Print DataFrame
        df = pd.DataFrame(processes, columns=["Process ID", "Arrival Time", "Burst Time", "Priority"])
        df["Completion Time"] = completion_time
        df["Turnaround Time"] = turnaround_time
        df["Waiting Time"] = waiting_time
        print(df)

        # Draw Gantt Chart
        draw_gantt_chart(gantt_chart)

    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numeric values.")

# GUI Setup
root = tk.Tk()
root.geometry("500x400")  
root.configure(bg="#f0f0f0")  
root.title("CPU Scheduler Simulator")

tk.Label(root, text="CPU Scheduling Simulator", font=("Arial", 14, "bold"), bg="#f0f0f0").grid(row=0, columnspan=4, pady=10)
tk.Label(root, text="Arrival Time", font=("Arial", 10, "bold"), bg="#f0f0f0").grid(row=1, column=0)
tk.Label(root, text="Burst Time", font=("Arial", 10, "bold"), bg="#f0f0f0").grid(row=1, column=1)
tk.Label(root, text="Priority (Only for Priority Scheduling)", font=("Arial", 10, "bold"), bg="#f0f0f0").grid(row=1, column=2)

entry_list = []
for i in range(4):  
    row_entries = [tk.Entry(root, width=10), tk.Entry(root, width=10), tk.Entry(root, width=10)]
    row_entries[0].grid(row=i+2, column=0)
    row_entries[1].grid(row=i+2, column=1)
    row_entries[2].grid(row=i+2, column=2)
    entry_list.append(row_entries)

tk.Label(root, text="Select Algorithm:").grid(row=6, column=0, pady=10)
algo_var = tk.StringVar(value="FCFS")
tk.OptionMenu(root, algo_var, "FCFS", "SJF", "Round Robin", "Priority").grid(row=6, column=1)

tk.Label(root, text="Time Quantum (Only for RR):").grid(row=7, column=0)
quantum_entry = tk.Entry(root, width=10)
quantum_entry.grid(row=7, column=1)

tk.Button(root, text="Run Scheduler", command=run_scheduler, bg="#007BFF", fg="white").grid(row=8, columnspan=3, pady=10)

root.mainloop()
