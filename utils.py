import requests
from params import *


def call_rpc(method: str, params: list | None = None) -> dict:
    if params is None:
        params = []

    payload = {
        "jsonrpc": "1.0",
        "id": "curltext",
        "method": method,
        "params": params
    }

    try:
        response = requests.post(RPC_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "error" in data and data["error"] is not None:
            return {"error": "RPC error occurred."}

        return {"result": data["result"]}
    except requests.exceptions.RequestException:
        return {"error": "Failed to communicate with the RPC server."}
