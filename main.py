import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
from discord.utils import get

#play sound
from gtts import gTTS
from discord import FFmpegPCMAudio
from waiting import wait

import time

from ai_bot import xuly
from easy_json import db

def talk(x):
  #start_time = time.time()
  #language='zh-CN'
  language = "vi"
  audio=gTTS(text=x,lang=language,slow=False, tld='com.au')
  audio.save("1.mp3")
  #end_time = time.time()
  #print('Total all time elapsed: %.6f seconds' % (end_time - start_time))


#start
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["mie,"],intents=intents)
#bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
  #start
  print('We have logged in as {0.user} msg bot'.format(bot))



@bot.command(name="talk")
async def _talk(ctx,*,message:str):

  def callback(member, packet):
    print(member, packet)

  if ctx.author.voice:
    talk_channel = ctx.guild.get_channel(948462920155684885)
    if ctx.author.voice.channel == talk_channel:
      print("in voice")
      try:
        vc = await talk_channel.connect()
      except:
        print("Already connected to a voice channel.")

      talk_message =  xuly(message)
      talk(talk_message)

      db[message] = talk_message

      vc = get(bot.voice_clients, guild=ctx.guild)
      vc.play(FFmpegPCMAudio(executable="FFmpeg/ffmpeg.exe", source="1.mp3"))

  else:
    talk_message =  xuly(message)
    db[message] = talk_message
    await ctx.reply(talk_message)


@bot.command(name="ai_data")
async def _talk(ctx):
  await ctx.send(file=discord.File("easy_json.json"))

load_dotenv()
my_secret = os.environ['BOT_TOKEN']
bot.run(my_secret)
