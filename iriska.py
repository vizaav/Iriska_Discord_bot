from discord.app_commands import AppCommand
from hikari import Intents
from lightbulb import BotApp, command, implements, PrefixCommand, Context, SlashCommand
from dotenv import load_dotenv
import os
import random

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = BotApp(token=DISCORD_TOKEN, prefix="=", intents=Intents.ALL)


# Register the command to the bot
@bot.command
# Use the command decorator to convert the function into a command
@command("ping", "checks the bot is alive")
# Define the command type(s) that this command implements
@implements(PrefixCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.Context when passed in
@implements(SlashCommand)
async def ping(ctx: Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("Pong!")
    await ctx.get_channel().send("$8 am i gay?")


@bot.command
@command("hello", "says hello")
@implements(PrefixCommand)
@implements(SlashCommand)
async def hello(ctx: Context) -> None:
    await ctx.get_channel().send("world")


@bot.command
@command("bully", "bully")
@implements(PrefixCommand)
@implements(SlashCommand)
async def bully(ctx: Context) -> None:
    await ctx.get_channel().send("$contact hello")


@bot.command
@command("8", "zapytaj")
@implements(PrefixCommand)
@implements(SlashCommand)
async def zapytaj(ctx: Context) -> None:
    responses = ["Zdecydowanie tak", "Nie mam żadnych wątpliwości", "Nigdy w to nie wątpiłam", "Jest to pewne", "Tak",
                 "Tak - zdecydowanie", "Nie licz na to", "Moja odpowiedź brzmi nie", "Moje źródła mówią nie",
                 "Absolutnie nie", "Absolutnie tak", "Jak mogłeś w to wątpić?",
                 "Czemu zadajesz takie oczywiste pytania? Oczywiście, że tak!"]
    await ctx.get_channel().send(random.choice(responses))


# Run the bot
# Note that this is blocking meaning no code after this line will run
# until the bot is shut off
if __name__ == '__main__':
    bot.run()
