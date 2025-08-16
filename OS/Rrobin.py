def round_robin(processes, burst_times, quantum):
    num_processes = len(processes)
    remaining_times = burst_times[:]
    waiting_times = [0] * num_processes
    turn_around_times = [0] * num_processes
    time_elapsed = 0

    while True:
        done = True
        for i in range(num_processes):
            #--------------------------------------------------------------remaining burst time check
            if remaining_times[i] > 0:
                done = False
                if remaining_times[i] > quantum:
                    time_elapsed += quantum
                    remaining_times[i] -= quantum
                else:
                    time_elapsed += remaining_times[i]
                    waiting_times[i] = time_elapsed - burst_times[i]
                    remaining_times[i] = 0

        if done:
            break

    #-------------------------------------------------------------------------turnaround time count
    for i in range(num_processes):
        turn_around_times[i] = burst_times[i] + waiting_times[i]

    return waiting_times, turn_around_times

num_processes = int(input("Enter the number of processes: "))
processes = []
burst_times = []

for i in range(num_processes):
    process_name = input(f"Enter the name of process {i + 1}: ")
    burst_time = int(input(f"Enter the burst time for process {process_name}: "))
    processes.append(process_name)
    burst_times.append(burst_time)

quantum = int(input("Enter the time quantum: "))

waiting_times, turn_around_times = round_robin(processes, burst_times, quantum)

print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turn_around_times[i]}")
