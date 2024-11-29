# Discord TruthSeeker BOT

This bot was created originally to help me exposed uncover hidden actions and expose dishonest behaviors. Specifically, it assists in exposing actions of individuals who may have betrayed or wronged you, such as personal relationships. The bot fetches audit logs and identifies suspicious activities on a Discord server, helping you understand the truth behind actions.

### Features
- Fetches recent audit logs from the server.
- Checks permissions to view audit logs.
- Sends simple responses when triggered with specific commands (e.g., `!hello`).

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Discord-TruthSeeker-BOT.git

2. **Install dependencies**:
   Make sure to install the necessary Python packages:
   ```bash
   pip install discord python-dotenv

3. **Set up environment variables**:
   Create a .env file in the root directory and add your bot token and user ID:
   ```bash
   YOUR_USER_ID=your_user_id_here
   DISCORD_BOT_TOKEN=your_bot_token_here

4. **Run the bot**:
   Execute the bot by running the Python script:
   ```bash
   python bot.py

### How to Use:

- **Command**: The bot responds to the `!hello` message by greeting the user.
- **Audit Log Fetching**: The bot checks for recent audit logs and prints them in the console if it has the necessary permissions.

By following the above steps and using the `.env` file for sensitive credentials, this bot ensures your information remains secure while allowing others to use and customize it.
