#### 3\. **Boundary Detection Module**

**Screen Edge Detection:**

-   **Cursor Monitoring:** Continuously monitor the cursor position and detect when it reaches the screen edge.
    -   **Libraries/Tools:** OS-specific APIs to track cursor position.
    -   **Example:** Implement a callback function that triggers when the cursor reaches the edge of the screen.

**Cursor Transition:**

-   **Seamless Transition:** Move the cursor to the adjacent device's screen when it reaches the boundary.
    -   **Libraries/Tools:** Send cursor position updates to the target device.
    -   **Example:** Calculate the relative position and update the cursor position on the target device.


boundary_detection/

│

├── server/

│   ├── __init__.py

│   ├── server.py            # Contains the server logic for receiving cursor position

│   ├── config.py            # Configuration settings for the server (e.g., IP, port)

│

├── client/

│   ├── __init__.py

│   ├── client.py            # Contains the client logic for sending cursor position

│   ├── monitor.py           # Contains the cursor monitoring logic and edge detection

│   ├── config.py            # Configuration settings for the client (e.g., target IP, port)

│

├── tests/

│   ├── __init__.py

│   ├── test_server.py       # Unit tests for server functionalities

│   ├── test_client.py       # Unit tests for client functionalities

│   ├── test_monitor.py      # Unit tests for cursor monitoring functionalities

│

├── utils/

│   ├── __init__.py

│   ├── logger.py            # Utility for logging events and debugging

│

├── main.py                  # Entry point script to run the client and server

├── README.md                # Documentation for the project

├── requirements.txt         # List of dependencies

└── setup.py                 # Setup script for packaging and installation