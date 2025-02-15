import googletrans, asyncio


async def main():
    # lang = googletrans.LANGUAGES
    # print(lang) # there are a LOT languages (over 100), organized by their language code
    trans = googletrans.Translator() # create a translator object
    translated=await trans.translate('Hola', dest='mr') # dectected language to english, or specifiy dest() to translate to a specific language
    print(translated.text) # print the translated text


asyncio.run(main())

# async is used to make the function asynchronous, so it can run in parallel with other functions
# await is used to wait for the function to finish, so the program doesn't continue until the function is done
# asyncio.run() is used to run the asynchronous function