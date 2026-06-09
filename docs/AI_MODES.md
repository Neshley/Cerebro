# 🤖 Cerebro AI Modes Guide

Complete guide to using Cerebro's online and offline AI capabilities.

## 📋 Table of Contents

1. [AI Modes Overview](#ai-modes-overview)
2. [Offline Mode (Local)](#offline-mode-local)
3. [Online Mode (Cloud)](#online-mode-cloud)
4. [Switching Between Modes](#switching-between-modes)
5. [Performance Comparison](#performance-comparison)
6. [API Integration](#api-integration)
7. [Troubleshooting](#troubleshooting)

---

## AI Modes Overview

### What are AI Modes?

Cerebro can use two different AI sources:

1. **Offline Mode** - Local AI running on your computer
2. **Online Mode** - Cloud-based AI (OpenAI, Claude)

### Quick Comparison

| Feature | Offline | Online |
|---------|---------|--------|
| **Speed** | Fast | Medium |
| **Quality** | Good | Excellent |
| **Privacy** | Perfect | Server-based |
| **Cost** | Free | Per-token |
| **Internet** | Not needed | Required |
| **Setup** | Easy | API keys needed |
| **Models** | Limited | Many options |

### Automatic Switching

Cerebro detects internet connection and **automatically switches**:

```
No Internet → Forces Offline Mode ✅
Internet Available → Uses configured mode (online/offline)
```

---

## Offline Mode (Local)

### What is Offline Mode?

Local AI models running on your computer via **Ollama**.

### Advantages
✅ **Privacy** - Data never leaves your computer
✅ **Free** - No subscription or API costs
✅ **No Internet** - Works without connection
✅ **Instant** - No network latency
✅ **Control** - You control the model

### Disadvantages
❌ **Quality** - Smaller models have lower quality
❌ **Speed** - Slower than cloud on average systems
❌ **Resources** - Uses CPU/RAM
❌ **Setup** - Requires Ollama installation

### Setup Offline Mode

#### Step 1: Install Ollama

Download from: https://ollama.ai

**macOS:**
```bash
brew install ollama
```

**Windows/Linux:**
Download installer from ollama.ai

#### Step 2: Start Ollama

```bash
ollama serve
```

You should see:
```
Listening on 127.0.0.1:11434
```

#### Step 3: Download a Model

In a new terminal:

```bash
# Download model (first time is large)
ollama pull llama2
```

Available models:
- **llama2** (7B) - Default, good balance
- **mistral** (7B) - Faster, smaller
- **neural-chat** (7B) - Optimized for chat
- **orca-mini** (3B) - Smallest, fastest
- **llama2:13b** - Larger, more capable

#### Step 4: Configure Cerebro

Edit `backend/.env`:
```env
AI_MODE=offline
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama2
```

#### Step 5: Restart Backend

```bash
# Stop backend (Ctrl+C)
python app.py
```

### Using Offline Mode

#### Chat Example

```
User: "What is Python?"

Cerebro (Offline): 
Python is a high-level programming language known for 
its simplicity and readability...
[Response generated locally on your computer]
```

#### Supported Capabilities

✅ General questions
✅ Code assistance
✅ Writing help
✅ Explanations
✅ Text processing

#### Limitations

❌ Real-time information
❌ Web search
❌ Current events
❌ Image understanding
❌ Advanced reasoning (smaller models)

### Offline Mode Performance

**Speed depends on:**
- Model size (3B, 7B, 13B)
- Your computer RAM
- Your CPU
- Model complexity

**Typical response times:**
- **3B Model**: 2-5 seconds
- **7B Model**: 5-15 seconds  
- **13B Model**: 10-30 seconds

### Changing Models

To use a different model:

```bash
# Download model
ollama pull mistral

# Update .env
OLLAMA_MODEL=mistral

# Restart Cerebro backend
```

**List available models:**
```bash
ollama list
```

---

## Online Mode (Cloud)

### What is Online Mode?

Using AI from cloud providers:
- **OpenAI** (ChatGPT, GPT-4)
- **Anthropic** (Claude)

### Advantages
✅ **Quality** - Advanced models (GPT-4)
✅ **Speed** - Optimized servers
✅ **Capabilities** - Web access, image, reasoning
✅ **Updates** - Always latest version
✅ **No resources** - Uses cloud compute

### Disadvantages
❌ **Cost** - Per-token pricing
❌ **Internet** - Must be connected
❌ **Privacy** - Data sent to servers
❌ **Latency** - Network dependent
❌ **API limits** - Rate limiting

### Setup Online Mode

#### Step 1: Choose Provider

**Option A: OpenAI (Recommended)**
- Models: GPT-4, GPT-3.5-turbo
- Cost: ~$0.01-0.03 per 1K tokens
- Get key: https://platform.openai.com/api-keys

**Option B: Claude (Anthropic)**
- Models: Claude 3 Sonnet, Opus
- Cost: ~$0.003-0.024 per 1K tokens
- Get key: https://console.anthropic.com/

#### Step 2: Get API Key

**For OpenAI:**
1. Go to https://platform.openai.com/api-keys
2. Login/create account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

**For Claude:**
1. Go to https://console.anthropic.com/
2. Login/create account
3. Go to API keys section
4. Create new key (starts with `sk-ant-`)

#### Step 3: Add to .env

For OpenAI:
```env
AI_MODE=online
OPENAI_API_KEY=sk-your-actual-key
OPENAI_MODEL=gpt-4
```

For Claude:
```env
AI_MODE=online
CLAUDE_API_KEY=sk-ant-your-actual-key
```

#### Step 4: Restart Backend

```bash
# Stop backend (Ctrl+C)
python app.py
```

### Using Online Mode

#### Chat Example

```
User: "What are the latest AI developments?"

Cerebro (Online): 
As of my knowledge cutoff, recent developments in AI include...
[Response from GPT-4 or Claude]
```

#### Supported Capabilities

✅ General questions
✅ Code assistance
✅ Complex reasoning
✅ Current events (if in training)
✅ Web browsing (planned)
✅ Image understanding (planned)
✅ Advanced analysis

#### Model Selection

**OpenAI Options:**

| Model | Speed | Cost | Quality |
|-------|-------|------|----------|
| gpt-3.5-turbo | ⚡⚡⚡ | $ | ⭐⭐⭐ |
| gpt-4 | ⚡ | $$$ | ⭐⭐⭐⭐⭐ |
| gpt-4-turbo | ⚡⚡ | $$ | ⭐⭐⭐⭐ |

### Online Mode Cost

**Typical costs (rough estimates):**

```
Simple question (100 tokens): ~$0.001
Medium response (500 tokens): ~$0.005
Long analysis (2000 tokens): ~$0.02
```

**Monitor your usage:**
- OpenAI: https://platform.openai.com/account/usage/overview
- Claude: Check your console

### Rate Limits

**OpenAI free trial:**
- Limited requests
- Expires after 3 months
- Purchase credits for continuous use

**Claude:**
- Usage-based billing
- No free trial (small amount free with account)

---

## Switching Between Modes

### Method 1: Edit .env File

```bash
# Edit configuration
nano backend/.env

# Change:
# From: AI_MODE=offline
# To: AI_MODE=online

# Save and exit
```

**Restart backend** for changes to take effect.

### Method 2: API Call

```bash
# Change mode via API
curl -X POST http://localhost:5000/api/config/settings/ai-mode \
  -H "Content-Type: application/json" \
  -d '{"mode": "online"}'
```

### Method 3: Web Interface (Planned)

Settings button in UI to switch modes.

### Verifying Mode Change

```bash
# Check current mode
curl http://localhost:5000/api/ai/mode
```

Response:
```json
{
  "mode": "offline"
}
```

---

## Performance Comparison

### Response Time

```
Offline (Local):
├─ Simple question: 2-5 seconds
├─ Code assistance: 5-15 seconds
└─ Long text: 15-30 seconds

Online (Cloud):
├─ Simple question: 1-3 seconds
├─ Code assistance: 2-5 seconds
└─ Long text: 3-8 seconds
```

### Quality Comparison

**Offline (Llama 2):**
- General knowledge: 8/10
- Code: 7/10
- Reasoning: 6/10
- Creativity: 7/10

**Online (GPT-4):**
- General knowledge: 10/10
- Code: 10/10
- Reasoning: 10/10
- Creativity: 10/10

### Resource Usage

**Offline Mode:**
- CPU: 50-100% (during response)
- RAM: 4-8GB (model size)
- Bandwidth: 0 KB/s
- Cost: $0

**Online Mode:**
- CPU: 5-10% (API calls)
- RAM: <100MB
- Bandwidth: ~1-10 KB/s
- Cost: $0.001-0.02 per query

---

## API Integration

### Getting Current AI Mode

```bash
GET /api/ai/mode

# Response:
{
  "mode": "offline"  # or "online"
}
```

### Changing AI Mode

```bash
POST /api/config/settings/ai-mode
Content-Type: application/json

{
  "mode": "online"
}

# Response:
{
  "mode": "online",
  "success": true
}
```

### Sending Chat Message

```bash
POST /api/ai/chat
Content-Type: application/json

{
  "message": "What is AI?"
}

# Response:
{
  "response": "AI stands for Artificial Intelligence...",
  "mode": "offline",  # Shows which mode was used
  "success": true
}
```

---

## Troubleshooting

### Issue: "API key invalid"

**Check:**
1. Key copied completely (no extra spaces)
2. Key format matches provider
3. Key hasn't been revoked

**For OpenAI:**
```bash
# Test key
curl -H "Authorization: Bearer sk-..." https://api.openai.com/v1/models
```

### Issue: "Cannot connect to Ollama"

**Check:**
1. Ollama is running: `ollama serve`
2. OLLAMA_HOST in .env is correct
3. Port 11434 is accessible

```bash
# Test connection
curl http://localhost:11434/api/tags
```

### Issue: "Mode didn't change"

**Solution:** Restart backend
```bash
# Stop: Ctrl+C
python app.py
```

### Issue: "Rate limit exceeded"

**For OpenAI:**
1. Wait a few minutes
2. Reduce request frequency
3. Upgrade your API tier

### Issue: "No internet - can't use online mode"

**Solution:**
- Reconnect to internet
- Or switch to offline mode
- Offline mode works without internet

### Issue: "Response quality is poor (offline)"

**Solutions:**
1. Try a larger model: `ollama pull llama2:13b`
2. Or switch to online mode
3. Check OLLAMA_MODEL setting

---

## Best Practices

### When to Use Offline
✅ Privacy is critical
✅ No internet available
✅ Testing/development
✅ Budget constraints
✅ Local/sensitive data

### When to Use Online
✅ Need best quality
✅ Complex reasoning needed
✅ Latest information
✅ Professional use
✅ Have internet connection

### Hybrid Approach (Recommended)

```env
# Development/testing
AI_MODE=offline

# Production/important tasks
AI_MODE=online
```

---

## Next Steps

- 📖 Read [SETUP.md](SETUP.md) for installation
- ⚙️ Read [CONFIGURATION.md](CONFIGURATION.md) for settings
- 🏗️ Read [ARCHITECTURE.md](ARCHITECTURE.md) for system design

---

**Questions?** Open an issue on [GitHub](https://github.com/Neshley/cerebro/issues)
