import discord
from discord.ext import commands

class TyperInfo(commands.Cog):
    
  def __init__(self, client):
    self.client = client
  @commands.Cog.listener()
  async def on_ready(self):
    print("TyperInfo.py is ready")

  @commands.command(aliases=["Carrd","typerinfo","info"])
  async def Card(self, ctx):
    embed = discord.Embed(title = "https://tyyper.carrd.co/", color=0x36393F)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)
    
  @commands.command(aliases=["yt"])
  async def Youtube(self, ctx):
    embed = discord.Embed(title = "https://www.youtube.com/Typer_MC", color=0xFF0000)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)

  @commands.command(aliases=["Instagram"])
  async def Insta(self, ctx):
    embed = discord.Embed(title = "https://www.instagram.com/typer.mc/", color=0x8a3ab9)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)

  @commands.command(aliases=["twt"])
  async def Twitter(self, ctx):
    embed = discord.Embed(title = "https://www.twitter.com/@typer980", color=0x1DA1F2)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)

  @commands.command(aliases=["Twi"])
  async def Twitch(self, ctx):
    embed = discord.Embed(title = "https://www.twitch.com/Tyyper", color=0x6441a5)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)

  @commands.command(aliases=["tictok"])
  async def Tiktok(self, ctx):
    embed = discord.Embed(title = "https://www.tiktok.com/@typermc", color=0xff0050)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)

  @commands.command(aliases=["Email", "mail"])
  async def Bmail(self, ctx):
    embed = discord.Embed(title = "**Please check your DMs**", color=0xDB4437)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
    await ctx.author.send("**typermc0@gmail.com**")

    await ctx.send(embed=embed)
    
  @commands.command(aliases=["dc"])
  async def Discord(self, ctx):
    embed = discord.Embed(title = "https://discord.gg/b7RMNYxsRY", color=0x7289d9)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

    await ctx.send(embed=embed)
      
  @commands.command(aliases=["inv"])
  @commands.has_permissions(administrator=True)
  async def Invite(self, ctx):
    
    embed = discord.Embed(title= "Invite Cyber to your servers!", description = "https://discord.com/api/oauth2/authorize?client_id=1050489527522840748&permissions=8&scope=bot", color=0xff0050)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
    
    await ctx.author.send(embed=embed)
    
   
    
  @commands.command(aliases=["tinv", "TInvite", "testInv"])
  async def TestInvite(self, ctx):
    
    embed = discord.Embed(title="Test Server Invite", description = "https://discord.gg/CRNtqvhvUh", color=0xff0050)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
    
    await ctx.author.send(embed=embed)
    
  @commands.command(aliases=["TS"])
  async def Typersocials(self, ctx):

     embed = discord.Embed(title="**Typer Socials**",color=discord.Color.teal())
     
     embed.add_field(name="Discord ", value="How are you using this commmand SUS", inline=False)
     embed.add_field(name="Youtube ", value="Give link to my Youtube Channel. `-Yt`", inline=False)
     embed.add_field(name="TikTok", value="Give link to my TikTok Account. `-TikTok`", inline=False)
     embed.add_field(name="Instagram", value="Give link to my Instagram Account. `-Insta`", inline=False)
     embed.add_field(name="Twitch", value="Give link to my Twitch Channel. `-Twitch`", inline=False)
     embed.add_field(name="Twitter", value="Give link to my Twitter Account. `-Twitter`", inline=False)     
     embed.add_field(name="Card", value="Give link to my Card. `-Card`", inline=False) 
     embed.add_field(name="Busniess Email", value="Get DM'ed for my busniess email. `-Bmail", inline=False)
     embed.add_field(name="**Not what you are looking for?**", value="Try `-ModHelp` OR  `-Help`", inline=False)     
     embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)

     await ctx.send(embed=embed)


async def setup(client):
  await client.add_cog(TyperInfo(client))