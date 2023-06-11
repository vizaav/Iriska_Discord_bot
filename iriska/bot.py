from hikari import Intents, Member
from hikari.events import *

from dotenv import load_dotenv
import os
import random
import lightbulb

from iriska.points import PointsManager

points = PointsManager()

# def assign_points(user, points):
#     lines = []
#
#     # Read existing data from the file
#     with open("points.csv", "r") as file:
#         reader = csv.reader(file)
#         lines = list(reader)
#
#     found = False
#     for line in lines:
#         if line[0] == str(user):
#             line[1] = str(int(line[1]) + points)
#             found = True
#             break
#
#     # Write updated data to the file
#     with open("points.csv", "w", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(lines)
#
#         # If the user was not found, add a new row
#         if not found:
#             writer.writerow([user, points])
#
#
# def get_points(user):
#     file = open("points.csv", "r")
#     reader = csv.reader(file)
#     lines = list(reader)
#     file.close()
#     for line in lines:
#         print("line: " + line.__str__())
#         if lines.__len__() == 0:
#             return 0
#         if line.__str__() == "":
#             continue
#         elif line[0] == user.__str__():
#             points = line[1].__str__()
#             user_login = line[0].__str__()
#             return "Człowiek " + user_login + " ma " + points + " punkty miłości Iriski :heart:"
#     return 0


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = lightbulb.BotApp(token=DISCORD_TOKEN, intents=Intents.ALL)


@bot.command
@lightbulb.option("pytanie", "Pytanie do Iriski")
@lightbulb.command("8", "zapytaj", ephemeral=False)
@lightbulb.implements(lightbulb.SlashCommand)
async def zapytaj(ctx: lightbulb.Context) -> None:
    if ctx.options['pytanie'] is None or ctx.options['pytanie'].endswith("?") is False:
        await ctx.respond("To nie jest pytanie *sus*")

    responses = ["Zdecydowanie tak", "Nie mam żadnych wątpliwości", "Nigdy w to nie wątpiłam", "Jest to pewne", "Tak",
                 "Tak - zdecydowanie", "Nie licz na to", "Moja odpowiedź brzmi nie", "Moje źródła mówią nie",
                 "Absolutnie nie", "Absolutnie tak", "Jak mogłeś w to wątpić?",
                 "Czemu zadajesz takie oczywiste pytania? Oczywiście, że tak!",
                 "Twoja stara"]

    await ctx.respond(random.choice(responses))


@bot.command
@lightbulb.command("dobranoc", "papa")
@lightbulb.implements(lightbulb.SlashCommand)
async def dobranoc(ctx: lightbulb.Context) -> None:
    guild = ctx.get_guild()
    if guild is None:
        return await ctx.respond("Nie jesteś na serwerze")
    members = guild.get_members()
    if members is None:
        return await ctx.respond("Nie ma nikogo na serwerze")
    members = list(filter(lambda x: x, members))
    favorite = members[random.choice(range(0, members.__len__()))]
    favorite = guild.get_member(favorite)
    await ctx.respond(
        "Dobranoc kochani, życzę wam słodkich snów, a w szczególności mojemu kochanemu " + favorite.__str__() + ":heart:")


@bot.command
@lightbulb.option("kto", "kto pytał", Member, required=False)
@lightbulb.command("trivia", "so trivial", ephemeral=False)
@lightbulb.implements(lightbulb.SlashCommand)
async def trivia(ctx: lightbulb.Context) -> None:
    siedemnascie_ce = [307598226184339457, 615940700730687502, 433215903539396609, 517050226570297346,
                       296626554027507715, 207196996669407233, 285146237613899776, 272427120074948612,
                       572512848270327849, 235351337179545611, 218333108825489408, 362284256053035008,
                       503534440006549525, 226403255842766849, 379260996126244874, 383635450306232320,
                       285146237613899776]
    favorite: Member = ctx.get_guild().get_member(random.choice(siedemnascie_ce))

    if ctx.options['kto']:
        favorite: Member = ctx.options['kto']

    second_favorite = ctx.get_guild().get_member(random.choice(siedemnascie_ce))

    if ctx.options['kto']:
        second_favorite: Member = ctx.options['kto']

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
    await ctx.respond(random.choice(trivias))


@bot.command
@lightbulb.command("siad", "help")
@lightbulb.implements(lightbulb.SlashCommand)
async def siad(ctx: lightbulb.Context) -> None:
    choices = random.choice(["*stoi dalej*", "*siada*", "*macha ogonkiem*", "*siada, bo cię kocha*"])
    await ctx.respond(choices)


@bot.command
@lightbulb.command("leżeć", "help")
@lightbulb.implements(lightbulb.SlashCommand)
async def leżeć(ctx: lightbulb.Context) -> None:
    choices = random.choice(
        ["*stoi dalej*", "*leży*", "*macha ogonkiem*", "*leży, bo cię kocha*", "*ucieka*", "*umiera*"])
    if choices == "*umiera*":
        await ctx.respond(choices)
        await ctx.respond("F")
        exit()
    await ctx.respond(choices)


@bot.command
@lightbulb.command("łapa", "help")
@lightbulb.implements(lightbulb.SlashCommand)
async def łapa(ctx: lightbulb.Context) -> None:
    choices = random.choice(
        ["*stoi dalej*", "*daje łapkę*", "*macha ogonkiem*", "*daje łapkę, bo cię kocha*", "*kładzie się na brzuszek*",
         "*daje główkę*", "*daje nóżkę*"])
    await ctx.respond(choices)


@bot.command
@lightbulb.command("smaczek", "help")
@lightbulb.implements(lightbulb.SlashCommand)
async def smaczek(ctx: lightbulb.Context) -> None:
    choices = random.choice(
        ["*ignoruje*", "*smakuje smaczka*", "*macha ogonkiem*", "*smakuje smaczka, bo cię kocha*", "*nie smakuje jej*",
         "*smakuje jej*"])
    if choices == "*nie smakuje jej*":
        await ctx.respond(choices)
        await points.update_points(str(ctx.author.id), -1)
        # assign_points(ctx.author, -1)
    elif choices == "*ignoruje*":
        await ctx.respond(choices)
    else:
        await ctx.respond(choices)
        await points.update_points(str(ctx.author.id), 1)
        await points.update_points(str(ctx.author.id), 1)


@bot.command
@lightbulb.command("spacer", "help")
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
    await ctx.respond(miejsce)
    await points.update_points(str(ctx.author.id), miejsca[miejsce])
    # assign_points(ctx.author, miejsca[miejsce])


@bot.command
@lightbulb.command("punkty", "help")
@lightbulb.implements(lightbulb.SlashCommand)
async def punkty(ctx: lightbulb.Context) -> None:
    await ctx.respond(points.get_points(str(ctx.author.id)))


@bot.command
@lightbulb.option("kto", "kto pytał", Member)
@lightbulb.option("co", "chcesz coś dodać od siebie??/", required=False)
@lightbulb.command("bully", "bully someone", ephemeral=False)
@lightbulb.implements(lightbulb.SlashCommand)
async def bully(ctx: lightbulb.Context):
    who_to_bully: Member = ctx.options['kto']
    await who_to_bully.send(f'Zostałeś zbullyizowany przez {ctx.author.mention}!')

    if ctx.options['co']:
        await who_to_bully.send(ctx.options['co'])

    await ctx.respond("Bullyizuje " + who_to_bully.mention + "!")


@bot.listen(GuildMessageCreateEvent)
async def listen_for_messages(event: GuildMessageCreateEvent) -> None:
    print(event.message.content)
    if event.message.author.is_bot:
        return
    choice = random.choice(range(0, 10000))
    answers = random.choice(
        ["Ta?", "Nie interesuje mnie to.", "Ok, i?", "Aha", "Ok", "Nie", "Tak", "Znajdź Boga.", "Przemsań",
         "It's time to stop"])
    if choice == 1:
        await event.message.respond(answers, reply=True)


@bot.listen(lightbulb.events.LightbulbStartedEvent)
async def bot_started(event: lightbulb.events.LightbulbStartedEvent) -> None:
    await points.sync()
