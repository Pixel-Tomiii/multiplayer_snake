import socket
import enum
import time

UPDATE_INTERVAL = 1/15

class Direction(enum.IntEnum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Snake():
    def __init__(self, direction, length, color, start_position, spare_parts=0):
        self.direction = direction
        self.length = length
        self.color
        self.body = body_positions
        self.parts = spare_parts

    def update(self):
        if self.has_parts():
            self.add_part()
            
        # Move the head
        if self.direction == Direction.NORTH:
            self.body[0][1] = self.body[0][1] - 1
        elif self.direction == Direction.EAST:
            self.body[0][0] = self.body[0][0] + 1
        elif self.direction == Direction.SOUTH:
            self.body[0][1] = self.body[0][1] + 1
        elif self.direction == Direction.WEST:
            self.body[0][0] = self.body[0][0] - 1

        # Update the rest of the body.
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index][0] = self.body[index-1][0]
            self.body[index][1] = self.body[index-1][1]

    def has_parts(self):
        return self.parts > 0

    def add_part(self):
        self.length += 1
        self.parts -= 1
        self.body.append([0, 0])


snakes = []

def eat_food(snake, food_value):
    snake.parts += food_value


def update_snakes(snakes):    
    for snake in enumerate(snakes):
        snake.update()


def set_direction(player, direction):
    snakes[player].direction = direction


def setup_server():
    """Creates a new UDP server, binding to an ip and port"""
    
    print(f"[{__name__}] Initialising server...")
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    comms = socket.socket(type=SOCK_DGRAM)
    comms.bind((ip, 0))
    port = comms.getsockname()[1]
    print(f"[{__name__}] Successfully initialised server on {ip}:{port}")

    host_comms.put(comms.getsockname())

    # TEMPORARY
    close_server(comms)


def create_lobby():
    print(f"[{__name__}] Creating lobby...")


def close_server(comms):
    comms.close()
    print(f"[{__name__}] Server successfully closed")


def start():
    pass
