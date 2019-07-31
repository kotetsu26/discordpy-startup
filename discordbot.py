from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

Player1 = "猫"
Player2 = "犬"
count = 0

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command(name="こんにちは")
async def hello(ctx):
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")

    
@bot.command()
async def rule(ctx):
    await ctx.send('プレイヤー１は「女勇者」か「村人（赤）」「村人（緑）」「村人（青）」を出せます。')
    await ctx.send('プレイヤー２は「魔王」か「スライム（赤）」「スライム（緑）」「スライム（青）」を出せます。')
    await ctx.send('「女勇者」は「魔王」に勝てますが、いずれの「スライム」にも勝つことはできません。')
    await ctx.send('「村人」は、自分と同じ色の「スライム」にのみ勝つことができます')
    
@bot.command()
async def start(ctx):
    Player1 = None
    Player2 = None
    count = 0
    await ctx.send('プレイヤー１の手番です。カードを出してください')
    
@bot.command()
async def play(ctx,arg):
    if count == 0
        Player1 = arg
        await ctx.send('プレイヤー2の手番です。カードを出してください')
    else if count ==1
        Player2 = arg
        await ctx.send(Player1)
        await ctx.send(Player2)
    
    
@bot.command()
async def test(ctx):
    Player1 = "女勇者"
    await ctx.send(Player1)
    await ctx.send('設定しました')


bot.run(token)
