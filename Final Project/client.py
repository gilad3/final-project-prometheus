# client.py
import socket
import time

WAIT_SECONDS = 60  # Global variable for testing

def read_status(filename='status.txt'):
    try:
        with open(filename, 'r') as f:
            station_id = int(f.readline().strip())
            alarm1 = int(f.readline().strip())
            alarm2 = int(f.readline().strip())
            return station_id, alarm1, alarm2
    except Exception as e:
        print(f"Error reading status file: {e}")
        return None

def send_to_server(data):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Attempting to connect to server...")
        client.connect(('127.0.0.1', 5003))
        message = f"{data[0]} {data[1]} {data[2]}"
        client.send(message.encode())
        client.close()
        print(f"Data sent to server: {message}")
    except Exception as e:
        print(f"Error sending to server: {e}")

def main():
    while True:
        print("Reading status file...")
        status = read_status()
        if status:
            print("Status read successfully:", status)
            print("Connecting to server...")
            send_to_server(status)
            print("Sent to server")
        else:
            print("Failed to read status.")
        time.sleep(WAIT_SECONDS)

if __name__ == '__main__':
    main()
