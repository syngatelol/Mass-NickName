import discord

USER_TOKEN = 'put your user token here'

SERVER_ID = 'put your server id here'

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

    server = bot.get_guild(int(SERVER_ID))
    
    bot_member = server.get_member(bot.user.id)
    
    members_sorted = sorted(server.members, key=lambda member: member.top_role.position, reverse=True)

    for member in members_sorted:
        if bot_member.top_role.position > member.top_role.position:
            new_nickname = ".gg/eviction"
            try:
                await member.edit(nick=new_nickname)
                print(f"Nickname changed for {member.display_name} ({member.id})")
            except discord.errors.Forbidden:
                print(f"Skipping {member.display_name} ({member.id}) due to missing permissions")
        else:
            print(f"Skipping {member.display_name} ({member.id}) due to role hierarchy")

    print("All nicknames changed.")

bot.run(USER_TOKEN, bot=False)
