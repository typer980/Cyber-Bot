import discord
import json
import asyncio
from datetime import datetime 
from discord.ext import commands

class Helper(commands.Cog):
  def __init__(self, client):
    self.client = client
  @commands.Cog.listener()
  async def on_ready(self):
    print("Helper.py is ready")
    
  #kicks command
  @commands.command(description="Kicks a member from a server. How to excuete `!kick``User Id``reason`")
  @commands.has_permissions(kick_members=True)
  async def Kick(self, ctx, member: discord.Member, *, modreason="None"):
      if member == ctx.author:
       await ctx.send(f"```{member.name} You can't ban yourself.```")
        
      else:
       conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
       conf_embed.add_field(name="Kicked:", value=f"{member.mention} has been kicked from **Typer's HQ** by {ctx.author.mention}.", inline=False)
       conf_embed.add_field(name="Reason:", value=modreason, inline=False)
       
       await member.send(embed=conf_embed) 

       embed = discord.Embed(title = "Success!", color=discord.Color.green())
       embed.add_field(name = "Kicked!", value=f"{member.mention} has been banned from **Typer's HQ**.")

       await ctx.guild.kick(member)
       
 #clear/purge channel     
  @commands.command(aliases=["purge"],description="Clears given amount of messages from a channel. How to excuete `!purge``Any postivie number e.g. 1,10.etc`")
  @commands.has_permissions(manage_messages=True)
  async def Clear(self, ctx, count: int):
      
      await ctx.channel.purge(limit=count)
      msg = (f"{count} message(s) have been deleted.")
      await ctx.send(msg)
      await msg.delete()
      
#warns user    
  @commands.command(description="Warns a user. How to excuete `!warn``User Id``reason`")
  @commands.has_permissions(kick_members=True)
  async def Warn(self, ctx, member: discord.Member, *, reason = None ):
     
      try:
         embed=discord.Embed(title="You have been warned!", color=discord.Color.red())
         embed.add_field(name="Reason:", value=reason, inline=True)
        
         await member.send(embed=embed)
        
         mbed=discord.Embed(title="Warn!", description=f"{member.mention} Has Been Warned.", color=discord.Color.red())
         mbed.add_field(name="Reason:", value=reason, inline=True)
         
         await ctx.send(embed=mbed)
      except:
         embed = discord.Embed(title="Error!", color=discord.Color.red())
         embed.add_field(name="DM NOT OPEN", value="Cyber was not able to DM the user.")
         
         await ctx.send(embed=embed)
    
async def setup(client):
  await client.add_cog(Helper(client))