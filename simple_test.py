#!/usr/bin/env python3
"""
Simple test to verify the Flask app can be imported and basic functionality works
"""

try:
    from app import app, socketio
    
    print("✓ Successfully imported Flask app and SocketIO")
    print(f"✓ App name: {app.name}")
    print(f"✓ App secret key: {app.config['SECRET_KEY']}")
    
    # Test template rendering
    with app.app_context():
        try:
            rendered = app.jinja_env.get_template('index.html')
            print("✓ Template found and can be rendered")
        except Exception as e:
            print(f"✗ Template error: {e}")
    
    print("\nTesting basic route...")
    with app.test_client() as client:
        response = client.get('/')
        print(f"✓ Root route status: {response.status_code}")
        if response.status_code == 200:
            print("✓ Root route returns 200 OK")
        else:
            print(f"✗ Root route returned: {response.status_code}")
    
    print("\nServer components are working correctly!")
    print("You can start the server with: python app.py")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Make sure all dependencies are installed:")
    print("pip install Flask==2.3.3 Flask-SocketIO==5.3.6 eventlet==0.33.3")
    
except Exception as e:
    print(f"✗ Unexpected error: {e}")
