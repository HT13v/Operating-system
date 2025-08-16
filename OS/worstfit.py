# Function to implement the Worst Fit algorithm
def worst_fit(block_sizes, process_sizes):
    # Number of memory blocks and processes
    num_blocks = len(block_sizes)
    num_processes = len(process_sizes)
    
    # To store the allocation of memory blocks to processes (-1 means not allocated)
    allocation = [-1] * num_processes
    
    # Iterate through each process
    for i in range(num_processes):
        # Initialize variables to find the worst fit block
        worst_index = -1
        
        for j in range(num_blocks):
            if block_sizes[j] >= process_sizes[i]:
                # If this block is better (larger), update worst_index
                if worst_index == -1 or block_sizes[j] > block_sizes[worst_index]:
                    worst_index = j
        
        # If a suitable block is found, allocate it to the process
        if worst_index != -1:
            allocation[i] = worst_index
            block_sizes[worst_index] -= process_sizes[i]
    
    return allocation

# Example usage
if __name__ == "__main__":
    # Example input
    print("Enter memory block sizes (space-separated):")
    block_sizes = list(map(int, input().split()))
    
    print("Enter process sizes (space-separated):")
    process_sizes = list(map(int, input().split()))
    
    # Perform Worst Fit allocation
    allocation = worst_fit(block_sizes, process_sizes)
    
    # Print the results
    print("\nProcess Allocation Results:")
    for i in range(len(process_sizes)):
        if allocation[i] != -1:
            print(f"Process {i} of size {process_sizes[i]} is allocated to block {allocation[i]}.")
        else:
            print(f"Process {i} of size {process_sizes[i]} cannot be allocated.")
