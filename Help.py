
from typing import Mapping, Optional
from discordUtils import getLaprOSEmbed, paginate
import discord
from discord.ext import commands

import sources.text as T

class Help(commands.DefaultHelpCommand):
    async def send_bot_help(self, mapping: Mapping[Optional[commands.Cog], list[commands.Command]]):
        pages = []
        for cog in mapping:
            if not cog: continue
            commands = mapping[cog]
            if not commands: continue
            pages.append({
                "embed": getLaprOSEmbed(**T.HELP.cogEmbed(cog.qualified_name, cog.description, [command.name for command in commands if not command.hidden]))
            })
        await paginate(self.context, pages)
    
    async def send_cog_help(self, cog: commands.Cog):
        commands = cog.get_commands()
        embed = getLaprOSEmbed(**T.HELP.cogEmbed(cog.qualified_name, cog.description, [command.name for command in commands if not command.hidden]))
        await self.context.send(embed=embed)
    
    async def send_group_help(self, group: commands.Group):
        await super().send_group_help(group)
    
    async def send_command_help(self, command: commands.Command):
        embed = getLaprOSEmbed(
            **T.HELP.commandEmbed(command.name, command.aliases, command.clean_params, command.help, command.cog_name)
        )
        await self.context.send(embed=embed)