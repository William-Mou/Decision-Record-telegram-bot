## 決策紀錄機器人 Decision Record telegram bot

可以幫一個 Telegram 群組記錄所有人的借貸關係，並且計算出只需要一個人就可以償還所有債務的 Telegram 機器人。 

## 設置
如果要在本機上運行的話，你會需要：

* Python
* [python-telegram-bot](https://python-telegram-bot.org/)

別忘記要跟[ @BotFather](https://telegram.me/BotFather) 拿取 token，並且在資料夾中創建 ```config.ini``` ，內容如下
```ini
[TELEGRAM]
ACCESS_TOKEN = ;在這裡放入 token 
WEBHOOK_URL = 
```
## 使用
[Telegram Bot 連結](t.me/)  
加入群組後，可以輸入以下指令：
```
/start - 開始紀錄
/add - 新增新判斷
/edit - 修改最近一筆判斷
/print - 列印時程表
/help - 列出所有可以輸入的指令以及其功用
```

---

## Decision Record Telegram Bot
An accounting bot for Telegram Messeenger to keep track of who borrowed or lent money to whom. Also, calculate a way to clear all the loans with only one person. 

## Setup
To run the bot yourself, you will need:
* Python
* [python-telegram-bot](https://python-telegram-bot.org/)

Don't forget to get a bot token from [@BotFather](https://telegram.me/BotFather) and create a new file called ```config.int``` in your folder. The following is the content.  
```ini
[TELEGRAM]
ACCESS_TOKEN = ;put your token here
WEBHOOK_URL = 
```
## How To Use
[Money Calculate Telegram Bot](t.me/)  
Put the bot in a chat, and you can type in the following commands to run the bot.
```
/start - launch the bot and start accounting
/add - add a record to list
/edit - edit last record in list
/print - print your Decision Timeline
/help - list all the commands
```