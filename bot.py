import os
from typing import Any

import discord
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
CHANNEL_NAME = "iriska"
PREFIX = "="  # Set the prefix for commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.message_content = True


class Client(discord.Client):
    def __init__(self, token: str, guild_name: str) -> None:
        super().__init__(intents=intents)
        self._token = token
        self._guild_name = guild_name
        self._guild = None

    def run(self, *args: Any, **kwargs: Any) -> None:
        super().run(self._token)

    async def on_ready(self) -> None:
        print(f"{self.user} has connected to Discord!")
        await self.wait_until_ready()  # Wait until the client is fully connected and ready
        print(f"{self.user} is ready!")
        for guild in self.guilds:
            print(f"Connected to guild: {guild.name}")
            channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
            if channel:
                await channel.send("Bot has logged in!")

    async def on_message(self, message: discord.Message):
        print(f"Message from {message.author}: {message.content} on channel {message.channel} in guild {message.guild}")
        if message.author == self.user:
            return
        if message.content.lower().startswith(PREFIX):
            # Remove the prefix from the message content
            command = message.content[len(PREFIX):].lower().strip()
            if command == "ping":
                print("ping")
                await message.channel.send("pong")
            elif command == "hello":
                print("hello")
                await message.channel.send("world")
            elif command == "bully the little guy":
                await message.channel.send("$contact hello")
            elif command.startswith("zapytaj iryska: "):
                await message.channel.send("$8 " + command.strip("zapytaj iryska: "))
            elif command.startswith("8"):
                responses = ["Zdecydowanie tak", "Nie mam żadnych wątpliwości", "Nigdy w to nie wątpiłam", "Jest to "
                                                                                                           "pewne"]


client = Client(DISCORD_TOKEN, DISCORD_GUILD)
client.run()
