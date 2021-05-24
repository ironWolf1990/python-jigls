# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['gui.py'],
             pathex=['D:\\codebase\\python\\jigls'],
             binaries=[],
             datas=[],
             hiddenimports=["PyQt5.QtWidgets", "PyQt5.QtGui", "PyQt5.QtCore"],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='jigls',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
