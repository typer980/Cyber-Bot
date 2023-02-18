import discord
import json
import asyncio
from datetime import datetime 
from discord.ext import commands

class Mod(commands.Cog):
  def __init__(self, client):
    self.client = client
  @commands.Cog.listener()
  async def on_ready(self):
    print("Mod.py is ready")
    
  #gives role to a member
  @commands.command(aliases=["addrole","giverole"], description="Give Member a Given Role. How to excuete `!addrole`User Id``Role ID` ")
  @commands.has_permissions(ban_members=True)
  async def Assignrole(self, ctx, member: discord.Member, * , role: discord.Role):

      embed = discord.Embed(title="Success!", color=discord.Color.green())
      embed.add_field(name="Added!",value=f"The role {role.mention} has been added to {member.name}.")
      
      await ctx.send(embed=embed)
    
      await member.add_roles(role)
   
  #removes role to a member    
  @commands.command(aliases=["removerole","takerole"], description="Remove Given Role from a member. How to excuete `!removerole`User Id``Role ID`")
  @commands.has_role("Big Clicker")
  async def Unassignrole(self, ctx, member: discord.Member, * , role: discord.Role):

      embed = discord.Embed(title="Success!", color=discord.Color.green())
      embed.add_field(name="Removed!",value=f"The role {role.mention} has been removed from {member.name}.")
      
      await ctx.send(embed=embed)
    
      await member.remove_roles(role)
      
  #ban command 
  @commands.command(description="Bans Member from server/guild. How to excuete `!ban``User Id``reason`")
  @commands.has_permissions(ban_members=True)
  async def Ban(self, ctx, member: discord.Member, *, modreason="modreason"):
        
      if member == ctx.author:
        await ctx.send(f"```{member.name} You can't ban yourself```")
      
      else:
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Banned:", value=f"{member.mention} has been banned from **Typer's HQ** by {ctx.author.mention}.", inline=False)
        conf_embed.add_field(name="Reason:", value=modreason, inline=False)
     
        await member.send(embed=conf_embed)

        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name = "Banned!", value=f"{member.mention} has been banned from **Typer's HQ**.")
      
        await ctx.send(embed=embed) 
     
        await ctx.guild.ban(member)
        
  #unban command
  @commands.command(description="Unbans Banned member. How to excuete `!unban``User Id`")
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def Unban(self, ctx, userId):
    user = discord.Object(id=userId)
    await ctx.guild.unban(user)

    conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
    conf_embed.add_field(name="Unbanned:", value=f"<@{userId}> has been unbanned from **Typer's HQ** by {ctx.author.mention}.", inline=False)

    await ctx.send(embed=conf_embed)
    

        
  #mute command       
  @commands.command(description="Mutes a member `Mutes in Second`. How to excuete `!mute``User Id``reason`")
  @commands.has_permissions(ban_members=True)
  async def Mute(self, ctx, member: discord.Member, *, reason="Not specified"):
      with open("cogs/json/mute.json", "r") as f:
        mute_role = json.load(f)

      if member == ctx.author:
       await ctx.send(f"```{member.name} You cannot mute yourself.```")

      else:
       mute_role = discord.utils.get(ctx.guild.roles, name=mute_role[str(ctx.guild.id)])  
       await ctx.channel.set_permissions(mute_role, speak=False, send_messages=False, read_message_history=False, read_messages=True)
       
       embed = discord.Embed(title="Muted", description=f"{member.mention} was muted ", color=discord.Color.green())
       embed.add_field(name="Reason: ", value=reason, inline=False)
    
       await ctx.send(embed=embed)
    
       conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
       conf_embed.add_field(name="Muted:", value=f"{member.mention} has been muted from **Typer's HQ** by {ctx.author.mention}.", inline=False)

       await member.send(embed=conf_embed)
       
       await member.add_roles(mute_role)
  
       
  #unmute command
  @commands.command(description="Unmutes a Muted User. How to excuete `!unmute``User Id``reason`")
  @commands.has_permissions(ban_members=True)
  async def Unmute(self, ctx, member: discord. Member, *, reason="Not specified"):
      with open("cogs/json/mute.json", "r") as f:
          mute_role = json.load(f)
          
      if member == ctx.author:
         await ctx.send(f"```{member.name} You can't unmute yourself```")

      else:
        mute_role = discord.utils.get(ctx.guild.roles, name= mute_role[str(ctx.guild.id)])
        await member.remove_roles(mute_role, reason=reason)
        
        conf_embed = discord.Embed(title="Success!", description=f" {member.mention} was unmuted ", color=discord.Color.green())
        conf_embed.add_field(name="Reason:", value=reason, inline=False)
                              
        await ctx.send(embed=conf_embed)

        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Unmuted:", value=f"{member.name} has been unmuted from **Typer's HQ** by {ctx.author.name}.", inline=False)

        await member.send(embed=conf_embed)
        
  #slowmode command
  @commands.command(aliases=["sm"], description="Add Slowmode in a channel. How to excuete `!sm``channel if needed``time in seconds` ") 
  @commands.has_permissions(ban_members=True)
  async def Slowmode(self, ctx, sm: int, channel=None):
      if channel is None:
        channel = ctx.channel
      
      if sm == 0:
          await channel.edit(slowmode_delay=sm)
          await channel.send("Slow Mode Off")
          return
      elif sm>=1:
          await channel.edit(slowmode_delay=sm)
          
          embed=discord.Embed(title="Slowmode!", color=discord.Color.green())
          embed.add_field(name="Time:", value=f"{sm} seconds ", inline=True)
         
          await channel.send(embed=embed)
      elif sm<=-1:
          embed=discord.Embed(title="ERROR", color=discord.Color.red())
          embed.add_field(name="Time:", value=f"Enter a positive value ", inline=True)
         
          await channel.send(embed=embed)
      else:
            return
            
          
  #sever message
  @commands.command(aliases=["speak","echo"], description="Server Message. Send message in another channel. How to excuete `!say``channel id` `message`")
  @commands.has_permissions(ban_members=True)
  async def Say(self, ctx, channel: discord.TextChannel,*, msg):     
    if channel is None:
            channel = ctx.author.channel
    elif channel is not None:
            channel = channel
            
    embed = discord.Embed(title="", description=f"{msg}", color=discord.Color.random()) 
    
    await ctx.send("Message sent to channel!")
    
    await channel.send(embed=embed)
  
  #DM message
  @commands.command(description="Sends DMs to a user. How to excuete `!DM `Dm User Id` `message` `")
  @commands.has_permissions(ban_members=True)
  async def DM(self, ctx, member: discord.Member, *, msg):
    
   embed=discord.Embed(title="New Alert", description=f"{msg}", color=discord.Color.random())
   embed.set_footer(text=f"This message was sent from  **{ctx.guild}** by {ctx.author.name} ", icon_url=ctx.author.avatar)
   
   await member.send(embed=embed)
  
  @commands.command(aliases=["rules","r"])
  async def rule(self, ctx, number: int):
   if number<=121:
         
    with open("rules.txt", "r") as f:

     rules = f.readlines()
     rule = rules[number-1]
      
     embed = discord.Embed(description=f"{rule}", title=" ",  color =discord.Color.random())
     embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)

     await ctx.send(embed=embed)
   else:
        await ctx.send("Enter a number from 1-11")
     
   
async def setup(client):
  await client.add_cog(Mod(client))