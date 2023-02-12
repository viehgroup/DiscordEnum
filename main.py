import subprocess
import discord

# Initialize discord client
client = discord.Client()

@client.event
async def on_ready():
    # Ask for Discord channel ID
    discord_channel_id = input('Enter your Discord channel ID: ')

    # Send message to discord channel
    await client.send_message(discord.Object(id=discord_channel_id), 'Target.com')

    # Ask for subdomain enumeration command
    subdomain_enumeration_command = input('Enter your subdomain enumeration command: ')

    # Process subdomain enumeration
    subdomain_enumeration = subprocess.run([subdomain_enumeration_command], stdout=subprocess.PIPE)

    # Ask for directory enumeration command
    directory_enumeration_command = input('Enter your directory enumeration command: ')

    # Process directory enumeration
    directory_enumeration = subprocess.run([directory_enumeration_command], stdout=subprocess.PIPE)

    # Write results to file
    with open('results.txt', 'w') as f:
        f.write(subdomain_enumeration.stdout.decode())
        f.write(directory_enumeration.stdout.decode())

    # Run nuclei with specified options
    nuclei = subprocess.run(['nuclei', '-l', 'results.txt', '-s', 'Critical,High,Medium,Low'], stdout=subprocess.PIPE)

    # Check for any severity
    if 'Critical' in nuclei.stdout.decode():
        await client.send_message(discord.Object(id=discord_channel_id), 'Critical severity found!')
    elif 'High' in nuclei.stdout.decode():
        await client.send_message(discord.Object(id=discord_channel_id), 'High severity found!')
    elif 'Medium' in nuclei.stdout.decode():
        await client.send_message(discord.Object(id=discord_channel_id), 'Medium severity found!')
    elif 'Low' in nuclei.stdout.decode():
        await client.send_message(discord.Object(id=discord_channel_id), 'Low severity found!')
    else:
        await client.send_message(discord.Object(id=discord_channel_id), 'No severity found.')

# Ask for Discord token
discord_token = input('Enter your Discord token: ')

client.run(discord_token)
