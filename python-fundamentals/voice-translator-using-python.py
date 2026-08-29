import googletrans
translator=googletrans.Translator()
translation=translator.translate("hello",dest="fr")
print(translation.text)

# print(googletrans.LANGUAGES)