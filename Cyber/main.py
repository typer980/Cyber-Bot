import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import json
from discord import app_commands
from config import TOKEN
from prefixe import prefixes

client = commands.Bot(command_prefix=prefixes ,intents=discord.Intents.all(), case_insensitive=True)

client_status = cycle(["Hello.py"])

@tasks.loop(seconds=60)
async def change_status():
  await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(client_status)))

@client.event
async def on_ready():
  print("Success: client is connected to Discord!")
  change_status.start()
  try:
       synced = await client.tree.sync()
       print (f"Synced {len (synced)} command(s)")
      
  except Exception as e:
        print (e)
      
@client.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}!", ephemeral=True)
  
@client.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}`", ephemeral=True)
  
client.remove_command('help')

#join autorole
@client.event
async def on_guild_join(guild):
     with open("cogs/json/autorole.json", "r") as f:
       auto_role = json.load(f)
    
     auto_role[str(guild.id)] = None
       
     with open("cogs/json/autorole.json", "w") as f:
       json.dump(auto_role, f, indent=4)
           
@client.event
async def on_guild_remove(guild):
    with open("cogs/json/autorole.json", "r") as f:
       auto_role = json.load(f)
    
    auto_role.pop[str(guild.id)]
       
    with open("cogs/json/autorole.json", "w") as f:
       json.dump(auto_role, f, indent=4)
            
#mute cogs
@client.event
async def on_guild_join(guild):
    with open("cogs/json/mute.json", "r") as f:
       mute_role = json.load(f)
    
    mute_role[str(guild.id)] = None
       
    with open("cogs/json/mute.json", "w") as f:
       json.dump(mute_role, f, indent=4)
           
@client.event
async def on_guild_remove(guild):
    with open("cogs/json/mute.json", "r") as f:
       mute_role = json.load(f)
    
    mute_role.pop[str(guild.id)]
       
    with open("cogs/json/mute.json", "w") as f:
       json.dump(mute_role, f, indent=4)
       
class Menu(discord.ui.View):
  def __init__(self):
     super().__init__()
     self.value=None

@client.command(aliases=["mh", "hm","HelpMod"])
async def ModHelp(ctx):
       embed = discord.Embed(title="Documentation For Cyber", color=discord.Color.dark_teal())
       embed.add_field(name="Cyber Docs", value="Click on the button to Read Cyber Documentation", inline=False)
       embed.add_field(name="**Not what you are looking for?**", value="Try `-TS` **OR ** `-Help`", inline=False)
       embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
       
      
       view = Menu()
       view.add_item(discord.ui.Button(label="Documentation",style=discord.ButtonStyle.link, url="https://cyber-docs.web.app/"))
       
       await ctx.send(embed=embed, view=view)

banned_words = ["owow~","owo~","owow","owo","uwuw","uwu","uwu~","uwuw~","nigga","fuck", "nigger", "anal", "anus", "ballsack", "bestiality","buttplug","boob","boner","blowjob","cock","condom","cum","clit","cunt","cunnilingus","clitoris","dick","dildo","dilf","erection","felching","fellate","fellatio","futanari","hentai","hitler","ISIS","jizz","kinky","KKK","kms","kys","labia","lewd","loli","lolicon","lolis","masturbate","milf","nazi","nudes","orgasm","orgies","orgy","penis","pussy","pornhub","pedo","pedophile","pedophilia","porn","pornography","rule34","rape","raping","r34","rapist","scrotum","smegma","swastika","shotacon","semen","testicles","thot","vore","virgin","virginity","whore","wank","wanker","sex","stalin","osama bin laden","gay","lesbian"]
@client.event
async def on_message(msg):
   for word in banned_words:
          
          if word in msg.content.lower():
            await msg.delete()
            break
            
          
   await client.process_commands(msg)
   
banned_words = ["uno","nou","no u","no you"]
@client.event
async def on_message(msg):
   for word in banned_words:
          
          if word in msg.content.lower():
            await msg.channel.send("https://th.bing.com/th/id/OIP.GyxIB-pezcOGpdK1pcpIigHaLQ?pid=ImgDet&rs=1")

          
   await client.process_commands(msg)
   
                  
#loading all the cogs file
async def main():
   async with client:
     await client.load_extension("cogs.Mod")
     await client.load_extension("cogs.Levels")
     await client.load_extension("cogs.Fun")
     await client.load_extension("cogs.Admin")
     await client.load_extension("cogs.Helper")
     await client.load_extension("cogs.TyperInfo")
     await client.start(TOKEN)

asyncio.run(main())
