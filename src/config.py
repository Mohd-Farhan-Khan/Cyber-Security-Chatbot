import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration settings
def get_api_key():
    """Get the Google API key from environment variables"""
    return os.getenv("GOOGLE_API_KEY")

def validate_api_key():
    """Validate that API key is set and not the default placeholder"""
    api_key = get_api_key()
    if not api_key or api_key == "YOUR_NEW_API_KEY_HERE":
        return False
    return True
