import discord
from discord.ext import commands

class chat(commands.Cog):
  def __init__ (self, client):
    self.client = client
    
  @commands.Cog.listener()
  async def on_message(self,message):
    usr = message.author
    idku = message.channel
    channel = self.client.get_channel(idku.id)
    sendmsg = channel.send
    if idku.id == 526100423250149389:
      if usr.bot == True:
        if usr.id != 749963191588487248 and usr.id != 559426966151757824:
          await message.delete()
          await sendmsg(f"Pakai Bot di <#526100982405267456>")
    
def setup(client):
  client.add_cog(chat(client))
