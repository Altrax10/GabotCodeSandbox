import discord
from discord import app_commands
from discord.ext import commands
import datetime
import pytz
import asyncio
import pymongo


class status(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print("status working")
    client = self.client
    print("status working")
    while True:
      dtobj1 = datetime.datetime.utcnow()
      dtobj3 = dtobj1.replace(tzinfo=pytz.UTC)
      dtobj = dtobj3.astimezone(pytz.timezone("Asia/Kuala_Lumpur"))
      jam = dtobj.hour
      if jam >= 22 or jam <= 8:
        await client.change_presence(activity=discord.Activity(
          type=discord.ActivityType.playing, name="💤"))

        await asyncio.sleep(5)

        await client.change_presence(activity=discord.Activity(
          type=discord.ActivityType.playing, name="💤💤"))

        await asyncio.sleep(5)

        await client.change_presence(activity=discord.Activity(
          type=discord.ActivityType.playing, name="💤💤💤"))

        await asyncio.sleep(5)

      else:
        await client.change_presence(activity=discord.Activity(
          type=discord.ActivityType.watching, name="OnePiece"))


async def setup(bot):
  await bot.add_cog(status(bot))
