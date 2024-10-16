import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28088290"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6998f2c585fdce65ac72dfa23d02b6ec")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Ramji:<db_Ramji@2019@ramji.hn1y5.mongodb.net/?retryWrites=true&w=majority&appName=Ramji")
