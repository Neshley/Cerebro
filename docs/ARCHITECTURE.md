# Cerebro Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    CEREBRO DESKTOP AI                        │
└─────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER                         │
│  ┌──────────────────┐      ┌──────────────────┐            │
│  │  Main Window     │      │ Floating Widget  │            │
│  │  (Chat UI)       │      │ (Icon + Dragging)│            │
│  └─────────┬────────┘      └────────┬─────────┘            │
│            │                        │                       │
│            │    Electron IPC        │                       │
└────────────┼────────────────────────┼──────────────────────┘
             │                        │
┌────────────▼────────────────────────▼──────────────────────┐
│              FRONTEND LAYER (React)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Chat Interface │ Status Bar │ Widget Controller    │  │
│  └────────────────────────┬─────────────────────────────┘  │
│                            │                                │
│                      Axios HTTP                             │
└────────────────────────────┼────────────────────────────────┘
                             │
            ┌────────────────▼─────────────────┐
            │     Backend API (Flask)          │
            │  :5000 /api/*                    │
            └────────────────┬──────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
   ┌────▼──────┐        ┌───▼────┐        ┌─────▼────┐
   │ AI Engine │        │ System │        │ Config   │
   │ Routes    │        │ Routes │        │ Routes   │
   └────┬──────┘        └───┬────┘        └──────────┘
        │                   │
   ┌────▼──────────────┬────▼────────────────┐
   │                   │                     │
┌──▼────────┐   ┌─────▼──────┐   ┌─────────▼──────┐
│ Online AI │   │ Offline AI │   │ System Access  │
│ (APIs)    │   │ (Ollama)   │   │ (File/Process) │
└───────────┘   └────────────┘   └────────────────┘
   │                │                    │
   │                │                    │
┌──▼───────┐   ┌────▼────────┐   ┌─────▼──────────┐
│ OpenAI   │   │ Local LLM    │   │ OS / Browser   │
│ Claude   │   │ Models       │   │ Services       │
└──────────┘   └─────────────┘   └────────────────┘
```

## Directory Structure

```
cerebro/
├── backend/                    # Python Flask Backend
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt       # Python dependencies
│   ├── .env.example           # Environment template
│   │
│   ├── routes/                # API Route Handlers
│   │   ├── ai_routes.py       # Chat & AI endpoints
│   │   ├── system_routes.py   # File/process endpoints
│   │   └── config_routes.py   # Configuration endpoints
│   │
│   ├── ai/                    # AI Integration Layer
│   │   ├── online_ai.py       # OpenAI/Claude integration
│   │   └── offline_ai.py      # Ollama integration
│   │
│   └── system/                # System Access Layer
│       ├── file_manager.py    # File operations
│       ├── process_manager.py # Process control
│       └── web_access.py      # Browser & web operations
│
├── frontend/                   # React + Electron Frontend
│   ├── package.json           # Node dependencies
│   ├── electron.js            # Electron main process
│   ├── public/
│   │   └── index.html         # HTML entry point
│   │
│   └── src/
│       ├── index.js           # React entry
│       ├── App.jsx            # Main app component
│       ├── App.css            # App styling
│       │
│       └── components/
│           ├── ChatInterface.jsx      # Chat UI
│           ├── ChatInterface.css      # Chat styling
│           ├── FloatingWidget.jsx     # Floating icon
│           ├── FloatingWidget.css     # Widget styling
│           ├── StatusBar.jsx          # Status display
│           └── StatusBar.css          # Status styling
│
└── docs/                       # Documentation
    ├── SETUP.md              # Setup guide
    ├── ARCHITECTURE.md       # This file
    ├── AI_MODES.md           # AI configuration
    ├── SYSTEM_ACCESS.md      # System integration
    └── CONFIGURATION.md      # Configuration guide
```

## Data Flow

### Chat Message Flow
1. User types message in Chat UI
2. React component sends POST to `/api/ai/chat`
3. Backend AI router receives message
4. Routes to Online AI (OpenAI/Claude) or Offline AI (Ollama) based on mode
5. AI processes and returns response
6. Response sent back to frontend
7. React displays message in chat

### System Command Flow
1. AI recognizes system command in conversation
2. Routes to `/api/system/*` endpoint
3. System manager (File/Process/Web) executes command
4. Returns result to AI
5. AI formats response to user
6. User sees result in chat

## Communication Protocols

### Frontend ↔ Backend
- **Protocol**: HTTP/REST
- **Port**: 5000
- **Format**: JSON
- **CORS**: Enabled for Electron

### Backend ↔ External APIs
- **OpenAI**: HTTPS REST with API key
- **Claude**: HTTPS REST with API key
- **Ollama**: HTTP REST on localhost:11434

### Electron ↔ Frontend
- **Protocol**: IPC (Inter-Process Communication)
- **Used for**: Window control, system tray integration

## Key Components

### Flask Backend
- Lightweight web framework
- Handles API routing and business logic
- Manages AI model selection and fallback

### React Frontend
- Component-based UI architecture
- State management for chat history and mode
- Real-time status updates

### Electron
- Cross-platform desktop app wrapper
- Manages floating widget window
- System integration (tray, keyboard shortcuts)

### AI Layer
- Abstraction for different AI providers
- Automatic fallback (online → offline)
- Connection detection and mode switching

## Security Considerations

1. **API Keys**: Store in .env, never in code
2. **File Access**: Restrict to user directories
3. **Process Management**: Whitelist allowed operations
4. **Local API**: Only listens on localhost
5. **CORS**: Only allows Electron requests

## Performance Optimizations

1. **Lazy Loading**: UI components loaded on demand
2. **Message Caching**: Recent messages kept in memory
3. **Connection Pooling**: Reuse HTTP connections
4. **Background Processing**: Long operations don't block UI
5. **Local-first**: Offline mode for reduced latency

## Extensibility

### Adding New AI Provider
1. Create new class in `backend/ai/`
2. Implement `chat()` method
3. Register in AI router

### Adding System Commands
1. Create handler in `backend/system/`
2. Add route in `system_routes.py`
3. Trigger from AI response

### Customizing UI
1. Modify components in `frontend/src/components/`
2. Update CSS files
3. Add new components as needed

## Future Enhancements

- [ ] Voice input/output
- [ ] Multiple conversation management
- [ ] Plugin system
- [ ] Mobile companion app
- [ ] Cloud sync of settings
- [ ] Advanced analytics
- [ ] Team collaboration features
