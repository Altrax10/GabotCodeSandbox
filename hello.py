import discord
from discord import app_commands
from discord.ext import commands
import interactions


class hello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        @commands.command()
        async def sync(self, ctx) -> None:
            fmt = await ctx.client.tree.sync(guild=ctx.guild)
            await ctx.send(f"Synced {len(fmt)} commands.")

        @app_commands.command(name="hello", description="hello Test")
        async def get_avatar(ctx: interactions.CommandContext, user: discord.User):
            # Get the user's avatar URL
            avatar_url = user.avatar_url

            # Send the avatar URL in the channel
            await ctx.send(f"{user.name}'s Avatar: {avatar_url}")


async def setup(bot: commands.Bot):
    await bot.add_cog(hello(bot))
