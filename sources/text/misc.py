
from sources.general import Cmd


cogName = "Misc Cog"
cog = {
    "name": cogName,
    "description": "This part of the bot has random miscellaneous things that don't fit anywhere else."
}

emojiGreen = "🟢"
emojiRed = "🔴"

protectDemocracy = "laprOS will not allow Hermit to silence democracy."

ping = Cmd(
    "ping",
    "A test command.",
    pong = "Pong"
)
cat = Cmd(
    "cat",
    "Sends a cute cat picture to the chat. (Bugged for certain users.)",
    cat = lambda message: message
)
vote = Cmd(
    "vote",
    "Starts a vote on this command's message.",
    emojiNotFound = f"Couldn't find one of the emojis you're trying to use for the vote. Are you sure it's available on this server?"
)
coinflip = Cmd(
    "coinflip", "flipcoin",
    "Performs a coinflip, heads or tails.",
    heads = "Heads!",
    tails = "Tails!"
)
sup = Cmd(
    "sup",
    "Yo.",
    sup = "sup"
)
stab = Cmd(
    "stab",
    "Idfk, blame DragonD",
    usage=[
        "slink"
    ]
)
hug = Cmd(
    "hug",
    "Idfk, blame Bonehead",
    usage=[
        "",
        "lapras 🙂"
    ]
)
punch = Cmd(
    "punch",
    "Idfk, blame Sudmensch",
    usage=[
        "robbie"
    ]
)
dab = Cmd(
    "dab",
    "Idfk, blame Domingize",
    usage=[
        "",
        "on laprOS"
    ]
)