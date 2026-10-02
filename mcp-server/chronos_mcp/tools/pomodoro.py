"""Pomodoro Technique — Francesco Cirillo, Italy, 1980s."""
from mcp.server.fastmcp import FastMCP
from loguru import logger


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def start_pomodoro(task: str, duration_minutes: int = 25) -> dict:
        """Start a Pomodoro focus session for the given task."""
        logger.info(f"Pomodoro start: task={task!r} duration={duration_minutes}m")
        return {
            "technique": "pomodoro",
            "task": task,
            "focus_minutes": duration_minutes,
            "break_minutes": 5,
            "message": f"Focus on '{task}' for {duration_minutes} minutes. Tomato time! 🍅",
        }

    @mcp.tool()
    async def complete_pomodoro(task: str, completed: bool = True) -> dict:
        """Log a finished Pomodoro session and recommend the next break."""
        return {
            "technique": "pomodoro",
            "task": task,
            "completed": completed,
            "next_break_minutes": 5 if completed else 0,
            "message": "Great work. Step away for 5 minutes — stretch, hydrate, breathe.",
        }
