import discord
from discord.ext import commands
import random
from prefixe import prefixes

class Fun(commands.Cog):
  def __init__(self, client):
    self.client = client 
  @commands.Cog.listener()
  async def on_ready(self):
    print("Fun.py is ready")
      
  @commands.command()
  async def Ping(self, ctx):
    
          
     bot_latency = round(self.client.latency * 1000)
     embed = discord.Embed(description=f"The bot latency is **{bot_latency}** ms",  color =discord.Color.dark_teal())
     embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

     await ctx.send(embed=embed)

         
  @commands.command(aliases=["8ball"])
  async def Ball(self, ctx, *, question):
    
      with open("responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
        
        embed = discord.Embed(description=f"**Question**: {question}", title=f"**Answer**: {response}", color=discord.Color.random())
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
        
        await ctx.send(embed=embed)
             
  @commands.command(aliases=["9ball", "luckyball"])
  async def Luck(self, ctx, *, question):
   
    with open("luck.txt", "r") as f:
      random_responses = f.readlines()
      response = random.choice(random_responses)  
      
      embed = discord.Embed(description=f"**Question**: {question}", title=f"**Answer**: {response}",  color = discord.Color.random())
      embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

      await ctx.send(embed=embed)
      
   
  @commands.command(aliases=["e"])
  async def Embed(self, ctx):
    
      embed = discord.Embed(title="E.M.B.E.D", description="**E=Emotional\nM=\nB=\nE=\nD=Damage**", color=0xFFFFFF)
      embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)

      await ctx.send(embed=embed)

    
  @commands.command()
  async def Prefix(self, ctx):
   
     embed = discord.Embed(title=f"The Prefix are `{prefixes}` ",  color = discord.Color.dark_orange())
     embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)

     await ctx.send(embed=embed)
     
     
  @commands.command(aliases=["av","pfp"])
  async def Avatar(self, ctx, member: discord.Member = None):
   
      if member is None: 
        member = ctx.author
      elif member is not None:
          member = member
       
      memberAvatar = member.avatar.url
     
      embed = discord.Embed(title = f"{member.name}'s Avatar",  color = discord.Color.random())
      embed.set_image(url = memberAvatar)
      embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
      await ctx.send(embed=embed )
       
  @commands.command(aliases=["about","whois","ui"])
  async def UserInfo(self, ctx, member: discord.Member=None):
   
      if member is None: 
          member = ctx.author
      elif member is not None:
          member = member
          
      roles = [role.mention for role in member.roles[1:]]   
      roles.append('@everyone')
      info_embed=discord.Embed(title=f"{member.name}`s User Information", description="All information about this user.", timestamp=ctx.message.created_at, color=member.color)
      info_embed.set_thumbnail(url=member.avatar) 
      info_embed.add_field(name="Name & Discriminator:", value=f"{member.name}#{member.discriminator}", inline=True)
      info_embed.add_field(name="Bot?", value=member.bot, inline=False)
      info_embed.add_field(name="Status:", value=member.status, inline=False)
      info_embed.add_field(name = 'Joined' , value = member.joined_at.strftime("%a, %b %d, %Y %I:%M %p"))
      info_embed.add_field(name = 'Registered' , value = member.created_at.strftime("%a, %b %d, %Y %I:%M %p") , inline = True)
      info_embed.add_field(name="Roles:", value=" ".join(roles), inline=False)
      info_embed.set_footer(text='ID: ' + str(member.id))
      
      await ctx.send(embed=info_embed)  
             
  @commands.command(aliases=["h"])
  async def help(self, ctx):
 
    help_embed = discord.Embed(title="Help Desk for Cyber", description="All commands for the bot.", color=discord.Color.random())
    help_embed.set_author(name="Cyber")
    help_embed.add_field(name="Ping", value="The Ping command show's Cyber Bot's Latency.", inline=False)
    help_embed.add_field(name="8Ball", value="The 8ball command just like a magic 8ball in real life the 8ball command will return a random answer when prompted by a user.", inline=False)
    help_embed.add_field(name="9Ball", value="The 9Ball command is just like 8ball command but it measures your luck!.", inline=False)
    help_embed.add_field(name="Embed", value="Oh! Trust me you don't want to do this.", inline=False)
    help_embed.add_field(name="Prefix", value="The Prefix command send the prefix of the bot.", inline=False)
    help_embed.add_field(name="Avatar", value="The Avatar command lets you view the avatar of either yourself or another user.", inline=False)
    help_embed.add_field(name="UserInfo", value="The UserInfo command displays user information of either yourself or another user.", inline=False)   
    help_embed.add_field(name="MFOTD", value="The MFOTD stands for 'Minecraft Fact of the Day' and it will show a random fact about Minecraft.", inline=False)
    help_embed.add_field(name="Help", value="The Help Command Show this message.", inline=False)
    help_embed.add_field(name="Not what you are looking for?", value="Try `-TS` or `-ModHelp`", inline=False)
    help_embed.set_footer(text=f"Requested by {ctx.author.name}.", icon_url=ctx.author.avatar)

    await ctx.send("Help is here", embed=help_embed) 
       
  @commands.command(aliases=["minecarftfact","mcfact","factmc"])
  async def MFOTD(self, ctx):
   
    with open("fact.txt", "r") as f:
      randoms = f.readlines()
      response = random.choice(randoms)  
      embed = discord.Embed(description=f"{response}", title=f"**Minecarft Fun Fact: ** ",  color = discord.Color.random())
      embed.set_footer(text=f"Requested by {ctx.author.name} • Made with help of Minecraftr#0680 ", icon_url=ctx.author.avatar)

      await ctx.send(embed=embed)
        

async def setup(client):
  await client.add_cog(Fun(client))