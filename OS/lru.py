from collections import deque

# Function to implement the LRU page replacement algorithm
def lru_page_replacement(pages, capacity):
    # Initialize variables
    memory = deque()  # To store the pages in memory (queue for efficient removal)
    page_faults = 0  # To count the number of page faults
    page_order = {}  # To store the order of pages for quick lookup
    
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
                # If memory is full, remove the least recently used page
                lru_page = memory.popleft()
                memory.append(page)
            
            print(f"{page:13} | {list(memory)} | Yes")
        else:
            # If page is already in memory, move it to the most recent position
            memory.remove(page)
            memory.append(page)
            print(f"{page:13} | {list(memory)} | No")
    
    return page_faults

# Example usage
if __name__ == "__main__":
    print("Enter the page reference string (space-separated):")
    pages = list(map(int, input().split()))
    
    print("Enter the memory capacity:")
    capacity = int(input())
    
    # Perform LRU page replacement
    page_faults = lru_page_replacement(pages, capacity)
    
    # Print the total number of page faults
    print("\nTotal Page Faults:", page_faults)
