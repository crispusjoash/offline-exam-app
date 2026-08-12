import React, { useState, useEffect } from 'react';
import QRCode from 'react-qr-code';
import { Lock, Copy, KeyRound, CheckCircle2, AlertCircle } from 'lucide-react';
import { checkActivationStatus, getDeviceHWID, validateUnlockCode } from '../utils/hwid';

export function ActivationLocker({ children }) {
  const [status, setStatus] = useState('checking'); // checking, locked, activated
  const [hwid, setHwid] = useState('');
  const [unlockCode, setUnlockCode] = useState('');
  const [error, setError] = useState('');
  const [isCopied, setIsCopied] = useState(false);

  // Bypass lock screen entirely during local development
  if (import.meta.env.DEV) {
    return children;
  }

  useEffect(() => {
    async function init() {
      const activation = await checkActivationStatus();
      if (activation.activated) {
        setStatus('activated');
      } else {
        const id = await getDeviceHWID();
        setHwid(id);
        setStatus('locked');
        if (activation.error) {
          setError(activation.error);
        }
      }
    }
    init();
  }, []);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(hwid);
      setIsCopied(true);
      setTimeout(() => setIsCopied(false), 2000);
    } catch (e) {
      console.error('Failed to copy', e);
    }
  };

  const handleUnlock = async (e) => {
    e.preventDefault();
    if (!unlockCode) return;

    const result = await validateUnlockCode(unlockCode);
    if (result.valid) {
      setStatus('activated');
    } else {
      setError(result.error || 'Invalid Unlock Code');
    }
  };

  if (status === 'checking') {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900 font-outfit">
        <div className="text-white flex items-center space-x-2">
          <Lock className="w-5 h-5 animate-pulse" />
          <span>Verifying License...</span>
        </div>
      </div>
    );
  }

  if (status === 'activated') {
    return children;
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-900 via-gray-800 to-black font-outfit p-4">
      <div className="w-full max-w-md backdrop-blur-xl bg-white/10 p-8 rounded-2xl shadow-2xl border border-white/20 relative overflow-hidden">
        {/* Glow effect */}
        <div className="absolute -top-24 -right-24 w-48 h-48 bg-purple-500 rounded-full mix-blend-multiply filter blur-3xl opacity-50"></div>
        <div className="absolute -bottom-24 -left-24 w-48 h-48 bg-blue-500 rounded-full mix-blend-multiply filter blur-3xl opacity-50"></div>

        <div className="relative z-10 flex flex-col items-center">
          <div className="w-16 h-16 bg-white/10 rounded-full flex items-center justify-center mb-6 shadow-lg border border-white/20">
            <Lock className="w-8 h-8 text-blue-400" />
          </div>
          
          <h1 className="text-2xl font-bold text-white mb-2 text-center tracking-tight">App Locked</h1>
          <p className="text-gray-300 text-center text-sm mb-8 leading-relaxed">
            This application is locked to your device. Please provide the Hardware ID below to your administrator to receive an Unlock Code.
          </p>

          <div className="w-full bg-black/40 rounded-xl p-4 mb-6 border border-white/10 flex flex-col items-center">
            <p className="text-xs text-gray-400 uppercase tracking-wider mb-2 font-semibold">Your Hardware ID</p>
            <div className="flex items-center justify-center space-x-3 w-full">
              <span className="text-2xl font-mono font-medium text-white tracking-widest">{hwid}</span>
              <button 
                onClick={handleCopy}
                className="p-2 rounded-lg bg-white/5 hover:bg-white/20 transition-colors text-gray-300 hover:text-white"
                title="Copy to Clipboard"
              >
                {isCopied ? <CheckCircle2 className="w-5 h-5 text-green-400" /> : <Copy className="w-5 h-5" />}
              </button>
            </div>
            
            <div className="mt-4 p-2 bg-white rounded-lg">
              <QRCode 
                value={hwid} 
                size={120} 
                bgColor={"#ffffff"} 
                fgColor={"#000000"} 
                level={"M"} 
              />
            </div>
          </div>

          <form onSubmit={handleUnlock} className="w-full">
            <div className="relative mb-4">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <KeyRound className="h-5 w-5 text-gray-400" />
              </div>
              <input
                type="text"
                placeholder="Enter 12-char Unlock Code"
                value={unlockCode}
                onChange={(e) => {
                  setError('');
                  let val = e.target.value.replace(/[^a-zA-Z0-9-]/g, '').toUpperCase();
                  if (val.length === 4 || val.length === 9) {
                     // small auto-formatting help if they type without dashes
                     if(unlockCode.length < val.length && !val.endsWith('-')) {
                        val = val + '-';
                     }
                  }
                  setUnlockCode(val);
                }}
                maxLength={14}
                className="w-full pl-10 pr-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent text-white placeholder-gray-500 font-mono tracking-widest outline-none transition-all"
              />
            </div>

            {error && (
              <div className="flex items-center space-x-2 text-red-400 text-sm mb-4 bg-red-400/10 p-3 rounded-lg border border-red-400/20">
                <AlertCircle className="w-4 h-4 flex-shrink-0" />
                <span>{error}</span>
              </div>
            )}

            <button
              type="submit"
              disabled={!unlockCode || unlockCode.length < 12}
              className="w-full py-3 px-4 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-semibold rounded-xl shadow-lg transform transition-all active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Unlock Application
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
