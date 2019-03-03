# Run 'python setup.py build' on cmd

import sys
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

options = {
    'build_exe': {
        'include_files': [
            'bg_music.wav',
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('game.py')
]

setup(name='Arkanoid',
      version='1.0',
      description='Python Game',
      options=options,
      executables=executables
      )
