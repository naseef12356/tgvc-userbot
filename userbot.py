# import logging
from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> 1787529245:AAFo9UcclqJqi8DFrhI7JyV-DTsEDJSdJos STARTED')
idle()
app.stop()
print('\n>>> 1787529245:AAFo9UcclqJqi8DFrhI7JyV-DTsEDJSdJos STOPPED')
