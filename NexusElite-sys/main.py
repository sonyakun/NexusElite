import discord
from discord.ext import commands
import Jishaku
from jishaku.features.baseclass import Feature

class MyBot(commands.Bot):
    async def is_owner(self, user: discord.User):
        if something:  # Implement your own conditions here
            return True

        # Else fall back to the original
        return await super().is_owner(user)

TOKEN = 'OTYyNTcyMTA0MTE1NTg1MDg1.YlJfIQ.g1XOtZJoY_91cP_1U1xrumQir9c'
bot = commands.Bot(command_prefix='s=')

@bot.command()
async def lordjsk(ctx):
    await ctx.send('📩`imported jishaku`')
    bot.load_extension('jishaku')



bot.run(TOKEN)
