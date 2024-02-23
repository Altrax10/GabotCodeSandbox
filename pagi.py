import discord
from discord.ext import commands

class pagi(commands.Cog):
  def __init__ (self, client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_message(self,message):
    if message.content == "<:pagilord:779677244271362078>":
      if not message.author.bot :
        await message.channel.send(f'<:pagilord:779677244271362078>')

def setup(client):
  client.add_cog(pagi(client))