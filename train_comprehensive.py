"""
Enhanced training script with comprehensive data and daily update capability
This trains the retriever with extensive domain knowledge
"""

import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai.simple_retriever import train_retriever
from ai.comprehensive_training import get_all_training_data

# Path for user-contributed data
USER_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'user_training_data.json')
DAILY_LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'training_logs.json')
RETRIEVER_PATH = os.path.join(os.path.dirname(__file__), 'simple_retriever.json')

def load_user_data():
    """Load user-contributed training data"""
    if os.path.exists(USER_DATA_PATH):
        try:
            with open(USER_DATA_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading user data: {e}")
    return []

def save_user_data(data):
    """Save user-contributed training data"""
    try:
        with open(USER_DATA_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving user data: {e}")

def add_user_entry(user_message, bot_response):
    """Add a new user-bot conversation pair to training data"""
    user_data = load_user_data()
    
    # Format as "question|answer"
    entry = f"{user_message.strip()}|{bot_response.strip()}"
    
    # Avoid duplicates
    if entry not in user_data:
        user_data.append(entry)
        save_user_data(user_data)
        return True
    return False

def log_training_event(event_type, details):
    """Log training events for analytics"""
    logs = []
    if os.path.exists(DAILY_LOG_PATH):
        try:
            with open(DAILY_LOG_PATH, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        except:
            logs = []
    
    logs.append({
        'timestamp': datetime.now().isoformat(),
        'type': event_type,
        'details': details
    })
    
    try:
        with open(DAILY_LOG_PATH, 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error logging event: {e}")

def train_comprehensive_model():
    """Train the retriever with all available data"""
    
    print("=" * 60)
    print("COMPREHENSIVE CHATBOT MODEL TRAINING")
    print("=" * 60)
    
    # Get all training data
    base_data = get_all_training_data()
    print(f"\n✓ Loaded {len(base_data)} base training entries from multiple domains")
    
    # Load user-contributed data
    user_data = load_user_data()
    print(f"✓ Loaded {len(user_data)} user-contributed entries")
    
    # Combine all data
    all_data = base_data + user_data
    total_entries = len(all_data)
    
    print(f"✓ Total entries to train: {total_entries}")
    
    # Remove duplicates while preserving order
    seen = set()
    unique_data = []
    for entry in all_data:
        if entry not in seen:
            seen.add(entry)
            unique_data.append(entry)
    
    print(f"✓ After removing duplicates: {len(unique_data)} unique entries")
    
    # Train the retriever
    print("\n[Training Model...]")
    model = train_retriever(unique_data, RETRIEVER_PATH)
    
    print(f"\n{'=' * 60}")
    print(f"MODEL TRAINING COMPLETE!")
    print(f"{'=' * 60}")
    print(f"\nModel Statistics:")
    print(f"  - Total entries: {model['num_entries']}")
    print(f"  - Model saved to: {RETRIEVER_PATH}")
    print(f"  - Training timestamp: {datetime.now().isoformat()}")
    
    # Log the training event
    log_training_event('training_complete', {
        'total_entries': model['num_entries'],
        'base_entries': len(base_data),
        'user_entries': len(user_data),
        'model_path': RETRIEVER_PATH
    })
    
    print(f"\nTraining Coverage:")
    print(f"  ✓ Greetings & Introductions")
    print(f"  ✓ About the Chatbot")
    print(f"  ✓ Technology & Programming")
    print(f"  ✓ Science & Nature")
    print(f"  ✓ Health & Wellness")
    print(f"  ✓ Business & Career")
    print(f"  ✓ Education & Learning")
    print(f"  ✓ Arts & Creativity")
    print(f"  ✓ Travel & Culture")
    print(f"  ✓ Food & Cooking")
    print(f"  ✓ Sports & Fitness")
    print(f"  ✓ Emotions & Relationships")
    print(f"  ✓ Environment & Sustainability")
    print(f"  ✓ Finance & Money")
    print(f"  ✓ Problem Solving")
    print(f"  ✓ Small Talk")
    print(f"  ✓ And more...")
    print(f"\nDaily user contributions will be automatically added and trained.")
    
    return model

if __name__ == "__main__":
    train_comprehensive_model()
