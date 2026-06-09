import React from 'react';
import { Wifi, WifiOff, Zap } from 'lucide-react';
import './StatusBar.css';

function StatusBar({ mode, isOnline }) {
  return (
    <div className="status-bar">
      <div className="status-left">
        <div className="status-item">
          {isOnline ? (
            <>
              <Wifi size={16} />
              <span>Online</span>
            </>
          ) : (
            <>
              <WifiOff size={16} />
              <span>Offline</span>
            </>
          )}
        </div>
      </div>

      <div className="status-center">
        <h1>Cerebro</h1>
      </div>

      <div className="status-right">
        <div className="status-item">
          <Zap size={16} />
          <span>Mode: {mode === 'online' ? '☁️ Cloud' : '🖥️ Local'}</span>
        </div>
      </div>
    </div>
  );
}

export default StatusBar;
