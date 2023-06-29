import os
import telebot
import subprocess
from scrapy.selector import Selector

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, how are you doing?")

@bot.message_handler(commands=['stop'])
def stop_bot(message):
    bot.reply_to(message, "Bot is shutting down...")
    bot.stop_polling()

@bot.message_handler(commands=['scrape'])
def start_scraping(message):
    bot.reply_to(message, "Please enter the URL(s) you want to scrape, separated by commas:")
    bot.register_next_step_handler(message, scrape_pages)

def scrape_pages(message):
    urls = message.text.split(',')
    urls = [url.strip() for url in urls]
    bot.reply_to(message, "Starting to scrape the provided URLs...")

    try:
        for url in urls:
            process = subprocess.Popen(['scrapy', 'shell', url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True)

            # Send the Scrapy command to the shell and capture the output
            command = b'response.body\n'
            output, _ = process.communicate(command)

            # Create a Scrapy Selector from the response body
            response_selector = Selector(text=output.decode('utf-8'))

            # Extract links using Scrapy Selector
            links = response_selector.css('a::attr(href)').getall()

            # Print the links for debugging
            print(f"Links from {url}:")
            for link in links:
                print(link)

            # Post the links to Telegram
            if links:
                bot.send_message(message.chat.id, f"Links from {url}:")
                for link in links:
                    bot.send_message(message.chat.id, link)

    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred: {str(e)}")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
