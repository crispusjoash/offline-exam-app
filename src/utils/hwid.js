import { Device } from '@capacitor/device';
import { Preferences } from '@capacitor/preferences';

const SECRET_SALT = 'OfflineExamSecret@2026';

// Generates an SHA-256 hash and returns it as a hex string
export async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

// Format a long string into blocks of 4 characters: AAAA-BBBB-CCCC
function formatCode(str) {
  return str.toUpperCase().match(/.{1,4}/g)?.join('-') || str;
}

// Fetch the unique device HWID
export async function getDeviceHWID() {
  const info = await Device.getId();
  let rawId = info.identifier;
  
  // Hash the raw UUID so the HWID is uniform and hides the actual UUID format
  const fullHash = await sha256(rawId + "HWID_SALT");
  const hwid = fullHash.substring(0, 8); // 8 characters for HWID (e.g. A1B2-C3D4)
  return formatCode(hwid); 
}

// Unlock code structure: [4 chars (Expiry Days in Hex)] - [8 chars (Signature)]
// e.g., 01A4-F8B2-9C1D

// Validate the unlock code against the device's HWID
export async function validateUnlockCode(code) {
  const cleanCode = code.replace(/-/g, '').toUpperCase();
  
  if (cleanCode.length !== 12) {
    return { valid: false, error: 'Invalid code length. Must be 12 characters.' };
  }

  const expiryHex = cleanCode.substring(0, 4);
  const signature = cleanCode.substring(4, 12);
  
  const expiryDays = parseInt(expiryHex, 16);
  if (isNaN(expiryDays)) {
    return { valid: false, error: 'Invalid code format.' };
  }

  // Get current device HWID
  const hwid = (await getDeviceHWID()).replace(/-/g, '');
  
  // Recalculate signature
  const expectedHash = await sha256(`${hwid}${expiryDays}${SECRET_SALT}`);
  const expectedSignature = expectedHash.substring(0, 8).toUpperCase();

  if (signature !== expectedSignature) {
    return { valid: false, error: 'The unlock code is invalid for this device.' };
  }

  // Check expiration (Days since Jan 1, 2024)
  const EPOCH = new Date('2024-01-01T00:00:00Z').getTime();
  const currentDays = Math.floor((Date.now() - EPOCH) / (1000 * 60 * 60 * 24));

  if (currentDays >= expiryDays) {
    return { valid: false, error: 'The unlock code has expired.' };
  }

  // Valid and not expired!
  await Preferences.set({ key: 'activationData', value: JSON.stringify({ expiryDays, signature }) });
  
  return { valid: true, expiryDays, currentDays };
}

// Check if the app is currently activated (runs on boot)
export async function checkActivationStatus() {
  const { value } = await Preferences.get({ key: 'activationData' });
  if (!value) return { activated: false };
  
  try {
    const data = JSON.parse(value);
    const hwid = (await getDeviceHWID()).replace(/-/g, '');
    
    // Re-verify the signature in case they tampered with local storage
    const expectedHash = await sha256(`${hwid}${data.expiryDays}${SECRET_SALT}`);
    const expectedSignature = expectedHash.substring(0, 8).toUpperCase();
    
    if (data.signature !== expectedSignature) {
       return { activated: false };
    }

    // Check expiration
    const EPOCH = new Date('2024-01-01T00:00:00Z').getTime();
    const currentDays = Math.floor((Date.now() - EPOCH) / (1000 * 60 * 60 * 24));
    
    if (currentDays >= data.expiryDays) {
      // Clean up expired key
      await Preferences.remove({ key: 'activationData' });
      return { activated: false, error: 'Subscription expired.' };
    }

    const daysRemaining = data.expiryDays - currentDays;
    return { activated: true, daysRemaining };
  } catch (e) {
    return { activated: false };
  }
}
