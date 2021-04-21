import discord 
from discord.ext import commands 
from discord.utils import get
import os
from subprocess import *

already_started = False

def run_command(*args):
    p = Popen(['java', '-jar']+list(args), stdout=PIPE,stderr=STDOUT)
    return iter(p.stdout.readline, b'')



client = commands.Bot(command_prefix="~")
@client.command() 
async def hello(ctx, arg):
     await ctx.send(arg)
@client.command()
async def start(ctx,arg):
     if arg == "-q":
          Popen.kill()
     else:
          global already_started
          if (already_started == True):
               await ctx.send("The server has already been activated")
          if ctx.channel.name == 'server-output':
               Sender = ctx.author
               Sender = str(Sender)
               print(Sender)
               Whitelist = open('Whitelist.txt', 'r')
               List_Whitelist = Whitelist.readlines()
               List_Whitelist = str(List_Whitelist)
               Whitelist.close()
               if Sender in List_Whitelist:
                    already_started = True
                    await ctx.send('`Starting server with verbose output`')
                    args = ['spigot-1.16.5.jar', 'nogui']
                    await ctx.send('`Please wait around a minute for the server to start`')
                    for output_line in run_command(*args):
                         await ctx.send("`{}`".format(output_line))
                         print(output_line)
               else:
                    await ctx.send("You are not in the minecrafter file, this incident will be reported")
                    return
          else:
               return



@client.command()
async def logs(ctx):
     if ctx.channel.name == 'server-output':
          await ctx.send(file=discord.File("minecraft/logs.log"))
     else:
          return




client.run('ODI4MjE0Mjc3MjczOTQ0MTE0.YGmUpw.TRgu8ZwmB-aOMuj7fWQG_Y9BvBc')
