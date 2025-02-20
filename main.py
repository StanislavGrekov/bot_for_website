import telebot
from dotenv import load_dotenv
import os
from connect import cursor,conn

load_dotenv()

bot_key = os.getenv('BOT_KEY')

bot = telebot.TeleBot(bot_key)

@bot.message_handler()
def get_uesr_text(message):

        cursor.execute('''
                        select w_c.name, w_c.phone, w_c.message, w_c.time_create from website_clients as w_c
                        where not w_c.state;
                             ''')

        data = cursor.fetchall()

        for element in data:
            messages = f"От пользователя {element[0]} с тел.номером {element[1]} пришло сообщение:\n{element[2]}"
            bot.send_message(message.chat.id, messages)

            request_to_update_data = "UPDATE website_clients SET state = %s WHERE name = %s AND phone = %s AND message = %s"
            cursor.execute(request_to_update_data, (True, element[0], element[1], element[2]))
            conn.commit()

bot.polling(none_stop=True)
