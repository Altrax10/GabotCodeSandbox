import discord
from discord.ext import commands

class gi(commands.Cog):
  def __init__ (self, client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_message(self,message):
    if message.content == "gi":
      user = message.author
      moderator = discord.utils.get(message.guild.roles, id=920676195799035934)
      await message.delete()
      await message.channel.send(f'Genshin Kuy {moderator.mention} By {user.mention}')


def setup(client):
  client.add_cog(gi(client))