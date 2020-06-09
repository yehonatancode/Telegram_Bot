import telepot

import json

import requests

import time

import random



token = '' #use your own token, for protection purposes.

URL = "https://api.telegram.org/bot{}/".format(token)





def get_url(url):

    response = requests.get(url)

    content = response.content.decode("utf8")

    return content





def get_json_from_url(url):

    content = get_url(url)

    js = json.loads(content)

    return js





def get_updates():

    url = URL + "getUpdates"

    js = get_json_from_url(url)

    return js





def get_last_chat_id_and_text(updates):

    num_updates = len(updates["result"])

    last_update = num_updates - 1

    text = updates["result"][last_update]["message"]["text"]

    chat_id = updates["result"][last_update]["message"]["chat"]["id"]

    return (text, chat_id)





def send_message(text, chat_id):

    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)

    get_url(url)





text, chat = get_last_chat_id_and_text(get_updates())

send_message(text, chat)



def general_message(chat_id, general_text):

    url = URL + "sendMessage?text={}&chat_id={}".format(general_text, chat_id)

    get_url(url)





def main():

    text, chat = get_last_chat_id_and_text(get_updates())

    start_msg = "Hey there! Would you like to play a guessing game? It's simple, just type a number between 1 and 1k"

    higher_msg = "you need to guess higher sir/madam"

    lower_msg = "you need to guess lower sir/madam"

    equal_msg = "Congratulations! it's a bingo"



    general_message(chat,start_msg)

    to_be_guessed = random.randint(1,1000)

    last_textchat = (None, None)

    flag = True

    while flag:

        text, chat = get_last_chat_id_and_text(get_updates())

        if (text, chat) != last_textchat:

           # send_message(text, chat)

            last_textchat = (text, chat)

            time.sleep(0.5)

            num = int(last_textchat[0])



            if num < to_be_guessed: general_message(chat,higher_msg)

            elif num > to_be_guessed : general_message(chat,lower_msg)

            else: general_message(chat,equal_msg)



         #if(last_textchat == "Exit"): flag=False







if __name__ == '__main__':

    main()





#https://api.telegram.org/bot<your-bot-token>/getme

#https://api.telegram.org/bot<your-bot-token>/getUpdates

#getting replies from the bot :

#https://api.telegram.org/bot1259018719:AAFJGpJfixEkBJBut-SyjFY43voF_aRBAIg/sendMessage?chat_id=698903663&text=TestReply



#TelegramBot = telepot.Bot(token)

#print (TelegramBot.getMe())

#TelegramBot.getUpdates()

#print(TelegramBot.getUpdates(649179764+1))