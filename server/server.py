from multiprocessing import Process
from multiprocessing import Queue

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


class Server():
    def __init__(self):
        self.server_return = Queue()
        self.server_process = Process(target=self.setup_server,
                                      name="snake_server",
                                      args=(self.server_return,))
        self.running = False

    

    def run_server(self):
        """Starts the server process and returns the address to the socket"""
        self.server_process.start()
        self.running = True
        return self.server_return.get()

        

snakes = []

def eat_food(snake, food_value):
    snake.parts += food_value


def update_snakes(snakes):    
    for snake in enumerate(snakes):
        snake.update()


def set_direction(player, direction):
    snakes[player].direction = direction



def create_lobby():
    print(f"[{__name__}] Creating lobby...")


def close_server(comms):
    comms.close()
    
def start_server():
    """Creates a new UDP server, binding to an ip and port"""
    print(f"[{__name__}] Initialising server...")
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    comms = socket.socket(type=socket.SOCK_DGRAM)
    comms.bind((ip, 0))
    address = comms.getsockname()
    return address
    print(f"[{__name__}] Successfully initialised server on {ip}:{address[1]}")


def wait(server_in, server_out):
    print(f"[{__name__}] Creating server process...")
    running = True
    while running:
        print(f"[{__name__}] Awaiting input...")
        result = server_in.get()

        if result == "STOP":
            running = False

        if result == "START":
            address = start_server()
            server_out.put(address)

    # CLOSE PROCESS
    print(f"[{__name__}] Closing process...")
    
    

def start():
    pass
