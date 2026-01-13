#!/usr/bin/env python3
"""
Calculator Server Wrapper

This wrapper adds vendored dependencies to the Python path before importing
the actual server code. This allows the server to run with pre-bundled
dependencies without requiring manual pip install.
"""

import sys
import os

# Add vendored dependencies to path
vendor_dir = os.path.join(os.path.dirname(__file__), 'vendored')
if os.path.exists(vendor_dir):
    sys.path.insert(0, vendor_dir)

# Import and run the actual server
from server import main

if __name__ == "__main__":
    main()
