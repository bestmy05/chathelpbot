import discord
import asyncio
import sys, string, os, subprocess
import random
import datetime
import urllib
import urllib.request
from urllib.request import urlopen, Request
import bs4
import 급식

#참고자료 https://coding-y.tistory.com/9

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    def check(m):
        return m.channel.id == message.channel.id and m.author == message.author

    if message.content.startswith('!서버'):
        subprocess.run(r'C:\discordbot\버킷(1.15.1)\b.bat')
    
    if message.content.startswith('!멤버'):
        msg = message.channel.members
        await message.channel.send(msg)

    if message.content.startswith('!test'):
        await message.channel.send('테스트')

    if message.content.startswith('!잭팟'):
        jekpot_list = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
        out = random.sample(jekpot_list, 3)
        await message.channel.send(out)
        if out == [1,1,1]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [2,2,2]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [3,3,3]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [4,4,4]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [5,5,5]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [6,6,6]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [7,7,7]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [8,8,8]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [9,9,9]:
            await message.channel.send("ㅊㅋㅊㅋ")
        if out == [10,10,10]:
            await message.channel.send("ㅊㅋㅊㅋ")

    if message.content.startswith('!tts'):
        await message.channel.send("이것은 tts테스트 입니다.", tts=True)

    if message.content.startswith('!가위바위보'):
        rsp = ["가위", "바위", "보"]
        embed = discord.Embed(title="가위바위보", description="가위바위보를 시작합니다 10초내로 [가위,바위,보]를 써주세요!", color=0x00aaaa)
        channel = message.channel
        msg1 = await message.channel.send(embed=embed)
        try:
            msg2 = await client.wait_for('message', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await msg1.delete()
            embed = discord.Embed(title="가위바위보", description="시간초과!", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        else:
            await msg1.delete()
            bot_rsp = str(random.choice(rsp))
            user_rsp = str(msg2.content)
            answer = ""
            if bot_rsp == user_rsp:
                answer = "저는 " + bot_rsp + "를 냈고,당신은 " + user_rsp + "를 내셨습니다.\n" + "아쉽게도 비겼네요."
            elif (bot_rsp == "가위" and user_rsp == "바위") or (bot_rsp == "보" and user_rsp == "가위") or (bot_rsp == "바위" and user_rsp == "보"):
                answer = "저는 " + bot_rsp + "를 냈고, 당신은 " + user_rsp + "를 내셨습니다.\n" + "아쉽지만 제가 졌습니다."
            elif (bot_rsp == "가위" and user_rsp == "보") or (bot_rsp == "보" and user_rsp == "주먹") or (bot_rsp == "바위" and user_rsp == "가위"):
                answer = "저는 " + bot_rsp + "를 냈고, 당신은 " + user_rsp + "를 내셨습니다.\n" + "제가 이겼습니다!"
            else:
                embed = discord.Embed(title="가위바위보", description="앗!, 가위, 바위, 보 중에서만 내셔야죠....", color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
            embed = discord.Embed(title="가위바위보", description=answer, color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
    
    if message.content.startswith("!시간표"):
        split_sigan = message.content.split(" ")
        len_sigan = len(split_sigan)
        T = ['월', '화', '수', '목', '금', '토', '일']
        R = datetime.datetime.today().weekday()
        today_week = T[R]
        if len_sigan<=1:
            await message.channel.send("반을 입력해주세요.\n!시간표 [숫자만]")
        else:
            class_room = split_sigan[1]
            int_class_room = int(class_room)
            if int_class_room == 1:    
                embed = discord.Embed(title='1반 시간표', description='1반 시간표입니다.', color=discord.Colour.blurple())
                embed.add_field(name='월요일', value='영어 수학 역사 과학 정보 국어', inline=False)
                embed.add_field(name='화요일', value='영어 미술 과학 사회 기가 기가 체육', inline=False)
                embed.add_field(name='수요일', value='국어 체육 수학 사회 정보 역사', inline=False)
                embed.add_field(name='목요알', value='국어주제 영어 창체진로 진로 과학 스포츠 스포츠', inline=False)
                embed.add_field(name='금요일', value='체육 수학 국어 과학 영어주제 음악')
                await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("!급식"):
        embed = discord.Embed(
            title='대호중 급식',
            description='급식입니다.',
            colour=discord.Colour.green()
        )
        embed.add_field(name='오늘', value=급식.lunchtext(), inline=False)
        embed.add_field(name='내일', value=급식.lunchtextD1(), inline=False)
        embed.add_field(name='모래', value=급식.lunchtextD2(), inline=False)
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("!날씨"):
        learn = message.content.split(" ")
        len_learn = len(learn)
        if len_learn<=1:
            await message.channel.send('지역을 입력해주세요.\n!날씨 [지역]')
        else:
            location = learn[1]
            enc_location = urllib.parse.quote(location+'날씨')
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=' + enc_location
            print(url)
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
            todayBase = bsObj.find('div', {'class': 'main_info'})

            todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
            todayTemp = todayTemp1.text.strip()  # 온도
            print(todayTemp)

            todayValueBase = todayBase.find('ul', {'class': 'info_list'})
            todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
            todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
            print(todayValue)

            todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
            todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
            print(todayFeelingTemp)

            todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
            todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
            todayMiseaMongi3 = todayMiseaMongi2.find('dd')
            todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
            print(todayMiseaMongi)

            tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
            tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
            tomorrowTemp2 = tomorrowTemp1.find('dl')
            tomorrowTemp3 = tomorrowTemp2.find('dd')
            tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
            print(tomorrowTemp)

            tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
            tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
            tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
            tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
            print(tomorrowMoring)

            tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
            tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
            print(tomorrowValue)

            tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
            tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
            tomorrowAfter1 = tomorrowAllFind[1]
            tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
            tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
            tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
            print(tomorrowAfterTemp)

            tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
            tomorrowAfterValue = tomorrowAfterValue1.text.strip()

            print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

            embed = discord.Embed(
                title=learn[1]+ ' 날씨 정보',
                description=learn[1]+ '날씨 정보입니다.',
                colour=discord.Colour.gold()
            )
            embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
            embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
            embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
            embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
            embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
            embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
            embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
            embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
            embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
            embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태

            await message.channel.send(message.channel, embed=embed)
        

    async def on_error(event, *args, **kwargs):
	    #내용
	    return
access_token = os.environ["BOT_TOKEN"]
client.run('BOT_TOKEN')