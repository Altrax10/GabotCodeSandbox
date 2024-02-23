import discord
from discord.ext import commands
import genshinstats as gs
import asyncio
from discord.ext import tasks, commands

cookies = gs.set_cookie(ltuid=21304544, ltoken="APjwoXzaN1FPywkPHWQbPseZAIZ1i4YOP0hperMu")
gs.set_authkey('https://webstatic-sea.mihoyo.com/ys/event/im-service/index.html?im_out=true&sign_type=2&auth_appid=im_ccs&authkey_ver=1&win_direction=portrait&lang=en&device_type=pc&ext=%7b%22loc%22%3a%7b%22x%22%3a-3000.31201171875%2c%22y%22%3a218.18482971191407%2c%22z%22%3a-4333.56982421875%7d%2c%22platform%22%3a%22WinST%22%7d&game_version=OSRELWin2.4.0_R5691054_S5715829_D5736476&plat_type=pc&authkey=GTOTYi1PzrzZOcuSx%2f7%2fVKDoapPz4r79H5v%2f%2bRPV148kEC8hYueoYWDQGffDZ2yi0fwBsPZp0P7gcTcEeaZk7cgJZ2Fyhtz4vEz1T5h2xuax4A4Qm3Sdt8NcDVxXQSt6Y8F2Bms1lXcOXvo0OqzXFGRn10LrDmxE0Tr1Sd9CtrnNjm3llILBl2QJJxKjN1iwwBeIf7c%2b%2bwuK2KmDBvY1ZRF7WZ9Pb7j2sOPlKqv5%2bP8p%2fAdVUDUShnDAGdInhRNv5qV51ZHrWSuclHHt8Ch%2b68Sf3Kxupy5lAdqEhxTahGrqHu2qiTzoyIj2Udp42AquDge9sX3r5425v%2b2okLpRwCIupkaxCfZFjgxSq55J9bRExFNgJWwxIBT0ovxYtI3z%2fc%2fkkfxUEug46iX1bKpyNUzBjQel3sNzQf%2fw4j9JRecwhxmxdUt53BkLvHg4hM6jQQWAS4FQdt84amCu52P2zVBtMujp5CaI5dzWaGycRh%2fF9JqZwntGZ%2bfdwUwLvLLmKHlFRplMKycZble9hKBd5nHEVdIv6wpICN5z1JpG%2boQfo9ksQYHdk7Rj1H6uxRx4Qla3Lxh9xJd6E4iI98jLqcQEfA%2f4imRCrr5aX%2fsG5mkl31oe4zKa9SoU0FrNl6iNRs0dMXHI2baCh74wA5humHZ2OcViRvNBW79iI6JPV5rt5XgmcfOPzpq%2fzKzdOrfgAQ8p6vvVXd5wQYcaBn2gW9AboUKYMtKVJrJSPm3wst0o93A2kvx8b8OCbcNQGMII2xB9Uknr3soGQb4JE9Lrc5TUePnSIl4iMdpFMWyADw11lziPipJhB3knAjQsKCxsr%2fjUFW5BWI0JDaJD78AsbTaGqq%2fNKNsWP4wzfvggTyByvAn8Uy8segeDHcmX5EbyntF6652h1imb4GxIe1lADWfy8CHoDkQ3MyNZx21PTs5nZIQqCFZasyCCMeePUlUjhFqKobL%2b%2f9UEiYBtAOKEBIHaeAEd9zggAvFksJAppeF1v8%2bbXsvHBNwh%2bmidqhqBQuNDOY4DKoURS4eYs0QdUAMP987O9q2%2b0rzx0RqS%2fgMGo3T%2bNkRyeZ4ggGXj%2fas8LBWAaDhge3ctIrZWLyrUJnPTZA6eaN4raWluGHtQg0rxFOvKiRwYtKDYWusw%2fTFDB7OCBJbTzelDfk4oVeN%2bAIsYPwUd%2boXb3j6SRDTXEMFs%2bZJDmub%2fAWvMu7%2fdYYuU07jDXVbXhdv0c%2fEVQA19xkNMWBFNYixIl1KHBCGE7kS716%2b%2bAqU7QAl1LwZGKQYT7PLbyELDvenfgOvmyf2sQbPlcz16GATccjVmq7S1bLvlSkswaEDTt%2f77FYqSrcNI54X5opNgWAieWtlhZtAF3A%3d%3d&game_biz=hk4e_global')

class Genshing(commands.Cog):
  def __init__ (self, client):
    self.client = client
    self.auto.start()
    global uid
    uid = gs.get_uid_from_hoyolab_uid(21304544)
    
    
  @commands.command()
  async def char(self,ctx):
    id = ctx.author.id
    if id == 441576175580610560:
      characters = gs.get_characters(uid)
      for char in characters:
        await ctx.send(f"{char['rarity']}* {char['name']:10} | lvl {char['level']:2} C{char['constellation']}")
    else:
      await ctx.send("`You dont have permission`")

  @commands.command()
  async def stats(self,ctx):
    id = ctx.author.id
    if id == 441576175580610560:
      stats = gs.get_user_stats(uid)['stats']
      for field, value in stats.items():
        await ctx.send(f"{field}: {value}")
    else:
      await ctx.send("`You dont have permission`")

  @commands.command()
  async def wish(self,ctx):
    id = ctx.author.id
    if id == 441576175580610560:
      for i in gs.get_wish_history():
        print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")
    else:
      await ctx.send("`You dont have permission`")

  @commands.command()
  async def cari(self,ctx,nama):
    id = ctx.author.id
    if id == 441576175580610560:
      for user in gs.search(str(nama)):
        await ctx.send(f"{user['nickname']} ({user['uid']}) - \"{user['introduce']}\"")

  @commands.command()
  async def claim(self,ctx):
    id = ctx.author.id
    if id == 441576175580610560:
      reward = gs.claim_daily_reward()
      if reward is not None:
          await ctx.send(f"Claimed daily reward - {reward['cnt']}x {reward['name']}")
      else:
          await ctx.send("Could not claim daily reward")

  @commands.command()
  async def myreward(self,ctx):
    id = ctx.author.id
    if id == 441576175580610560:
      for i in gs.get_claimed_rewards():
        await ctx.send(f"{i['cnt']}, {i['name']}")

  @tasks.loop(hours=24.0)
  async def auto(self):
    await self.client.wait_until_ready()
    channel = self.client.get_channel(940895290645446667)
    reward = gs.claim_daily_reward()
    if reward is not None:
      await channel.send(f"Claimed daily reward - {reward['cnt']}x {reward['name']}")
    else:
      await channel.send("Could not claim daily reward")
    

def setup(client):
  client.add_cog(Genshing(client))