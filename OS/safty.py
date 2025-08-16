# Function to check if the system is in a safe state
def is_safe_state(processes, available, max_need, allocation):
    n = len(processes)  # Number of processes
    m = len(available)  # Number of resource types
    
    # Calculate the need matrix
    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    
    # Mark all processes as not finished
    finished = [False] * n
    safe_sequence = []
    
    # Make a copy of available resources
    work = available[:]
    
    while len(safe_sequence) < n:
        allocated = False
        
        for i in range(n):
            if not finished[i]:
                # Check if the current process can be allocated resources
                if all(need[i][j] <= work[j] for j in range(m)):
                    # Simulate resource allocation to process `i`
                    for j in range(m):
                        work[j] += allocation[i][j]
                    
                    safe_sequence.append(processes[i])
                    finished[i] = True
                    allocated = True
                    break
        
        if not allocated:
            # No process can be allocated resources, unsafe state
            return False, []
    
    # Safe sequence found
    return True, safe_sequence

# Function to take user input for Banker's Algorithm
def get_user_input():
    print("Enter the number of processes:")
    n = int(input())
    print("Enter the number of resource types:")
    m = int(input())
    
    print("Enter the allocation matrix (space-separated rows):")
    allocation = []
    for i in range(n):
        row = list(map(int, input(f"Allocation for process {i}: ").split()))
        allocation.append(row)
    
    print("Enter the maximum need matrix (space-separated rows):")
    max_need = []
    for i in range(n):
        row = list(map(int, input(f"Maximum need for process {i}: ").split()))
        max_need.append(row)
    
    print("Enter the available resources (space-separated):")
    available = list(map(int, input().split()))
    
    processes = list(range(n))  # Create a list of process IDs (0 to n-1)
    
    return processes, available, max_need, allocation

# Main function to run the Banker's Algorithm
if __name__ == "__main__":
    print("Banker's Algorithm Simulation")
    
    # Get user input
    processes, available, max_need, allocation = get_user_input()
    
    # Check if the system is in a safe state
    safe, sequence = is_safe_state(processes, available, max_need, allocation)
    
    if safe:
        print("The system is in a safe state.")
        print("Safe sequence:", sequence)
    else:
        print("The system is not in a safe state.")
