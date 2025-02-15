import googletrans, asyncio


async def main():
    # lang = googletrans.LANGUAGES
    # print(lang) # there are a LOT languages (over 100), organized by their language code
    trans = googletrans.Translator() # create a translator object
    translated=await trans.translate('Hola') # dectected language to english, or specifiy dest() to translate to a specific language
    print(translated.text) # print the translated text


    #dectect before translating
    texts = "Hello, Hola, Bonjour, Ciao, Namaste, Salaam, Konnichiwa, Ni Hao, Hallo, Shalom, Ola, Marhaba, Zdravstvuyte, Merhaba, Sawubona"

    dt1 = await trans.detect(texts)
    print(dt1) # print the detected language code

    translated = await trans.translate(texts, dest='mr', src=dt1.lang) # translate to Marathi
    print(translated.text)

asyncio.run(main())

# async is used to make the function asynchronous, so it can run in parallel with other functions
# await is used to wait for the function to finish, so the program doesn't continue until the function is done
# asyncio.run() is used to run the asynchronous function

#From one to another
