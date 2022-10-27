from multiprocessing import Process
import socket
from socket import SOCK_DGRAM

menu_items = [
    "play",
    "options",
    "exit"]

play_menu = [
    "host",
    "join"]

def on_play():
    pass

def on_host():
    """Spawns a server to host a lobby"""
    from __main__ import create_server
    address = create_server()

    # Connect to created server.
    server = socket.socket(type=SOCK_DGRAM).connect(address)
    print(f"[{__name__}] Host successfully connected to server")
    
        
def load_options():
    pass

def save_options():
    pass

def exit():
    pygame.exit()
    os._exit()
