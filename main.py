# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "tcppinglib",
#     "uvicorn","pydantic",
#     "pydantic-extra-types",
# ]
# ///
from ipaddress import IPv4Address

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel , PositiveInt
from tcppinglib import async_tcpping , TCPHost

app = FastAPI ( docs_url = '/', redoc_url = None, swagger_ui_oauth2_redirect_url = None )


class ResultPing ( BaseModel ) :
	avg_rtt: float
	ip_address: IPv4Address
	is_alive: bool
	max_rtt: float
	min_rtt: float
	packet_loss: float
	packets_received: int
	packets_sent: int
	port: int
	stddev_rtt: float


@app.get ( '/ping' , response_model = ResultPing )
async def ping ( address: IPv4Address , port: PositiveInt , interval: float = .5 , count: int = 2 ) -> TCPHost :
	host = await async_tcpping ( address.exploded , count = count , interval = interval , port = port )
	return host


if __name__ == "__main__" :
	uvicorn.run ( "main:app" , port = 8000 , log_level = "info" )
