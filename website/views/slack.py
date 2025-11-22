import os

from django.shortcuts import render

from website.slack_commands_data import SLACK_COMMANDS


def slack_landing_page(request):
    """
    Landing page for Slack integration:
    - Explains what the BLT Slack bot does
    - Provides an \"Add to Slack\" button that triggers OAuth
    """

    # Read Slack client ID from environment
    client_id = os.environ.get("SLACK_CLIENT_ID", "")

    slack_oauth_url = ""
    if client_id:
        # Basic OAuth URL – scopes may be adjusted later by maintainers
        slack_oauth_url = (
            "https://slack.com/oauth/v2/authorize"
            f"?client_id={client_id}"
            "&scope=commands,chat:write,im:history,im:write,users:read"
            "&user_scope="
        )

    context = {"slack_oauth_url": slack_oauth_url, "slack_commands": SLACK_COMMANDS}
    return render(request, "slack/index.html", context)
