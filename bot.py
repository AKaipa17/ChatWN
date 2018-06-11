from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl import types, functions
from telethon.tl.types import InputPeerUser
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.types import UpdateShortMessage
from telethon import utils
from telethon.tl.functions.messages import GetInlineBotResultsRequest
from telethon.tl.functions.messages import SendInlineBotResultRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from time import sleep
from flask import Flask
from telethon.tl.functions.channels import JoinChannelRequest
import os
import sched, time
import random
import string
from threading import Timer
from datetime import timezone
from datetime import datetime
from multiprocessing import Pool
import pytz
import asyncio
import threading
import psutil
from threading import Thread
from multiprocessing import Process
from multiprocessing.dummy import Pool as ThreadPool
from flask import send_from_directory
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon import events
import sys


app = Flask(__name__)
kaipa = 259885177
oratorID = 566539993
otryad = PeerChannel(1327713488)
bot = "ChatWarsBot"
botid = 265204902



def main():
	global kaipa
	global bot
	global botid
	global otryad
	global oratorID


	client = TelegramClient("bot", 243918, '2ace13b37b702eb5407964ff753fc37d', spawn_read_thread=False, update_workers = 1)
	client.start()

	local_tz = pytz.timezone('Europe/Moscow')

	def mess(messag):
		client.send_message(bot, messag)

	def utc_to_local(utc_dt):
		local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
		return local_tz.normalize(local_dt)

	@client.on(events.NewMessage)
	def attack(update):
		global lastpin
		if update.message.from_id == oratorID and update.message.to_id == otryad:
			theMessage = update.message.message
			if "⚔️🖤" in theMessage:
				lastpin = "🖤"
				sleep(random.randint(1, 2))
				client.send_message(bot, "⚔Атака")
			elif "⚔️☘️" in theMessage:
				lastpin = "☘️"
				sleep(random.randint(1, 2))
				client.send_message(bot, "⚔Атака")
			elif "⚔️🍁" in theMessage:
				lastpin = "🍁"
				sleep(random.randint(1, 2))
				client.send_message(bot, "⚔Атака")
			elif "⚔️🐢" in theMessage:
				lastpin = "🐢"
				sleep(random.randint(1, 2))
				client.send_message(bot, "⚔Атака")
			elif "⚔️🦇" in theMessage:
				lastpin = "🦇"
				sleep(random.randint(1, 2))
				client.send_message(bot, "⚔Атака")
			elif "⚔️🍆" in theMessage:
				lastpin = "🍆"
				sleep(random.randint(1, 2))
				client.send_message(bot, "⚔Атака")
			elif "⚔️🌹" in theMessage:
				lastpin = "🌹"
				sleep(random.randint(1, 2))
				client.send_message(bot, "⚔Атака")

		if "Сводки с полей" in update.message.message:
			sleep(random.randint(10, 16))
			client.send_message(bot, "/report")

		if "Смелый вояка!" in update.message.message:
			print(lastpin)
			sleep(random.randint(1, 2))
			mess(lastpin)
			lastpin = "🦇"

		if "/go" in update.message.message:
			sleep(random.randint(7, 15))
			client.send_message(bot, "/go")

		if update.message.from_id == kaipa and "#les" in update.message.message:
			number_of = update.message.message.split()
			les(int(number_of[0]))

		if update.message.from_id == botid and "Твои результаты в бою" in update.message.message:
			print(update.message.message)
			sleep(random.randint(3, 5))
			client(ForwardMessagesRequest(from_peer=client.get_entity(PeerUser(botid)), id=[update.message.id], to_peer=client.get_entity(otryad)))

		if update.message.message == "Выносливость восстановлена: ты полон сил. Вперед, на поиски приключений!":
			if utc_to_local(datetime.utcnow()).hour > 1 and utc_to_local(datetime.utcnow()).hour < 7:
				corovan(2)
			else:
				les(3)

		if update.message.message == "test":
			threading.Timer(random.randint(2, 3), mess, ["🏅Герой"]).start()


	def les(num):
		if num>0:
			threading.Timer(random.randint(1, 4), mess, ["🗺Квесты"]).start()
			threading.Timer(random.randint(5, 7), mess, ["🌲Лес"]).start()
			threading.Timer(random.randint(480,600), les, [num-1]).start()

	def corovan(num):
		if num>0:
			sleep(random.randint(1, 5))
			client.send_message(bot, "🗺Квесты")
			sleep(random.randint(2, 4))
			client.send_message(bot, "🗡ГРАБИТЬ КОРОВАНЫ")
			sleep(random.randint(480, 600))
			corovan(num-1)
	client.idle()



@app.route('/')
def root():
	return 'hi'

if __name__ == '__main__':
	backProc = Process(target = main, args=())
	backProc.start()
	port = int(os.environ.get('PORT', 5020))
	app.run(host='0.0.0.0', port = port, debug=True, use_reloader=False)
