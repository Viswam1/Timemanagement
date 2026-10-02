"""Read-only resources exposing technique metadata."""
from mcp.server.fastmcp import FastMCP

TECHNIQUES = {
    "pomodoro": {
        "name": "Pomodoro Technique",
        "origin": "Italy, 1980s",
        "author": "Francesco Cirillo",
        "summary": "25-minute focus blocks separated by 5-minute breaks.",
        "accent": "#e63946",
    },
    "qin_han": {
        "name": "Qin/Han Workday",
        "origin": "China, 221 BCE – 220 CE",
        "summary": "A structured 5AM–5PM day used by imperial officials.",
        "accent": "#d4a017",
    },
    "asante_cycle": {
        "name": "Asante Adaduanan",
        "origin": "West Africa, Asante Empire",
        "summary": "A 42-day cyclical planning rhythm combining 6- and 7-day weeks.",
        "accent": "#2a9d8f",
    },
    "egyptian_flow": {
        "name": "Egyptian Water Clock",
        "origin": "Ancient Egypt",
        "summary": "Deep, uninterrupted flow timed like water emptying from a vessel.",
        "accent": "#1e6fbf",
    },
    "greco_roman": {
        "name": "Greco-Roman Routine",
        "origin": "Greece & Rome, classical antiquity",
        "summary": "A day shaped by lectio, disputatio, gymnasium and examinatio.",
        "accent": "#8d99ae",
    },
}


def register(mcp: FastMCP) -> None:

    @mcp.resource("chronos://techniques")
    def list_techniques() -> dict:
        """List all historical techniques Chronos supports."""
        return TECHNIQUES

    @mcp.resource("chronos://techniques/{slug}")
    def get_technique(slug: str) -> dict:
        """Get a single technique's metadata by slug."""
        return TECHNIQUES.get(slug, {"error": "not found", "slug": slug})
