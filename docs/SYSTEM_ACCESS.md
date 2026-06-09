# 💻 Cerebro System Access Guide

Complete guide to system integration and commands in Cerebro.

## 📋 Table of Contents

1. [System Access Overview](#system-access-overview)
2. [File Management](#file-management)
3. [Process Management](#process-management)
4. [Web Access](#web-access)
5. [Command Examples](#command-examples)
6. [Security Considerations](#security-considerations)
7. [Troubleshooting](#troubleshooting)

---

## System Access Overview

### What is System Access?

Cerebro can interact with your computer:
- 📁 Browse and read files
- ⚙️ Manage running processes
- 🌐 Open websites
- 🎯 Execute commands

### Capabilities

✅ **Read files** (any readable file)
✅ **List directories** (view folder contents)
✅ **List processes** (see running apps)
✅ **Kill processes** (close apps)
✅ **Open URLs** (launch websites)
✅ **Open programs** (start applications)

### API Endpoints

```
POST   /api/system/files/list       - List directory
POST   /api/system/files/read       - Read file contents
GET    /api/system/processes/list   - List processes
POST   /api/system/processes/kill   - Kill process
POST   /api/system/web/open        - Open URL
```

---

## File Management

### List Directory Contents

**Command:**
```
"Show me what's in my Documents folder"
"List my home directory"
"What files are in Downloads?"
```

**API Endpoint:**
```bash
POST /api/system/files/list
Content-Type: application/json

{
  "path": "~/Documents"
}

# Response:
{
  "files": [
    {
      "name": "report.pdf",
      "path": "/home/user/Documents/report.pdf",
      "is_directory": false,
      "size": 2048576
    },
    {
      "name": "Projects",
      "path": "/home/user/Documents/Projects",
      "is_directory": true,
      "size": null
    }
  ],
  "path": "~/Documents",
  "success": true
}
```

### Supported Path Formats

```
~/                    Home directory
~/.config            Hidden folders
/home/username/docs  Absolute paths
./relative/path      Relative paths
C:\Users\name\docs   Windows paths
```

### Read File Contents

**Command:**
```
"Read my config file"
"Show me the README.md"
"What's in my .env file?"
```

**API Endpoint:**
```bash
POST /api/system/files/read
Content-Type: application/json

{
  "path": "~/Documents/notes.txt"
}

# Response:
{
  "content": "File contents here...",
  "path": "~/Documents/notes.txt",
  "success": true
}
```

### File Type Support

**Can read:**
- Text files (.txt, .md, .csv, .json, .xml)
- Code files (.py, .js, .html, .css, .java)
- Config files (.env, .yaml, .ini)
- Data files (.json, .xml)

**Size limits:**
- Up to 10MB (to avoid memory issues)
- Larger files may fail

### Directory Navigation

```
# List home directory
"ls ~"

# List current directory
"pwd"

# List with details
"List /home/user with details"

# Show hidden files
"Show hidden files in Documents"
```

---

## Process Management

### List Running Processes

**Command:**
```
"Show running processes"
"What apps are open?"
"List all running programs"
```

**API Endpoint:**
```bash
GET /api/system/processes/list

# Response:
{
  "processes": [
    {
      "pid": 1234,
      "name": "chrome",
      "status": "running"
    },
    {
      "pid": 5678,
      "name": "code",
      "status": "running"
    }
  ],
  "success": true
}
```

### Get Process Info

**Command:**
```
"What's using CPU?"
"Memory usage of processes"
"Details on chrome process"
```

**Get Process Details:**
```bash
# Get info for specific process
POST /api/system/processes/info
{
  "pid": 1234
}

# Response:
{
  "pid": 1234,
  "name": "chrome",
  "status": "running",
  "memory_percent": 15.5,
  "cpu_percent": 8.2
}
```

### Kill a Process

**Command:**
```
"Close chrome"
"Kill process 1234"
"Stop the Firefox app"
```

**API Endpoint:**
```bash
POST /api/system/processes/kill
Content-Type: application/json

{
  "pid": 1234
}

# Response:
{
  "success": true,
  "message": "Process terminated"
}
```

### Common Processes

```
# Browsers
chrome, firefox, safari, edge

# Editors
code (VS Code), vim, nano

# Development
node, python, java, docker

# Communication
slack, discord, zoom

# Utilities
terminal, explorer, finder
```

---

## Web Access

### Open a Website

**Command:**
```
"Open Google"
"Go to GitHub"
"Launch Facebook"
"Open https://github.com"
```

**API Endpoint:**
```bash
POST /api/system/web/open
Content-Type: application/json

{
  "url": "https://github.com"
}

# Response:
{
  "url": "https://github.com",
  "success": true
}
```

### URL Handling

**Formats supported:**
```
Full URL:    https://github.com
Short URL:   github.com
Domain only: github.com
Search:      "search term" (opens search)
```

### Automatic URL Detection

```
"Open localhost:3000"        → http://localhost:3000
"Go to google"               → https://google.com
"Visit reddit.com"           → https://reddit.com
"Check 192.168.1.1:8080"     → http://192.168.1.1:8080
```

### Supported Actions

```
✅ Open URL in default browser
✅ Open localhost apps
✅ Open file URLs
✅ Open local servers
```

---

## Command Examples

### File Management Examples

```
# List home directory
User: "Show my home directory"
Cerebro: [Lists all files and folders in home]

# Read file
User: "Read my favorite-websites.txt"
Cerebro: [Displays file contents]

# Navigate folders
User: "What's in my Downloads?"
Cerebro: [Shows Downloads folder contents]

# Find files
User: "Do I have any PDF files in Documents?"
Cerebro: [Scans and reports]
```

### Process Examples

```
# Check what's running
User: "What apps are currently running?"
Cerebro: [Lists all processes with details]

# Monitor resource usage
User: "Which app is using the most CPU?"
Cerebro: [Analyzes and reports top CPU usage]

# Close app
User: "Close VS Code"
Cerebro: [Terminates the process]

# Check specific app
User: "Is Chrome running?"
Cerebro: [Checks process list and confirms]
```

### Web Access Examples

```
# Open common sites
User: "Open GitHub"
Cerebro: [Opens GitHub in browser]

User: "Go to Stack Overflow"
Cerebro: [Opens Stack Overflow]

# Open local development servers
User: "Open my local app on 3000"
Cerebro: [Opens http://localhost:3000]

# Open admin panels
User: "Open router admin"
Cerebro: [Opens 192.168.1.1]
```

---

## Security Considerations

### 🔐 What You Should Know

1. **File Access**
   - Can read any file user can access
   - Cannot read files you don't have permission for
   - Be careful with sensitive files (.env, passwords)

2. **Process Control**
   - Can terminate running processes
   - Be careful what you kill
   - Some processes are system-critical

3. **Web Access**
   - Opens URLs in your default browser
   - Follows normal browser security
   - HTTPS connections are secure

### 🛡️ Security Best Practices

**Do:**
✅ Use environment variables for secrets
✅ Set file permissions appropriately
✅ Review commands before executing
✅ Keep browser and OS updated
✅ Use strong passwords

**Don't:**
❌ Store passwords in plain text
❌ Share .env files
❌ Kill unknown processes
❌ Visit untrusted URLs via Cerebro
❌ Give Cerebro unnecessary permissions

### 🔒 Privacy

- Local mode: All commands run locally
- No monitoring of your activities
- No data sent to servers (offline mode)
- Your data stays on your computer

---

## Advanced Usage

### Combine Commands

```
User: "Open my project folder and start development server"
Cerebro: 
1. Opens VS Code with project
2. Starts npm dev server
3. Opens localhost:3000
```

### File Automation

```
User: "List Python files in my projects"
Cerebro: [Finds and lists .py files]

User: "Show me the largest file in Downloads"
Cerebro: [Scans and reports]
```

### Process Management Workflow

```
User: "Kill old Node processes and start a new one"
Cerebro:
1. Finds Node processes
2. Terminates them
3. Starts new Node server
```

---

## Troubleshooting

### Issue: "Permission denied" when reading file

**Cause:** File has restricted permissions
**Solution:** 
- Check file permissions: `ls -l filename`
- Run with appropriate user
- Or read a different file

### Issue: "File not found"

**Check:**
1. Path is correct (case-sensitive on Linux/Mac)
2. File hasn't been deleted
3. Correct home directory path

**Use:**
```
ls ~               # List home
pwd                # Check current path
find ~ -name file  # Search for file
```

### Issue: "Cannot open URL"

**Check:**
1. URL format is correct
2. Website is online
3. Internet connection active

**Try:**
```
"Open https://google.com"  # Full URL
"Open localhost:3000"      # Local server
```

### Issue: "Process cannot be killed"

**Cause:** 
- System process (protected)
- Already terminated
- Permission issues

**Try:**
```
# Kill specific process
killall processname

# Force kill (use carefully)
kill -9 pid
```

---

## API Reference

### File List

```bash
POST /api/system/files/list
{
  "path": "~/Documents"
}

Response:
{
  "files": [...],
  "path": "~/Documents",
  "success": true
}
```

### File Read

```bash
POST /api/system/files/read
{
  "path": "~/file.txt"
}

Response:
{
  "content": "file contents",
  "path": "~/file.txt",
  "success": true
}
```

### Process List

```bash
GET /api/system/processes/list

Response:
{
  "processes": [
    {
      "pid": 1234,
      "name": "process_name",
      "status": "running"
    }
  ],
  "success": true
}
```

### Web Open

```bash
POST /api/system/web/open
{
  "url": "https://github.com"
}

Response:
{
  "url": "https://github.com",
  "success": true
}
```

---

## Limitations

### Current Limitations

❌ Cannot write files (read-only)
❌ Cannot install packages
❌ Cannot execute arbitrary shell commands
❌ Cannot access network in offline mode
❌ Limited file size (10MB)

### Planned Features

🔜 Write files
🔜 Execute scripts
🔜 Network commands
🔜 File monitoring
🔜 Scheduled tasks

---

## Next Steps

- 📖 Read [SETUP.md](SETUP.md) for installation
- 🤖 Read [AI_MODES.md](AI_MODES.md) for AI configuration
- 🏗️ Read [ARCHITECTURE.md](ARCHITECTURE.md) for system design

---

**Questions?** Open an issue on [GitHub](https://github.com/Neshley/cerebro/issues)
