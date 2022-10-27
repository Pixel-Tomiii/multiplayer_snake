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

def on_host(server_in, server_out):
    """Spawns a server to host a lobby
    Creates a subprocess to run the server."""
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
