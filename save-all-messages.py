import discord
from discord.ext import commands



token = input("Insert Token: ")

client = discord.Client()
client= commands.Bot(command_prefix='.', self_bot=True)
client.remove_command('help')



@client.event
async def on_connect():
    print(f"Connected to => {client.user.name}")


@client.command()
async def log(ctx, amount: int):
    await ctx.message.delete()
    open("messages.txt", "w").close()
    async for message in ctx.message.channel.history(limit=amount):
        try:
           print(f"{message.author}:{message.content} ")
           with open('messages.txt', 'a') as (f):
                f.write(f"{message.author}: {message.content} -  https://discord.com/channels/@me/{ctx.channel.id}/{message.id}\n")

        except:
            pass


try: 
    client.run(token, reconnect=True, bot=False)
except Exception:
    pass
