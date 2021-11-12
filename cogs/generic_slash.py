import discord
from discord.ext import commands
from discord.commands import permissions
import util.logging.convert_logging as convert_logging
from util.cog_helpers.generic_helper import get_version
from util.constants import guild_ids
import util.discord.easy_embed as ezembed
from util.discord.paginator import Paginate

log = convert_logging.get_logging()


class GenericSlash(commands.Cog, description="Generic Functions"):
    statuses = []
    version = ""

    def __init__(self, client):
        self.client = client
        self.version = get_version()

    @commands.slash_command(
        guild_ids=guild_ids,
        name="ping",
        description="Get ping of bot to discord api in milliseconds",
    )
    async def _ping(self, ctx: commands.Context):
        await ctx.respond("Pong! {}ms".format(round(self.client.latency * 1000, 2)))

    @commands.slash_command(
        guild_ids=guild_ids, name="version", description="Displays bot version"
    )
    async def _version(self, ctx: commands.Context):
        await ctx.respond(f"Bot Version is {self.version}", ephemeral=True)

    @commands.slash_command(
        guild_ids=guild_ids, name="source", description="Displays Github Source Code"
    )
    async def _source(self, ctx: commands.Context):
        await ctx.respond(
            "Here is the source code\nhttps://github.com/NottCurious/TMIndiaBot",
            ephemeral=True,
        )

    @commands.slash_command(
        guild_ids=guild_ids,
        name="invite",
        description="Gives you an invite link for the server",
    )
    async def _invite(self, ctx: commands.Context):
        await ctx.respond(
            "Here is an invite for you to share with your friends\nhttps://discord.gg/yvgFYsTKNr",
            ephemeral=True,
        )

    @commands.slash_command(guild_ids=guild_ids, name="testpagination")
    @permissions.is_owner()
    async def _test(self, ctx: commands.Context):
        embed1 = ezembed.create_embed(
            title="Testing 1", description="Testing 1's Description"
        )
        embed2 = ezembed.create_embed(
            title="Testing 2", description="Testing 2's Description"
        )
        embed3 = ezembed.create_embed(
            title="Testing 3",
            description="adjskbabdjasdjlaskbdawkudbuiwabdiwbdkbsgfrduidgbufdjklasljkdwbaldlalkds",
        )
        embed4 = ezembed.create_embed(
            title="Testing 4", description="Testing 4's Description"
        )
        embed_list = [embed1, embed2, embed3, embed4]

        my_pag = Paginate(pages=embed_list)
        await my_pag.run(ctx)


def setup(client):
    client.add_cog(GenericSlash(client))