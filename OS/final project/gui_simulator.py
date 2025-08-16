import tkinter as tk
from tkinter import ttk
from page_simulator import PageSimulator

class SecondChanceSimulatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Second Chance Paging Simulator")
        self.master.geometry("800x600")

        self.frame_count = tk.IntVar()
        self.page_number = tk.StringVar()
        self.simulator = None

        self.create_widgets()

    def create_widgets(self):
        # Frame count input
        ttk.Label(self.master, text="Number of frames:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.master, textvariable=self.frame_count).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="Set", command=self.set_frame_count).grid(row=0, column=2, padx=5, pady=5)

        # Page number input
        ttk.Label(self.master, text="Page number:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(self.master, textvariable=self.page_number).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="Access", command=self.access_page).grid(row=1, column=2, padx=5, pady=5)

        # Frames display
        self.frames_canvas = tk.Canvas(self.master, width=780, height=400, bg="white")
        self.frames_canvas.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Status display
        self.status_label = ttk.Label(self.master, text="")
        self.status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # Page faults display
        self.page_faults_label = ttk.Label(self.master, text="Total page faults: 0")
        self.page_faults_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def set_frame_count(self):
        try:
            frame_count = self.frame_count.get()
            self.simulator = PageSimulator(frame_count)
            self.update_display()
            self.status_label.config(text=f"Simulator initialized with {frame_count} frames")
        except tk.TclError:
            self.status_label.config(text="Invalid frame count")

    def access_page(self):
        if not self.simulator:
            self.status_label.config(text="Please set the number of frames first")
            return

        try:
            page_number = int(self.page_number.get())
            page_fault = self.simulator.access_page(page_number)
            self.update_display()
            if page_fault:
                self.status_label.config(text=f"Accessing page {page_number}: Page fault", foreground="red")
            else:
                self.status_label.config(text=f"Accessing page {page_number}: Page hit", foreground="green")
            self.page_faults_label.config(text=f"Total page faults: {self.simulator.get_page_faults()}")
        except ValueError:
            self.status_label.config(text="Invalid page number")

    def update_display(self):
        self.frames_canvas.delete("all")
        frames = self.simulator.get_frames()
        second_chance_bits = self.simulator.get_second_chance_bits()

        for i, frame in enumerate(frames):
            x = 20 + i * 80
            y = 20
            self.frames_canvas.create_rectangle(x, y, x + 60, y + 60, outline="black")
            if frame != -1:
                self.frames_canvas.create_text(x + 30, y + 30, text=str(frame))
                if second_chance_bits[i]:
                    self.frames_canvas.create_oval(x + 45, y + 45, x + 55, y + 55, fill="yellow")

def run_gui():
    root = tk.Tk()
    SecondChanceSimulatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()

