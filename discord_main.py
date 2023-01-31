import io
import sys
import discord
from discord.ext import commands
import draw
import translate
import detach

intents = discord.Intents.default()

intents.message_content = True
intents.emojis = True


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')


@bot.command(name='이모지')
async def emoji(ctx, arg):
    emoji_names = set(map(lambda emoji: emoji.name, ctx.guild.emojis))
    exists = set()
    success = set()
    for char in arg:
        emoji_name = translate.process(detach.process(char))
        byteio = io.BytesIO()
        if emoji_name in emoji_names or emoji_name in success:
            exists.add(emoji_name)
            continue
        draw.process(word=char,
                     filename=emoji_name,
                     fontsize=72,
                     indent=15,
                     io=byteio)
        await ctx.guild.create_custom_emoji(
            name=emoji_name,
            image=byteio.getvalue(),
            roles=[],
            reason='bot command emoji')
        success.add(emoji_name)
    await ctx.send(f'이미 있는 이모지 {len(exists)}개를 제외하고, {len(success)}개의 이모지를 만들었어요!')

if len(sys.argv) == 1:
    print('token not found')
    sys.exit(-1)

token = sys.argv[1]
bot.run(token)
