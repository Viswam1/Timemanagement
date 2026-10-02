"""Greco-Roman daily routine builder."""
from mcp.server.fastmcp import FastMCP


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def build_graeco_roman_routine(goal: str) -> dict:
        """Build a day inspired by Aristotle, Plato and Cicero.

        Args:
            goal: The single thing you want the day to serve.
        """
        return {
            "technique": "greco_roman",
            "goal": goal,
            "blocks": [
                {"name": "Dawn — Lectio", "duration_min": 30,
                 "detail": "Read something difficult. No screens."},
                {"name": "Morning — Disputatio", "duration_min": 120,
                 "detail": f"Argue with the problem: {goal}"},
                {"name": "Midday — Gymnasium", "duration_min": 45,
                 "detail": "Walk, exercise, let the mind idle."},
                {"name": "Afternoon — Compositio", "duration_min": 120,
                 "detail": "Turn thinking into artefacts."},
                {"name": "Evening — Examinatio", "duration_min": 20,
                 "detail": "Review the day in writing. What would Seneca say?"},
            ],
        }

    @mcp.tool()
    async def stoic_reflection(prompt: str) -> dict:
        """Return a Stoic reflection prompt for the day."""
        return {
            "technique": "greco_roman",
            "prompt": prompt,
            "questions": [
                "What is within my control today?",
                "What is outside it, and can I let it go?",
                "What would virtue look like in this next hour?",
            ],
        }
