from os import access
from wit import Wit

from config import API_TOKEN

class Bot:
    def __init__(self):
        self.client = Wit(API_TOKEN)
    
    def query_wit(self, message):
        answer = self.client.message(message)
        print(answer)

def main():
    bot = Bot()
    bot.query_wit("How can I stay safe")

if __name__ == "__main__":
    main()