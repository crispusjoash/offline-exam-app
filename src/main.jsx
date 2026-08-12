import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import 'katex/dist/katex.min.css'
import '@fontsource/inter/400.css';
import '@fontsource/inter/500.css';
import '@fontsource/inter/600.css';
import '@fontsource/inter/700.css';
import '@fontsource/outfit/400.css';
import '@fontsource/outfit/500.css';
import '@fontsource/outfit/600.css';
import '@fontsource/outfit/700.css';
import '@fontsource/outfit/800.css';
import '@fontsource/outfit/900.css';


// Global error boundary to prevent total blank page on runtime crash
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  componentDidCatch(error, info) {
    console.error('[CBC Portal] Runtime crash:', error, info);
  }
  render() {
    if (this.state.hasError) {
      return (
        <div style={{
          minHeight: '100vh',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          background: '#0f172a',
          padding: '2rem',
          fontFamily: 'sans-serif',
          color: '#f1f5f9',
          textAlign: 'center',
        }}>
          <div style={{
            background: '#1e293b',
            border: '1px solid #334155',
            borderRadius: '1rem',
            padding: '2rem',
            maxWidth: '480px',
            width: '100%',
          }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '0.75rem' }}>⚠️</div>
            <h1 style={{ fontSize: '1.2rem', fontWeight: '700', marginBottom: '0.5rem', color: '#f87171' }}>
              Something went wrong
            </h1>
            <p style={{ fontSize: '0.875rem', color: '#94a3b8', marginBottom: '1.5rem', lineHeight: 1.7 }}>
              {this.state.error?.message || 'An unexpected error occurred. Please restart the app.'}
            </p>
            <button
              onClick={() => { this.setState({ hasError: false, error: null }); window.location.hash = '/'; }}
              style={{
                background: 'linear-gradient(135deg, #2563eb, #7c3aed)',
                color: '#fff',
                border: 'none',
                borderRadius: '0.65rem',
                padding: '0.75rem 1.5rem',
                fontSize: '0.9rem',
                fontWeight: '700',
                cursor: 'pointer',
                width: '100%',
              }}
            >
              Restart App
            </button>
          </div>
        </div>
      );
    }
    return this.props.children;
  }
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>
)
