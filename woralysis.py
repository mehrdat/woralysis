import sys
from langdetect import detect
from PyDictionary import PyDictionary
import re

class trt:
    def __init__(self,word=None):
        self.word=word
        self.dictionary = self.load_translation_data('words.txt')
        if self.word:
            self.en_fa()
        
        
    def load_translation_data(self,file_path):
        translation_data = {}
        try: 
            with open(file_path, 'r') as file:
                for line in file:
                    line = re.sub(r':\s+', ':', line)
                    key, value = line.strip().split(':')
                    translation_data[key] = value
        except FileNotFoundError:
            print('File not found')
        return translation_data
    
    # def en_fa(self):
    #     detected_language = detect(self.word)
    #     if detected_language == 'en':
    #         return self.en_to_fa(self.word)
    #     elif detected_language == 'fa':
    #         return self.fa_to_en(self.word)
    
    def en_fa(self):
        if self.word in self.dictionary.keys():#[w.strip() for w in self.dictionary.keys()]:
            return self.en_to_fa()
        elif self.word in self.dictionary.values():#[w.strip() for w in self.dictionary.values()]:
            return self.fa_to_en()
    
    def en_to_fa(self):
        words = self.word.split()
        
        translated_words = []
        for word in words:
            translated_word = self.dictionary.get(word, 'could not find')
            translated_words.append(translated_word)
        return ' '.join(translated_words)
    
    def fa_to_en(self):
        
        for _,value in self.dictionary.items():
            if self.word in value.split(","):
                return next((k for k, v in self.dictionary.items() if self.word == v or self.word in v.split(",")), None)
        
        # for key, value in self.dictionary.items():
            
        #     if (value == self.word) or (self.word in value.split(",").strip()) :
        #         return key
        return "Word not found"
    
    def __str__(self):
        return str(self.en_fa())

    
# dictionary=PyDictionary()
# print (dictionary.meaning("obituary"))
# print (dictionary.synonym("baricate"))
# print (dictionary.antonym("baricate"))
# print (dictionary.translate("obituary",'fa'))

def main():
    file_path = "words.txt"

    while True:
        text = input("Enter the text to translate (or 'q' to quit): ")
        if text.lower() == "q":
            break

        print("Translated text:", trt(text))

if __name__ == "__main__":
    main()


#print(trt("cat,dog"))


