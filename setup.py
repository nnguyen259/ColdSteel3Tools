from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['frames', 'packer', 'randomizer', 'ref', 'schema', 'unpacker'], excludes = [])

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(script = 'cs3Tools.py', base=base, targetName = 'CS3Tools', icon = 'icon.ico')
]

setup(name='ColdSteel3Tools',
      version = '1.0',
      description = 'Modding Tool for Trails of Cold Steel 3',
      options = dict(build_exe = buildOptions),
      executables = executables)