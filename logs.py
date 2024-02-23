import discord
import pymongo
from discord.ext import commands
import datetime
import pytz
import asyncio
from discord.ext import tasks
import schedule
import time

class logs(commands.Cog):
  def __init__ (self, client):
      self.client = client
      global myclient, mydb, mycol, urutan
      myclient = pymongo.MongoClient("mongodb+srv://altrax:jomblo69@gabut.sgqfb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

      mydb = myclient["Discord"]

      mycol = mydb["List"]

      test = mycol.find().sort("_id",-1)

      a = test[0]
    
      urutan = a["urutan"]

      

  @commands.Cog.listener()
  async def on_message(self,message):
    idku = message.channel
    channel = self.client.get_channel(idku.id)
    if message.author.bot != True:
      if message.channel.id == 936902421165277214:
        a = message.content
        b = a.split(' ')
        nama = b[0]
        harga = b[1]
        sum = 0
        global urutan
        urutan += 1
        
        myquery = { 
          "nama": nama,
          "harga": int(harga),
          "urutan": urutan
          }
  
        mycol.insert_one(myquery)
  
        await channel.trigger_typing()
        await channel.send("Catatan:")
        for x in mycol.find():
          sum = sum + x["harga"]
          jumlah = '{:,}'.format(sum)
          angka = '{:,}'.format(x["harga"])
          await channel.send(f'`{x["urutan"]}. {x["nama"]} Rp. {angka}`')
        await channel.send(f'`Jumlah: Rp. {jumlah}`')
        await channel.send(f"=======================")
      
      
  @commands.command()
  async def create(self,ctx,db,col):
    id = ctx.author.id
    if id == 441576175580610560:
      mydb = myclient[db]
      mycol = mydb[col]
      mydict = { 
        "Temp": "Temp",
        "Temp": "Temp"
        }
      mycol.insert_one(mydict)
      await ctx.send("Succesfully Created")
    else:
      await ctx.send("`You dont have permission`")

  @commands.command()
  async def add(self,ctx,*args):
    id = ctx.author.id
    sum = 0
    if id == 441576175580610560:
      nama,harga = args
      global urutan
      urutan += 1
      myquery = { 
        "nama": nama,
        "harga": int(harga),
        "urutan": urutan
        }

      mycol.insert_one(myquery)

      await ctx.trigger_typing()
      await ctx.send("Berhasil Ditambahkan")
      await ctx.message.delete()
      await ctx.send("Catatan:")
      for x in mycol.find():
        sum = sum + x["harga"]
        jumlah = '{:,}'.format(sum)
        angka = '{:,}'.format(x["harga"])
        await ctx.send(f'`{x["urutan"]}. {x["nama"]} Rp. {angka}`')
      await ctx.send(f'`Jumlah: Rp. {jumlah}`')
      await ctx.send(f"=======================")
    else:
      await ctx.send("`You dont have permission`")

  @commands.command()
  async def all(self,ctx):
    await ctx.message.delete()
    sum = 0
    for x in mycol.find():
      sum = sum + x["harga"]
      jumlah = '{:,}'.format(sum)
    id = ctx.author.id
    if id == 441576175580610560:
      x = mycol.find()
      results = list(x)
      if len(results) == 0:
        await ctx.send("Empty")
      for x in mycol.find():
        angka = '{:,}'.format(x["harga"])
        await ctx.send(f'`{x["urutan"]}. {x["nama"]} Rp. {angka}`')
      await ctx.send(f'`Jumlah: Rp. {jumlah}`')
      await ctx.send(f"=======================")
    else:
      await ctx.send("`You dont have permission`")

  @commands.command()
  async def drop(self,ctx,db):
    id = ctx.author.id
    if id == 441576175580610560:
      myclient.drop_database(str(db))
      await ctx.send("DB Dropped")
    else:
      await ctx.send("`You dont have permission`")

  @commands.command()
  async def clear(self,ctx):
    await ctx.message.delete()
    id = ctx.author.id
    if id == 441576175580610560:
      mycol.delete_many({})
      await ctx.send("`list Cleared`")
      global urutan
      urutan = 0
    else:
      await ctx.send("`You dont have permission`")

  @commands.command()
  async def find(self,ctx,nama):
    id = ctx.author.id
    if id == 441576175580610560:
      myquery = { "Laku": nama }

      mydoc = mycol.find(myquery)
      
      for x in mydoc:
        angka = '{:,}'.format(x["harga"])
        await ctx.send(f'`{x["urutan"]}. {x["nama"]} Rp. {angka}`')
    else:
      await ctx.send("You dont have permission")

  @commands.command()
  async def jumlah(self,ctx):
    sum = 0
    for x in mycol.find():
      sum = sum + x["harga"]
      jumlah = '{:,}'.format(sum)
    await ctx.message.delete()
    await ctx.send(f'`Rp. {jumlah}`')
    

  @commands.command()
  async def edit(self,ctx,nama,harga):
    myquery = { nama : harga }
    
    newvalues = { "$set": { "address": "Canyon 123" } }
    mycol.update_one(myquery, newvalues)

def setup(client):
  client.add_cog(logs(client))