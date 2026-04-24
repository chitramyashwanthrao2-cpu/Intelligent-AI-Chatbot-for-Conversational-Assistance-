import json
import urllib.request

# Test chat endpoint
req = urllib.request.Request(
    'http://127.0.0.1:5000/chat',
    data=json.dumps({'message': 'Hello, how are you?'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)

with urllib.request.urlopen(req, timeout=10) as response:
    result = json.loads(response.read().decode())
    print('Chat Test:')
    print('  User: Hello, how are you?')
    print('  Bot:', result.get('reply'))
    print('  Sentiment:', result.get('sentiment'))
    print('  Topic:', result.get('topic'))
    print('  Intent:', result.get('intent'))

# Test analytics
with urllib.request.urlopen('http://127.0.0.1:5000/analytics', timeout=10) as response:
    result = json.loads(response.read().decode())
    print('\nAnalytics Test:')
    print('  Total conversations:', result.get('total_conversations'))
    print('  Status: Working!')

# Test training status
with urllib.request.urlopen('http://127.0.0.1:5000/training-status', timeout=10) as response:
    result = json.loads(response.read().decode())
    print('\nTraining Status:')
    print('  Model entries:', result.get('model_entries'))
    print('  Features:', len(result.get('features', [])), 'enabled')
