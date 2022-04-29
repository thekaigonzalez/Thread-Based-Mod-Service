import discord

client = discord.Bot(debug_guilds=[969083846110879744], intents=discord.Intents.all())

mod_chan = 969266297504428092

users = {}
usersX = {}
usersO = {}

cu = 0;

@client.event
async def on_message(msg: discord.Message):
    global cu
    if (msg.author.bot): return
    if (cu == None): cu = 0;

    if (msg.guild == None and users.get(msg.author.id) == None):
        ms = client.get_channel(mod_chan)
        
        s = await ms.send("A new thread has opened!")
        cu += 1
        eth = await s.create_thread(name="User-" + str(cu), auto_archive_duration=60)
        users[msg.author.id] = eth.id
        usersX[eth.id] = msg.author.id
        usersO[eth.id] = msg.author
        await ms.send(f"**{msg.author.display_name}:** " + msg.content)
        
    
    elif (users.get(msg.author.id) != None and msg.guild == None):
        await client.get_channel(users[msg.author.id]).send(f"**{msg.author.display_name}:**  " + msg.content)

    elif (usersX.get(msg.channel.id) != None):
        l = usersO.get(msg.channel.id)

        await l.send(f"**{msg.author.display_name}:** " + msg.content)
    
        


@client.slash_command(name = "close", description = "Closes the current thread based on the channel you're in.")
async def _h(ctx):
    await ctx.respond("closing thread...")
    
    

    if (usersO.get(ctx.channel.id) != None):
        await usersO[ctx.channel.id].send("This thread has been closed by a moderator.")
        del usersO[ctx.channel.id]
        del users[ctx.author.id]
        del usersX[ctx.channel.id]
        await ctx.channel.delete();


client.run("")