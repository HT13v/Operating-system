class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_fcfs(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        process.completion_time = current_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

    print("\nProcess ID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process in processes:
        print(f"{process.pid}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

    print(f"\nAverage Turnaround Time: {total_turnaround_time / len(processes):.2f}")
    print(f"Average Waiting Time: {total_waiting_time / len(processes):.2f}")

if __name__ == "__main__":
    processes = []
    n = int(input("Enter the number of processes: "))
    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for Process {i+1}: "))
        burst_time = int(input(f"Enter burst time for Process {i+1}: "))
        pid = f"P{i+1}"
        processes.append(Process(pid, arrival_time, burst_time))

    calculate_fcfs(processes)
