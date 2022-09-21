from wit import Wit
from config import API_TOKEN
# tests to make requests to Wit's API and parse the results for intents, locations and named entities

def main():
    client = Wit(API_TOKEN)
    while True:
        query = str(input("Enter query: "))
        response = client.message(query)
        #print(response)
        entities = response["entities"]
        #print(entities)

        #intent = response['intents'][0]['name']
        #print(inten t)

        _get_intents = lambda response: response['intents'][0]['name'] if len(response['intents']) > 0 else None
        intents = _get_intents(response)
        print(intents)

        _get_myths = lambda entities: entities['myths:myths'][0]['value'] if 'myths:myths' in entities else None
        myths = _get_myths(entities)
        print(myths)

        _get_info = lambda entities: entities['info:info'][0]['value'] if 'info:info' in entities else None
        info = _get_info(entities)
        print(info)

        _get_country = lambda entities: entities['wit$location:location'][0]['resolved']['values'][0]['name'] if 'wit$location:location' in entities else None
        country = _get_country(entities)
        if (country != None):
            country = country.capitalize()  # Capitalize first letter
        print(country)

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
        
def parse_entities(data):
    return data['info:info'][0]['value']

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
    data = {'text': 'How many are dead in india', 'intents': [{'id': '165231897808831', 'name': 'get_deaths', 'confidence': 0.9206}], 'entities': {'wit$location:location': [{'id': '946933389103387', 'name': 'wit$location', 'role': 'location', 'start': 21, 'end': 26, 'body': 'india'
, 'confidence': 0.999, 'entities': [], 'resolved': {'values': [{'name': 'India', 'domain': 'country', 'coords': {'lat': 22, 'long': 79}, 'timezone': 'Asia/Kolkata', 'external': {'geonames': '1269750', 'wikidata': 'Q668', 'wikipedia': 'India'}, 'attributes': {}}, {'name':
 'Piriyāpatna', 'domain': 'locality', 'coords': {'lat': 12.334970474243, 'long': 76.100730895996}, 'timezone': 'Asia/Kolkata', 'external': {'geonames': '1259535', 'wikidata': 'Q2738759', 'wikipedia': 'Piriyapatna'}, 'attributes': {}}]}, 'type': 'resolved'}]}, 'traits': {
}}
    #data = {'wit$location:location': [{'id': '946933389103387', 'name': 'wit$location', 'role': 'location', 'start': 21, 'end': 26, 'body': 'india', 'confidence': 0.999, 'entities': [], 'resolved': {'values': [{'name': 'India', 'domain': 'country', 'coords': {'lat': 22, 'long': 79}, 'timezone': 'Asia/Kolkata', 'external': {'geonames': '1269750', 'wikidata': 'Q668', 'wikipedia': 'India'}, 'attributes': {}}, {'name': 'Piriyāpatna', 'domain': 'locality', 'coords': {'lat': 12.334970474243, 'long': 76.100730895996}, 'timezone': 'Asia/Kolkata', 'external': {'geonames': '1259535', 'wikidata': 'Q2738759', 'wikipedia': 'Piriyapatna'}, 'attributes': {}}]}, 'type': 'resolved'}]}
    data = data['entities']
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
    #data = {'info:info': [{'id': '211cc832-6ba1-4b68-a3bf-23e07898505f', 'name': 'info', 'role': 'info', 'start': 13, 'end': 21, 'body': 'symptoms', 'confidence': 1, 'entities': [], 'value': 'symptoms', 'type': 'value'}]}
    data = {'text': 'What are the symptoms', 'intents': [], 'entities': {'info:info': [{'id': '211cc832-6ba1-4b68-a3bf-23e07898505f', 'name': 'info', 'role': 'info', 'start': 13, 'end': 21, 'body': 'symptoms', 'confidence': 1, 'entities': [], 'value': 'symptoms', 'type': 'value'}]}
, 'traits': {}}
    value = data['entities']['info:info'][0]['value']
    print(value)


def function():
    print("Function invoked")

if __name__ == "__main__":
    main()