# pylint: disable=C0116,C0411,C0301,C0303
import pyautogui
import pygetwindow as gw
import time
import socket
import pyautogui


def monitor_cursor():
    screen_width, screen_height = pyautogui.size()

    while True:
        x, y = pyautogui.position()
        print(x, y)
        # Check if cursor is at the edge of the screen
        if x == 0 or y == 0 or x == screen_width - 1 or y == screen_height - 1:
            on_cursor_reach_edge(x, y)

        time.sleep(0.1)


def send_cursor_position(x, y, target_ip, target_port=9999):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, target_port))
    print("client connected")
    # Send the cursor position
    data = f"{x},{y}".encode("utf-8")
    client_socket.sendall(data)

    client_socket.close()


def on_cursor_reach_edge(pos_x, pos_y):
    print("Cursor has reached the edge of the screen!")

    # Example IP address of the adjacent device
    target_ip = "0.0.0.0"

    # Send cursor to the adjacent device's screen
    send_cursor_position(pos_x, pos_y, target_ip)


if __name__ == "__main__":
    monitor_cursor()
