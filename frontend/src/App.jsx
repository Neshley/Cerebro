import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import ChatInterface from './components/ChatInterface';
import FloatingWidget from './components/FloatingWidget';
import StatusBar from './components/StatusBar';

function App() {
  const [isWidget, setIsWidget] = useState(false);
  const [aiMode, setAiMode] = useState('offline');
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    // Check if running as widget
    const params = new URLSearchParams(window.location.search);
    setIsWidget(params.get('widget') === 'true');

    // Check internet connection
    window.addEventListener('online', () => setIsOnline(true));
    window.addEventListener('offline', () => setIsOnline(false));

    // Fetch initial mode
    fetchAiMode();

    return () => {
      window.removeEventListener('online', () => setIsOnline(true));
      window.removeEventListener('offline', () => setIsOnline(false));
    };
  }, []);

  const fetchAiMode = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/ai/mode');
      setAiMode(response.data.mode);
    } catch (error) {
      console.error('Error fetching AI mode:', error);
    }
  };

  const handleSendMessage = async (message) => {
    try {
      const response = await axios.post('http://localhost:5000/api/ai/chat', {
        message: message
      });

      setMessages([
        ...messages,
        { role: 'user', content: message },
        { role: 'assistant', content: response.data.response }
      ]);

      setAiMode(response.data.mode);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages([
        ...messages,
        { role: 'user', content: message },
        { role: 'error', content: 'Failed to get response from AI' }
      ]);
    }
  };

  if (isWidget) {
    return <FloatingWidget onToggleChat={() => {}} />;
  }

  return (
    <div className="app">
      <StatusBar mode={aiMode} isOnline={isOnline} />
      <ChatInterface 
        messages={messages}
        onSendMessage={handleSendMessage}
        mode={aiMode}
      />
    </div>
  );
}

export default App;
