import discord
import hikari.channels
from discord.app_commands import AppCommand
from hikari import Intents, GuildVoiceChannel, channels, guilds, snowflakes, Event, Member, Guild, Embed, Status

from dotenv import load_dotenv
import os
import random
import lightbulb
import csv


def assign_points(user, points):
    lines = []

    # Read existing data from the file
    with open("points.csv", "r") as file:
        reader = csv.reader(file)
        lines = list(reader)

    found = False
    for line in lines:
        if line[0] == str(user):
            line[1] = str(int(line[1]) + points)
            found = True
            break

    # Write updated data to the file
    with open("points.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

        # If the user was not found, add a new row
        if not found:
            writer.writerow([user, points])


def get_points(user):
    file = open("points.csv", "r")
    reader = csv.reader(file)
    lines = list(reader)
    file.close()
    for line in lines:
        print("line: " + line.__str__())
        if lines.__len__() == 0:
            return 0
        if line.__str__() == "":
            continue
        elif line[0] == user.__str__():
            points = line[1].__str__()
            user_login = line[0].__str__()
            return "Człowiek " + user_login + " ma " + points + " punkty miłości Iriski :heart:"
    return 0


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = lightbulb.BotApp(token=DISCORD_TOKEN, prefix="=", intents=Intents.ALL)


# Register the command to the bot
@bot.command
# Use the command decorator to convert the function into a command
@lightbulb.command("ping", "checks the bot is alive")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.PrefixCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.Context when passed in
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("Pong!")


@bot.command
@lightbulb.command("witaj", "says hello")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx: lightbulb.Context) -> None:
    await ctx.get_channel().send("Dzień dobry wszystkim! :heart:")


@bot.command
@lightbulb.command("bully", "bully")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def bully(ctx: lightbulb.Context) -> None:
    await ctx.get_channel().send("$contact hello")


@bot.command
@lightbulb.command("8", "zapytaj")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def zapytaj(ctx: lightbulb.Context) -> None:
    responses = ["Zdecydowanie tak", "Nie mam żadnych wątpliwości", "Nigdy w to nie wątpiłam", "Jest to pewne", "Tak",
                 "Tak - zdecydowanie", "Nie licz na to", "Moja odpowiedź brzmi nie", "Moje źródła mówią nie",
                 "Absolutnie nie", "Absolutnie tak", "Jak mogłeś w to wątpić?",
                 "Czemu zadajesz takie oczywiste pytania? Oczywiście, że tak!",
                 "Twoja stara"]
    await ctx.get_channel().send(random.choice(responses))


@bot.command
@lightbulb.command("dobranoc", "papa")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def dobranoc(ctx: lightbulb.Context) -> None:
    guild = ctx.get_guild()
    if guild is None:
        return await ctx.get_channel().send("Nie jesteś na serwerze")
    members = guild.get_members()
    if members is None:
        return await ctx.get_channel().send("Nie ma nikogo na serwerze")
    members = list(filter(lambda x: x, members))
    favorite = members[random.choice(range(0, members.__len__()))]
    favorite = guild.get_member(favorite)
    await ctx.get_channel().send(
        "Dobranoc kochani, życzę wam słodkich snów, a w szczególności mojemu kochanemu " + favorite.__str__() + ":heart:")


@bot.command
@lightbulb.command("trivia", "so trivial")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def trivia(ctx: lightbulb.Context) -> None:
    siedemnascie_ce = [307598226184339457, 615940700730687502, 433215903539396609, 517050226570297346,
                       296626554027507715, 207196996669407233, 285146237613899776, 272427120074948612,
                       572512848270327849, 235351337179545611, 218333108825489408, 362284256053035008,
                       503534440006549525, 226403255842766849, 379260996126244874, 383635450306232320,
                       285146237613899776]
    favorite = ctx.get_guild().get_member(random.choice(siedemnascie_ce))
    second_favorite = ctx.get_guild().get_member(random.choice(siedemnascie_ce))

    trivias = [f"Czy wiedzieliście, że {favorite.mention} jest najlepszym programistą w swojej grupie?",
               f"Czy wiedzieliście, że {favorite.mention} miał w gimnazjum przezwisko 'Kicia'?",
               f"Czy wiedzieliście, że {favorite.mention} w trakcie liceum wdał się w niejednoznaczną relację z nauczycielką matematyki?",
               f"Czy wiedzieliście, żen {favorite.mention} nigdy nie nauczył się robić gwiazdek na konsoli w Javie?",
               f"Czy wiedzieliście, że {favorite.mention} kiblował z HKJ?",
               f"Czy wiedzieliście, że {favorite.mention} ma na imię Michał?",
               f"Czy wiedzieliście, że {favorite.mention} nadal ma ITN ze Wstępu do Zarządzania?",
               f"Czy wiedzieliście, że ulubionym językiem programowania {favorite.mention} jest Java 1.8?",
               f"Czy wiedzieliście, że {favorite.mention} podkochuje się w Szumi Mamie?",
               f"Czy wiedzieliście, że {favorite.mention} jest fanatykiem UML?",
               f"Czy wiedzieliście, że {favorite.mention} jest twórcą najmniej wydajnego kodu w historii i była to gra w Swingu?",
               f"Czy wiedzieliście, że {favorite.mention} był jedyną osobą, która rozumie Mrówkę?",
               f"Czy wiedzieliście, że {favorite.mention} rozlał kiedyś kawę w windzie?",
               f"Czy wiedzieliście, że {favorite.mention} nie był na ani jednych zajęciach z MUL?",
               f"Czy wiedzieliście, że mama {favorite.mention} pisze mu podania o usprawiedliwienie nieobecności?",
               f"Czy wiedzieliście, że {favorite.mention} bardzo niski?",
               f"Czy wiedzieliście, że {favorite.mention} jest bacznie obserwowany przez Tomaszewa?",
               f"Czy wiedzieliście, że to {favorite.mention} zepsuł SDKP, nie zamykając serwera?",
               f"Czy wiedzieliście, że {favorite.mention} codziennie programuje w Bashu?",
               f"Nie że coś, ale {favorite.mention} zaliczył MAD-y w bardzo podejrzany sposób...",
               f"Nie że coś, ale {favorite.mention} zaliczył SAD-y w bardzo podejrzany sposób...",
               f"Nie że coś, ale {favorite.mention} zaliczył ostatnie kolokwium w bardzo podejrzany sposób...",
               f"{favorite.mention} jest w związku, ale ukrywa to od ponad roku...",
               f"Czy wiedzieliście, że {favorite.mention} jest mikrocelebrytą na 4chanie?",
               f"Czy wiedzieliście, że {favorite.mention} ma wspólną szczoteczkę ze swoim kotem?",
               f"Czy wiedzieliście, że {favorite.mention} jest fanem języków niskiego poziomu?",
               f"Czy wiedzieliście, że {favorite.mention} jest frontasiem? Pewnie tak, ale jest też femboyem!",
               f"Czy wiedzieliście, że {favorite.mention} ma bardzo bliską relację z pewną mamą-Youtuberką?",
               f"Czy wiedzieliście, że {favorite.mention} jest potajemnie w związku z {second_favorite.mention}?",
               f"Czy wiedzieliście, że {favorite.mention} i {second_favorite.mention} tak na prawdę są jedną osobą?",
               f"Czy wiedzieliście, że {favorite.mention} to ex {second_favorite.mention}?",
               f"Czy wiedzieliście, że {favorite.mention} podkochuje się w {second_favorite.mention}?",
               f"Czy wiedzieliście, że {favorite.mention} jest fanem {second_favorite.mention}?",
               f"Czy wiedzieliście, że {favorite} wszystkim się myli z {second_favorite.mention}?",
               f"Czy wiedzieliście, że {favorite.mention} najchętniej pije z {second_favorite.mention}?",
               f"Czy wiedzieliście, że {favorite.mention} nigdy nie był na zajęciach z {second_favorite.mention}?",
               f"Czy wiedzieliście, że {favorite.mention} jest tak na prawdę ćwiczeniowcem na PJATK?",
               f"Czy wiedzieliście, że {favorite.mention} jest szpiegiem z działu promocji?",
               f"Nie ma trivii. Jest tylko {favorite.mention}.",
               f"Czy wiedzieliście, że {favorite.mention} błagał na kolanach o 3 z SAD?",
               f"{favorite.mention} umie wyzerować całą butelkę Jacka Daniela",
               f"Czy wiedzieliście, że {favorite.mention} był rodzony w wannie?",
               f"Czy wiedzieliście, że {favorite.mention} jest niesamowicie shrexy?",
               f"Czy wiedzieliście, że {favorite.mention} spędził dzisiejszą noc z matką {second_favorite.mention}?",
               f"Nie zasługujesz na trivię, {ctx.author.mention}.",
               f"A co ty taki ciekawy, {ctx.author.mention}?",
               f"Nie ma trivii. Mam bardzo bliskie relacje z twoją matką, {ctx.author.mention}.",
               f"Nie ma trivii. Mam bardzo bliskie relacje z twoim ojcem, {ctx.author.mention}.",
               f"Przestań mnie męczyć, {ctx.author.mention}.",
               f"Nie ma trivii. Nie zasługujesz na trivię, {ctx.author.mention}.",
               f"Czy wiedzieliście, że {favorite.mention} dzisiaj obudził się obok {second_favorite.mention}?"
               ]
    await ctx.get_channel().send(random.choice(trivias))


@bot.command
@lightbulb.command("siad", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def siad(ctx: lightbulb.Context) -> None:
    choices = random.choice(["*stoi dalej*", "*siada*", "*macha ogonkiem*", "*siada, bo cię kocha*"])
    await ctx.get_channel().send(choices)


@bot.command
@lightbulb.command("leżeć", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def leżeć(ctx: lightbulb.Context) -> None:
    choices = random.choice(
        ["*stoi dalej*", "*leży*", "*macha ogonkiem*", "*leży, bo cię kocha*", "*ucieka*", "*umiera*"])
    if choices == "*umiera*":
        await ctx.get_channel().send(choices)
        await ctx.get_channel().send("F")
        exit()
    await ctx.get_channel().send(choices)


@bot.command
@lightbulb.command("łapa", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def łapa(ctx: lightbulb.Context) -> None:
    choices = random.choice(
        ["*stoi dalej*", "*daje łapkę*", "*macha ogonkiem*", "*daje łapkę, bo cię kocha*", "*kładzie się na brzuszek*",
         "*daje główkę*", "*daje nóżkę*"])
    await ctx.get_channel().send(choices)


@bot.command
@lightbulb.command("smaczek", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def smaczek(ctx: lightbulb.Context) -> None:
    choices = random.choice(
        ["*ignoruje*", "*smakuje smaczka*", "*macha ogonkiem*", "*smakuje smaczka, bo cię kocha*", "*nie smakuje jej*",
         "*smakuje jej*"])
    if choices == "*nie smakuje jej*":
        await ctx.get_channel().send(choices)
        assign_points(ctx.author, -1)
    elif choices == "*ignoruje*":
        await ctx.get_channel().send(choices)
    else:
        await ctx.get_channel().send(choices)
        assign_points(ctx.author, 1)


@bot.command
@lightbulb.command("spacer", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def spacer(ctx: lightbulb.Context) -> None:
    miejsca = {
        "Poszliście do parku. Iriska jest zachwycona! - 3 punkty": 3,
        "Poszliście do lasu. Iriska jest zachwycona! - 3 punkty": 3,
        "Poszliście na PJATK. Iriska się zestresowała! - -1 punkt": -1,
        "Poszliście na spacer po mieście. Iriska spotkała inne pieski! - 1 punkt": 1,
        "Poszliście do Mrozów. Iriska spotkała Iryska! - 4 punkty": 4,
        "Poszliście na Pragę Północ. Iriska ledwo uszła z życiem! - -2 punkty": -2,
        "Poszliście na Bulwary. Iriska się wychillowała. - 1 punkt": 1,
        "Poszliście dookoła bloku. - 1 punkt": 1,
        "Poszliście na teren wojskowy. Iriska została aresztowana! - -2 punkty": -2,
        "Poszliście do ciemnego tunelu między Śródmieściem a Powiślem. wtf? - -3 punkty": -3,
    }
    miejsce = random.choice(list(miejsca.keys()))
    await ctx.get_channel().send(miejsce)
    assign_points(ctx.author, miejsca[miejsce])


@bot.command
@lightbulb.command("punkty", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def punkty(ctx: lightbulb.Context) -> None:
    await ctx.get_channel().send(get_points(ctx.author))




@bot.command
@lightbulb.command("bullyiza", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def bullyiza(ctx: lightbulb.Context) -> None:
    await ctx.get_channel().send("Bullyizuje " + ctx.get_guild().get_member(615940700730687502).mention + "!")
    await ctx.get_guild().get_member(615940700730687502).send(
        "Bullyizuje " + ctx.get_guild().get_member(615940700730687502).__str__() + "!")


@bot.command
@lightbulb.command("bullycyprian", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def bullycyprian(ctx: lightbulb.Context) -> None:
    await ctx.get_channel().send("Bullycyprianuję " + ctx.get_guild().get_member(307598226184339457).mention + "!")
    await ctx.get_guild().get_member(307598226184339457).send(
        "Bullycyprianuję " + ctx.get_guild().get_member(307598226184339457).__str__() + "!")


@bot.command
@lightbulb.command("bullykrystian", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def bully(ctx: lightbulb.Context) -> None:
    await ctx.get_channel().send("Bullykrystianuję " + ctx.get_guild().get_member(285146237613899776).mention + "!")
    await ctx.get_guild().get_member(285146237613899776).send(
        "Bullykrystianuję " + ctx.get_guild().get_member(285146237613899776).__str__() + "!")


@bot.command
@lightbulb.command("bullydede", "help")
@lightbulb.implements(lightbulb.PrefixCommand)
@lightbulb.implements(lightbulb.SlashCommand)
async def bully(ctx: lightbulb.Context) -> None:
    await ctx.get_channel().send("Bullydeduję " + ctx.get_guild().get_member(517050226570297346).mention + "!")
    await ctx.get_guild().get_member(517050226570297346).send(
        "Bullydeduję " + ctx.get_guild().get_member(517050226570297346).__str__() + "!")


# Run the bot
# Note that this is blocking meaning no code after this line will run
# until the bot is shut off
if __name__ == '__main__':
    bot.run()
