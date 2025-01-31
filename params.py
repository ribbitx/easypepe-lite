import os

from dotenv import load_dotenv

load_dotenv()

RPC_USER = os.getenv("RPC_USER")
RPC_PASSWORD = os.getenv("RPC_PASSWORD")
RPC_HOST = os.getenv("RPC_HOST", "127.0.0.1")
RPC_PORT = os.getenv("RPC_PORT", "33873")
RPC_URL = f"http://{RPC_USER}:{RPC_PASSWORD}@{RPC_HOST}:{RPC_PORT}"
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = os.getenv("API_PORT", "4555")
headers = {"content-type": "application/json"}
