import React, { useState, useRef, useEffect } from 'react';
import { Send, Loader } from 'lucide-react';
import './ChatInterface.css';

function ChatInterface({ messages, onSendMessage, mode }) {
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setIsLoading(true);
    await onSendMessage(input);
    setInput('');
    setIsLoading(false);
  };

  return (
    <div className="chat-interface">
      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <h1>Welcome to Cerebro</h1>
            <p>Your AI Desktop Companion</p>
            <p className="mode-indicator">Mode: {mode === 'online' ? '🌐 Online' : '📴 Offline'}</p>
          </div>
        ) : (
          messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.role}`}>
              <div className="message-content">
                {msg.content}
              </div>
            </div>
          ))
        )}
        {isLoading && (
          <div className="message assistant">
            <div className="message-content loading">
              <Loader className="spinner" />
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="chat-input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask Cerebro anything..."
          disabled={isLoading}
          className="chat-input"
        />
        <button
          type="submit"
          disabled={isLoading || !input.trim()}
          className="send-button"
        >
          <Send size={20} />
        </button>
      </form>
    </div>
  );
}

export default ChatInterface;
