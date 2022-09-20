from wit import Wit

def main():
    client = Wit("FJFYEZABWC6GHMP6UA2UHW74GSVRWGUM")
    while True:
        query = str(input("Enter query: "))
        response = client.message(query)
        entities = response["entities"]
        for entity in entities:
            print(entity)
        

def get_values(entities, entity):
        if entity not in entities:  # returns none if unknown entity
            return None

        value = entities[entity][0]['value']  # get value from Wit response

        if not value:
            return None

        if isinstance(value, dict) == True:
            return value['value']
        else:
            return value

if __name__ == "__main__":
    main()