import discord
from discord import colour
from discord.ext import commands
import json
import logging
from datetime import datetime
from dotenv import load_dotenv

import functions.logging.convert_logging as convert_logging
import functions.common_functions.common_functions as common_functions
import functions.cog_helpers.generic_functions
from functions.logging.usage import record_usage, finish_usage

load_dotenv()
# log_level = os.getenv("LOG_LEVEL")
# version = os.getenv("VERSION")
# discord_log_level = os.getenv("DISCORD_LOG_LEVEL")

log = logging.getLogger(__name__)
log = convert_logging.get_logging()

DEFAULT_PREFIX = "*"


class Owner(commands.Cog, description="Owner Functions"):
    def __init__(self, client):
        self.client = client

    @commands.command(name="load", hidden=True)
    @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str):
        log.debug(f"Attempting to Load {cog}")

        try:
            log.debug(f"Attempting Load of {cog}")
            self.client.load_extension(cog)
            log.debug(f"Loaded {cog}")
        except Exception as e:
            log.error(f"An Exception Occured, Sending Embed")
            await ctx.send(
                embed=discord.Embed(
                    title=f"**`ERROR:`** {type(e).__name__} - {e}",
                    colour=discord.Colour.red(),
                )
            )
        else:
            log.debug(f"Successfully Completed, Sending Embed")
            await ctx.send(
                embed=discord.Embed(title=f"Success!", colour=discord.Colour.green())
            )

    @commands.command(name="unload", hidden=True)
    @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str):
        log.debug(f"Attempting to Load {cog}")

        try:
            log.debug(f"Attempting Unload of {cog}")
            self.client.unload_extension(cog)
            log.debug(f"Unloaded {cog}")
        except Exception as e:
            log.error(f"An Exception Occured, Sending Embed")
            await ctx.send(
                embed=discord.Embed(
                    title=f"**`ERROR:`** {type(e).__name__} - {e}",
                    colour=discord.Colour.red(),
                )
            )
        else:
            log.debug(f"Successfully Completed, Sending Embed")
            await ctx.send(
                embed=discord.Embed(title=f"Success!", colour=discord.Colour.green())
            )

    @commands.command(name="reload", hidden=True)
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):
        log.debug(f"Attempting to Reload {cog}")

        try:
            log.debug(f"Attempting Unload of {cog}")
            self.client.unload_extension(cog)
            log.debug(f"Unloaded {cog}")
            log.debug(f"Loading {cog}")
            self.client.load_extension(cog)
            log.debug(f"Loaded {cog}")
        except Exception as e:
            log.error(f"An Exception Occured, Sending Embed")
            await ctx.send(
                embed=discord.Embed(
                    title=f"**`ERROR:`** {type(e).__name__} - {e}",
                    colour=discord.Colour.red(),
                )
            )
        else:
            log.debug(f"Successfully Completed, Sending Embed")
            await ctx.send(
                embed=discord.Embed(title=f"Success!", colour=discord.Colour.green())
            )


def setup(client):
    client.add_cog(Owner(client))
