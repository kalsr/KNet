# python
# mcp_provider.py
"""
MCP Provider (FastAPI) - minimal but complete example.

Provides 2 tool endpoints:
 - POST /tools/check_ip_reputation
 - POST /tools/lookup_cve_sim

Requires API key in header: X-API-KEY
Logs every request/response to audit log file (mcp_audit.log).
"""

from fastapi import FastAPI, HTTPException, Header, Request
from pydantic import BaseModel, Field
from typing import List, Optional, Any
from datetime import datetime
import uvicorn
import json
import os
import logging
import random

# ----------------------
# Config
# ----------------------
API_KEY = os.environ.get("MCP_API_KEY", "test-api-key")  # override with real key in prod
AUDIT_LOG_PATH = os.environ.get("MCP_AUDIT_LOG", "mcp_audit.log")

# Setup file logger for audit
logger = logging.getLogger("mcp_audit")
logger.setLevel(logging.INFO)
fh = logging.FileHandler(AUDIT_LOG_PATH)
fh.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(fh)

app = FastAPI(title="MCP Provider (Demo)")

# ----------------------
# Request models
# ----------------------
class IPReputationRequest(BaseModel):
    ips: List[str] = Field(..., description="List of IP addresses to check")

class PackageItem(BaseModel):
    package: str
    version: Optional[str] = "0.0.0"

class CVELookupRequest(BaseModel):
    packages: List[PackageItem]

# ----------------------
# Helper: Audit log
# ----------------------
def audit_log(tool_name: str, input_payload: Any, output_payload: Any, client_ip: str = "unknown"):
    rec = {
        "timestamp": datetime.utcnow().isoformat(),
        "tool": tool_name,
        "client_ip": client_ip,
        "input": input_payload,
        "output": output_payload
    }
    logger.info(json.dumps(rec))

# ----------------------
# Simple API key check
# ----------------------
def verify_api_key(x_api_key: Optional[str]):
    if x_api_key is None or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

# ----------------------
# Tool endpoints
# ----------------------
@app.post("/tools/check_ip_reputation")
async def check_ip_reputation(
    payload: IPReputationRequest,
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    verify_api_key(x_api_key)
    ips = payload.ips
    MALICIOUS = {"203.0.113.5", "198.51.100.7", "192.0.2.77"}
    results = {}
    for ip in ips:
        if ip in MALICIOUS:
            results[ip] = {"reputation": "malicious", "score": 95}
        else:
            try:
                last = int(ip.split('.')[-1])
                score = (last % 20)
            except Exception:
                score = 5
            results[ip] = {"reputation": "clean", "score": score}
    out = {"results": results}
    client_ip = request.client.host if request.client else "unknown"
    audit_log("check_ip_reputation", payload.dict(), out, client_ip)
    return out

@app.post("/tools/lookup_cve_sim")
async def lookup_cve_sim(
    payload: CVELookupRequest,
    request: Request,
    x_api_key: Optional[str] = Header(None)
):
    verify_api_key(x_api_key)
    pkgs = payload.packages
    results = {}
    for p in pkgs:
        name = p.package
        if "legacy" in name or "openssl" in name:
            results[name] = {"cve_count": random.randint(1, 6)}
        else:
            results[name] = {"cve_count": random.randint(0, 2)}
    out = {"results": results}
    client_ip = request.client.host if request.client else "unknown"
    audit_log("lookup_cve_sim", payload.dict(), out, client_ip)
    return out

@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}

# ----------------------
# CLI entrypoint
# ----------------------
if __name__ == "__main__":
    uvicorn.run("mcp_provider:app", host="0.0.0.0", port=8000, reload=False)
