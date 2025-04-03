import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Function to run the scheduler
def run_scheduler():
    processes = entry_processes.get().split(',')
    burst_times = list(map(int, entry_burst.get().split(',')))
    
    if len(processes) != len(burst_times):
        messagebox.showerror("Input Error", "Number of processes and burst times must be equal.")
        return
    
    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)

    # Calculate Waiting Time and Turnaround Time
    for i in range(1, len(processes)):
        waiting_time[i] = waiting_time[i - 1] + burst_times[i - 1]
        turnaround_time[i] = waiting_time[i] + burst_times[i]

    avg_waiting_time = sum(waiting_time) / len(waiting_time)
    avg_turnaround_time = sum(turnaround_time) / len(turnaround_time)

    # Display Performance Metrics
    messagebox.showinfo(
        "Performance Metrics", 
        f"Average Waiting Time: {avg_waiting_time:.2f}\nAverage Turnaround Time: {avg_turnaround_time:.2f}"
    )

    # Display results in a table
    df = pd.DataFrame({
        "Process": processes,
        "Burst Time": burst_times,
        "Waiting Time": waiting_time,
        "Turnaround Time": turnaround_time
    })
    
    result_label.config(text=df.to_string(index=False))

# Function to clear all input fields
def clear_fields():
    entry_processes.delete(0, tk.END)
    entry_burst.delete(0, tk.END)
    result_label.config(text="")

# Main Window
root = tk.Tk()
root.title("CPU Scheduler Simulator")
root.geometry("500x400")
root.configure(bg="#f4f4f4")  # Light gray background
root.resizable(False, False)  # Prevent resizing

# Title Label
title_label = tk.Label(root, text="CPU Scheduler Simulator", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)

# Process Entry
frame1 = tk.Frame(root, bg="#f4f4f4")
frame1.pack(pady=5)
tk.Label(frame1, text="Processes (comma-separated):", font=("Arial", 12), bg="#f4f4f4").pack(side=tk.LEFT)
entry_processes = tk.Entry(frame1, font=("Arial", 12), width=20)
entry_processes.pack(side=tk.LEFT, padx=5)

# Burst Time Entry
frame2 = tk.Frame(root, bg="#f4f4f4")
frame2.pack(pady=5)
tk.Label(frame2, text="Burst Times (comma-separated):", font=("Arial", 12), bg="#f4f4f4").pack(side=tk.LEFT)
entry_burst = tk.Entry(frame2, font=("Arial", 12), width=20)
entry_burst.pack(side=tk.LEFT, padx=5)

# Buttons
frame3 = tk.Frame(root, bg="#f4f4f4")
frame3.pack(pady=10)
run_button = tk.Button(frame3, text="Run Scheduler", font=("Arial", 12, "bold"), bg="#28a745", fg="white", command=run_scheduler)
run_button.pack(side=tk.LEFT, padx=10)
clear_button = tk.Button(frame3, text="Clear", font=("Arial", 12, "bold"), bg="#dc3545", fg="white", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Courier", 10), bg="#f4f4f4", justify="left")
result_label.pack(pady=10)

root.mainloop()
