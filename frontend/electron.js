const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const isDev = require('electron-is-dev');

let mainWindow;
let floatingWidget;

// Create main application window
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  const startUrl = isDev
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../build/index.html')}`;

  mainWindow.loadURL(startUrl);

  if (isDev) {
    mainWindow.webContents.openDevTools();
  }

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

// Create floating widget window
function createFloatingWidget() {
  floatingWidget = new BrowserWindow({
    width: 100,
    height: 100,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    skipTaskbar: true,
  });

  const startUrl = isDev
    ? 'http://localhost:3000/widget'
    : `file://${path.join(__dirname, '../build/index.html')}?widget=true`;

  floatingWidget.loadURL(startUrl);

  floatingWidget.on('closed', () => {
    floatingWidget = null;
  });
}

// App event listeners
app.on('ready', () => {
  createWindow();
  createFloatingWidget();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});

// IPC handlers
ipcMain.on('toggle-widget-visibility', (event) => {
  if (floatingWidget) {
    floatingWidget.isVisible() ? floatingWidget.hide() : floatingWidget.show();
  }
});

ipcMain.on('move-widget', (event, { x, y }) => {
  if (floatingWidget) {
    floatingWidget.setPosition(x, y);
  }
});
