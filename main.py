

def create_server():
    """Creates a subprocess and returns the address to the server"""
    if __name__ == "__main__":
        print(f"[{__name__}] Creating server...")
        server_comms = Queue()
        print("queue created")
        server = Process(target=setup_server,
                         name="snake_server",
                         args=(server_comms,))
        print("process created")
        server.start()
        print("process started")
        address = server_comms.get()
        print("address found")
    return address


if __name__ == "__main__":
    from multiprocessing import Process
    from multiprocessing import Queue
    from server.server import setup_server
    from application.game import on_host

    on_host()


