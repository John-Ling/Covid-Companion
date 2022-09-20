from ast import parse
from wit import Wit

def main():
    client = Wit("FJFYEZABWC6GHMP6UA2UHW74GSVRWGUM")
    while True:
        query = str(input("Enter query: "))
        response = client.message(query)
        print(response)
        entities = response["entities"]
        print(entities)
        intents = response['intents']
        print(intents)


        myth = get_values(entities, 'myths:myths')
        print(myth)

        if myth is not None:
            print("Myth")

        intent = response['intents']
        print(intent)

        country = get_values(entities, 'wit$location:location')
        if (country != None):
            country = country.capitalize()  # Capitalize first letter
        print(country)

        info = get_values(entities, 'info:info')
        print(info)

        # if intent:
        #     if (intent == 'get_infections' or intent == 'get_deaths' or intent == 'get_recoveries'):
        #         ans = function()
        #     elif (intent == 'explain_disease'):
        #         ans = function()
        #     elif (intent == 'get_precautions'):
        #         ans = function()
        #     elif (intent == 'get_not_do'):
        #         ans = function()
        #     elif myth:
        #         ans = function()
        #     elif info:
        #         ans = function()
        #     else:
        #         ans = ("Sorry I couldn't get that")
        

def get_values(entities, entity):
        if entity not in entities:  # returns none if unknown entity
            return None

        value = entities[entity][0]['value']  # get value from Wit response
        print(f"Value: {value}")
        if not value:
            return None

        if isinstance(value, dict) == True:
            return value['value']
        else:
            return value

def parse_location_test():
    data = {'wit$location:location': [{'id': '946933389103387', 'name': 'wit$location', 'role': 'location', 'start': 21, 'end': 26, 'body': 'india', 'confidence': 0.999, 'entities': [], 'resolved': {'values': [{'name': 'India', 'domain': 'country', 'coords': {'lat': 22, 'long': 79}, 'timezone': 'Asia/Kolkata', 'external': {'geonames': '1269750', 'wikidata': 'Q668', 'wikipedia': 'India'}, 'attributes': {}}, {'name': 'Piriyāpatna', 'domain': 'locality', 'coords': {'lat': 12.334970474243, 'long': 76.100730895996}, 'timezone': 'Asia/Kolkata', 'external': {'geonames': '1259535', 'wikidata': 'Q2738759', 'wikipedia': 'Piriyapatna'}, 'attributes': {}}]}, 'type': 'resolved'}]}
    data = data['wit$location:location']
    data = data[0]['resolved']['values'][0]['name']
    print(data)

def parse_intent_test():
    data = {'text': 'How many are dead in india', 'intents': [{'id': '165231897808831', 'name': 'get_deaths', 'confidence': 0.9206}], 'entities': {'wit$location:location': [{'id': '946933389103387', 'name': 'wit$location', 'role': 'location', 'start': 21, 'end': 26, 'body': 'india'
, 'confidence': 0.999, 'entities': [], 'resolved': {'values': [{'name': 'India', 'domain': 'country', 'coords': {'lat': 22, 'long': 79}, 'timezone': 'Asia/Kolkata', 'external': {'geonames': '1269750', 'wikidata': 'Q668', 'wikipedia': 'India'}, 'attributes': {}}, {'name':
 'Piriyāpatna', 'domain': 'locality', 'coords': {'lat': 12.334970474243, 'long': 76.100730895996}, 'timezone': 'Asia/Kolkata', 'external': {'geonames': '1259535', 'wikidata': 'Q2738759', 'wikipedia': 'Piriyapatna'}, 'attributes': {}}]}, 'type': 'resolved'}]}, 'traits': {
}}

    data = data['intents'][0]['name']
    print(data)

def parse_entities_test():
    data = {'info:info': [{'id': '211cc832-6ba1-4b68-a3bf-23e07898505f', 'name': 'info', 'role': 'info', 'start': 13, 'end': 21, 'body': 'symptoms', 'confidence': 1, 'entities': [], 'value': 'symptoms', 'type': 'value'}]}
    value = data['info:info'][0]['value']
    print(value)


def function():
    print("Function invoked")

if __name__ == "__main__":
    parse_entities_test()