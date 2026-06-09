import React, { useState, useRef } from 'react';
import { MessageCircle, X } from 'lucide-react';
import './FloatingWidget.css';

function FloatingWidget({ onToggleChat }) {
  const [isDragging, setIsDragging] = useState(false);
  const [position, setPosition] = useState({ x: 20, y: 20 });
  const [offset, setOffset] = useState({ x: 0, y: 0 });
  const widgetRef = useRef(null);

  const handleMouseDown = (e) => {
    setIsDragging(true);
    setOffset({
      x: e.clientX - position.x,
      y: e.clientY - position.y
    });
  };

  const handleMouseMove = (e) => {
    if (!isDragging) return;
    
    setPosition({
      x: e.clientX - offset.x,
      y: e.clientY - offset.y
    });
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  React.useEffect(() => {
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, [isDragging, offset]);

  return (
    <div
      ref={widgetRef}
      className="floating-widget"
      style={{
        left: `${position.x}px`,
        top: `${position.y}px`,
        cursor: isDragging ? 'grabbing' : 'grab'
      }}
      onMouseDown={handleMouseDown}
    >
      <div className="widget-icon">
        <div className="icon-circle">
          <MessageCircle size={32} />
        </div>
        <div className="online-indicator"></div>
      </div>
    </div>
  );
}

export default FloatingWidget;
