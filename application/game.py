import socket
from socket import SOCK_DGRAM
from multiprocessing import Process
from multiprocessing import Queue
from server.server import wait

menu_items = [
    "play",
    "options",
    "exit"]

play_menu = [
    "host",
    "join"]

def on_play():
    pass

def start():
    on_host()
    pass

def game_loop():
    while True:
        ui = input()

        if ui == "host":
            on_host()
    

def on_host():
    """Spawns a server to host a lobby
    Creates a subprocess to run the server."""
    server_in = Queue()
    server_out = Queue()
    server_proc = Process(target=wait,
                          name="snake_server",
                          args=(server_in, server_out))
    server_proc.start()
    print("Starting server")
    server_in.put("START")
    print("Started")
    address = server_out.get()

    sock = socket.socket(type=socket.SOCK_DGRAM).connect(address)
    print(address)
    
def load_options():
    pass

def save_options():
    pass

def exit():
    pygame.exit()
    os._exit()

