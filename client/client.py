class Client:
    def __init__(self, com_1, com_2):
        self.com_1_port = com_1["port"]
        self.com_2_port = com_2["port"]
        self.com_1_bits = com_1["bits"]
        self.com_2_bits = com_2["bits"]
        self.com_1_even = com_1["even"]
        self.com_1_speed = com_1["speed"]
        self.com_2_speed = com_2["speed"]
        self.com_1_stop = com_1["stop"]
        self.com_2_stop = com_2["stop"]
        self.com_2_even = com_2["even"]

        # Add so on for 1 and 2 coms
