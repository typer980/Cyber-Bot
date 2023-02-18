import discord
import json
import asyncio
from datetime import datetime 
from discord.ext import commands

class Admin(commands.Cog):
  def __init__(self, client):
    self.client = client
  @commands.Cog.listener()
  async def on_ready(self):
    print("Admin.py is ready")
    
  #setting mute role  
  @commands.command(description="Set Mute Role. How to excuete `!setmuterole``Role ID`")
  @commands.has_permissions(administrator=True)
  async def Setmuterole(self, ctx, role: discord.Role):
        with open("cogs/json/mute.json", "r") as f:
          mute_role = json.load(f)
    
        mute_role[str(ctx.guild.id)] = role.name
       
        with open("cogs/json/mute.json", "w") as f:
           json.dump(mute_role, f, indent=4)
        
        conf_embed = discord.Embed(title="Success!", color = discord.Color.green())
        conf_embed.add_field(name="Mute role has been set!", value=f"The muted role has been assigned to {role.mention}. All the members who have this role will be muted.")
        
        await ctx.send(embed=conf_embed)
    
    
  @commands.command(description="Set Auto Join Role .How to excuete `!joinrole``Role ID`")
  @commands.has_permissions(administrator=True)
  async def joinrole(self, ctx, role: discord.Role):
        with open("cogs/json/autorole.json", "r") as f:
          auto_role = json.load(f)
    
        auto_role[str(ctx.guild.id)] = role.name
       
        with open("cogs/json/autorole.json", "w") as f:
           json.dump(auto_role, f, indent=4)
        
        embed = discord.Embed(title="Success!", color = discord.Color.green())
        embed.add_field(name="Auto role has been set!", value=f"The auto role has been assigned to {role.mention}.")
        
        await ctx.send(embed=embed)
        
 #gives automatic role when a user joins     
  @commands.Cog.listener()
  async def on_member_join(self, member):
       with open("cogs/json/autorole.json", "r") as f:
          auto_role = json.load(f)
          
       join_role = discord.utils.get(member.guild.roles, name=auto_role[str(member.guild.id)])

       await member.add_roles(join_role)
async def setup(client):
  await client.add_cog(Admin(client))