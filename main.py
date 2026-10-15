#!/usr/bin/env python3
"""Android entry point for pyside6-android-deploy.

The tool requires the main script to be named main.py.
This simply delegates to the normal run.py logic.
"""
import os
import sys

# Ensure project root is on the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules import core

if __name__ == "__main__":
    core.run()
