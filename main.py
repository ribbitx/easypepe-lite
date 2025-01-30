import os
from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv

load_dotenv()

RPC_USER = os.getenv("RPC_USER")
RPC_PASSWORD = os.getenv("RPC_PASSWORD")
RPC_HOST = os.getenv("RPC_HOST", "127.0.0.1") 
RPC_PORT = os.getenv("RPC_PORT", "33873")  
RPC_URL = f"http://{RPC_USER}:{RPC_PASSWORD}@{RPC_HOST}:{RPC_PORT}"

if not RPC_USER or not RPC_PASSWORD:
    print("RPC_USER or RPC_PASSWORD not set. Exiting.")
    exit(1)

print(f"Connecting to RPC server at {RPC_URL}")

app = Flask(__name__)

def call_rpc(method, params=[]):
    headers = {"content-type": "application/json"}
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
    except requests.exceptions.RequestException as e:

        return {"error": "Failed to communicate with the RPC server."}

@app.route("/api/network/info", methods=["GET"])
def get_network_info():
    return jsonify(call_rpc("getnetworkinfo"))

@app.route("/api/blockchain/info", methods=["GET"])
def get_blockchain_info():
    return jsonify(call_rpc("getblockchaininfo"))

@app.route("/api/mempool/info", methods=["GET"])
def get_mempool_info():
    return jsonify(call_rpc("getmempoolinfo"))

@app.route("/api/getblockcount", methods=["GET"])
def get_block_count():
    return jsonify(call_rpc("getblockcount"))

@app.route("/api/getblockhash/<int:index>", methods=["GET"])
def get_block_hash(index):
    return jsonify(call_rpc("getblockhash", [index]))

@app.route("/api/getblock/<string:block_hash>", methods=["GET"])
def get_block(block_hash):
    return jsonify(call_rpc("getblock", [block_hash]))

@app.route("/api/getrawtransaction/<string:txid>", methods=["GET"])
def get_raw_transaction(txid):
    return jsonify(call_rpc("getrawtransaction", [txid, True]))

@app.route("/api/tx/<string:txid>", methods=["GET"])
def get_transaction(txid):
    return jsonify(call_rpc("getrawtransaction", [txid, True]))

@app.route("/api/getnetworkhashps", methods=["GET"])
def get_network_hash_ps():
    return jsonify(call_rpc("getnetworkhashps"))

@app.route("/api/peerinfo", methods=["GET"])
def get_peer_info():
    return jsonify(call_rpc("getpeerinfo"))

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=4555)
