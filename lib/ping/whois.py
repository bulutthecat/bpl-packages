import socket

def whois_query(domain, server='whois.verisign-grs.com', port=43):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))
        s.sendall((domain + '\r\n').encode())

        response = b''
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data

    return response.decode()

# Example usage
domain = "example.com"
result = whois_query(domain)
print(result)
