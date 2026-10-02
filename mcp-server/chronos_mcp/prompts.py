"""Optional prompt templates for the LLM."""
from mcp.server.fastmcp import FastMCP


def register(mcp: FastMCP) -> None:

    @mcp.prompt()
    def plan_day(goal: str, energy: str = "medium") -> str:
        """Prompt the LLM to design a day using Chronos techniques."""
        return (
            f"You are Chronos, a time-management coach versed in historical "
            f"methods (Pomodoro, Qin/Han, Asante Adaduanan, Egyptian water clock, "
            f"Greco-Roman routines). The user's goal is: {goal}. Their energy is "
            f"{energy}. Recommend 1–2 techniques, explain why, and give a "
            f"concrete schedule for today."
        )

    @mcp.prompt()
    def reflect(day_summary: str) -> str:
        """Prompt for a Stoic end-of-day reflection."""
        return (
            f"Here is what the user did today: {day_summary}. Ask three Stoic "
            f"reflection questions and suggest one adjustment for tomorrow."
        )
