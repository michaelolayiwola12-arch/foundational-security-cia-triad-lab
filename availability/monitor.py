#!/usr/bin/env python3

import requests
import sys
from datetime import datetime

URL = "http://localhost:8000"
TIMEOUT = 5

def check_service():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        response = requests.head(URL, timeout=TIMEOUT)
        
        if response.status_code == 200:
            print(f"[{timestamp}] Service Status: UP")
            sys.exit(0)
        else:
            print(f"[{timestamp}] Service Status: DOWN (Status: {response.status_code})")
            sys.exit(1)
    
    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] Service Status: DOWN")
        print(f"[{timestamp}] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_service()
