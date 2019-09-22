# -*- mode: python -*-

block_cipher = None


a = Analysis(['Money_for_a_payphone.py'],
             pathex=['C:\\Users\\willi\\Desktop\\ICS_whatever\\assignment_school\\WRIT_39B'],
             binaries=[],
             datas=[('C:\\Users\\willi\\Desktop\\ICS_whatever\\assignment_school\\WRIT_39B\\game_assets','game_assets')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Money_for_a_payphone',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\willi\\Desktop\\ICS_whatever\\assignment_school\\WRIT_39B\\game_assets\\circle_char_icon.ico')
