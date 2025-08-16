from collections import deque

class PageSimulator:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.frames = []
        self.second_chance_bits = []
        self.page_queue = deque()
        self.page_to_frame_map = {}
        self.page_faults = 0

    def access_page(self, page_number):
        if page_number in self.page_to_frame_map:
            frame_index = self.page_to_frame_map[page_number]
            self.second_chance_bits[frame_index] = True
            return False

        self.page_faults += 1

        if len(self.frames) < self.frame_count:
            self.frames.append(page_number)
            self.second_chance_bits.append(False)
            self.page_queue.append(page_number)
            self.page_to_frame_map[page_number] = len(self.frames) - 1
        else:
            while True:
                oldest_page = self.page_queue.popleft()
                frame_index = self.page_to_frame_map[oldest_page]

                if self.second_chance_bits[frame_index]:
                    self.second_chance_bits[frame_index] = False
                    self.page_queue.append(oldest_page)
                else:
                    del self.page_to_frame_map[oldest_page]
                    self.frames[frame_index] = page_number
                    self.second_chance_bits[frame_index] = False
                    self.page_queue.append(page_number)
                    self.page_to_frame_map[page_number] = frame_index
                    break

        return True

    def get_page_faults(self):
        return self.page_faults

    def get_frames(self):
        return self.frames

    def get_second_chance_bits(self):
        return self.second_chance_bits

