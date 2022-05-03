import socket

listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
reader_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def RunServer(host, port):

    reader_socket.setblocking(False)
    reader_socket.connect(("127.0.0.1","54913")) # blocks to connect to CAENDPPServer on Local host

    print("Connected to CAEN server on loopback interface...")

    listener_socket.bind(("", "69420"))
    listener_socket.listen(1) # allow one single connection

    print("Establishing listener on :69420")

    writer_socket, address = listener_socket.accept() #blocks
    with writer_socket:
        print("Connection accpeted from ", address)
        try:
            while True:
                data = reader_socket.recv(4096) #does not block
                if data:
                    writer_socket.sendall(data) #blocks for all data transferred
        except Exception as e:
            print("Exception thrown: ", e)


if __name__ == "__main__":
    RunServer()