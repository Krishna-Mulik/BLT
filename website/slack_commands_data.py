SLACK_COMMANDS = {
    "discover": {
        "command": "/discover",
        "description": (
            "Discover OWASP and BLT projects to work on. Returns a curated "
            "list of projects with descriptions, tech stack and tags."
        ),
        "examples": ["/discover blt"],
    },
    "contrib": {
        "command": "/contrib",
        "description": (
            "Show a guided checklist for contributing to OWASP projects: how to join "
            "Slack channels, find project channels, read pinned messages, pick issues "
            "and coordinate with project leaders."
        ),
        "examples": ["/contrib"],
    },
    "gsoc25": {
        "command": "/gsoc25",
        "description": (
            "Get key information about OWASP Google Summer of Code 2025, "
            "including links to ideas, projects and mentors. You can filter "
            "by technology, mentor or project topic."
        ),
        "examples": [
            "/gsoc25 python",
            "/gsoc25 javascript",
            "/gsoc25 mentor:donnie",
        ],
    },
    "blt": {
        "command": "/blt",
        "description": (
            "User profiles — get the OWASP profile for a specific GitHub user."
            "View information about OWASP chapters."
            "Discover OWASP projects and explore where to contribute."
            "Explore OWASP GSoC projects and ideas."
            "Get details on upcoming OWASP events."
            "View information about OWASP committees."
        ),
        "examples": [
            "/blt user krishnamulik",
            "/blt chapters",
            "/blt projects",
            "/blt gsoc",
            "/blt gsoc python",
            "/blt events",
            "/blt committees",
        ],
    },
    "help": {
        "command": "/help",
        "description": "Show the list of available Slack bot commands.",
        "examples": ["/help"],
    },
    "report": {
        "command": "/report",
        "description": ("Report a bug or issue directly from Slack. Creates an issue with the provided description."),
        "examples": [
            "/report Signup page crashes when clicking submit",
            "/report Unable to connect Slack bot to BLT workspace",
        ],
    },
    "stats": {
        "command": "/stats",
        "description": (
            "Show OWASP platform statistics such as project counts, issues, users, domains and overall activity."
        ),
        "examples": ["/stats"],
    },
}
