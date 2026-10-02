"""Entry point for the Chronos MCP server."""
from mcp.server.fastmcp import FastMCP
from loguru import logger

from chronos_mcp.tools import (
    pomodoro,
    qin_han,
    asante_cycle,
    egyptian_flow,
    greco_roman,
)
from chronos_mcp import resources, prompts

mcp = FastMCP("chronos")

pomodoro.register(mcp)
qin_han.register(mcp)
asante_cycle.register(mcp)
egyptian_flow.register(mcp)
greco_roman.register(mcp)

resources.register(mcp)
prompts.register(mcp)


if __name__ == "__main__":
    logger.info("Chronos MCP server starting…")
    mcp.run()
