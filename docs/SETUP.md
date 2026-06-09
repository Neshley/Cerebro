# 🚀 Cerebro Setup Guide

Complete step-by-step installation and configuration guide for Cerebro.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [Offline Mode Setup](#offline-mode-setup)
6. [Online Mode Setup](#online-mode-setup)
7. [Troubleshooting](#troubleshooting)
8. [First Run](#first-run)

---

## Prerequisites

Before you begin, make sure you have:

### Required
- **Git** - [Download](https://git-scm.com/)
- **Node.js** 16.x or higher - [Download](https://nodejs.org/)
- **Python** 3.9 or higher - [Download](https://www.python.org/)
- **Ollama** (for offline mode) - [Download](https://ollama.ai)

### Optional
- **Visual Studio Code** - [Download](https://code.visualstudio.com/)
- **Postman** - For API testing
- **Git GUI** - For easier git management

### System Requirements
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 2GB free space
- **Internet**: For online mode and initial setup

---

## Installation

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/Neshley/cerebro.git

# Navigate to project directory
cd cerebro
```

### Step 2: Backend Setup

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

**Verify installation:**
```bash
pip list
# Should show: Flask, Flask-CORS, python-dotenv, requests, etc.
```

### Step 3: Frontend Setup

```bash
# Navigate to frontend folder
cd ../frontend

# Install Node dependencies
npm install

# Verify installation
npm list react
# Should show React version 18.2.0+
```

---

## Configuration

### Step 1: Environment Setup

```bash
# In backend folder
cd backend

# Copy environment template
cp .env.example .env

# Edit .env file with your settings
# Use your favorite editor (VS Code, nano, etc.)
nano .env
```

### Step 2: Configure AI Mode

Edit `backend/.env`:

```env
# Choose: 'online' or 'offline'
AI_MODE=offline
```

### Step 3: Add API Keys (If Using Online Mode)

For **OpenAI**:
```env
OPENAI_API_KEY=sk-your-actual-key-here
OPENAI_MODEL=gpt-4
```

Get key: https://platform.openai.com/api-keys

For **Claude (Anthropic)**:
```env
CLAUDE_API_KEY=sk-ant-your-actual-key-here
```

Get key: https://console.anthropic.com/

### Step 4: Server Configuration

```env
# Backend server settings
FLASK_ENV=development
FLASK_DEBUG=True
BACKEND_PORT=5000

# Ollama settings (for offline mode)
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama2
```

---

## Running the Application

### Option 1: Development Mode (Recommended for First Run)

You'll need **3 terminal windows**:

**Terminal 1 - Backend API:**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python app.py
```
✅ Backend running at `http://localhost:5000`

**Terminal 2 - Frontend Dev Server:**
```bash
cd frontend
npm start
```
✅ Frontend running at `http://localhost:3000`
✅ Automatically opens in your browser

**Terminal 3 - Electron App (Optional):**
```bash
cd frontend
npm run electron
```
✅ Desktop app launches

### Option 2: Web-Only (No Electron)

Use only Terminal 1 and 2 above. Access at `http://localhost:3000`

### Option 3: Production Build

```bash
cd frontend

# Build optimized version
npm run build

# Create distributable
npm run dist
```

---

## Offline Mode Setup

### Step 1: Install Ollama

Download and install from: https://ollama.ai

**macOS:**
```bash
# Download and run the installer
# Or use homebrew:
brew install ollama
```

**Windows:**
- Download installer from ollama.ai
- Run the .exe file
- Follow installation wizard

**Linux:**
```bash
curl https://ollama.ai/install.sh | sh
```

### Step 2: Start Ollama Service

```bash
# Start Ollama
ollama serve
```

You should see:
```
Listening on 127.0.0.1:11434
```

### Step 3: Pull a Language Model

In a **new terminal**:

```bash
# Pull Llama 2 (recommended)
ollama pull llama2

# Or try Mistral (smaller, faster)
ollama pull mistral

# Or Neural Chat
ollama pull neural-chat
```

This downloads the model (1-7GB depending on model).

### Step 4: Verify Setup

```bash
# Check available models
ollama list

# Test the API
curl http://localhost:11434/api/tags
```

### Step 5: Configure Cerebro for Offline

Edit `backend/.env`:
```env
AI_MODE=offline
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama2
```

**Restart backend** for changes to take effect.

---

## Online Mode Setup

### Step 1: Choose Your AI Provider

**Option A: OpenAI (Recommended)**
- Models: GPT-4, GPT-3.5 Turbo
- More capabilities
- Costs per token

**Option B: Anthropic Claude**
- Models: Claude 3 Sonnet, Opus
- Excellent for long-form content
- Different pricing model

### Step 2: Get API Key

**For OpenAI:**
1. Go to https://platform.openai.com/api-keys
2. Login or create account
3. Click "Create new secret key"
4. Copy the key (save it safely!)
5. Add to `backend/.env`:
```env
OPENAI_API_KEY=sk-proj-your-key-here
```

**For Claude:**
1. Go to https://console.anthropic.com/
2. Login or create account
3. Go to API keys
4. Create new key
5. Add to `backend/.env`:
```env
CLAUDE_API_KEY=sk-ant-your-key-here
```

### Step 3: Configure Cerebro for Online

Edit `backend/.env`:
```env
AI_MODE=online
OPENAI_API_KEY=sk-your-key-here
# or
CLAUDE_API_KEY=sk-ant-your-key-here
```

### Step 4: Test Connection

```bash
# In backend folder, with virtual env activated
python -c "import openai; print('OpenAI imported successfully')"
```

**Restart backend** for changes to take effect.

---

## Troubleshooting

### Backend Issues

**Port 5000 already in use:**
```bash
# Find what's using port 5000
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Change port in .env
BACKEND_PORT=5001
```

**Virtual environment not activating:**
```bash
# Try deleting and recreating
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Python modules not installing:**
```bash
# Upgrade pip first
pip install --upgrade pip
pip install -r requirements.txt
```

### Frontend Issues

**Port 3000 already in use:**
```bash
# Kill process using port 3000
lsof -i :3000  # macOS/Linux
# Then restart npm start
```

**Node modules corrupted:**
```bash
# Clear and reinstall
rm -rf node_modules package-lock.json
npm install
npm start
```

**Electron won't launch:**
- Ensure backend is running (Terminal 1)
- Ensure frontend dev server is running (Terminal 2)
- Check firewall isn't blocking connections

### Ollama Issues

**Ollama not starting:**
```bash
# Check if already running
ps aux | grep ollama

# Try restarting
killall ollama
ollama serve
```

**Model not found:**
```bash
# List downloaded models
ollama list

# Pull a model
ollama pull llama2

# Verify it downloaded
ollama list
```

**Connection timeout:**
```bash
# Check OLLAMA_HOST in .env
# Default: http://localhost:11434

# Test connection
curl -X POST http://localhost:11434/api/generate -d '{"model":"llama2","prompt":"test"}'
```

### API Key Issues

**"Invalid API key" error:**
- Check key is copied correctly
- Ensure no extra spaces
- Check key hasn't been revoked
- Try creating a new key

**"Rate limit exceeded":**
- Wait a few minutes
- Check your API usage at provider's dashboard
- Upgrade plan if needed

---

## First Run

### 1. All Services Running?

Check all three terminals:
- ✅ Backend: `http://localhost:5000/api/health` returns `{"status": "healthy"}`
- ✅ Frontend: `http://localhost:3000` loads the app
- ✅ Ollama (if offline): `ollama serve` running

### 2. Test the Chat

1. Go to `http://localhost:3000`
2. Type a simple message: "Hello"
3. You should get a response

### 3. Check Status Bar

Top-right shows:
- 🌐 Online or 📴 Offline (internet status)
- ☁️ Cloud or 🖥️ Local (AI mode)

### 4. Try File Access

Type: "List my home directory"

Should show your home folder contents.

### 5. Try Web Access

Type: "Open GitHub"

Should open GitHub in your browser.

---

## Common Commands Reference

```bash
# Backend
cd backend
source venv/bin/activate          # Activate venv
python app.py                     # Start backend
deactivate                        # Exit venv

# Frontend
cd frontend
npm start                         # Dev server
npm run build                     # Production build
npm run electron                  # Desktop app
npm run dist                      # Create installer

# Ollama
ollama serve                      # Start Ollama
ollama pull llama2               # Download model
ollama list                      # List models
```

---

## Next Steps

✅ **Setup complete!** Now:

1. 📖 Read the [Architecture](ARCHITECTURE.md) to understand how it works
2. 🎨 Customize the UI in `frontend/src/components/`
3. 🤖 Modify AI behavior in `backend/ai/`
4. 📁 Add system access features in `backend/system/`
5. 🚀 Build and deploy your app

---

## Getting Help

- 📚 Check [README](../README.md) for overview
- 🏗️ Check [ARCHITECTURE](ARCHITECTURE.md) for system design
- 🐛 Open an [Issue on GitHub](https://github.com/Neshley/cerebro/issues)
- 💬 Join [GitHub Discussions](https://github.com/Neshley/cerebro/discussions)

---

**Happy coding! 🚀**
