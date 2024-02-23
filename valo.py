import discord
from discord.ext import commands
import asyncio

class valo(commands.Cog):
  def __init__ (self, bot):
    self.bot = bot
    
  
  @commands.Cog.listener()
  async def on_message(self,message):
    if message.content == "valo":
      user = message.author
      moderator = discord.utils.get(message.guild.roles, id=759000226022948895)
      await message.delete()
      await message.channel.send(f'Login Kuy {moderator.mention} By {user.mention}')
      # await dudu.add_reaction("✅")

      # def check(reaction, user):
      #       return user == message.author.member.roles.has(759000226022948895) and str(reaction.emoji) == '✅'

      # while True:
      #   reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
      #   if str(reaction.emoji) == "✅":
      #       await dudu.channel.send('{} Ikoet'.format(user))
      #       return
async def setup(bot):
  await bot.add_cog(valo(bot))