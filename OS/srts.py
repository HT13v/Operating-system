class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


def srtf_scheduling(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    minimum_remaining_time = float('inf')
    shortest = 0
    check = False
    time_chart = []

    while completed != n:
        #-----------------------------------------------------------------------------------------------------shortest remaining time
        for i in range(n):
            if processes[i].arrival_time <= current_time and processes[i].remaining_time < minimum_remaining_time and processes[i].remaining_time > 0:
                minimum_remaining_time = processes[i].remaining_time
                shortest = i
                check = True

        if not check:
            current_time += 1
            continue
        #-----------------------------------------------------------------------------------------------------------process starts
        time_chart.append(processes[shortest].pid)
        processes[shortest].remaining_time -= 1
        minimum_remaining_time = processes[shortest].remaining_time

        if minimum_remaining_time == 0:
            minimum_remaining_time = float('inf')
        if processes[shortest].remaining_time == 0:
            completed += 1
            check = False
            finish_time = current_time + 1
            processes[shortest].completion_time = finish_time
            processes[shortest].turnaround_time = finish_time - processes[shortest].arrival_time
            processes[shortest].waiting_time = processes[shortest].turnaround_time - processes[shortest].burst_time
        current_time += 1
    return processes

def print_results(processes):
    total_turnaround_time = 0
    total_waiting_time = 0
    print("\nProcess\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

    print(f"\nAverage Turnaround Time: {total_turnaround_time / len(processes):.2f}")
    print(f"Average Waiting Time: {total_waiting_time / len(processes):.2f}")

if __name__ == "__main__":
    processes = []
    n = int(input("Enter number of processes: "))

    for i in range(n):
        pid = f"P{i+1}"
        arrival_time = int(input(f"Enter arrival time for process {pid}: "))
        burst_time = int(input(f"Enter burst time for process {pid}: "))
        processes.append(Process(pid, arrival_time, burst_time))

    processes.sort(key=lambda x: x.arrival_time)
    processes = srtf_scheduling(processes)
    print_results(processes)
