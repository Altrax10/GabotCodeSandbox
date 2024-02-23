from flask import Flask
from threading import Thread
import discord
from discord.ext import commands


class alive(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


app = Flask('')


@app.route('/')
def main():
  return "Your bot is alive!"


def run():
  app.run(host="0.0.0.0", port=8080)


def keep_alive():
  server = Thread(target=run)
  server.start()


async def setup(bot):
  await bot.add_cog(alive(bot))
