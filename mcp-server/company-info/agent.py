#!/usr/bin/env python3
"""Simple agent that calls the Company Info MCP server using FastMCP client.

Usage:
  uv run agent.py
"""
import asyncio
import os
from fastmcp.client import Client, StreamableHttpTransport


async def main():
  host = os.getenv("HOST", "127.0.0.1")
  port = int(os.getenv("PORT", "8081"))
  base_url = f"http://{host}:{port}/mcp"

  transport = StreamableHttpTransport(url=base_url)
  async with Client(transport=transport) as client:
    # Call tools by name
    location = await client.call_tool("get_company_location", {"company_name": "Acxiom"})
    print("Location result:\n", location)

    details = await client.call_tool("get_company_details", {"company_name": "Allied Van Lines"})
    print("Details result:\n", details)

if __name__ == "__main__":
  try:
    asyncio.run(main())
  except Exception as e:
    print(f"Agent error: {e}")
