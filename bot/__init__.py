"""Class gotten from python-discord/bot which is licensed under MIT License"""
import asyncio
import os
from functools import partial, partialmethod

from discord.ext import commands

from bot import log, monkey_typing

log.setup()

# On Windows, the selector event loop is required for aiodns.
if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

monkey_typing.patch_typing()

# This patches any convertors that use PartialMessage, but not the PartialMessageConverter itself
# as library objects are made by this mapping.
# https://github.com/Rapptz/discord.py/blob/1a4e73d59932cdbe7bf2c281f25e32529fc7ae1f/discord/ext/commands/converter.py#L984-L1004
commands.converter.PartialMessageConverter = monkey_typing.FixedPartialMessageConverter

# Monkey-patch discord.py decorators to use the Command subclass which supports root aliases.
# Must be patched before any cogs are added.
commands.command = partial(commands.command, cls=monkey_typing.Command)
commands.GroupMixin.command = partialmethod(
    commands.GroupMixin.command, cls=monkey_typing.Command
)