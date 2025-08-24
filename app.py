#!/usr/bin/env python3
"""
Real-time Chat Application Server
Web-based chat application using Flask and SocketIO
"""

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import eventlet
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production

# Initialize SocketIO with async_mode
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

# Store connected users
connected_users = {}

@app.route('/')
def index():
    """Serve the chat interface"""
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """Handle new client connection"""
    client_id = request.sid
    logger.info(f"Client connected: {client_id}")
    emit('connection_response', {'message': 'Connected to chat server'})

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    client_id = request.sid
    username = connected_users.get(client_id, 'Unknown')
    logger.info(f"Client disconnected: {username} ({client_id})")
    
    # Remove user from connected users
    if client_id in connected_users:
        del connected_users[client_id]
    
    # Broadcast user left message
    emit('user_left', {'username': username, 'message': f'{username} left the chat'}, broadcast=True)
    emit('update_users', {'users': list(connected_users.values())}, broadcast=True)

@socketio.on('set_username')
def handle_set_username(data):
    """Set username for connected client"""
    client_id = request.sid
    username = data.get('username', 'Anonymous').strip()
    
    if not username:
        username = 'Anonymous'
    
    connected_users[client_id] = username
    logger.info(f"User set username: {username}")
    
    # Send confirmation to user
    emit('username_set', {'username': username})
    
    # Broadcast user joined message to all clients
    emit('user_joined', {'username': username, 'message': f'{username} joined the chat'}, broadcast=True)
    
    # Send updated user list to all clients
    emit('update_users', {'users': list(connected_users.values())}, broadcast=True)

@socketio.on('send_message')
def handle_send_message(data):
    """Handle incoming chat messages"""
    client_id = request.sid
    message = data.get('message', '').strip()
    username = connected_users.get(client_id, 'Anonymous')
    
    if message:
        logger.info(f"Message from {username}: {message}")
        
        # Broadcast message to all connected clients
        emit('new_message', {
            'username': username,
            'message': message,
            'timestamp': 'Now'  # You can add proper timestamp formatting
        }, broadcast=True)

@socketio.on('typing')
def handle_typing(data):
    """Handle typing indicators"""
    client_id = request.sid
    username = connected_users.get(client_id, 'Anonymous')
    is_typing = data.get('typing', False)
    
    emit('user_typing', {
        'username': username,
        'typing': is_typing
    }, broadcast=True, include_self=False)

if __name__ == '__main__':
    logger.info("Starting chat server...")
    logger.info("Server will be available at http://localhost:5000")
    logger.info("Press Ctrl+C to stop the server")
    
    # Run the application with SocketIO
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
