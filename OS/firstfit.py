# Function to implement the First Fit algorithm
def first_fit(block_sizes, process_sizes):
    # Number of memory blocks and processes
    num_blocks = len(block_sizes)
    num_processes = len(process_sizes)
    
    # To store the allocation of memory blocks to processes (-1 means not allocated)
    allocation = [-1] * num_processes
    
    # Iterate through each process
    for i in range(num_processes):
        # Find the first block that can accommodate the process
        for j in range(num_blocks):
            if block_sizes[j] >= process_sizes[i]:
                # Allocate block `j` to process `i`
                allocation[i] = j
                
                # Reduce the available size of the memory block
                block_sizes[j] -= process_sizes[i]
                break  # Stop searching for a block for this process
    
    return allocation

# Example usage
if __name__ == "__main__":
    # Example input
    print("Enter memory block sizes (space-separated):")
    block_sizes = list(map(int, input().split()))
    
    print("Enter process sizes (space-separated):")
    process_sizes = list(map(int, input().split()))
    
    # Perform First Fit allocation
    allocation = first_fit(block_sizes, process_sizes)
    
    # Print the results
    print("\nProcess Allocation Results:")
    for i in range(len(process_sizes)):
        if allocation[i] != -1:
            print(f"Process {i} of size {process_sizes[i]} is allocated to block {allocation[i]}.")
        else:
            print(f"Process {i} of size {process_sizes[i]} cannot be allocated.")
