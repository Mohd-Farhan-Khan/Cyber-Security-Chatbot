import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "AIzaSyB73DvTX0xvV9YrgGFECD7JPM_PyafeDfY")
