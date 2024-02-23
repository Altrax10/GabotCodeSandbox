import discord
from discord.ext import commands
import asyncio
from datetime import datetime
import alive
import os
import interactions
import requests
from io import BytesIO

cogs = ['hello']
MYTOKEN = os.environ.get['MYTOKEN']
TOKEN = MYTOKEN
client = commands.Bot(command_prefix='$', intents=discord.Intents.all())
remove_bg_api_key = 'SkYd9kP4Bg9cAxKHEwEiC69X'
pfp_path = "Profile Picture/luffy-bruh.gif"

fp = open(pfp_path, 'rb')
pfp = fp.read()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="OnePiece"))
    print("moshi moshi")
    await client.user.edit(avatar=pfp)
    for i in cogs:
        try:
            synced = await client.tree.sync()
            print(f'Synced {len(synced)} command(s)')
            await client.load_extension(i)
            print(i + " Terload")
        except Exception as e:
            print(e)


bot = interactions.Client(token=TOKEN)


@client.tree.command(
    name="klaim",
    description="klaim badge dev",
)
async def klaim(ctx: interactions.CommandContext):
    await ctx.response.send_message(
        "Terklaim cek status mu disini : http://discord.com/developers/active-developer"
    )


@client.tree.command(
    name="sync",
    description="sync command to your guild",
)
async def sync(ctx: interactions.CommandContext):
    for i in cogs:
        try:
            synced = await client.tree.sync()
            print(f'Synced {len(synced)} command(s)')
            await client.load_extension(i)
            await ctx.response.defer()
            await asyncio.sleep(10)
            print(i + " Terload")
            # await ctx.reponse.send_message(i + "Terload")
            await ctx.followup.send(i + "Terload")
        except Exception as e:
            await ctx.response.defer()
            await asyncio.sleep(10)
            await ctx.followup.send(e)
            print(e)


@client.event
async def on_member_join(member):
    guild = client.get_guild(526100423250149386)
    apatar = member.avatar
    uid = member.id
    auth = member.guild.name
    guildav = member.guild.icon
    membercount = guild.member_count
    isit = member.bot
    test = member.created_at.strftime("%j")
    test1 = datetime.now()
    test2 = test1.strftime("%j")
    d0 = int(test)
    d1 = int(test2)
    delta = d0 - d1
    member = member.mention
    channel = client.get_channel(751053851456700557)
    sendmsg = channel.send
    embed = discord.Embed(
        title="Member Joined",
        description=f"User : {member}\n User ID : `({uid})`\n Bot : `{isit}`\n Akun Dibuat : `{delta} Hari yang lalu`",
        colour=discord.Colour.green(),
    )
    embed.set_author(name=auth, icon_url=guildav)
    embed.set_thumbnail(url=apatar)
    embed.set_footer(text=f"{membercount} Members")
    await sendmsg(embed=embed)


@client.event
async def on_member_remove(member):
    guild = client.get_guild(526100423250149386)
    apatar = member.avatar
    uid = member.id
    auth = member.guild.name
    guildav = member.guild.icon
    membercount = guild.member_count
    test = member.created_at.strftime("%j")
    test1 = datetime.now()
    test2 = test1.strftime("%j")
    d0 = int(test)
    d1 = int(test2)
    delta = d0 - d1
    isit = member.bot
    member = member.mention
    channel = client.get_channel(751053851456700557)
    sendmsg = channel.send
    embed = discord.Embed(
        title="Member Left",
        description=f"User : {member}\n User ID : `({uid})`\n Bot : `{isit}`\n Akun Dibuat : `{delta} Hari yang lalu`",
        colour=discord.Colour.red())
    embed.set_author(name=auth, icon_url=guildav)
    embed.set_thumbnail(url=apatar)
    embed.set_footer(text=f"{membercount} Members")
    await sendmsg(embed=embed)


@client.event
async def on_message_delete(message):
    channel = client.get_channel(922660132507238431)
    auth = message.author
    guildav = auth.avatar
    sendmsg = channel.send
    mem = auth.bot
    if mem == True:
        return
    else:
        embed = discord.Embed(title="Message Deleted",
                              description=message.content,
                              colour=discord.Colour.red())
        embed.set_author(name=auth, icon_url=guildav)
        embed.set_footer(text=f'#{message.channel}')
        await sendmsg(embed=embed)


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself

    if message.channel.id == 1199987797667348600 and message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith(('.png', '.jpg', '.jpeg')):
                image_url = attachment.url
                result_image = remove_bg(image_url)
                if result_image:
                    await message.channel.send(file=discord.File(BytesIO(result_image), filename='removed_bg.png'))

    await client.process_commands(message)


def remove_bg(image_url):
    api_url = 'https://api.remove.bg/v1.0/removebg'
    headers = {'X-Api-Key': remove_bg_api_key}
    files = {'image_url': (None, image_url)}

    response = requests.post(api_url, headers=headers, files=files)

    if response.status_code == 200:
        return response.content
    else:
        print(f'Remove.bg API error: {response.status_code} - {response.text}')
        return None


alive.keep_alive()
client.run(TOKEN)
