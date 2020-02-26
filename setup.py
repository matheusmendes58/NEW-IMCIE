import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
executables = [Executable("NEW IMCIE.py", base=base)]

buildOptions = dict(packages=[],
                    includes=[],
                    include_files=["icon.ico", "newimc.png"],
                    excludes=[])
setup(
    name='NEWIMCIE',
    version='1.0.0',
    description='Calculadora de imc',
    options=dict(build_exe=buildOptions),
    executables=executables
)