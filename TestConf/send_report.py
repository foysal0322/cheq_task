import requests
import inspect

# Discord Webhook URL (Replace with your webhook)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1351086319815888916/GkSxw4XAuJDCeshqZ95GBLYiwwgk7VCv3LFL7qDsPBIqXebwBshikJd8HcJm-9OT0H6B"


def send_discord_notification(message):
    """Send a message to Discord via Webhook."""
    data = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("✅ Report sent successfully to Discord!")
    else:
        print(f"❌ Failed to send report: {response.status_code} - {response.text}")


# Example Usage

