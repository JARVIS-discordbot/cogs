from redbot.core import commands
import random
class GuessTheNumber(commands.Cog):
    def init(self, bot):
        self.bot = bot
    @commands.command()
    async def guessthenumber(self, ctx):
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guess = None
        await ctx.send("Welcome to 'Guess the Number'! Guess a number between 1 and 100:")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        while guess != number_to_guess:
            try:
                message = await self.bot.wait_for('message', check=check, timeout=30.0)
                guess = int(message.content)
                attempts += 1
                if guess < number_to_guess:
                    await ctx.send("Too low! Try again.")
                elif guess > number_to_guess:
                    await ctx.send("Too high! Try again.")
                else:
                    await ctx.send(f"Congratulations! You guessed the number in {attempts} attempts.")
            except ValueError:
                await ctx.send("Please enter a valid number.")
            except TimeoutError:
                await ctx.send("Time's up! Please start a new game.")
                break



