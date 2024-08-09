import socket
import pyautogui


def receive_cursor_position():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 9999))
    server_socket.listen(1)

    while True:
        client_socket, _ = server_socket.accept()
        data = client_socket.recv(1024)
        # if not data:
        #     break

        # # Decode the received data
        x, y = map(int, data.decode("utf-8").split(","))
        print('data: ', x, y)

        # # Move cursor to the new position
        # pyautogui.moveTo(x, y)

        # client_socket.close()


if __name__ == "__main__":
    receive_cursor_position()
