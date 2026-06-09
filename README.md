# 🧠 Cerebro - Desktop AI Companion

> Your intelligent AI assistant living on your desktop. Access it anywhere, anytime with a beautiful floating widget.

[![License: Boost](https://img.shields.io/badge/License-Boost%201.0-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-green.svg)](https://www.python.org/)
[![Node 16+](https://img.shields.io/badge/Node-16+-green.svg)](https://nodejs.org/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg?logo=react)](https://react.dev/)
[![Electron](https://img.shields.io/badge/Electron-25+-47848F.svg?logo=electron)](https://www.electronjs.org/)

---

## ✨ Features

### 🎯 Core Capabilities
- 💬 **AI Chat** - Conversational AI with context awareness
- 🌐 **Dual Mode** - Seamless online (cloud) and offline (local) switching
- 🖥️ **System Access** - Full laptop access for files, processes, and web
- 🎨 **Beautiful UI** - Modern gradient interface with smooth animations
- 📍 **Floating Widget** - Always-accessible draggable desktop icon

### 🚀 Advanced Features
- 🌍 **Online Mode** - OpenAI GPT-4, Claude 3, or other cloud APIs
- 📴 **Offline Mode** - Local LLMs (Llama 2, Mistral) via Ollama
- 🔄 **Auto-switching** - Intelligent detection and mode switching
- 📁 **File Management** - Browse, read, and manage your files
- ⚙️ **Process Control** - Monitor and manage running processes
- 🌐 **Web Integration** - Open websites and execute web commands
- 💾 **Chat History** - Persistent conversation tracking
- ⚡ **Real-time Status** - See connection and mode indicators

---

## 📦 Tech Stack

### Frontend
- **React 18** - UI component framework
- **Electron 25** - Cross-platform desktop application
- **Lucide React** - Icon library
- **CSS3** - Modern styling with animations

### Backend
- **Python 3.9+** - Core language
- **Flask** - Web framework with REST API
- **Ollama** - Local LLM integration
- **OpenAI/Anthropic** - Cloud AI APIs

### Architecture
```
Desktop App (Electron)
    ↓
React Frontend (Port 3000)
    ↓
Flask Backend (Port 5000)
    ↓
AI Engine (Online/Offline)
    ↓
System Access (Files, Process, Web)
```

---

## 🚀 Quick Start

### Prerequisites
- **Node.js** 16.x or higher
- **Python** 3.9 or higher
- **Git**
- **Ollama** (for offline mode) - [Download](https://ollama.ai)

### 1. Clone Repository
```bash
git clone https://github.com/Neshley/cerebro.git
cd cerebro
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys
```

### 3. Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install
```

### 4. Run Development Server

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
# Backend runs at http://localhost:5000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
# Frontend runs at http://localhost:3000
```

**Terminal 3 - Electron App (Optional):**
```bash
cd frontend
npm run electron
# Desktop app launches
```

---

## ⚙️ Configuration

### Environment Variables

Create `backend/.env`:

```env
# AI Mode: 'online' or 'offline'
AI_MODE=offline

# OpenAI Configuration (for online mode)
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4

# Claude Configuration (alternative)
CLAUDE_API_KEY=your-claude-key-here

# Ollama Configuration (for offline mode)
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama2

# Server Configuration
FLASK_ENV=development
FLASK_DEBUG=True
BACKEND_PORT=5000
```

### Offline Mode Setup

1. **Install Ollama**
   - Download from [ollama.ai](https://ollama.ai)
   - Follow installation instructions for your OS

2. **Pull a Model**
   ```bash
   ollama pull llama2
   # or
   ollama pull mistral
   ```

3. **Start Ollama**
   ```bash
   ollama serve
   ```
   - Runs at `http://localhost:11434`

### Online Mode Setup

1. **Get API Keys**
   - **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - **Claude**: [console.anthropic.com](https://console.anthropic.com/)

2. **Add to `.env`**
   ```env
   AI_MODE=online
   OPENAI_API_KEY=sk-...
   ```

---

## 📚 API Endpoints

### AI Endpoints
```
POST   /api/ai/chat              - Send message to AI
GET    /api/ai/mode              - Get current AI mode
GET    /api/ai/models            - List available models
```

### System Endpoints
```
POST   /api/system/files/list    - List directory contents
POST   /api/system/files/read    - Read file contents
GET    /api/system/processes/list - List running processes
POST   /api/system/web/open      - Open website in browser
```

### Config Endpoints
```
GET    /api/config/settings      - Get settings
POST   /api/config/settings/ai-mode - Change AI mode
```

---

## 🎨 UI Components

### ChatInterface
- Message display with real-time updates
- Input field with send button
- Loading states and animations
- Welcome screen with mode indicator

### FloatingWidget
- Draggable circular icon
- Hover and float animations
- Online indicator with pulse effect
- Always-on-top window

### StatusBar
- Connection status (Online/Offline)
- Current AI mode (Cloud/Local)
- Real-time updates

---

## 📁 Project Structure

```
cerebro/
├── backend/                    # Python Flask Backend
│   ├── app.py                 # Main application
│   ├── requirements.txt       # Dependencies
│   ├── .env.example           # Config template
│   ├── routes/                # API endpoints
│   │   ├── ai_routes.py
│   │   ├── system_routes.py
│   │   └── config_routes.py
│   ├── ai/                    # AI integration
│   │   ├── online_ai.py       # OpenAI/Claude
│   │   └── offline_ai.py      # Ollama
│   └── system/                # System access
│       ├── file_manager.py
│       ├── process_manager.py
│       └── web_access.py
│
├── frontend/                  # React + Electron
│   ├── package.json
│   ├── electron.js
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.jsx
│       ├── index.js
│       └── components/
│           ├── ChatInterface.jsx
│           ├── FloatingWidget.jsx
│           └── StatusBar.jsx
│
└── docs/                      # Documentation
    ├── SETUP.md              # Setup guide
    ├── ARCHITECTURE.md       # System design
    └── CONFIGURATION.md      # Configuration details
```

---

## 🔧 Development

### Backend Development
```bash
cd backend
source venv/bin/activate
python app.py
```

### Frontend Development
```bash
cd frontend
npm start
# Hot reloads at http://localhost:3000
```

### Building for Production

**Build Frontend:**
```bash
cd frontend
npm run build
# Creates optimized build in build/
```

**Build Electron App:**
```bash
cd frontend
npm run dist
# Creates distributable in dist/
```

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check Python version
python --version  # Should be 3.9+

# Verify virtual environment activated
which python  # Should show venv path

# Port 5000 in use?
lsof -i :5000  # Check what's using port
```

### Frontend won't start
```bash
# Clear cache
rm -rf node_modules package-lock.json
npm install

# Check Node version
node --version  # Should be 16+

# Port 3000 in use?
lsof -i :3000
```

### Ollama not connecting
```bash
# Ensure Ollama is running
ollama serve

# Test connection
curl http://localhost:11434/api/tags

# Verify OLLAMA_HOST in .env matches
```

### Chat not responding
1. Check backend is running: `curl http://localhost:5000/api/health`
2. Check frontend can reach backend
3. Verify AI mode setting
4. Check API keys in `.env` (for online mode)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Code Style
- Python: Follow PEP 8
- JavaScript: Use ESLint config
- Components: Follow React best practices

---

## 📖 Documentation

- **[Setup Guide](docs/SETUP.md)** - Detailed installation instructions
- **[Architecture](docs/ARCHITECTURE.md)** - System design and data flow
- **[Configuration](docs/CONFIGURATION.md)** - Complete config reference

---

## 🗺️ Roadmap

- [ ] Voice input/output support
- [ ] Multiple conversation management
- [ ] Plugin/extension system
- [ ] Mobile companion app
- [ ] Cloud sync of settings
- [ ] Advanced analytics dashboard
- [ ] Team collaboration features
- [ ] Custom model fine-tuning
- [ ] Keyboard shortcuts customization
- [ ] Theme system (dark/light/custom)

---

## 💡 Usage Examples

### Chat with AI
```
User: "What is the weather today?"
Cerebro: "I don't have real-time weather data, but I can help you open a weather website."
```

### System Commands
```
User: "Show me my downloads folder"
Cerebro: [Opens file manager to Downloads]

User: "Open GitHub"
Cerebro: [Opens GitHub in your browser]
```

### File Operations
```
User: "Read my config file"
Cerebro: [Reads and displays file contents]
```

---

## ⚠️ Security & Privacy

- **Local Processing**: Offline mode processes data locally
- **API Keys**: Never stored in code, only in `.env`
- **File Access**: Limited to specified directories
- **No Telemetry**: No tracking or data collection
- **Open Source**: Audit the code yourself

---

## 📝 License

This project is licensed under the **Boost Software License 1.0** - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ Free to use commercially
- ✅ Free to modify
- ✅ Free to distribute
- ✅ No warranty provided
- ℹ️ Must include license in distributions

---

## 🙏 Acknowledgments

- **React** - UI framework
- **Electron** - Desktop application
- **Flask** - Backend framework
- **Ollama** - Local AI inference
- **OpenAI** - Cloud AI
- **Anthropic Claude** - Alternative cloud AI

---

## 📞 Support

- 📧 **Issues**: [GitHub Issues](https://github.com/Neshley/cerebro/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Neshley/cerebro/discussions)
- 📖 **Documentation**: See `docs/` folder

---

## 🎯 Quick Links

- 🏠 [Repository](https://github.com/Neshley/cerebro)
- 📚 [Documentation](docs/)
- 🐛 [Report Issues](https://github.com/Neshley/cerebro/issues)
- ⭐ [Star on GitHub](https://github.com/Neshley/cerebro)

---

## 👨‍💻 Author

Created by **[Neshley](https://github.com/Neshley)**

---

<div align="center">

**Made with ❤️ by Neshley**

Star ⭐ if you find this project helpful!

</div>
