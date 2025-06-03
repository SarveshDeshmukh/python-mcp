# server.py
from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("AI Sticky Notes")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_FILE_PATH = os.path.join(SCRIPT_DIR, "notes.txt")

def ensure_notes_file():
    """Ensure that the notes.txt file exists."""
    if not os.path.exists(NOTES_FILE_PATH):
        with open(NOTES_FILE_PATH, "w") as f:
            f.write("")

@mcp.tool()
def add_note(note: str) -> str:
    """Add a sticky note with the given text to the notes.txt file."""
    ensure_notes_file()
    print("NOTE FILE PATH:", NOTES_FILE_PATH)
    with open(NOTES_FILE_PATH, "a") as f:
        f.write(note + "\n")
    
    return f"Note saved: {note}"

