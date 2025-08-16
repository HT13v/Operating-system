import sys
from page_simulator import PageSimulator
from cli_simulator import run_cli
from gui_simulator import run_gui

def main():
    print("Second Chance Paging Simulator")
    print("1. CLI mode")
    print("2. GUI mode")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
            frame_count = int(input("Enter the number of frames: "))
            simulator = PageSimulator(frame_count)
            run_cli(simulator)
        elif choice == 2:
            run_gui()
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

