import utils

class InGameUI:
    def __init__(self, total_steps_taken):
        self.total_steps_taken = total_steps_taken
    
    def display_position(self, total_steps_taken):
        position = int(self.total_steps_taken) 
        # Save current cursor position.
        print("\x1b[s", end="")
        # Counter display position.
        utils.move_cursor_up(7)
        # Print the counter and overwrite the same line
        print(f"\r{position}", end="")
        # Restore saved cursor position (back to player movement area)
        print("\x1b[u", end="") 
        """
         ____    
        | 60 |
         ‾‾‾‾
        """
