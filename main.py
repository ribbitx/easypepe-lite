from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

rpc_user = os.getenv("RPC_USER", "")
rpc_password = os.getenv("RPC_PASSWORD", "")
rpc_host = os.getenv("RPC_HOST", "127.0.0.1")
rpc_port = os.getenv("RPC_PORT", "8332")
rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"

def setup_rpc_info():
    global rpc_user, rpc_password, rpc_host, rpc_port, rpc_url
    print("Welcome to EasyPepe Lite API Setup")
    rpc_user = input("Enter RPC username: ")
    rpc_password = input("Enter RPC password: ")
    rpc_host = input("Enter RPC host (default 127.0.0.1): ") or "127.0.0.1"
    rpc_port = input("Enter RPC port (default 8332): ") or "8332"
    rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"

def call_rpc(method, params=[]):
    headers = {"content-type": "application/json"}
    payload = {"jsonrpc": "1.0", "id": "curltext", "method": method, "params": params}
    response = requests.post(rpc_url, json=payload, headers=headers)
    return response.json()

@app.route("/api/getdifficulty", methods=["GET"])
def get_difficulty():
    return jsonify(call_rpc("getdifficulty"))

@app.route("/api/getconnectioncount", methods=["GET"])
def get_connection_count():
    return jsonify(call_rpc("getconnectioncount"))

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
    return jsonify(call_rpc("getrawtransaction", [txid, 1]))

@app.route("/api/getnetworkhashps", methods=["GET"])
def get_network_hash_ps():
    return jsonify(call_rpc("getnetworkhashps"))

@app.route("/api/getmoneysupply", methods=["GET"])
def get_money_supply():
    return jsonify(call_rpc("getmoneysupply"))

@app.route("/api/getdistribution", methods=["GET"])
def get_distribution():
    return jsonify(call_rpc("getdistribution"))

@app.route("/api/gettx/<string:txid>", methods=["GET"])
def get_tx(txid):
    return jsonify(call_rpc("gettx", [txid]))

@app.route("/api/getnetworkpeers", methods=["GET"])
def get_network_peers():
    return jsonify(call_rpc("getpeerinfo"))

if __name__ == "__main__":
    if not all([rpc_user, rpc_password]):
        setup_rpc_info()
    app.run(host="0.0.0.0", port=5000)
