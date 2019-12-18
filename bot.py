import discord

TOKEN = ""   #TOKEN MUST BE PLACED INSIDE THE DOUBLE QUOTES

SKIP_BOTS=FALSE

cliet =discord.Client()

@client.event
async def on_ready():
print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
print('Created By Ravi')
for member in client.get_all_members():
        if member.bot and SKIP_BOTS:
            continue
        await member.ban(reason="Banned by BanBot", delete_message_days=7)
        print(f"Banned {member.display_name}!")
    print("Banning is complete!")

client.run(TOKEN)
