# -*- coding: UTF-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from modules import Decision
import logging
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

updater = Updater(
    token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(filename='bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

group = {}


def start(update, context):
    id = update.effective_chat.id
    if id not in group:
        group[id] = Decision.Decision(id)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="決策紀錄機器人在此為您服務，請輸入您投資的股票編號")
    group[id].set_stock_status(True)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def add(update, context):
    id = update.effective_chat.id
    group[id].set_bbi(context.args[0], 0)
    group[id].set_decision(context.args[1], 0)
    group[id].set_timeline(str(update.message.date), 0)


add_handler = CommandHandler('add', add)
dispatcher.add_handler(add_handler)


def edit(update, context):
    id = update.effective_chat.id
    group[id].set_decision(context.args[0], 1)
    group[id].set_timeline(str(update.message.date), 1)


edit_handler = CommandHandler('edit', edit)
dispatcher.add_handler(edit_handler)


def print(update, context):
    id = update.effective_chat.id

    group[id].show_stock()
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=open(str(id)+"_stock.png", 'rb'))

    group[id].print_pic()
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=open(str(id)+".png", 'rb'))


print_handler = CommandHandler('print', print)
dispatcher.add_handler(print_handler)


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
/start - 開始紀錄
/add - 新增新判斷
/edit - 修改最近一筆判斷
/print - 列印時程表
/help - 列出所有可以輸入的指令以及其功用

更多資訊：
For more help please see the project's page on Github
""")


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


def no(update, context):
    input = str(update.message.text).split()

    #ontext.bot.send_message(
    #    chat_id=update.effective_chat.id, text=update.message.text)

    id = update.effective_chat.id
    if group[id].get_stock_status() == True:
        group[id].set_stock(input[0])
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="決策紀錄機器人已紀錄您的股票編號")
        group[id].set_stock_status(False)
    else:
        group[id].set_bbi(input[0], 0)
        group[id].set_decision(input[1], 0)
        group[id].set_timeline(str(update.message.date), 0)


no_handler = MessageHandler(Filters.text & (~Filters.command), no)
dispatcher.add_handler(no_handler)


def unknown(update, context):
    id = update.effective_chat.id
    group[id].set_decision(context.args[0], 0)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="不好意思，我不清楚您的指令，可以查看/help以獲得更多資訊")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.start_polling()
updater.idle()
