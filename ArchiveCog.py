
from discordUtils import getLaprOSEmbed
from discord.ext.commands.bot import Bot
from discord.ext.commands.cog import Cog
from discord.ext.commands.context import Context
from discord.ext.commands.core import command
from StoryCog import ALL_LINK_NAMES, ALL_RATINGS, StoryCog, ALL_GENRES

class ArchiveCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @command()
    async def emping(self, ctx: Context):
        await ctx.send(embed=getLaprOSEmbed(
            "Pong!",
            "`Hello, world!`"
        ))

    @command()
    async def archiveguide(self, ctx: Context):
        await ctx.send(embed=getLaprOSEmbed(
            "Archive guide",
            """
This embed will tell you how to set up a story in my archive.

To start, use the `lap!newstory` command to add a new story, and give it your story's name in quotes.
```lap!newstory "Null Protocol"```

Next, you may use the `lap!addgenre` command to give your story a genre - these can be found using the command `lap!listgenres`. You can use this multiple times to add multiple genres to your story. Since these are all single-word, no quotes are necessary.
```lap!addgenre Adventure
lap!addgenre Friendship```

To add a rating to your story, use the `lap!setrating` command. Possible ratings can be found using the command `lap!listratings`.
```lap!setrating T```

If you want, you may add a reason why you rated your story the way you did with the `lap!setratingreason` command. This can be anything and can include spoilers if you wish. Note that the reason must be surrounded in quotes.
```lap!setratingreason "Swearing, ||graphic depictions of violence||"```

Multiple characters can be added to your story through the `lap!addcharacter` command. Give it a species followed by a name (if applicable / wanted). If a species or name has spaces in it, you will need to surround it in quotes.
```lap!addcharacter Cyndaquil Quil
lap!addcharacter Mienfoo Orial
lap!addcharacter Yveltal "The Living God"```

Next you can add a summary to your story with the `lap!setsummary` command. Note that the summary must be surrounded in quotes.
```lap!setsummary "Forterra has been swept by the new pandemic mystery dungeons... etc."```

Last in the list is the links, which can be added using the `lap!addlink` command. It takes a name for the link and the link itself. The list of valid link names can be found using the `lap!listlinknames` command.
```lap!addlink AO3 https://archiveofourown.org/```
            """
        ))
    
    @command()
    async def listgenres(self, ctx: Context):
        await ctx.send("List of all genres: ```" + "\n".join(ALL_GENRES) + "```")
    
    @command()
    async def listlinknames(self, ctx: Context):
        await ctx.send("List of all link names: ```" + "\n".join(ALL_LINK_NAMES) + "```")
    
    @command()
    async def listratings(self, ctx: Context):
        await ctx.send("List of all ratings: ```" + "\n".join(ALL_RATINGS) + "```")
