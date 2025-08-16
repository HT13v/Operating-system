from collections import deque

# Function to implement the Second Chance (Clock) page replacement algorithm
def second_chance_page_replacement(pages, capacity):
    # Initialize variables
    memory = deque()  # To store the pages in memory (acting as a circular queue)
    reference_bits = []  # To store the reference bits (0 or 1)
    page_faults = 0  # To count the number of page faults
    
    print("\nPage Reference | Memory State | Reference Bits | Page Fault")
    print("-" * 50)
    
    for page in pages:
        if page not in memory:
            # If the page is not in memory, it's a page fault
            page_faults += 1
            
            if len(memory) < capacity:
                # If there is space in memory, just add the page
                memory.append(page)
                reference_bits.append(1)  # Set the reference bit to 1 for the newly added page
            else:
                # If memory is full, find a page to replace (clock hand movement)
                while reference_bits[0] == 1:
                    # Give the page at the front of the queue a second chance by setting its reference bit to 0
                    reference_bits[0] = 0
                    memory.append(memory.popleft())
                    reference_bits.append(reference_bits.pop(0))
                
                # Replace the page at the front with the new page
                memory.popleft()
                reference_bits.pop(0)
                memory.append(page)
                reference_bits.append(1)  # Set the reference bit to 1 for the newly added page
            
            print(f"{page:13} | {list(memory)} | {reference_bits} | Yes")
        else:
            # If the page is already in memory, set its reference bit to 1
            idx = memory.index(page)
            reference_bits[idx] = 1
            print(f"{page:13} | {list(memory)} | {reference_bits} | No")
    
    return page_faults

# Example usage
if __name__ == "__main__":
    print("Enter the page reference string (space-separated):")
    pages = list(map(int, input().split()))
    
    print("Enter the memory capacity:")
    capacity = int(input())
    
    # Perform Second Chance page replacement
    page_faults = second_chance_page_replacement(pages, capacity)
    
    # Print the total number of page faults
    print("\nTotal Page Faults:", page_faults)
