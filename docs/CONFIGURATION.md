# 🏗️ Cerebro Configuration Guide

Complete configuration reference for Cerebro environment variables and settings.

## 📋 Table of Contents

1. [Environment Variables](#environment-variables)
2. [AI Configuration](#ai-configuration)
3. [Server Configuration](#server-configuration)
4. [System Access Configuration](#system-access-configuration)
5. [Development vs Production](#development-vs-production)
6. [Configuration Examples](#configuration-examples)
7. [Troubleshooting Configuration](#troubleshooting-configuration)

---

## Environment Variables

### Location
```
cerebro/backend/.env
```

### Creating the File

```bash
# Copy from template
cp .env.example .env

# Edit the file
nano .env
# or
code .env
# or
vim .env
```

---

## AI Configuration

### AI_MODE

**Options:** `online` | `offline`

```env
# Use local AI (Ollama)
AI_MODE=offline

# Use cloud API (OpenAI/Claude)
AI_MODE=online
```

**Default:** `offline`

**What it does:**
- `offline`: Uses local LLM via Ollama (no internet needed)
- `online`: Uses OpenAI or Claude APIs (requires internet)

---

### OpenAI Configuration

```env
OPENAI_API_KEY=sk-your-actual-key-here
OPENAI_MODEL=gpt-4
```

#### OPENAI_API_KEY
**Required for:** Online mode with OpenAI
**How to get:**
1. Go to https://platform.openai.com/api-keys
2. Create or copy your API key
3. Paste in .env

**Format:** Starts with `sk-`

**Example:**
```env
OPENAI_API_KEY=sk-proj-abc123xyz789...
```

#### OPENAI_MODEL
**Options:**
- `gpt-4` (Most advanced, slower, more expensive)
- `gpt-3.5-turbo` (Fast, affordable, good quality)
- `gpt-4-turbo-preview` (Balance of speed and quality)

**Default:** `gpt-3.5-turbo`

**Example:**
```env
OPENAI_MODEL=gpt-4
```

---

### Claude Configuration

```env
CLAUDE_API_KEY=sk-ant-your-actual-key-here
```

#### CLAUDE_API_KEY
**Required for:** Online mode with Claude
**How to get:**
1. Go to https://console.anthropic.com/
2. Create or copy your API key
3. Paste in .env

**Format:** Starts with `sk-ant-`

**Example:**
```env
CLAUDE_API_KEY=sk-ant-abc123xyz789...
```

---

### Ollama Configuration

```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama2
```

#### OLLAMA_HOST
**Default:** `http://localhost:11434`

**Format:** `http://hostname:port`

**Examples:**
```env
# Local machine (default)
OLLAMA_HOST=http://localhost:11434

# Remote machine
OLLAMA_HOST=http://192.168.1.100:11434

# Custom port
OLLAMA_HOST=http://localhost:8000
```

#### OLLAMA_MODEL
**Options:**
- `llama2` (Default, good all-around)
- `mistral` (Smaller, faster)
- `neural-chat` (Optimized for chat)
- `orca-mini` (Very small, fast)

**Default:** `llama2`

**Example:**
```env
OLLAMA_MODEL=mistral
```

**To install models:**
```bash
ollama pull llama2
ollama pull mistral
ollama pull neural-chat
ollama list  # See all installed
```

---

## Server Configuration

### FLASK_ENV

**Options:** `development` | `production`

```env
FLASK_ENV=development
```

**Default:** `development`

**What it does:**
- `development`: Shows errors, debug mode enabled
- `production`: Hides errors, optimized, no debug

### FLASK_DEBUG

**Options:** `True` | `False`

```env
FLASK_DEBUG=True
```

**Default:** `True`

**What it does:**
- `True`: Auto-reload on code changes, detailed errors
- `False`: Requires manual restart for changes

### BACKEND_PORT

**Default:** `5000`

```env
BACKEND_PORT=5000
```

**When to change:**
- Port already in use
- Running multiple instances
- Restricted ports on your system

**Example - Custom port:**
```env
BACKEND_PORT=5001
```

**Check if port is available:**
```bash
# macOS/Linux
lsof -i :5000

# Windows
netstat -ano | findstr :5000
```

---

## System Access Configuration

Currently no special configuration needed, but you can extend:

```env
# Future: Restrict file access to specific directories
ALLOWED_FILE_PATHS=/home,/documents,/downloads

# Future: Whitelist processes
ALLOWED_PROCESSES=chrome,vscode,node

# Future: API rate limiting
RATE_LIMIT=100  # requests per minute
```

---

## Development vs Production

### Development Configuration

```env
# Development .env
AI_MODE=offline
FLASK_ENV=development
FLASK_DEBUG=True
BACKEND_PORT=5000
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama2
```

**Use when:**
- Building and testing locally
- Experimenting with code
- Debugging issues

### Production Configuration

```env
# Production .env
AI_MODE=online
FLASK_ENV=production
FLASK_DEBUG=False
BACKEND_PORT=5000
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-3.5-turbo
```

**Use when:**
- Deploying to users
- Running in background
- Sharing the app

---

## Configuration Examples

### Example 1: Local Development (Offline)

```env
# .env
AI_MODE=offline
FLASK_ENV=development
FLASK_DEBUG=True
BACKEND_PORT=5000
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama2
```

### Example 2: Cloud-Based (Online with OpenAI)

```env
# .env
AI_MODE=online
FLASK_ENV=production
FLASK_DEBUG=False
OPENAI_API_KEY=sk-proj-your-key-here
OPENAI_MODEL=gpt-3.5-turbo
```

### Example 3: Cloud-Based (Online with Claude)

```env
# .env
AI_MODE=online
FLASK_ENV=production
FLASK_DEBUG=False
CLAUDE_API_KEY=sk-ant-your-key-here
```

### Example 4: Remote Ollama Server

```env
# .env
AI_MODE=offline
FLASK_ENV=development
OLLAMA_HOST=http://192.168.1.100:11434
OLLAMA_MODEL=mistral
```

### Example 5: Testing with Multiple Ports

```env
# Running multiple instances
BACKEND_PORT=5001
FLASK_ENV=development
AI_MODE=offline
```

---

## Changing Configuration

### Method 1: Edit .env File

```bash
nano backend/.env
# Edit and save
```

**Then restart backend:**
```bash
# Stop current backend (Ctrl+C)
# In backend folder:
python app.py
```

### Method 2: Environment Variables

On Linux/macOS:
```bash
export AI_MODE=online
export OPENAI_API_KEY=sk-...
python app.py
```

On Windows:
```cmd
set AI_MODE=online
set OPENAI_API_KEY=sk-...
python app.py
```

### Method 3: .env.local (Override)

Create `backend/.env.local` for personal overrides:
```env
OPENAI_API_KEY=your-personal-key
```

---

## Verifying Configuration

### Check Backend Configuration

```bash
cd backend
curl http://localhost:5000/api/config/settings
```

Response:
```json
{
  "ai_mode": "offline",
  "backend_port": 5000,
  "ollama_host": "http://localhost:11434"
}
```

### Check AI Mode

```bash
curl http://localhost:5000/api/ai/mode
```

Response:
```json
{
  "mode": "offline"
}
```

### Check Health

```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "status": "healthy",
  "service": "Cerebro Backend",
  "version": "1.0.0"
}
```

---

## Troubleshooting Configuration

### Issue: "AI mode not changing"

**Solution:** Restart backend
```bash
# Stop backend (Ctrl+C)
python app.py
```

### Issue: "Invalid API key"

**Check:**
1. Key is copied correctly (no spaces)
2. Key hasn't been revoked
3. Correct provider (OpenAI vs Claude)

**For OpenAI:**
```bash
# Verify key is valid
curl -H "Authorization: Bearer sk-..." https://api.openai.com/v1/models
```

### Issue: "Cannot connect to Ollama"

**Check:**
1. Ollama is running: `ollama serve`
2. OLLAMA_HOST matches: `http://localhost:11434`
3. Port is correct: `lsof -i :11434`

### Issue: "FLASK_DEBUG not working"

**Make sure .env has:**
```env
FLASK_ENV=development
FLASK_DEBUG=True
```

**And restart:** `python app.py`

### Issue: "Port already in use"

**Change port in .env:**
```env
BACKEND_PORT=5001
```

**Restart backend**

---

## Security Best Practices

### 🔐 API Keys
- ✅ Store in `.env` (NEVER in code)
- ✅ Add `.env` to `.gitignore`
- ✅ Never commit API keys
- ❌ Don't share .env file
- ❌ Don't paste keys in chat/issues

### 🔐 Production Deployment
```env
# Never use these in production:
FLASK_DEBUG=False      # Always False
FLASK_ENV=production   # Always production
```

### 🔐 Port Security
- Use firewall to restrict access
- Don't expose port 5000 publicly
- Use reverse proxy (nginx, Apache) for production

---

## Configuration Reference Table

| Variable | Options | Default | Required |
|----------|---------|---------|----------|
| AI_MODE | online, offline | offline | ✅ |
| OPENAI_API_KEY | sk-... | - | ⚠️ if online |
| OPENAI_MODEL | gpt-4, gpt-3.5-turbo | gpt-3.5-turbo | ⚠️ if online |
| CLAUDE_API_KEY | sk-ant-... | - | ⚠️ if online |
| OLLAMA_HOST | http://... | localhost:11434 | ✅ if offline |
| OLLAMA_MODEL | llama2, mistral, etc | llama2 | ✅ if offline |
| FLASK_ENV | development, production | development | ❌ |
| FLASK_DEBUG | True, False | True | ❌ |
| BACKEND_PORT | 1000-65535 | 5000 | ❌ |

---

## Next Steps

- 📖 Read [SETUP.md](SETUP.md) for installation
- 🏗️ Read [ARCHITECTURE.md](ARCHITECTURE.md) for system design
- 🚀 Start building!

---

**Need help?** Open an issue on [GitHub](https://github.com/Neshley/cerebro/issues)
