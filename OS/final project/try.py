import tkinter as tk
from tkinter import messagebox
import os
import platform
import subprocess


# Page Replacement Algorithms
def fifo_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0
    for page in pages:
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1
    return page_faults

def lru_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0
    for page in pages:
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                lru = min(frame, key=lambda x: pages[:pages.index(page)].count(x))
                frame.remove(lru)
                frame.append(page)
            page_faults += 1
        else:
            frame.remove(page)
            frame.append(page)
    return page_faults

def optimal_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0
    for i in range(len(pages)):
        if pages[i] not in frame:
            if len(frame) < frame_size:
                frame.append(pages[i])
            else:
                future_uses = {page: (pages[i + 1:].index(page) if page in pages[i + 1:] else float('inf')) for page in frame}
                farthest_page = max(future_uses, key=future_uses.get)
                frame.remove(farthest_page)
                frame.append(pages[i])
            page_faults += 1
    return page_faults

def second_chance_page_replacement(pages, frame_size):
    frame = []
    use_bit = {}
    page_faults = 0
    pointer = 0
    for page in pages:
        if page in frame:
            use_bit[page] = 1
        else:
            if len(frame) < frame_size:
                frame.append(page)
                use_bit[page] = 1
            else:
                while use_bit[frame[pointer]] == 1:
                    use_bit[frame[pointer]] = 0
                    pointer = (pointer + 1) % frame_size
                use_bit.pop(frame[pointer])
                frame[pointer] = page
                use_bit[page] = 1
                pointer = (pointer + 1) % frame_size
            page_faults += 1
    return page_faults

# System Info Functions
def system_info():
    os_info = platform.system()
    version = platform.version()
    release = platform.release()
    arch = platform.architecture()[0]
    return f"OS: {os_info} {release}\nVersion: {version}\nArchitecture: {arch}"

def show_system_info():
    info = system_info()
    messagebox.showinfo("System Info", info)

def list_running_processes():
    try:
        if platform.system() == "Linux" or platform.system() == "Darwin":
            process_list = subprocess.check_output(["ps", "-e"], text=True)
        elif platform.system() == "Windows":
            process_list = subprocess.check_output(["tasklist"], text=True)
        else:
            process_list = "Unsupported OS for process listing."
        return process_list
    except Exception as e:
        return f"Error retrieving processes: {str(e)}"

def show_running_processes():
    processes = list_running_processes()
    process_window = tk.Toplevel()
    process_window.title("Running Processes")
    process_window.geometry("600x400")

    text_widget = tk.Text(process_window, wrap="none")
    text_widget.insert("1.0", processes)
    text_widget.config(state="disabled")
    text_widget.pack(expand=True, fill="both")

def disk_usage():
    try:
        if platform.system() == "Linux" or platform.system() == "Darwin":
            usage = subprocess.check_output(["df", "-h"], text=True)
        elif platform.system() == "Windows":
            usage = subprocess.check_output(["wmic", "logicaldisk", "get", "size,freespace,caption"], text=True)
        else:
            usage = "Unsupported OS for disk usage."
        return usage
    except Exception as e:
        return f"Error retrieving disk usage: {str(e)}"

def show_disk_usage():
    usage = disk_usage()
    usage_window = tk.Toplevel()
    usage_window.title("Disk Usage")
    usage_window.geometry("600x400")

    text_widget = tk.Text(usage_window, wrap="none")
    text_widget.insert("1.0", usage)
    text_widget.config(state="disabled")
    text_widget.pack(expand=True, fill="both")

# Handling User Input
def validate_input():
    try:
        pages = list(map(int, entry_pages.get().split()))
        frame_size = int(entry_frame_size.get())
        if frame_size <= 0:
            raise ValueError("Frame size must be positive.")
        return pages, frame_size
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")
        return None, None

# Displaying Results and Explanation
def show_fifo():
    pages, frame_size = validate_input()
    if pages is not None and frame_size is not None:
        faults = fifo_page_replacement(pages, frame_size)
        messagebox.showinfo("FIFO Result", f"Total Page Faults: {faults}\nFIFO Explanation: Replaces the oldest page.")

def show_lru():
    pages, frame_size = validate_input()
    if pages is not None and frame_size is not None:
        faults = lru_page_replacement(pages, frame_size)
        messagebox.showinfo("LRU Result", f"Total Page Faults: {faults}\nLRU Explanation: Replaces the least recently used page.")

def show_optimal():
    pages, frame_size = validate_input()
    if pages is not None and frame_size is not None:
        faults = optimal_page_replacement(pages, frame_size)
        messagebox.showinfo("Optimal Result", f"Total Page Faults: {faults}\nOptimal Explanation: Replaces the page that won't be used for the longest time.")

def show_second_chance():
    pages, frame_size = validate_input()
    if pages is not None and frame_size is not None:
        faults = second_chance_page_replacement(pages, frame_size)
        messagebox.showinfo("Second Chance Result", f"Total Page Faults: {faults}\nSecond Chance Explanation: Uses a reference bit to decide which page to replace.")

# Creating the Interface
def create_interface():
    root = tk.Tk()
    root.title("Page Replacement Algorithms")
    root.geometry("500x700")

    tk.Label(root, text="Page Replacement Simulator", font=("Arial", 18), fg="blue").pack(pady=15)

    tk.Label(root, text="Enter Pages (space-separated):", font=("Arial", 12)).pack()
    global entry_pages
    entry_pages = tk.Entry(root, width=40)
    entry_pages.pack(pady=5)

    tk.Label(root, text="Enter Frame Size:", font=("Arial", 12)).pack()
    global entry_frame_size
    entry_frame_size = tk.Entry(root, width=20)
    entry_frame_size.pack(pady=5)

    tk.Button(root, text="FIFO", width=25, height=2, bg="lightblue", command=show_fifo).pack(pady=10)
    tk.Button(root, text="LRU", width=25, height=2, bg="lightgreen", command=show_lru).pack(pady=10)
    tk.Button(root, text="Optimal", width=25, height=2, bg="lightyellow", command=show_optimal).pack(pady=10)
    tk.Button(root, text="Second Chance", width=25, height=2, bg="lightcoral", command=show_second_chance).pack(pady=10)

    tk.Button(root, text="System Info", width=25, height=2, bg="lightgray", command=show_system_info).pack(pady=10)
    tk.Button(root, text="Running Processes", width=25, height=2, bg="lightpink", command=show_running_processes).pack(pady=10)
    tk.Button(root, text="Disk Usage", width=25, height=2, bg="lightcyan", command=show_disk_usage).pack(pady=10)

    root.mainloop()

if __name__ == "_main_":
    create_interface()