import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { VitePWA } from 'vite-plugin-pwa'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  base: './',
  plugins: [
    react(),
    tailwindcss(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.svg', 'assets/images/*.webp'],
      manifest: {
        name: 'CBC Offline Exam Portal',
        short_name: 'CBC Portal',
        description: 'Offline CBC Exam application for students.',
        theme_color: '#ffffff',
        background_color: '#f8fafc',
        display: 'standalone',
      },
      // Disable service worker in dev — prevents caching issues where old
      // apps served on the same port get intercepted and served indefinitely
      devOptions: {
        enabled: false,
      }
    })
  ],
  resolve: {
    alias: {
      crypto: path.resolve(__dirname, 'src/crypto-polyfill.js')
    }
  },
  optimizeDeps: {
    exclude: ['jeep-sqlite', 'sql.js']
  }
})
