import socket

listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
reader_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
writer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#The actual loop when the server is fully connected
def ServerLoop(address):
    print("Connection accepted from: ", address)
    try:
        while True:
            data = reader_socket.recv(4096)
            if data:
                writer_socket.sendall(data)
    except KeyboardInterrupt:
        print("Keyboard interrput received. Shutting down server.")
        return False
    except Exception:
        return True

#Startup and signal handling
def RunServer(host, port):

    reader_socket.connect(("127.0.0.1","54913")) # blocks to connect to CAENDPPServer on Local host

    print("Connected to CAEN server on loopback interface...")

    listener_socket.bind(("", "52324"))
    listener_socket.listen(1) # allow one single connection

    print("Establishing listener on :52324")

    while True:
        print("Waiting for a client...")
        writer_socket, address = listener_socket.accept() #blocks
        with writer_socket:
            if not ServerLoop(address):
                return
            elif reader_socket.fileno() == -1:
                print("Parent CAEN server closed. Shutting down server.")
                return
            else:
                print("Client connection closed.")


if __name__ == "__main__":
    RunServer()