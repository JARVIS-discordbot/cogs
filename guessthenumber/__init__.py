from .guessthenumber import GuessTheNumber

async def setup(bot):
    await bot.add_cog(GuessTheNumber(bot))