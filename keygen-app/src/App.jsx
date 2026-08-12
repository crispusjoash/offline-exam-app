import React, { useState, useEffect } from 'react';
import { generateUnlockCode, getHistory } from './utils/crypto';
import { Preferences } from '@capacitor/preferences';
import { KeyRound, Shield, Clock, Settings, Copy, Camera, Check, History, X, LogOut } from 'lucide-react';

function App() {
  const [screen, setScreen] = useState('login'); // login, generator, history, settings
  const [password, setPassword] = useState('');
  const [authError, setAuthError] = useState('');
  const [savedPassword, setSavedPassword] = useState('Admin@2026');

  // Generator State
  const [hwid, setHwid] = useState('');
  const [duration, setDuration] = useState(12);
  const [generatedCode, setGeneratedCode] = useState('');
  const [copied, setCopied] = useState(false);
  const [genError, setGenError] = useState('');
  const [historyData, setHistoryData] = useState([]);

  // Settings State
  const [newPass, setNewPass] = useState('');

  useEffect(() => {
    async function loadData() {
      const { value } = await Preferences.get({ key: 'adminPassword' });
      if (value) setSavedPassword(value);
      
      const hist = await getHistory();
      setHistoryData(hist);
    }
    loadData();
  }, [screen]);

  const handleLogin = (e) => {
    e.preventDefault();
    if (password === savedPassword) {
      setScreen('generator');
      setAuthError('');
      setPassword('');
    } else {
      setAuthError('Incorrect Password');
    }
  };

  const handleGenerate = async () => {
    try {
      setGenError('');
      if (!hwid || hwid.length < 8) {
        setGenError('Please enter a valid HWID (min 8 characters)');
        return;
      }
      const code = await generateUnlockCode(hwid, duration);
      setGeneratedCode(code);
    } catch (e) {
      setGenError(e.message || String(e));
    }
  };

  const handleCopy = async (text) => {
    await navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleChangePass = async (e) => {
    e.preventDefault();
    if (newPass.length < 4) return;
    await Preferences.set({ key: 'adminPassword', value: newPass });
    setSavedPassword(newPass);
    setNewPass('');
    alert('Password updated successfully!');
    setScreen('generator');
  };

  if (screen === 'login') {
    return (
      <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
        <form onSubmit={handleLogin} className="bg-gray-800 p-8 rounded-2xl shadow-2xl w-full max-w-sm border border-gray-700">
          <div className="flex justify-center mb-6">
            <div className="bg-blue-500/20 p-4 rounded-full">
              <Shield className="w-10 h-10 text-blue-500" />
            </div>
          </div>
          <h1 className="text-2xl text-white font-bold text-center mb-6">Keygen Auth</h1>
          <input 
            type="password" 
            placeholder="Enter Password" 
            value={password}
            onChange={e => setPassword(e.target.value)}
            className="w-full bg-gray-900 border border-gray-700 text-white rounded-lg p-3 mb-4 focus:ring-2 focus:ring-blue-500 outline-none"
          />
          {authError && <p className="text-red-400 text-sm mb-4 text-center">{authError}</p>}
          <button type="submit" className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg transition-colors">
            Unlock Keygen
          </button>
        </form>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Navbar */}
      <nav className="bg-gray-800 p-4 shadow-md flex justify-between items-center sticky top-0 z-10 border-b border-gray-700">
        <div className="flex items-center space-x-2 text-blue-400 font-bold text-xl">
          <KeyRound className="w-6 h-6" />
          <span>CBC Keygen</span>
        </div>
        <div className="flex space-x-4 text-gray-400">
          <button onClick={() => setScreen('generator')} className={`hover:text-white ${screen === 'generator' ? 'text-white' : ''}`}><KeyRound className="w-6 h-6" /></button>
          <button onClick={() => setScreen('history')} className={`hover:text-white ${screen === 'history' ? 'text-white' : ''}`}><History className="w-6 h-6" /></button>
          <button onClick={() => setScreen('settings')} className={`hover:text-white ${screen === 'settings' ? 'text-white' : ''}`}><Settings className="w-6 h-6" /></button>
          <button onClick={() => setScreen('login')} className="hover:text-red-400"><LogOut className="w-6 h-6" /></button>
        </div>
      </nav>

      {/* Main Content */}
      <div className="p-4 max-w-lg mx-auto mt-4">
        {screen === 'generator' && (
          <div className="space-y-6">
            <div className="bg-gray-800 p-6 rounded-2xl border border-gray-700 shadow-xl">
              <h2 className="text-xl font-bold mb-4 flex items-center"><Camera className="mr-2 w-5 h-5 text-blue-400" /> Customer HWID</h2>
              <input 
                type="text" 
                placeholder="Paste HWID here (e.g. A1B2-C3D4)"
                value={hwid}
                onChange={e => setHwid(e.target.value.toUpperCase())}
                className="w-full bg-gray-900 border border-gray-700 rounded-lg p-4 font-mono text-lg tracking-wider focus:ring-2 focus:ring-blue-500 outline-none mb-2"
              />
              <p className="text-gray-400 text-xs text-center">(QR Scanner feature can be integrated here)</p>
            </div>

            <div className="bg-gray-800 p-6 rounded-2xl border border-gray-700 shadow-xl">
              <h2 className="text-xl font-bold mb-4 flex items-center"><Clock className="mr-2 w-5 h-5 text-blue-400" /> Subscription Plan</h2>
              <div className="grid grid-cols-3 gap-3">
                {[4, 8, 12].map(m => (
                  <button 
                    key={m}
                    onClick={() => setDuration(m)}
                    className={`py-3 rounded-lg border font-bold transition-all ${duration === m ? 'bg-blue-600 border-blue-500 text-white' : 'bg-gray-900 border-gray-700 text-gray-400 hover:border-gray-500'}`}
                  >
                    {m} Months
                  </button>
                ))}
              </div>
            </div>

            <button 
              onClick={handleGenerate}
              className="w-full bg-green-600 hover:bg-green-500 text-white font-bold py-4 rounded-xl shadow-lg transform transition active:scale-95 text-lg"
            >
              Generate Unlock Code
            </button>

            {genError && <p className="text-red-400 text-center font-bold">{genError}</p>}

            {generatedCode && (
              <div className="bg-gradient-to-r from-blue-900 to-indigo-900 p-6 rounded-2xl border border-blue-500/30 text-center animate-in fade-in zoom-in duration-300 shadow-2xl">
                <p className="text-blue-200 text-sm font-bold uppercase tracking-widest mb-2">Generated Code</p>
                <div className="text-3xl font-mono font-bold tracking-widest text-white mb-6 bg-black/30 py-4 rounded-lg shadow-inner">
                  {generatedCode}
                </div>
                <button 
                  onClick={() => handleCopy(generatedCode)}
                  className="inline-flex items-center space-x-2 bg-white/10 hover:bg-white/20 px-6 py-3 rounded-full transition-colors"
                >
                  {copied ? <Check className="w-5 h-5 text-green-400" /> : <Copy className="w-5 h-5" />}
                  <span>{copied ? 'Copied!' : 'Copy Code'}</span>
                </button>
              </div>
            )}
          </div>
        )}

        {screen === 'history' && (
          <div className="bg-gray-800 rounded-2xl border border-gray-700 overflow-hidden shadow-xl">
            <div className="p-4 bg-gray-700/50 border-b border-gray-700 font-bold flex items-center">
              <History className="mr-2 w-5 h-5" /> Recent Generations
            </div>
            {historyData.length === 0 ? (
              <p className="text-gray-400 p-6 text-center">No history yet.</p>
            ) : (
              <ul className="divide-y divide-gray-700 max-h-[70vh] overflow-y-auto">
                {historyData.map((h, i) => (
                  <li key={i} className="p-4 hover:bg-gray-750 transition-colors">
                    <div className="flex justify-between items-start mb-1">
                      <span className="font-mono text-blue-400 font-bold">{h.code}</span>
                      <span className="text-xs bg-gray-900 px-2 py-1 rounded text-gray-400">{new Date(h.date).toLocaleDateString()}</span>
                    </div>
                    <div className="flex justify-between text-sm text-gray-400">
                      <span>HWID: {h.hwid}</span>
                      <span>{h.months} Months</span>
                    </div>
                  </li>
                ))}
              </ul>
            )}
          </div>
        )}

        {screen === 'settings' && (
          <div className="bg-gray-800 p-6 rounded-2xl border border-gray-700 shadow-xl">
            <h2 className="text-xl font-bold mb-6 flex items-center"><Settings className="mr-2 w-5 h-5 text-blue-400" /> Security Settings</h2>
            <form onSubmit={handleChangePass}>
              <label className="block text-sm text-gray-400 mb-2">New Password / PIN</label>
              <input 
                type="text" 
                value={newPass}
                onChange={e => setNewPass(e.target.value)}
                placeholder="Enter new password"
                className="w-full bg-gray-900 border border-gray-700 text-white rounded-lg p-3 mb-6 focus:ring-2 focus:ring-blue-500 outline-none"
              />
              <button 
                type="submit"
                disabled={newPass.length < 4}
                className="w-full bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white font-bold py-3 rounded-lg transition-colors"
              >
                Update Password
              </button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
