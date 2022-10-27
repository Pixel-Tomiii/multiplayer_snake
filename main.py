

if __name__ == "__main__":
    from multiprocessing import Process
    from multiprocessing import Queue
    from server.server import wait
    from application.game import on_host

    server_in = Queue()
    server_out = Queue()
    server_proc = Process(target=wait,
                          name="snake_server",
                          args=(server_in, server_out))
    server_proc.start()
    print("Started process")

    
    on_host(server_in, server_out)


