def fifo_page_replacement(pages, capacity):
    # Initialize variables
    memory = []  # To store the pages in memory
    page_faults = 0  # To count the number of page faults
    
    print("\nPage Reference | Memory State | Page Fault")
    print("-" * 40)
    
    for page in pages:
        if page not in memory:
            # If page is not in memory, it's a page fault
            page_faults += 1
            
            if len(memory) < capacity:
                # If there is space in memory, add the page
                memory.append(page)
            else:
                # If memory is full, replace the oldest page (FIFO)
                memory.pop(0)
                memory.append(page)
            
            print(f"{page:13} | {memory} | Yes")
        else:
            # If page is already in memory, no page fault
            print(f"{page:13} | {memory} | No")
    
    return page_faults

# Example usage
if __name__ == "__main__":
    print("Enter the page reference string (space-separated):")
    pages = list(map(int, input().split()))
    
    print("Enter the memory capacity:")
    capacity = int(input())
    
    # Perform FIFO page replacement
    page_faults = fifo_page_replacement(pages, capacity)
    
    # Print the total number of page faults
    print("\nTotal Page Faults:", page_faults)
