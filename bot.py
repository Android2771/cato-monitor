import subprocess
import discord
import os

bot = discord.Bot()

@bot.command(name="video")
async def video(ctx, seconds: int = 20):     
    command = [
        'ffmpeg',
        '-f', 'v4l2',
        '-framerate', '30',
        '-video_size', '1280x720',
        '-c:v', 'mjpeg',
        '-i', '/dev/video0',
        '-f', 'pulse',
        '-i', 'default',
        '-t', str(seconds),
        '-c:v', 'libx264',
        'output.mov',
        '-y'
    ]
    
    await ctx.response.defer()
    result = subprocess.run(command, capture_output=True, text=True)

    # # Print the output
    print("Output:", result.stdout)
    print("Error:", result.stderr)
    print("Return Code:", result.returncode)
    
    # Create a discord.File object
    file = discord.File("output.mov")

    # Send the file in a follow-up response
    await ctx.followup.send(file=file)
   
@bot.command(name="picture")
async def picture(ctx):     
    command = [
        'fswebcam',
        '--frames', '10',
        '-r', '1280x720',
        '--no-banner',
        'output.jpg'
    ]
    
    await ctx.response.defer()
    result = subprocess.run(command, capture_output=True, text=True)

    # # Print the output
    print("Output:", result.stdout)
    print("Error:", result.stderr)
    print("Return Code:", result.returncode)
    
    # Create a discord.File object
    file = discord.File("output.jpg")

    # Send the file in a follow-up response
    await ctx.followup.send(file=file)

@bot.event
async def on_ready():
    await bot.sync() #sync the command tree
    print("Bot is ready and online")

@bot.event
async def on_ready():
        print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    print(message)

token = open("token.txt", "r").read().strip()
bot.run(token)