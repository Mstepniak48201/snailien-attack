class Player:
    def __init__(self, name):
        self.name = name
        self.sprite = "🌀\x1b[1;92m<\x1b[0m"
        self.counter = 0
        self.slime_trail = "\x1b[1;92m_\x1b[0m"

    def update_sprite(self, counter):
        self.counter = counter
        if self.counter > 75 and self.counter < 80:
            self.sprite = "🟢🌀\x1b[1;92m<\x1b[0m"
        else:
            self.sprite = "🌀\x1b[1;92m<\x1b[0m"
        
            
