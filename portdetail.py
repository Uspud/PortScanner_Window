import socket

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((ip, port))
            return True
    except (socket.timeout, socket.error):
        return False

def get_data(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((ip, port))
            data = s.recv(4096).decode('utf-8', errors='replace')
            return data
    except (socket.timeout, socket.error):
        return None

def main():
    target_ip = input("IP: ")
    target_port = int(input("Target port: "))

    if scan_port(target_ip, target_port):
        print(f"Port {target_port} is open!")
        data = get_data(target_ip, target_port)
        if data:
            print(f"Response data: {data}")
        else:
            print("No data response")
    else:
        print(f"{target_port} is closed.")

if __name__ == "__main__":
    main()