import random
import requests
import discord
import json
import io
from pars import p1, p2, p3, p4, p5, p6, p7
from lists import hiest, money, out_hi, out_grub, table, photo, sabaton, lang, ozk
from matugi import mat
from discord.ext import commands

prf = "&"
client = commands.Bot(command_prefix=prf)
admin = "<@&880913860293443644>"
moder = "<@&880939501436940328>"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    await member.send(f"Добро пожаловать {member.mention} в наш Discord канал, \n "
                      f"чтоб просмотреть доступные комманды напишите &commands")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    my_files = [
        discord.File('gey.jpg'),
        discord.File('bro.jpg'),
        discord.File('sabaton.jpg'),
        discord.File('sabaton2.jpg'),
        discord.File('bender.jpg'),
        discord.File('bender2.jpg'),
        discord.File('mk1.jpg'),
        discord.File('mk2.jpg'),
        discord.File('mk3.jpg'),
        discord.File('mk4.webp'),
        discord.File('mk5.jpg'),
    ]
    msg_in = message.content
    m_out = message.channel
    if msg_in.startswith("$oh, nigger"):
        await m_out.send('Hello, massa :grinning:!')
    if msg_in.startswith('$hey, bot'):
        await m_out.send('What the fuck do you want?')
    if msg_in.startswith("$Расписание"):
        await m_out.send(':skull:| Время начала и окончания пар\n'
                         ':paperclip:| 1 пара: 08:30 - 10:05\n'
                         ':paperclip:| 2 пара: 10:20 - 11:55\n'
                         ':paperclip:| 3 пара: 12:10 - 13:45\n'
                         ':paperclip:| 4 пара: 14:15 - 15:50\n'
                         ':paperclip:| 5 пара: 16:05 - 17:40\n'
                         ':paperclip:| 6 пара: 17:50 - 19:25\n'
                         ':paperclip:| 7 пара: 19:35 - 21:10')
    if any(word in msg_in for word in p1):
        await m_out.send(':paperclip:| 1 пара: 08:30 - 10:05')
    if any(word in msg_in for word in p2):
        await m_out.send(':paperclip:| 2 пара: 10:20 - 11:55')
    if any(word in msg_in for word in p3):
        await m_out.send(':paperclip:| 3 пара: 12:10 - 13:45')
    if any(word in msg_in for word in p4):
        await m_out.send(':paperclip:| 4 пара: 14:15 - 15:50')
    if any(word in msg_in for word in p5):
        await m_out.send(':paperclip:| 5 пара: 16:05 - 17:40')
    if any(word in msg_in for word in p6):
        await m_out.send(':paperclip:| 6 пара: 17:50 - 19:25')
    if any(word in msg_in for word in p7):
        await m_out.send(':paperclip:| 7 пара: 19:35 - 21:10')
    if msg_in.startswith('Бот, спать' or 'бот, спать'):
        await m_out.send('Ок')
    if any(word in msg_in for word in photo):
        await m_out.send(file=(my_files[random.randint(0, 1)]))
    if any(word in msg_in for word in sabaton):
        await m_out.send(file=(my_files[random.randint(2, 3)]))
    if any(word in msg_in for word in ozk):
        await m_out.send(file=(my_files[random.randint(4, 9)]))
    if any(word in msg_in for word in money):
        await m_out.send(random.choice(out_grub))
    if any(word in msg_in for word in lang):  # питонька
        await m_out.send(":snake:")
    if any(word in msg_in for word in mat):
        await m_out.send(
            "<@&880913860293443644>, <@&880939501436940328>. Замечено нарушение: кожаный мешок возомнил себя крутым и начал материться!")
    if any(word in msg_in for word in hiest):
        await m_out.send(random.choice(out_hi))
    if any(word in msg_in for word in table):  # Саня который с охуенным столом, админ дискорда бомонки, firstnafanya
        await m_out.send('https://vk.com/firstnafanya')
    await client.process_commands(message)


@client.command(pass_context=True)
async def clear(ctx, cls=1000):
    await ctx.channel.purge(limit=cls)


@client.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)


@client.command(pass_context=True)
async def commands(ctx):
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(colour=discord.Color.blue(), title='Команды')
    emb.add_field(name='commands', value='Комманда для просмотра пользовательских комманд!')
    emb.add_field(name='clear', value='Комманда для очистки (1000)')
    emb.add_field(name='site', value='Комманда для перехода на сайт КФ МГТУ им.Баумана')
    emb.add_field(name='псевдокоманды',
                  value='Псевдокоманды имеют другой префикс -$- \n $Расписание\n $первая пара (7 всего)\n '
                        '--в будущем они дополнятся ;) --')
    emb.set_footer(text='Примеры выполнения => &ping (показывает пинг бота)| &clear')
    await ctx.send(embed=emb)


@client.command(pass_context=True)
async def rools(ctx):
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(colour=discord.Color.blue(), title='Правила')
    emb.add_field(name=":metal:",
                  value="Уважаемые студенты, вот список правил, которые необходимо соблюдать на данном сервере.\n 1. "
                        "На сервере запрещены прямые оскорбления(в любом канале)\n 2. Спамить можно только в каналах "
                        "для спама. Просим вас не мешать другим студентам.\n "
                        "3. Запрещено скидывать NSFW-контент и контент 18+ (Кровь и т.п.).\n 4. Запрещено скидывать "
                        "картинки/гифки/видео оскорбительного содержания.\n 5. Если в канале есть закреплённые "
                        "сообщения, обязательно их прочитать.")
    emb.set_footer(text='Берегите себя, ребята')
    await ctx.send(embed=emb)


@client.command()
async def ping(ctx):
    latency = client.latency
    await ctx.send(latency)


@client.command()
async def site(ctx):
    link = "https://bmstu-kaluga.ru/"
    await ctx.send(link)


client.run('ODYzODE2NTc3MTExMjkzOTUy.YOsZ4A.U5vcrzn-tI48IYBFkZ87pGF8990')
