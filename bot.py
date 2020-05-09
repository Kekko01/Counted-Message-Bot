import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from credenziali import *
import sys, time
import os

telegrambot = telepot.Bot("TELEGRAM_TOKEN")
channel_id = 0

def telegram_chat(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(msg)
    if content_type == "text" and msg['text'] == "/start":
        if chat_id > 0:
            telegrambot.sendMessage(chat_id,"Ciao! Grazie per avermi avviato!! Io ti creerò un messaggio uguale a quello che mi invierai e ti risponderò con un messaggio con il contatore di visite, così da poterlo inoltrare a chi vuoi e vedere quante persone lo vedono!\nTi consiglio vivamente di non inviarmi dati sensibili e per trasparenza puoi controllare il codice del bot su GitHub da qui: https://github.com/Kekko01/Counted-Message-Bot \n\nHi! Thanks for starting me !! I will create a message equal to what you send me and I will reply with a message with the hit counter, so that I can forward it to whoever you want and see how many people see it!\nI strongly advise you not to send me sensitive data and for transparency you can check the bot code on GitHub from here: https://github.com/Kekko01/Counted-Message-Bot\n\nBot creato da @Kekko01, canale ufficiale @Kekko01Channel\nBot created by @Kekko01, official channel @Kekko01Channel")
        else:
            telegrambot.sendMessage(chat_id,"Ciao! Grazie per avermi avviato nel gruppoo!! Io vi creerò un messaggio uguale a quello che mi invierete e vi risponderò con un messaggio con il contatore di visite, così da poterlo inoltrare a chi volete o anche no e vedere quante persone lo vedono!\nVi consiglio vivamente di non inviarmi dati sensibili e per trasparenza potete controllare il codice del bot su GitHub da qui: https://github.com/Kekko01/Counted-Message-Bot \n\nHi! Thanks for starting me in the group !! I will create a message equal to the one you send me and I will reply with a message with the hit counter, so that I can forward it to whoever you want or not and see how many people see it! - I strongly advise you not to send me sensitive data and for transparency you can check the bot code on GitHub from here:https://github.com/Kekko01/Counted-Message-Bot\n\nBot creato da @Kekko01, canale ufficiale @Kekko01Channel\nBot created by @Kekko01, official channel @Kekko01Channel")
    else:
        message=msg['message_id']
        #print(message)
        try:
            telegrambot.forwardMessage(channel_id,chat_id, message)
            with open("num.txt","r") as target:
                #print(text)
                message = int(target.readline())
            telegrambot.forwardMessage(chat_id,channel_id, message)
            telegrambot.deleteMessage((channel_id, message))
            with open("num.txt","w") as target:
                target.write(str(message+1))
        except:
            telegrambot.sendMessage(chat_id,"Mi dispiace, non sono riuscito a inoltrare il tuo messaggio, cambia tipo di messaggio\nSorry, I was unable to forward your message, change message type")


telegrambot.message_loop(telegram_chat)

while True:
    time.sleep(2)
