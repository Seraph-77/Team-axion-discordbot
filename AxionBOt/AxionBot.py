import discord
import youtube_dl
import os
from discord.ext import commands
import random
from discord.utils import get
#Everything starts here stuff

client = commands.Bot (command_prefix = 'a.')
client.remove_command('help')

client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------')
    print('Version 2.0.0')
    print('thanks @FCCloud')
    print('thanks @Kam')
    print('----------')
    print('bot is active')
    print('----------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Satelite-77'))
    
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')




#Image commands

@client.command()
async def cartoons(ctx):
    await ctx.send('https://i.ytimg.com/vi/LTEhUi1DJbw/hqdefault.jpg')

@client.command()
async def pogchamp(ctx):
    await ctx.send('https://tenor.com/view/pogchamp-gif-7331571')

@client.command()
async def servermap(ctx):
    await ctx.send('Error: Unable to connect to Satelite-33: Interference')

@client.command()
async def aimassist(ctx):
    await ctx.send('https://pbs.twimg.com/media/EYeWl0tX0AEb-7R.jpg')







#8ball section
#_8Ball section

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
                 'It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Dont count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                'Very doubtful.'  ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#Default help


@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        color = discord.Colour.green()
    ) 

    embed.set_author(name='Help')
    embed.add_field(name='.ping', value='Returns Pong! and m/s', inline=True)
    embed.add_field(name='.8ball', value='ask 8ball a question!', inline=True)
    embed.add_field(name='.servermap', value='sends a screenshot of Kowas server map', inline=True)
    embed.add_field(name='.8ball', value='ask 8ball a question!', inline=True)
    embed.add_field(name='.building', value='pulls up an IDlist of all building materials', inline=True)
    embed.add_field(name='.(insert gun name)', value='pulls up an unturned gun and its info', inline=True)
    embed.add_field(name='.clear', value='clears 100 : you need delete message perms to do this', inline=True)
    embed.add_field(name='.pogchamp', value='it does what you think it does', inline=True)
    embed.add_field(name='.aimassist', value='look whos crying about aim assist instead of being good', inline=True)
    embed.add_field(name='.cartoons', value='( ͡° ͜ʖ ͡°)',inline=True)
    embed.add_field(name='.creator', value='Check out the bot creators stuff!',inline=True)
    embed.add_field(name='.version', value='determines the version of the bot',inline=True)
    embed.add_field(name='.github', value='link to github, along with a bot template',inline=True)
    embed.add_field(name='.website', value='link to server website, basic staff info, etc.',inline=True)
    embed.add_field(name='.admintools', value='an embed of some admin commands',inline=True)
    embed.add_field(name='.musichelp',value='pulls up a list of music commands and how to use', inline=True)
    await ctx.send(embed=embed)




#Music Embed

@client.command(pass_context=True)
async def musichelp(ctx):
    embed = discord.Embed(
        color = discord.Colour.dark_magenta()
    )

    embed.set_author(name='Music Commands')
    embed.add_field(name='.join',value='gets bot to join your VC in a server', inline=True)
    embed.add_field(name='.leave',value='gets bot to leave your VC in a server', inline=True)
    embed.add_field(name='.play ',value ='do a.play (URL) when inside a voice call with the bot to play music', inline=True)
    embed.add_field(name='.CQ',value='**IMPORTANT you must do this after each song to play a new song or it wont work**', inline=True)

    await ctx.send(embed=embed)






#Admintools embed


@client.command(pass_context=True)
async def admintools(ctx):  
    embed = discord.Embed(
        color = discord.Colour.purple()
    ) 

    embed.set_author(name='Admin tools')
    embed.add_field(name='.ping', value='Returns Pong! and m/s', inline=True)
    embed.add_field(name='.version', value='determines bot version', inline=True)
    embed.add_field(name='.testforcog', value='determines if all cogs loaded successfully', inline=True)
    embed.add_field(name='.website', value='Pulls up Metro Networks Unturneds website', inline=True)
    embed.add_field(name='.github', value='pulls up the Axion Bots Github rep. (note: only contributors will see it)', inline=True)
    embed.add_field(name='.creator', value='Shameless self promotion from Kowa', inline=True)
    
    await ctx.send(embed=embed)







#Gunlist commands






@client.command()
async def ace(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Ace')
@client.command()
async def avenger(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Avenger')
@client.command()
async def augewehr(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Augewehr')
@client.command()
async def backlash(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Backlash')
@client.command()
async def bluntforce(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Bluntforce')
@client.command()
async def woodbow(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Bow_(disambiguation)')
@client.command()
async def bulldog(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Bulldog')
@client.command()
async def callingcard(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Calling_Card')
@client.command()
async def cobra(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Cobra')
@client.command(aliases=['1911'])
async def _1911(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/1911')
@client.command()
async def compoundbow(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Compound_Bow')
@client.command()
async def crossbow(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Crossbow')
@client.command()
async def desertfalcon(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Desert_Falcon')
@client.command()
async def dragonfang(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Dragonfang')
@client.command()
async def eaglefire(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Eaglefire')
@client.command()
async def ekho(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Ekho')
@client.command()
async def fusilaut(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Fusilaut')
@client.command()
async def grizzly(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Grizzly')
@client.command()
async def hawkhound(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Hawkhound')
@client.command()
async def heartbreaker(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Heartbreaker')
@client.command()
async def hellsfury(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Hell%27s_Fury')
@client.command()
async def pdw(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Honeybadger')
@client.command()
async def kryzkarek(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Kryzkarek')
@client.command()
async def masterkey(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Masterkey')
@client.command()
async def matamorez(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Matamorez')
@client.command()
async def maplestrike(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Maplestrike')
@client.command()
async def nightraider(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Nightraider')
@client.command()
async def nykorev(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Nykorev')
@client.command()
async def peacemaker(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Peacemaker')
@client.command()
async def rifle(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Rifle')
@client.command()
async def rocketlauncher(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Rocket_Launcher')
@client.command()
async def sabertooth(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Sabertooth')
@client.command()
async def scalar(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Scalar')
@client.command()
async def schofield(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Schofield')
@client.command()
async def shadowstalker(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Shadowstalker')
@client.command()
async def snaperskya(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Snayperskya')
@client.command()
async def sportshot(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Sportshot')
@client.command()
async def teklowvka(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Teklowvka')
@client.command()
async def timberwolf(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Timberwolf')
@client.command()
async def viper(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Viper')
@client.command()
async def vonya(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Vonya')
@client.command()
async def yuri(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Yuri')
@client.command()
async def zubeknakov(ctx):
    await ctx.send('https://unturned.fandom.com/wiki/Zubeknakov')
@client.command()
async def building(ctx):
    await ctx.send('https://unturnedhub.com/items/structure')

@client.command()
async def creator(ctx):
    await ctx.send('Creators discord: @壊れた(Kowa)#1182 ')
    await ctx.send('Creators YT: https://www.youtube.com/channel/UCMxhPJ8O4i-63CM0or8i_cg?view_as=subscriber')
    await ctx.send('Creators twitter: https://twitter.com/ikowareta')

    


#Cog section


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')





#IMPORTANT!!!
#ADMINTOOLS
    




    
@client.command()
async def version(ctx):
    await ctx.send('Version 2.0.0')

@client.command()
async def github(ctx):
    await ctx.send('https://www.github.com/Kowaaaaa')

@client.command()
async def website(ctx):
    await ctx.send('https://www.sites.google.com/view/mnunturned')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)







#music (finished)
#Finished as of 10/6/2020






ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
 
 
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
 
@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()




@client.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.voice:
        
        channel = ctx.message.guild.voice_client
        await channel.disconnect()
 
 
@client.command(pass_context=True)
async def play(ctx, url):
 
    try:
        if os._exists("song.mp3"):
            os.remove("song.mp3")
    except PermissionError:
        await ctx.message.channel.send("Music is playing right now! Use +stop to stop it.")
 
    voice = get(client.voice_clients,guild=ctx.guild)
    ydl_options={
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key':'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '150'
        }],
 
    }
 
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        await ctx.message.channel.send("Loading music...")
        try:
            ydl.download([url])
        except:
            await ctx.message.channel.send("Error in loading music!")
            return
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            print(f"Renaming file : {file}")
            os.rename(file, "song.mp3")


            
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.1



@client.command()
async def cq(ctx):
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            await ctx.send('clearing songs')
            os.remove("song.mp3")










#token
client.run('insert token here')

#Bot made by @Kam and @~Kowareta~
#you do not have permission to use this code for your own bot
#this bot is designated for Metro Networks
#this bot was made as a management tool for my server and approved servers
#Special thanks to @RWBY, @Fluffy and @FCCloud for suggestions and help
