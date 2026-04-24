# Quick Reference Guide

## 🚀 Start the Chatbot

### Terminal 1: Backend Server

```bash
cd c:\Users\manda\Downloads\NLP_Chatbot_Project_Final
python run_backend.py
# Server running at http://127.0.0.1:5000
```

### Terminal 2: HTTP Server

```bash
cd c:\Users\manda\Downloads\NLP_Chatbot_Project_Final
python -m http.server 8000 --bind 127.0.0.1
# Serving at http://127.0.0.1:8000
```

### Open Demo

```
Browser: http://127.0.0.1:8000/DEMO.html
```

---

## 🎯 Common Tasks

### Clear a Conversation

- Click trash icon (🗑️) in header
- Confirm deletion
- Conversation cleared

### Save Conversation

- Click save icon (💾) in header
- Automatically saves to backend and localStorage

### Download Conversation

- Click download icon (⬇️) in header
- JSON file downloads to your computer

### Create New Chat

- Click + button in sidebar
- New guest conversation created
- Switch between chats in history

### Send a Message

- Type message
- Press Enter or click send button
- Wait for response from backend

---

## 📊 Model Management

### Retrain Model (Add User Data)

```bash
# Option 1: HTTP Request
curl -X POST http://127.0.0.1:5000/retrain

# Option 2: Command Line
python train_comprehensive.py
```

### Check Model Status

```bash
curl http://127.0.0.1:5000/training-status
```

### View Training Logs

```bash
# Windows PowerShell
type training_logs.json | ConvertFrom-Json | Format-Table -AutoSize

# Or just view raw
cat training_logs.json
```

### View User Data

```bash
type user_training_data.json
```

---

## 📁 Important Files

| File                           | Purpose                 |
| ------------------------------ | ----------------------- |
| `DEMO.html`                    | Chat interface          |
| `run_backend.py`               | Start backend server    |
| `backend/app.py`               | Flask API endpoints     |
| `ai/comprehensive_training.py` | 104 training entries    |
| `train_comprehensive.py`       | Retraining orchestrator |
| `simple_retriever.json`        | The trained model       |
| `user_training_data.json`      | User-contributed Q&A    |
| `training_logs.json`           | All training events     |

---

## 🔍 Troubleshooting

### Backend Won't Start

```bash
# Check Python
python --version

# Install dependencies
python -m pip install flask flask-cors nltk textblob numpy pandas

# Try running
python run_backend.py
```

### Demo Not Loading

```bash
# Check HTTP server is running
# Port 8000 should be serving files

# Try accessing directly
# http://127.0.0.1:8000/DEMO.html
```

### Delete Button Not Working

```bash
# Open browser console (F12)
# Click delete button
# Check for JavaScript errors
# Try refreshing page
```

### Chatbot Not Responding

```bash
# Check backend is running
# Open http://127.0.0.1:5000 in browser
# Should see health check info

# Test /chat endpoint
curl -X POST http://127.0.0.1:5000/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"hello\"}"
```

---

## 📈 Growth Tracking

### Current Status

- **Base Training**: 104 entries
- **User Data**: (grows daily)
- **Total Model**: 104+ entries

### Weekly Tracking

```bash
# Check how much data we've accumulated
wc -l user_training_data.json  # Line count

# See recent entries
tail -5 user_training_data.json

# Retrain with new data
python train_comprehensive.py

# Check improvement
curl http://127.0.0.1:5000/training-status
```

---

## 💡 Tips & Tricks

### Get Better Responses

- Ask specific questions: "What is machine learning?" ✅
- Rather than: "What is it?" ❌
- Provide context for unclear queries
- Use natural language

### Speed Up Training

- Have more conversations
- Ask diverse questions
- Use different topics daily
- Retrain weekly

### Monitor Quality

- Check `training_logs.json` for patterns
- Look for common unclear queries
- Add custom training data if needed
- Test bot regularly

---

## 🎓 Sample Queries to Try

```
"What can you do?"
"How are you?"
"Tell me about machine learning"
"What is python?"
"How do I improve my memory?"
"Tell me something interesting"
"Can you help me with coding?"
"What is artificial intelligence?"
"How should I study effectively?"
"What makes a good leader?"
```

---

## 🔄 Daily Workflow

### Morning

1. Start backend: `python run_backend.py`
2. Start HTTP server: `python -m http.server 8000`
3. Open demo: `http://127.0.0.1:8000/DEMO.html`
4. Chat and collect data

### Evening (Optional)

```bash
# Retrain model with new data
python train_comprehensive.py

# Check status
curl http://127.0.0.1:5000/training-status
```

### Weekly

1. Review `training_logs.json`
2. Check `user_training_data.json` growth
3. Run comprehensive retrain
4. Monitor improvements

---

## 📞 Support

### Logs to Check

- `training_logs.json` - Training events
- `user_training_data.json` - User contributions
- Backend console - Server errors
- Browser console (F12) - Frontend errors

### Model Files

- `ai/simple_retriever.json` - Current model
- `ai/comprehensive_training.py` - Base data
- `train_comprehensive.py` - Training script

### API Health Check

```bash
curl http://127.0.0.1:5000/
# Shows all available endpoints and features
```

---

## ✅ Everything is Ready!

Your chatbot is fully operational with:

- ✅ 104 training entries
- ✅ Daily user learning
- ✅ Fixed delete button
- ✅ Multi-guest support
- ✅ Persistent storage
- ✅ Model monitoring

**Happy chatting! 🎉**
