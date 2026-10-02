"""Asante Adaduanan — 42-day cycle, West Africa."""
from datetime import date, timedelta
from mcp.server.fastmcp import FastMCP


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def start_asante_cycle(start_date: str | None = None) -> dict:
        """Start (or resume) a 42-day Adaduanan planning cycle.

        Args:
            start_date: ISO date (YYYY-MM-DD). Defaults to today.
        """
        start = date.fromisoformat(start_date) if start_date else date.today()
        end = start + timedelta(days=41)
        return {
            "technique": "asante_cycle",
            "start": start.isoformat(),
            "end": end.isoformat(),
            "total_days": 42,
            "weeks": 6,
            "message": "Six weeks to a goal. Review weekly, honour the cycle.",
        }

    @mcp.tool()
    async def get_cycle_day(cycle_start: str, today: str | None = None) -> dict:
        """Return the current day number within a 42-day Asante cycle."""
        start = date.fromisoformat(cycle_start)
        now = date.fromisoformat(today) if today else date.today()
        day = (now - start).days + 1
        return {
            "cycle_start": cycle_start,
            "today": now.isoformat(),
            "day_number": day,
            "day_of_42": ((day - 1) % 42) + 1,
            "week": ((day - 1) // 7) + 1,
        }
