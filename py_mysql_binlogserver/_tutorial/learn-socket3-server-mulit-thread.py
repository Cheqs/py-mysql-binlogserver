import threading
import socketserver


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        """
        计算器，返回表达式的值
        """
        while True:
            try:
                data = str(self.request.recv(1024), 'ascii').strip()
                if "q" in data:
                    self.finish()
                    break
                response = bytes("{} = {}\r\n".format(data, eval(data)), 'ascii')
                print(response.decode("ascii").strip())
                self.request.sendall(response)
            except:
                self.request.sendall(bytes("\n", 'ascii'))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":

    server = ThreadedTCPServer(("127.0.0.1", 9000), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    print(f"Calculator Server start at {ip} : {port}")
    server_thread.start()

