from bs4 import BeautifulSoup
from wit import Wit
import requests

class Bot:
    def __init__(self, client):
        country = None
        self.client = Wit(client)

    def message_wit(self, query):
        global msg
        query = str(query)
        msg = self.client.message(query)  # message the Wit api as a client

        return msg

    def get_values(self, entities, entity):

        if entity not in entities:  # returns none if unknown entity
            return None

        value = entities[entity][0]['value']  # get value from Wit response

        if not value:
            return None

        if isinstance(value, dict) == True:
            return value['value']
        else:
            return value

    def get_precautions(self):
        global ans

        ans = ('''
1) Frequently wash your hands with warm water and soap
2) Maintain a distance of at least 1 metre from anyone coughing or sneezing
3) Avoid touching your eyes, nose and mouth
4) Cover your mouth when coughing or sneezing
5) Stay at home and self isolate if you feel unwell
6) Seek medical attention if you experience flu-like symptoms
7) Follow advice given by your healthcare provider
8) Avoid traveling thorugh hotspots (areas where Covid-19 is spreading widely)
9) Be vigilant against fake news and cautious when sourcing information
10) Keep your wits about yourself and don't panic''')
        return ans

    def get_not_do(self):  # i literally couldn't come up with a better name
        global ans

        ans = ('''
1) Smoking
2) Wearing multiple masks
3) Taking antibiotics
4) Believe anything posted online
5) Panic''')
        return ans

    def explain_disease(self):
        global ans
        ans = ('''
Covid-19 is a recently discovered member of the Coronavirus family.
This new virus and disease was unknown before the outbreak 
began in Wuhan, China in December 2019.''')
        return ans

    def get_stats(self, intent, country):
        global ans

        base_URL = 'https://www.worldometers.info/coronavirus/'

        if (country != None):  # check if a country is given
            URL = base_URL + 'country/' + country
        else:
            URL = base_URL

        statsPage = requests.get(URL)

        statsContent = BeautifulSoup(statsPage.content, 'html.parser')

        # total infections,deaths and recoveries
        stats = statsContent.find_all(
            'div', attrs={'class': 'maincounter-number'})

        try:  # return infections,deaths or recoveries
            if (intent == 'get_infections'):
                status = " are infected"

            elif (intent == 'get_deaths'):
                status = " are dead"

            elif (intent == 'get_recoveries'):
                status = " have recovered"

            strip = ((stats[0]).text).rstrip("\n ")  # remove line breaks

            if (country != None):
                ans = "Currently " + strip + status + " in " + country
            else:
                ans = "Currently " + strip + status

        except IndexError:  # attempting to access the stats of a page that doesn't exist should throw an error
            ans = "There are no cases of Covid-19 in " + country

        return ans

    def process_message(self, msg):
        global ans
        try:
            # extract values from entities
            entities = msg['entities']
            myth = self.get_values(entities, 'myths')
            print(myth)

            intent = self.get_values(entities, 'intent')
            print(intent)

            country = self.get_values(entities, 'location')
            if (country != None):
                country = country.capitalize()  # Capitalize first letter
            print(country)

            info = self.get_values(entities, 'info')
            print(info)

            if intent:
                if (intent == 'get_infections' or intent == 'get_deaths' or intent == 'get_recoveries'):
                    ans = self.get_stats(intent, country)

                elif (intent == 'explain_disease'):
                    ans = self.explain_disease()

                elif (intent == 'get_precautions'):
                    ans = self.get_precautions()

                elif (intent == 'get_not_do'):  # its literally midnight my brain is not working
                    ans = self.get_not_do()

            elif myth:
                from myths import debunk_myth
                ans = debunk_myth(myth)

            elif info:
                from info import get_info
                ans = get_info(info)

            else:
                ans = ("Sorry I couldn't get that")

        except Exception as e:
            print(e)
            ans = "An error occurred"

        return ans