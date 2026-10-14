const { app, BrowserWindow, dialog } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const fs = require('fs');

let pythonProcess = null;
let mainWindow = null;

function getPythonAppPath() {
  if (app.isPackaged) {
    return path.join(process.resourcesPath, 'python-app', 'DeepLiveCum.exe');
  }
  // Dev mode fallback
  return path.join(__dirname, '..', 'dist', 'DeepLiveCum', 'DeepLiveCum.exe');
}

function startPythonApp() {
  const exePath = getPythonAppPath();
  if (!fs.existsSync(exePath)) {
    dialog.showErrorBox('Error', `Python app not found at:\n${exePath}\n\nPlease build with PyInstaller first.`);
    app.quit();
    return;
  }

  pythonProcess = spawn(exePath, [], {
    cwd: path.dirname(exePath),
    detached: false,
    stdio: 'ignore'
  });

  pythonProcess.on('error', (err) => {
    dialog.showErrorBox('Launch Error', `Failed to start Deep-Live-Cum:\n${err.message}`);
    app.quit();
  });

  pythonProcess.on('exit', (code) => {
    if (code !== 0 && code !== null) {
      console.log(`Python app exited with code ${code}`);
    }
    app.quit();
  });
}

function createWindow() {
  // Optional minimal Electron window (can be hidden)
  mainWindow = new BrowserWindow({
    width: 400,
    height: 200,
    show: false, // Hide since Qt app is the real UI
    webPreferences: {
      nodeIntegration: true
    }
  });
  mainWindow.loadURL('data:text/html,<h2>Deep-Live-Cum is starting...</h2>');
}

app.whenReady().then(() => {
  createWindow();
  startPythonApp();
});

app.on('window-all-closed', () => {
  if (pythonProcess) {
    pythonProcess.kill();
  }
  app.quit();
});

app.on('before-quit', () => {
  if (pythonProcess && !pythonProcess.killed) {
    pythonProcess.kill();
  }
});
