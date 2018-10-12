# -*- mode: python -*-

block_cipher = None


a = Analysis(['visitoolkit_psc2alm\\psc2alm.py'],
             pathex=['C:\\Users\\Asenta\\PycharmProjects\\visitoolkit_psc2alm'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='visitoolkit_psc2alm_v0.0.1_x86',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='visitoolkit_psc2alm_v0.0.1_x86')
