"""
SUBMISSION FOR CODE JAM #9

Bot is located at https://wit.ai/WeirdInnit/Covid_Companion

Information sourced from:

https://www.worldometers.info/coronavirus/
https://www.who.int/health-topics/coronavirus#tab=tab_1
"""
# install with pip
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import threading
import requests

import time

from tkinter import *
import tkinter.font as tkFont

from config import API_TOKEN
from bot import Bot


class App():

    def __init__(self):
        self.bot = Bot(API_TOKEN)
        self.reply = None
        self.window = Tk()
        self.window.configure(bg='#F5F5F5')
        self.window.geometry("800x400")

        self.window.title("Covid Companion")

        self.titleFont = tkFont.Font(family="Courier New", size=20)
        self.replyFont = tkFont.Font(
            family="Courier New", size=13)  # font for bot replies
        self.entryFont = tkFont.Font(
            family="Courier New", size=15)  # font for text box
        self.newsFont = tkFont.Font(family="Courier New", size=10)

        self.title = Label(self.window, text="Covid Companion",
                           font=self.titleFont).pack()

        self.textBox = Entry(self.window, width=30,
                             bg='#DCDCDC', font=self.entryFont)
        self.textBox.pack(ipadx=10, ipady=8)

        # press enter to submit
        self.window.bind("<Return>", self.keyboard_submit)
        self.window.bind("<Escape>", self.end_program)

        self.askButton = Button(self.window, text="Ask",
                                width=7, height=2, command=self.button_submit)
        self.askButton.place(relx=1, x=-160, y=55, anchor=CENTER)

        self.newsThread = threading.Thread(
            target=self.news_countdown, args=(), daemon=True)
        self.newsThread.start()
        self.window.mainloop()

    def end_program(self, event):
        quit()

    def keyboard_submit(self, event):
        try:
            query = self.textBox.get()
            self.process(query)
        except:
            pass

    def button_submit(self):
        try:
            query = self.textBox.get()

            self.process(query)
        except:
            pass

    def display_news(self):
        global news

        news_URL = 'https://www.worldometers.info/coronavirus/#news'
        newsPage = requests.get(news_URL)
        newsContent = BeautifulSoup(newsPage.content, 'html.parser')

        try:
            news.destroy()
        except:
            pass

        news = newsContent.find_all('div', attrs={'class': 'news_body'})
        news = news[0].text  # gets first result from news section
        return news

    def news_countdown(self):
        timer = 5  # 5 minutes in seconds
        while True:
            time.sleep(1)
            timer -= 1
            if (timer == 0):
                timer = 300
                news = self.display_news()
                news = Label(self.window, text=news, font=self.newsFont)
                news.place(relx=1, x=-100, y=360, anchor=E)

    def process(self, query):  # get input from entry box and messages wit ai
        global reply
        replyText = ''' 
        '''
        self.bot.message_wit(query)
        from bot import msg
        self.bot.process_message(msg)
        from bot import ans

        try:  # check if there already is text
            reply.destroy()
        except:
            pass

        replyText = ans
        print(replyText)
        self.textBox.delete(0, 'end')  # clear text box
        reply = Label(self.window, text=replyText,
                      font=self.replyFont, bg='#F5F5F5')  # output text label
        reply.config(width=100, height=20)
        reply.pack()

    def get_features(self):
        ans = ('''
- Get current infections, deaths and recoveries in all countries
- Explain information about Covid-19 
- Give advice on how to stay safe
- Debunk common myths and misconceptions
- Displays updates on cases in different countries
''')
        reply = Label(window, text=ans, font=replyFont,
                      bg='#F5F5F5')  # output text label
        reply.config(width=100, height=20)
        reply.pack()


if __name__ == '__main__':
    app = App()
