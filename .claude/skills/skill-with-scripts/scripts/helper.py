#!/usr/bin/env python3
"""
Minimal helper script for skill-with-scripts demonstration.
Shows how skills can bundle executable code.
"""

import sys
import json
from datetime import datetime

def main():
    """Simple helper that outputs JSON with metadata."""
    result = {
        "message": "Hello from skill-with-scripts!",
        "timestamp": datetime.now().isoformat(),
        "python_version": sys.version.split()[0],
        "purpose": "Demonstrating that skills can execute scripts",
        "skill": "skill-with-scripts"
    }
    
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
