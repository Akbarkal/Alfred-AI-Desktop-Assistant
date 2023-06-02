####------------------------------- Translator ------------------------------


################################### Import Modules ##################################

from MainFiles.Database.modules import sr, Translator, speak, playsound, gTTS, os, sys, requests

################################### All Language Code Dict ##########################

dic = ('afrikaans', 'af', 'albanian', 'sq',
	'amharic', 'am', 'arabic', 'ar',
	'armenian', 'hy', 'azerbaijani', 'az',
	'basque', 'eu', 'belarusian', 'be',
	'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
	'bg', 'catalan', 'ca', 'cebuano',
	'ceb', 'chichewa', 'ny', 'chinese',
	'zh-cn', 'chinese',
	'zh-tw', 'corsican', 'co', 'croatian', 'hr',
	'czech', 'cs', 'danish', 'da', 'dutch',
	'nl', 'english', 'en', 'esperanto', 'eo',
	'estonian', 'et', 'filipino', 'tl', 'finnish',
	'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
	'gl', 'georgian', 'ka', 'german',
	'de', 'greek', 'el', 'gujarati', 'gu',
	'haitian creole', 'ht', 'hausa', 'ha',
	'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
	'hi', 'hmong', 'hmn', 'hungarian',
	'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
	'id', 'irish', 'ga', 'italian',
	'it', 'japanese', 'ja', 'javanese', 'jw',
	'kannada', 'kn', 'kazakh', 'kk', 'khmer',
	'km', 'korean', 'ko', 'kurdish (kurmanji)',
	'ku', 'kyrgyz', 'ky', 'lao', 'lo',
	'latin', 'la', 'latvian', 'lv', 'lithuanian',
	'lt', 'luxembourgish', 'lb',
	'macedonian', 'mk', 'malagasy', 'mg', 'malay',
	'ms', 'malayalam', 'ml', 'maltese',
	'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
	'mn', 'myanmar (burmese)', 'my',
	'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
	'pashto', 'ps', 'persian', 'fa',
	'polish', 'pl', 'portuguese', 'pt', 'punjabi',
	'pa', 'romanian', 'ro', 'russian',
	'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
	'serbian', 'sr', 'sesotho', 'st',
	'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
	'slovak', 'sk', 'slovenian', 'sl',
	'somali', 'so', 'spanish', 'es', 'sundanese',
	'su', 'swahili', 'sw', 'swedish',
	'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
	'te', 'thai', 'th', 'turkish',
	'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
	'ug', 'uzbek', 'uz',
	'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
	'yiddish', 'yi', 'yoruba',
	'yo', 'zulu', 'zu')

################################### Take query from user ############################

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,15)
    try:
        print('Recognizing....\n')
        query = r.recognize_google(audio, language='en-hi')
        print(f"You : {query}\n")
	
    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query.lower()

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold = 1
		audio = r.listen(source,0,6)
	try:
		print('Recognizing....\n')
		query = r.recognize_google(audio, language='en-hi')
		print(f"You : {query}\n")
		if "*" in query:
			query = query.replace('*','x')

	except Exception as e:
		print("Say that again Please...")
		return "None"
	
	return query.lower()

################################### Take query from user in Hindi ###################

def tookHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,6)

    try:
        print('Recognizing....\n')
        query = r.recognize_google(audio, language='hi')

    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query.lower()

################################### Convert query Eng to Hin ########################

def HinToEng():
	query = tookHindi()
	print(query)
	try:
		translator = Translator()
		text_to_translate = translator.translate(query)
		text = text_to_translate.text
		text1 = text.lower()
		print(f"You said : {text1}")
		if text1==None:
			pass
		else:
			return text1
	except Exception as e:
		pass

################################### Take query from user in Hindi ###################

def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....\n')
        query = r.recognize_google(audio, language='hi')
        print(f"You : {query}\n")

    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query

################################### Eng to any Language Translator ##################

def destination_language(query, user):
	to_lang = query.lower()
	to_lang = to_lang.replace(' ','')

	if to_lang in dic:
		to_lang1 = dic[dic.index(to_lang)+1]
		speak("ok. what would you like to translate")
		query1 = takeCommand()
		if query1 =='None':
			pass
		else:
			translator = Translator()
			text_to_translate = translator.translate(query1, dest=to_lang1)
			text = text_to_translate.text
			speak1 = gTTS(text=text, lang=to_lang1, slow=False)
			speak1.save("captured_voice.mp3")
			print(f"In {to_lang}, {query1} is ")
			speak(f"In {to_lang}, {query1} is ")
			print(text)
			playsound('captured_voice.mp3')
			os.remove('captured_voice.mp3')
	else:
		speak(f"Sorry {user}, I can't translate into {to_lang} yet.")

def short_trans(lang, query, user):
	to_lang = lang.lower()
	to_lang = to_lang.replace(' ','')

	try:
		if to_lang in dic:
			to_lang1 = dic[dic.index(to_lang)+1]
			query1 = query
			if query1 =='None':
				pass
			else:
				translator = Translator()
				text_to_translate = translator.translate(query1, dest=to_lang1)
				text = text_to_translate.text
				speak1 = gTTS(text=text, lang=to_lang1, slow=False)
				speak1.save("captured_voice.mp3")
				print(f"In {to_lang}, {query1} is ")
				speak(f"In {to_lang}, {query1} is ")
				print(text)
				playsound('captured_voice.mp3')
				os.remove('captured_voice.mp3')
		else:
			speak(f"Sorry {user}, I can't translate into {to_lang} yet.")
	except Exception as e:
		speak(f"Sorry {user}, I can't translate into {to_lang} yet.")

################################### Hindi to any Lang Translator ####################

def hindi_language(query, user):
	to_lang = query.lower()
	to_lang = to_lang.replace(' ','')

	if to_lang in dic:
		to_lang1 = dic[dic.index(to_lang)+1]
		speak("ok. what would you like to translate")
		query1 = TakeHindi()
		if query1 =='None':
			pass
		else:
			translator = Translator()
			text_to_translate = translator.translate(query1, dest=to_lang1)
			text = text_to_translate.text
			print(text)
			speak1 = gTTS(text=text, lang=to_lang1, slow=False)
			speak1.save("captured_voice.mp3")
			print(f"In {to_lang}, {query1} is ")
			speak(f"In {to_lang}, {query1} is ")
			print(text)
			playsound('captured_voice.mp3')
			os.remove('captured_voice.mp3')
	else:
		speak(f"Sorry {user}, I can't translate into {to_lang} yet.")

############################################### End #################################