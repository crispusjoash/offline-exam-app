/** @type {import('electron-builder').Configuration} */
module.exports = {
  appId: 'com.cbc.offlineexam',
  productName: 'CBC Portal',
  electronDist: 'node_modules/electron/dist',
  directories: {
    output: 'build_output',
    buildResources: 'assets',
  },
  files: [
    'build/**/*',
    'app/**/*',
    'generated/**/*',
    'package.json',
    // Platform runtime + plugins, prepared by `capacitor-electron vendor`.
    { from: 'vendor/node_modules', to: 'node_modules' },
  ],
  win: {
    target: ['nsis']
  },
  nsis: {
    oneClick: false,
    perMachine: false,
    allowToChangeInstallationDirectory: true,
    createDesktopShortcut: true,
    createStartMenuShortcut: true,
    shortcutName: 'CBC Portal Premium'
  }
};
