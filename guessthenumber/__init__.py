from .guessthenumber import GuessTheNumber
async def setup(bot):
    bot.add_cog(GuessTheNumber(bot))
