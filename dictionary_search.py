import requests

class DictionarySearch():
    def __init__(self):
        pass

    def search(self,word):
        request_url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+str(word)
        response = requests.get(request_url)
        if response.status_code == 200:
            data = response.json()[0].get("meanings")[0]
            print(word+". "+data.get("partOfSpeech")+". "+data.get("definitions")[0].get("definition"))
        else:
            data = response.json()
            print(data.get("title")+". "+data.get("resolution"))

d1 = DictionarySearch()
word = input("Word? ")
d1.search(word)
