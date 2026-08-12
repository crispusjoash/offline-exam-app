import { Preferences } from '@capacitor/preferences';

const SECRET_SALT = 'OfflineExamSecret@2026';

// Generates an SHA-256 hash and returns it as a hex string
export async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

// Generate the 12-character unlock code
export async function generateUnlockCode(hwid, durationMonths) {
  const cleanHwid = hwid.replace(/-/g, '').toUpperCase();
  
  if (cleanHwid.length !== 8) {
    throw new Error("Invalid HWID format. Expected 8 characters.");
  }
  
  // Calculate expiration (Days since Jan 1, 2024)
  const EPOCH = new Date('2024-01-01T00:00:00Z').getTime();
  const currentDays = Math.floor((Date.now() - EPOCH) / (1000 * 60 * 60 * 24));
  
  const durationDays = durationMonths * 30; // Approx 30 days per month
  const expiryDays = currentDays + durationDays;
  
  // Expiry days to hex (4 chars)
  const expiryHex = expiryDays.toString(16).padStart(4, '0').toUpperCase();
  
  // Signature
  const fullHash = await sha256(`${cleanHwid}${expiryDays}${SECRET_SALT}`);
  const signature = fullHash.substring(0, 8).toUpperCase();
  
  const unlockCode = `${expiryHex}${signature}`;
  
  // Format for easy reading: AAAA-BBBB-CCCC
  const formattedCode = unlockCode.match(/.{1,4}/g)?.join('-') || unlockCode;
  
  // Save to history log
  await addToHistory(cleanHwid, formattedCode, durationMonths);
  
  return formattedCode;
}

// Manage History
export async function getHistory() {
  const { value } = await Preferences.get({ key: 'keygenHistory' });
  return value ? JSON.parse(value) : [];
}

async function addToHistory(hwid, code, months) {
  const history = await getHistory();
  history.unshift({
    hwid,
    code,
    months,
    date: new Date().toISOString()
  });
  // Keep last 100 entries
  if (history.length > 100) history.length = 100;
  
  await Preferences.set({ key: 'keygenHistory', value: JSON.stringify(history) });
}
