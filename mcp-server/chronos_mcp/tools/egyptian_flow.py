"""Egyptian water-clock inspired flow timer."""
from mcp.server.fastmcp import FastMCP


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def start_flow(intent: str, minutes: int = 90) -> dict:
        """Begin a water-clock flow session: deep, uninterrupted work.

        Args:
            intent: What you will work on.
            minutes: Duration (default 90 — one full water-clock pour).
        """
        return {
            "technique": "egyptian_flow",
            "intent": intent,
            "minutes": minutes,
            "message": (
                f"Let the water flow for {minutes} minutes. No tabs, no pings — "
                f"only '{intent}'. When the last drop falls, you stop."
            ),
        }

    @mcp.tool()
    async def end_flow(intent: str, what_was_done: str) -> dict:
        """Log the end of a flow session."""
        return {
            "technique": "egyptian_flow",
            "intent": intent,
            "outcome": what_was_done,
            "message": "The vessel is empty. Rest before you refill it.",
        }
