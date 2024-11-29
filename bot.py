from dotenv import load_dotenv
import discord
import logging
import os

# Load environment variables from .env file
load_dotenv()

# Setting up logging for the bot
logging.basicConfig(level=logging.INFO)

# Create an instance of the client
intents = discord.Intents.default()
intents.message_content = True  # Allow bot to read messages

bot = discord.Client(intents=intents)

# Fetch sensitive data from environment variables
YOUR_USER_ID = os.getenv("YOUR_USER_ID")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    guild = bot.get_guild(796000399252652033)  # Replace with your actual guild ID

    if guild is None:
        print("Could not find the guild.")
        return

    # Check if the bot has permission to view audit logs
    if guild.me.guild_permissions.view_audit_log:
        print("Bot has permission to view audit logs.")

        # Fetch the audit logs (up to 10 most recent entries)
        try:
            async for entry in guild.audit_logs(limit=10):
                log_user = await bot.fetch_user(YOUR_USER_ID)
                print(f"Audit Log Entry: {entry} - Actioned by {entry.user} at {entry.created_at}")
        except discord.errors.Forbidden:
            print("Bot does not have the necessary permissions to fetch the audit logs.")
    else:
        print("Bot does not have the 'View Audit Log' permission.")

@bot.event
async def on_message(message):
    if message.content.lower() == "!hello":
        await message.channel.send(f"Hello, {message.author}!")

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
