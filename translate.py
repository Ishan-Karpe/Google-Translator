import googletrans, asyncio


async def main(input_text):
    # lang = googletrans.LANGUAGES
    # print(lang) # there are a LOT languages (over 100), organized by their language code
    trans = googletrans.Translator() # create a translator object
    translated=await trans.translate(input_text) # dectected language to english, or specifiy dest() to translate to a specific language
    print(translated.text) # print the translated text


    #dectect before translating
    texts = "Hello, Hola, Bonjour, Ciao, Namaste, Salaam, Konnichiwa, Ni Hao, Hallo, Shalom, Ola, Marhaba, Zdravstvuyte, Merhaba, Sawubona"

    dt1 = await trans.detect(texts)
    print(dt1) # print the detected language code

    translated = await trans.translate(texts, dest='mr', src=dt1.lang) # translate to Marathi
    print(translated.text)

    translated = await trans.translate(input_text, dest='es', src=dt1.lang) # translate to Marathi
    print(translated.text)

asyncio.run(main("to be or not to be"))

# async is used to make the function asynchronous, so it can run in parallel with other functions
# await is used to wait for the function to finish, so the program doesn't continue until the function is done
# asyncio.run() is used to run the asynchronous function

#From one to another


'''In Summary:
1. Create a Translator object using googletrans.Translator()
2. Use the translate() method to translate text
3. Use the detect() method to detect the language of text
4. Use the src parameter to specify the source language
5. Use the dest parameter to specify the destination language
6. Use the text attribute to get the translated text'''