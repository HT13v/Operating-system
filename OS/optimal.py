def find_farthest_page(memory, pages, current_index, frames):
    farthest = -1
    farthest_index = -1
    # Iterate through memory pages to find the one to replace
    for i in range(frames):
        j = current_index
        # Find the next occurrence of the page in future references
        while j < len(pages) and memory[i] != pages[j]:
            j += 1
        # If page is not found in the future, it will be replaced
        if j == len(pages):
            return i
        # Find the page that will be used farthest in the future
        if j > farthest:
            farthest = j
            farthest_index = i
    return farthest_index

def main():
    n = int(input("Enter the number of pages: "))
    pages = list(map(int, input("Enter the page sequence: ").split()))
    frames = int(input("Enter the number of frames: "))
    
    memory = []  # Store pages in memory
    page_faults = 0

    for i in range(n):
        page = pages[i]
        # Check if the page is already in memory
        if page not in memory:
            # Page not found in memory (Page fault)
            if len(memory) == frames:
                # Find the page to replace (the farthest page)
                replace_index = find_farthest_page(memory, pages, i, frames)
                memory[replace_index] = page
            else:
                # Add the new page if there's space
                memory.append(page)
            page_faults += 1
        
        # Display the current frame content
        print(f"Frame content: {' '.join(map(str, memory))}")

    print(f"Total page faults (Optimal): {page_faults}")

if __name__ == "__main__":
    main()
