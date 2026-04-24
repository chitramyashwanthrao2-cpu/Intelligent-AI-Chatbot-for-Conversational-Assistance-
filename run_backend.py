import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.app import app

if __name__ == '__main__':
    print("Starting AI Chatbot Backend Server...")
    print("Server running at http://127.0.0.1:5000")
    print("Press Ctrl+C to stop")
    app.run(debug=False, host='127.0.0.1', port=5000)
