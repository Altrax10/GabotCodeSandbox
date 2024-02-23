import discord
from discord.ext import commands
import youtube_dl
import asyncio

class music(commands.Cog):
    def __init__ (self, client):
      self.client = client

    @commands.command()
    async def join(self,ctx,aliases=['j']):
      if ctx.author.voice is None:
        await ctx.send("Anda Tidak Di Voice Channel")

      voice_channel = ctx.author.voice.channel
      if ctx.voice_client is None:
        await voice_channel.connect()
              
        await ctx.guild.change_voice_state(channel=voice_channel, self_deaf=True)

      else:
        await ctx.voice_client.moveto(voice_channel)

    @commands.command()
    async def dc(self,ctx):
     await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url,aliases=['p']):
      ctx.voice_client.stop()
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1  -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      YDL_OPTIONS = {'format':'bestaudio'}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url, download=False)
          url2 = info["formats"] [0] ['url']
          source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
          vc.play(source)

      while ctx.voice_client.is_connected():
        # checks if the bot is the only one in the channel
        if len(ctx.voice_client.channel.members) == 1:
            # disconnects
            await asyncio.sleep(20)
            await ctx.voice_client.disconnect()
            break
        # checks if client is pause
        elif ctx.voice_client.is_paused():
            await asyncio.sleep(1)
        # Checks if client is playing
        elif ctx.voice_client.is_playing():
            await asyncio.sleep(1)
        # if nothing of the above is fulfilled
        else:
            # disconnect
            await ctx.voice_client.disconnect()
            break
    @commands.command()
    async def pause(self,ctx,aliases=['ps']):
     ctx.voice_client.pause()
     await ctx.send("⏸️")

    @commands.command()
    async def resume(self,ctx,aliases=['rs']):
     ctx.voice_client.resume()
     await ctx.send("▶️")

def setup(client):
  client.add_cog(music(client))