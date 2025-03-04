# server.py
import socket
import sqlite3
import datetime
from threading import Thread

def create_database():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS station_status (
        station_id INT,
        last_date TEXT,
        alarm1 INT,
        alarm2 INT,
        PRIMARY KEY(station_id) )''')
    conn.commit()
    conn.close()

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        print(f"Received data: {data}")
        station_id, alarm1, alarm2 = map(int, data.split())
        print(f"Parsed data - Station ID: {station_id}, Alarm1: {alarm1}, Alarm2: {alarm2}")

        conn = sqlite3.connect('data.sqlite')
        c = conn.cursor()
        last_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        c.execute('INSERT OR REPLACE INTO station_status VALUES (?, ?, ?, ?)',
                  (station_id, last_date, alarm1, alarm2))
        conn.commit()
        conn.close()
        print("Data inserted into database")
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
        print("Client connection closed")

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5003))
    server.listen(5)

    create_database()
    print("Server started, waiting for connections...")

    while True:
        try:
            client_sock, address = server.accept()
            print(f"Connection accepted from {address}")
            client_handler = Thread(target=handle_client, args=(client_sock,))
            client_handler.start()
        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == '__main__':
    run_server()
