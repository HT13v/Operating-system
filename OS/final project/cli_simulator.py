import sys
from page_simulator import PageSimulator

# ANSI color codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

def run_cli(simulator):
    print("Enter page numbers (space-separated) or 'q' to quit:")
    while True:
        try:
            user_input = input(f"{BLUE}> {RESET}")
            if user_input.lower() == 'q':
                break

            page_numbers = list(map(int, user_input.split()))
            for page_number in page_numbers:
                page_fault = simulator.access_page(page_number)

                print(f"Accessing page {page_number}: ", end="")
                if page_fault:
                    print(f"{RED}Page fault{RESET}")
                else:
                    print(f"{GREEN}Page hit{RESET}")

                print("Frames: ", end="")
                frames = simulator.get_frames()
                second_chance_bits = simulator.get_second_chance_bits()
                for i, frame in enumerate(frames):
                    if frame == -1:
                        print("[ ] ", end="")
                    else:
                        print(f"[{frame}", end="")
                        if second_chance_bits[i]:
                            print(f"{YELLOW}*{RESET}", end="")
                        print("] ", end="")
                print()

            print(f"Total page faults: {simulator.get_page_faults()}")
        except ValueError:
            print(f"{RED}Invalid input. Please enter integers or 'q' to quit.{RESET}")

if __name__ == "__main__":
    frame_count = int(input("Enter the number of frames: "))
    simulator = PageSimulator(frame_count)
    run_cli(simulator)

