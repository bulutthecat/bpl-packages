# Copywrite (c) 2024 Kevin Dalli

import http.client
import urllib.parse
import socket
import ssl
import ftplib

class HttpClient:
    def __init__(self, base_url):
        parsed_url = urllib.parse.urlparse(base_url)
        self.scheme = parsed_url.scheme
        self.host = parsed_url.netloc
        self.conn = None

        if self.scheme == 'https':
            self.conn = http.client.HTTPSConnection(self.host)
        else:
            self.conn = http.client.HTTPConnection(self.host)

    def get(self, path, headers=None):
        self.conn.request("GET", path, headers=headers)
        response = self.conn.getresponse()
        return response.status, response.read()

    def post(self, path, data=None, headers=None):
        if headers is None:
            headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.conn.request("POST", path, body=urllib.parse.urlencode(data), headers=headers)
        response = self.conn.getresponse()
        return response.status, response.read()

    def close(self):
        self.conn.close()


class SocketClient:
    def __init__(self, host, port, use_ssl=False):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if use_ssl:
            self.context = ssl.create_default_context()
            self.sock = self.context.wrap_socket(self.sock, server_hostname=self.host)

    def connect(self):
        self.sock.connect((self.host, self.port))

    def send(self, data):
        self.sock.sendall(data.encode())

    def receive(self, buffer_size=4096):
        return self.sock.recv(buffer_size).decode()

    def close(self):
        self.sock.close()


class FtpClient:
    def __init__(self, host, user='', passwd=''):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.ftp = ftplib.FTP(self.host)

    def login(self):
        self.ftp.login(user=self.user, passwd=self.passwd)

    def list_files(self, directory='.'):
        return self.ftp.nlst(directory)

    def upload_file(self, file_path, remote_path):
        with open(file_path, 'rb') as file:
            self.ftp.storbinary(f'STOR {remote_path}', file)

    def download_file(self, remote_path, file_path):
        with open(file_path, 'wb') as file:
            self.ftp.retrbinary(f'RETR {remote_path}', file.write)

    def close(self):
        self.ftp.quit()


# Example usage:
#if __name__ == "__main__":
#    # HTTP Client example
#    http_client = HttpClient('https://jsonplaceholder.typicode.com')
#    status, content = http_client.get('/todos/1')
#    print(f"Status: {status}, Content: {content.decode()}")
#    http_client.close()
#
#    # Socket Client example
#    socket_client = SocketClient('example.com', 80)
#    socket_client.connect()
#    socket_client.send("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
#    print(socket_client.receive())
#    socket_client.close()
#
#    # FTP Client example
#    ftp_client = FtpClient('ftp.dlptest.com')
#    ftp_client.login()
#    print("Files:", ftp_client.list_files())
#    ftp_client.upload_file('local_file.txt', 'remote_file.txt')
#    ftp_client.download_file('remote_file.txt', 'downloaded_file.txt')
#    ftp_client.close()
