# Real-time Web Chat Application

A real-time chat application built with Flask and SocketIO featuring a modern web interface with particles.js background.

## Features

- Real-time messaging using WebSockets
- Multiple user support
- Username system
- Online users list
- Typing indicators
- Beautiful particles.js background
- Responsive design

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and go to `http://localhost:5000`

## Usage

1. When you first connect, you'll be prompted to enter a username
2. Start typing messages in the input field
3. Press Enter or click Send to send messages
4. See other users' messages in real-time
5. View the list of online users in the sidebar

## Technical Details

- **Backend**: Flask with Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript with SocketIO client
- **Real-time Communication**: WebSockets via SocketIO
- **Background Effects**: particles.js

## File Structure

```
.
├── app.py              # Flask server with SocketIO
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # Chat interface
```

## Dependencies

- Flask: Web framework
- Flask-SocketIO: WebSocket integration
- eventlet: Async server for SocketIO
- python-socketio: SocketIO client library

## Browser Support

Works in all modern browsers that support WebSockets and ES6+ JavaScript.

## Notes

- The server runs on port 5000 by default
- All users connect to the same chat room
- Messages are broadcast to all connected users
- No message history is persisted (messages are lost when server restarts)
