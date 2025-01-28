# EasyPepe Lite API (Beta)

EasyPepe Lite API is a lightweight and experimental API designed to interact with the PepeCoin Core blockchain. It provides endpoints for retrieving blockchain data, simplifying the development of applications that need to communicate with the PepeCoin network. This version is a demo and beta preview, with the full EasyPepe API coming soon.

---

## Features

- **Lightweight:** Minimal dependencies and easy to set up.
- **Endpoints:** Access blockchain data such as difficulty, block count, transaction details, and more.
- **Customizable:** Allows easy configuration of RPC settings.

---

## Requirements

- **Python 3.7+**
- **Flask**
- **Requests**
- A running instance of **PepeCoin Core** with RPC enabled

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd easypepe-lite-api
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask requests
   ```

4. **Ensure PepeCoin Core is running** with RPC enabled. Update the configuration file (`pepecoin.conf`) with:
   ```
   rpcuser=your_rpc_user
   rpcpassword=your_rpc_password
   rpcallowip=127.0.0.1
   rpcport=8332
   ```

---

## First-Time Setup

When you run the API for the first time, it will prompt you to enter your RPC credentials:

```bash
python api.py
```

You will be asked to provide:
- **RPC Username**
- **RPC Password**
- **RPC Host** (default: `127.0.0.1`)
- **RPC Port** (default: `8332`)

These credentials are used to connect to your PepeCoin Core instance. They can also be set as environment variables:

```bash
export RPC_USER=your_rpc_user
export RPC_PASSWORD=your_rpc_password
export RPC_HOST=127.0.0.1
export RPC_PORT=8332
```

---

## Usage

Run the API:
```bash
python api.py
```

The API will be available at `http://localhost:5000`. You can use tools like `curl`, Postman, or your web browser to test the endpoints.

---

## API Endpoints

### 1. `/api/getdifficulty`
Returns the current mining difficulty.

### 2. `/api/getconnectioncount`
Returns the number of connections to other nodes.

### 3. `/api/getblockcount`
Returns the current block count.

### 4. `/api/getblockhash/<index>`
Returns the block hash for a given block index.

Example:
```bash
GET /api/getblockhash/1000
```

### 5. `/api/getblock/<block_hash>`
Returns detailed information about a block.

Example:
```bash
GET /api/getblock/000000000000...
```

### 6. `/api/getrawtransaction/<txid>`
Returns detailed information about a transaction.

Example:
```bash
GET /api/getrawtransaction/txid_here
```

### 7. `/api/getnetworkhashps`
Returns the estimated network hashes per second.

### 8. `/api/getmoneysupply`
Returns the total money supply.

### 9. `/api/getdistribution`
Returns the coin distribution.

### 10. `/api/gettx/<txid>`
Returns details about a transaction by ID.

### 11. `/api/getnetworkpeers`
Returns a list of connected peers.

---

## Notes

- **Beta Notice:** This API is a beta version and is meant for demonstration purposes only. The full EasyPepe API will include more features and enhancements.
- **Security:** Do not expose your RPC credentials or this API to the public without proper security measures in place.

---

## Troubleshooting

1. **Dependency Issues:** Ensure all dependencies are installed with `pip install flask requests`.
2. **Connection Errors:** Check if PepeCoin Core is running and RPC is enabled with the correct settings.
3. **Invalid Credentials:** Double-check the RPC username and password in your configuration.

---

## Contribution

Contributions are welcome! Submit issues and pull requests to improve the API.

---

## License

This project is released under the MIT License.

---

For further questions, stay tuned for the full EasyPepe API release.

