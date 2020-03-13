import requests
from bs4 import BeautifulSoup as bs 

MainUrl = 'https://wooordhunt.ru/'
TargetUrl = 'https://wooordhunt.ru/'

def get_page(url=None):
    if url:
        resp = requests.get(url)
        return resp
    return False


class Parse():
    
    def __init__(self, raw_page):
        if raw_page: 
            self.page = bs(raw_page.text, 'html.parser') 
        else:
            pass

    def parse_title(self, ):
        title = self.page.find('h1').get_text().split('-')[0].strip()
        return title


    def parse_transcription(self, ):
        transcription = self.page.find_all('span', class_='transcription')[0].get_text().strip()
        return transcription

    def parse_definition_ru(self, ):
        definition = self.page.find("span", class_="t_inline_en").get_text().split(',')
        return definition
    
    def parse_phrases(self):
        phrases = self.page.find("div", class_="phrases").get_text()
        raw_list_phrases = phrases.split('   ')
        
        word_phrases = {}
        numb = 1

        for item in raw_list_phrases:
            try:
                res = item.split('\u2002—\u2002')
                word_phrases[numb] = { 'eng': res[0], 'rus': res[1],}
            except: 
                pass

            numb += 1
                
        return word_phrases



    def parse_phrases_example(self):

        # cleaning data 
        for item in phrases.split(' '):
            print(item.split('\u2002—\u2002'))

        #print(phrases)

        examples = soup.find_all('div', class_='block')[2]
        ru = examples.find_all('div', class_='ex_o')
        print(ru)
    

        print(phrases)
        return phrases
