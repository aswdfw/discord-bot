import discord
import asyncio

client = discord.Client()

token = "ODY5MTg4ODk5MjQ1Nzg1MDk4.YP6lPg.DQ7mhIvUEb4IlHql7_XiIC7o2BM"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('League of Legends')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "돼지당":
        await message.channel.send("나다") 

    if message.content == "돼지":
        await message.channel.send("잘생겼다")

    if message.content == "sans(샌즈)":
        await message.channel.send("만들수있다")
    if message.content == "구독":
        embed = discord.Embed(title="혜성TV,재환TV구독", description="좋아요도", color=0x00ff00)
        embed.add_field(name="찔리면 지금이라도 누르기 ㅇㅋ?", value="싫으면 나가든가",inline=True)
        embed.add_field(name="찔리면 지금이라도 누르기 ㅇㅋ? (2스택)", value="싫으면 나가든가 (2스택)",inline=True)
        embed.set_footer(text="구독자 300명을 원한다")
        await message.channel.send(embed=embed)

client.run(token)