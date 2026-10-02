"""Qin/Han 16-hour workday — Ancient China."""
from mcp.server.fastmcp import FastMCP


SEGMENTS = [
    ("05:00", "Morning review & planning"),
    ("07:00", "Primary deep work block"),
    ("11:00", "Midday meal & rest"),
    ("13:00", "Secondary work block"),
    ("16:00", "Correspondence & reporting"),
    ("17:00", "Day closes — reflect and rest"),
]


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def get_qin_han_schedule() -> dict:
        """Return the traditional Qin/Han 5AM–5PM structured workday."""
        return {
            "technique": "qin_han",
            "era": "Qin–Han dynasty, China (221 BCE – 220 CE)",
            "segments": [{"time": t, "activity": a} for t, a in SEGMENTS],
        }

    @mcp.tool()
    async def plan_qin_han_day(priority_task: str) -> dict:
        """Plan a Qin/Han-style day around a single priority task."""
        return {
            "technique": "qin_han",
            "priority_task": priority_task,
            "plan": [
                {"time": "05:00", "activity": f"Review the day; define success for: {priority_task}"},
                {"time": "07:00", "activity": f"Deep work block 1 — advance {priority_task}"},
                {"time": "11:00", "activity": "Meal, walk, and mental reset"},
                {"time": "13:00", "activity": f"Deep work block 2 — refine {priority_task}"},
                {"time": "16:00", "activity": "Wrap up, reply to messages, tidy loose ends"},
                {"time": "17:00", "activity": "Close the day — journal one sentence of progress"},
            ],
        }
