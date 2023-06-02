####------------------------------- Main Function (Brain of Alfred) -----------------


################################### Import Modules ##################################

from MainFiles.Database.Chatbot import *
from MainFiles.Database.Command import *
from MainFiles.Database.Translator import *
from MainFiles.Database.Bulb import *
from MainFiles.sound.Sound import *
from MainFiles.Database.modules import *
#### END


################################### Query as Command ################################

def TaskExecution(permission, devices_list, User, contact_list, light, ReplyBrain, music_dir):
    openSound()
    Command = permission.replace("alfred","")
    if " " in Command:        
        query = Command
    else:
        query = takeCommand()
        if 'None' not in query:
            midSound()
    while True:
        try:
#-----------------------------logic for executing task based on query------------------------

            if ' wikipedia' in query:
                speak('Searching Wikipedia....')
                query = query.replace("wikipedia", "")
                query = qReplace(query)
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                printX(results)
                speak(results)
                speak('would you like to hear more')
                ask = takeCommand()
                if 'yes' in ask:
                    full_result = wikipedia.summary(query,5)
                    new_result = full_result.replace(results,"")
                    printX(new_result)
                    speak(new_result)
                else:
                    speak('okay')


####------------------------------------------Commands---------------------------------------

            elif "play " in query:
                if "youtube music" in query:
                    try:
                        song1 = qReplace(query).split("from")
                        song = song1[0].replace("play","")
                        printX('playing ' + song + 'from youtube music')
                        speak('playing ' + song + 'from youtube music')
                        url = playonytm("play",song)
                        webbrowser.open(url)
                        t.sleep(5)
                        pyautogui.press('space')
                    except Exception as e:
                        print(e)
                        printX(f"sorry {User} repeat that again")
                        speak(f"sorry {User} repeat that again")

                elif "youtube" in query:
                    try:
                        song1 = qReplace(query).split("from")
                        song = song1[0].replace("play","")
                        printX('playing ' + song + 'from youtube')
                        speak('playing ' + song + 'from youtube')
                        kit.playonyt(song)
                        t.sleep(5)
                    except Exception as e:
                        print(e)
                        printX(f"sorry {User} repeat that again")
                        speak(f"sorry {User} repeat that again")

                elif "downloaded " in query:
                    printX("Playing downloaded songs for you")
                    speak("Playing downloaded songs for you")
                    music("downloaded_songs")

                elif 'music' in query:
                    printX("Playing songs for you")
                    speak("Playing songs for you")
                    try:
                        music("music_dir")
                    except Exception as e:
                        print(e)
                        printX("music directory path not specified...")
                        speak("music directory path not specified...")
                        pass
                    
                elif " " in query:
                    try:
                        song = qReplace(query)
                        printX('playing ' + song + 'from youtube music')
                        speak('playing ' + song + 'from youtube music')
                        url = playonytm("play",song)
                        print(url)
                        webbrowser.open(url)
                        t.sleep(5)
                        pyautogui.press('space')
                        # pyautogui.getActiveWindow().minimize()
                    except Exception as e:
                        print(e)
                        printX(f"sorry {User} repeat that again")
                        speak(f"sorry {User} repeat that again")

                else:
                    pass

            elif " song" in query:
                if "next" in query:
                    pyautogui.press("nexttrack")
                elif "previous" in query:
                    pyautogui.press("prevtrack",2)
                elif "repeat" in query:
                    pyautogui.press("prevtrack")
                elif "pause" in query or "play" in query:
                    pyautogui.press("playpause")
                elif "download" in query:
                    printX("tell me the name of the song.")
                    speak("tell me the name of the song")
                    song = takeCommand()
                    if song=="None":
                        break
                    song = qReplace(song)
                    song_id = playonytm("download", song)
                    printX(f"downloading the {song} song for you, please wait")
                    speak(f"downloading the {song} song for you, please wait")
                    cwd = music_dir
                    done = download_music(song_id)
                    if done==True:
                        printX(f"{song} Song downloaded..")
                        speak(f"{song} Song downloaded..")
                        if cwd == "" or cwd=="*****":
                            cwd = str(os.getcwd())+"\\MainFiles\\music"
                        popupNotification("Song Downloaded", cwd)
                    else:
                        printX("something went wrong, please try again.")
                        speak("something went wrong, please try again.")

            elif ' email' in query or " mail" in query:
                printX('to whom')
                speak('to whom')
                to = ""
                person = takeCommand()
                if "None" in person or person in chatbot:
                    break
                for pers in contact_list:
                    if pers["first_name"] == person:
                        to = pers['email_id']
                        break
                if to == "":
                    printX(f"there is no {person} in your contact")
                    speak(f"there is no {person} in your contact")
                    printX(f"If you want to add {person} in your contacts, just say, Hey Alfred! add some contacts.")
                    speak(f"If you want to add {person} in your contacts, just say, Hey Alfred! add some contacts.")
                    break
                try:
                    printX("what should i say?")
                    speak("what should i say?")
                    content = takeCommand()
                    sendEmail(to, content)
                    EmailSent()
                    printX(f"email has been sent to {person}!")
                    speak(f"email has been sent to {person}!")
                except Exception as e:
                    print(e)
                    printX(f"sorry {User}. I am not able to send this email.")
                    speak(f"sorry {User}. I am not able to send this email")

            elif "make a note" in query or "write down" in query:
                printX("What would you like me to write down?")
                speak("What would you like me to write down?")
                note_text = takeCommand()
                note(note_text)
                printX(f"I created a note, {note_text}")
                speak(f"I created a note, {note_text}")

            elif "send a message" in query or 'send message' in query:
                # if "whatsapp" in query:
                    printX('to whom')
                    speak('to whom')
                    to = ""
                    person = takeCommand()
                    if "None" in person or person in chatbot:
                        break
                    for pers in contact_list:
                        if pers["first_name"] == person:
                            to = pers['cell_phone']
                            break
                    if to == "":
                        printX(f'there is no {person} in your contacts')
                        speak(f'there is no {person} in your contacts')
                        printX(f"If you want to add {person} in your contacts, just say, Hey Alfred! add some contacts.")
                        speak(f"If you want to add {person} in your contacts, just say, Hey Alfred! add some contacts.")
                        break
                    try:
                        printX("what should i say")
                        speak("what should i say")
                        message = takeCommand()
                        hour = int(datetime.datetime.now().hour)
                        min = int(datetime.datetime.now().minute)
                        kit.sendwhatmsg(to, message, hour, min+1)
                        MsgSent()
                    except Exception as e:
                        print(e)
                        printX(f"sorry {User}. I am not able to send this message.")
                        speak(f"sorry {User}. I am not able to send this message")

            elif 'full screen mode' in query:
                pyautogui.press("f11")
                t.sleep(1)

            elif 'take a screenshot' in query or 'take screenshot' in query:
                t.sleep(1)
                screenshot()
                screenshotSound()
                printX("screenshot saved")
                speak("screenshot saved")
                cwd = str(os.getcwd())+"\\MainFiles\\Screenshot"
                popupNotification("Screenshot Saved", cwd)

            elif "selfie" in query or "take a photo" in query:
                os.startfile('microsoft.windows.camera:')
                t.sleep(3)
                pyautogui.press("enter")

            elif 'recycle bin' in query:
                printX(f"are you sure, {User}")
                speak(f"are you sure, {User}")
                per = takeCommand()
                if per=="None":
                    break
                if "yes" in per:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    printX("Recycle Bin is empty.")
                    speak("Recycle Bin is empty.")
                else:
                    pass

            elif "don't listen" in query or "stop listening" in query: 
                printX(f"are you sure, {User}")
                speak(f"are you sure, {User}")
                per = takeCommand()
                if "yes" in per:
                    printX("for how much time you want to stop me from listening commands")
                    speak("for how much time you want to stop me from listening commands")
                    time = takeCommand()
                    string = query
                    integer_str = ''
                    for char in string:
                        if char.isdigit():
                            integer_str += char
                        elif integer_str:
                            break
                    if integer_str:
                        integer_len = len(integer_str)
                        integer_start = string.find(integer_str)
                        integer_end = integer_start + integer_len
                        query = string[:integer_start] + string[integer_end:]
                        ti = int(integer_str)
                    else:
                        ti = 1
                    if time=="None":
                        break
                    if "minute" in time:
                        a = 60*ti
                        printX(f"Okay {User}, goodbye for now!!!")
                        speak(f"Okay {User}, goodbye for now!!!")
                        t.sleep(a)
                    else:
                        a = ti
                        printX(f"Okay {User}, goodbye for now!!!")
                        speak(f"Okay {User}, goodbye for now!!!")
                        t.sleep(a)
                else:
                    pass

            elif " system" in query or " device" in query or " pc" in query:
                if "shutdown" in query:
                    printX(f"are you sure, {User}")
                    speak(f"are you sure, {User}")
                    approve = takeCommand()
                    if "yes" in approve:
                        printX("In 30 seconds, system will shutdown.")
                        speak("In 30 seconds, system will shutdown.")
                        os.system("shutdown /s /t 30")
                elif "restart" in query:
                    printX(f"are you sure, {User}")
                    speak(f"are you sure, {User}")
                    approve = takeCommand()
                    if "yes" in approve:
                        printX("In 30 seconds, system will be restarted")
                        speak("In 30 seconds, system will be restarted")
                        os.system("shutdown /r /t 30")
                elif "log of" in query:
                    printX(f"are you sure, {User}")
                    speak(f"are you sure, {User}")
                    approve = takeCommand()
                    if "yes" in approve:
                        printX("now, system will log off")
                        speak("now, system will log off")
                        os.system("shutdown /l")
#### END


####---------------------------------Home Automation---------------------------------------

            elif ' light' in query:
                if light:
                    if 'turn on' in query:
                        try:
                            turn_on(devices_list)
                            printX("the lights are on")
                            speak("the lights are on")
                        except Exception as e:
                            printX("sorry, I don't find any active device")
                            speak("sorry, I don't find any active device")

                    elif 'turn off' in query:
                        try:
                            turn_off(devices_list)
                            printX("the lights are off")
                            speak("the lights are off")
                        except Exception as e:
                            printX("sorry, I don't find any active device")
                            speak("sorry, I don't find any active device")
                    
                    elif 'colour' in query:
                        try:
                            res = color(devices_list, query)
                            if res==None:
                                color(devices_list, query)
                            else:
                                printX(res)
                                speak(res)
                        except Exception as e:
                            printX("sorry, I don't find any active device")
                            speak("sorry, I don't find any active device")

                    elif 'brightness' in query or 'dim' in query:
                        try:
                            brightness(devices_list, query)
                            if 'dim' in query:
                                printX(f"is it okay {User}")
                                speak(f"is it okay {User}")
                        except Exception as e:
                            printX("sorry, I don't find any active device")
                            speak("sorry, I don't find any active device")

                    elif 'blink' in query:
                        blink_times = 0
                        for i in range(0,5):
                            if blink_times<10:
                                turn_off(devices_list)
                                t.sleep(0.1)
                                turn_on(devices_list)
                                t.sleep(0.1)
                                blink_times+=blink_times
                            else:
                                break
                    
                    else:
                        pass
                else:
                    printX("sorry, No active devices found")
                    speak("sorry, No active devices found")
                    printX(f"If you want to use this feature, you can add info to my database by clicking the user icon on main window")
                    speak(f"If you want to use this feature, you can add info to my database by clicking the user icon on main window")
#### END


####--------------------------------Device Automation--------------------------------------

            elif "brightness" in query:
                string = query
                num1 = ''
                for char in string:
                    if char.isdigit():
                        num1 += char
                    elif num1:
                        break
                if "low" in query:
                    num1 = 10
                elif "full" in query:
                    num1 = 100
                elif "zero" in query:
                    num1 = 0
                elif num1 == "":
                    break
                num = int(num1)
                display_brightness(num)

            elif "volume" in query:
                volume(query)

            elif "alarm" in query:
                if "delete" in query:
                    printX("Do you want to delete all your alarms?")
                    speak("Do you want to delete all your alarms?")
                    permit = takeCommand()
                    if "yes" in permit:
                        command = "start ms-clock:"
                        subprocess.run(command, shell=True)
                        t.sleep(2)
                        pyautogui.getActiveWindow().maximize()
                        t.sleep(1)
                        pyautogui.click(x=147, y=149)
                        pyautogui.click(x=1683, y=967)
                        t.sleep(0.5)
                        for i in range(6):
                            pyautogui.click(x=663, y=87)
                        os.system(f"taskkill /f /im time.exe")
                        speak("I've deleted all your alarms.")
                    else:
                        pass
                
                elif "close" in query or "off" in query:
                    pyautogui.click(x=1817, y=951)
                    pyautogui.click(x=1817, y=951)          
                
                else:
                    try:
                        if "for" in query:
                            time = query.replace("set","").replace("an","").replace("alarm","").replace("for","").replace(" ","")
                            timer = time.split(":")
                            time1 = timer[0]
                            Time = time.replace(":","")
                        else:
                            for i in range(2):
                                printX("for what time")
                                speak("for what time")
                                time = takeCommand()
                                if "None" in time:
                                    pass
                                elif time in chatbot:
                                    break
                                else:
                                    break
                            timer = time.split(":")
                            time1 = timer[0]
                            Time = time.replace(":","")
                        if Time=="None":
                            text = "sorry i couldn't hear you"
                            printX(text)
                            speak(text)
                            
                        elif Time in chatbot:
                            printX('okay.')
                            speak('okay.')
                        else:
                            n = 1
                            chunks = [Time[i:i+n] for i in range(0, len(Time), n)]
                            if "12" in time1 or "11" in time1 or "10" in time1:
                                h1 = chunks[0]+chunks[1]
                                print(h1)
                                s1 = chunks[2]
                                s2 = chunks[3]
                            else:
                                h1 = chunks[0]
                                s1 = chunks[1]
                                s2 = chunks[2]
                            if "p.m." in Time:
                                h = int(h1)+12
                                if h==24:
                                    h=0
                                hour = str(h)
                                am_pm = "p.m."
                            else:
                                hour = str(h1)
                                am_pm = "a.m."
                            alarm(hour,s1,s2)
                            printX(f"your alarm is set for {h1}:{s1+s2} {am_pm}")
                            speak(f"your alarm is set for {h1}:{s1+s2} {am_pm}")
                    except Exception as e:
                        speak("Sorry, say that again.")
#### END


####-----------------------------------Other Info Commands----------------------------------

            elif 'activate how to do mode' in query:
                printX("how to do mode is activated, please tell me what you want to know")
                speak("how to do mode is activated, please tell me what you want to know")
                how = takeCommand()
                # while True:
                try:
                        if how in chatbot:
                            printX(f"okay {User},closing how to do mode..")
                            speak(f"okay {User},closing how to do mode..")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            print(how_to)
                            assert len(how_to) == 1
                            how_to[0].print()
                            note(str(how_to[0].summary))
                            speak(how_to[0].summary)

                except Exception as e:
                    print(e)
                    speak(f"sorry {User}, i'm unable to find this")
        
            elif "the meaning of" in query:
                try:
                    word = qReplace(query)
                    text = word.replace('meaning','')
                    if text=="":
                        printX("meaning of what?")
                        speak("meaning of what?")
                        text = takeCommand()
                        if "None" in text:
                            break
                    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+text
                    meaning = requests.get(url).json()
                    txtmeaning = str(meaning[0]['meanings'][0]['definitions'][0]['definition'])
                    printX(txtmeaning)
                    speak(txtmeaning)
                except Exception as e:
                    printX(f"sorry {User}, i didn't catch the word. please try again")
                    speak(f"sorry {User}, i didn't catch the word. please try again")

            elif 'how to say ' in query or 'how can i say' in query:
                query = query.replace("how to say ","")
                query = query.replace('how can i say ',"")
                if "in" in query:
                    li = query.split("in",1)
                    # print(li)
                    lang = li[1].replace(" ","")
                    query = li[0]
                    if lang=="":
                        printX("translate into which language?")
                        speak("translate into which language?")
                        lang = takeCommand()
                        if "None" in lang:
                            break
                    short_trans(lang, query, User)
                else:
                    pass

            elif 'how to ' in query:
                kit.search(query)
                printX(f"okay, I've found this on the web for {query}")
                speak(f"okay, I've found this on the web for {query}")

            elif " advice" in query:
                printX(f"Here's a piece of advice for you, {User}")
                speak(f"Here's a piece of advice for you, {User}")
                advice = get_random_advice()
                printX(advice)
                speak(advice)
#### END


####------------------------------------Add user contacts-----------------------------------

            elif "add " in query:
                if "contact" in query:
                    os.startfile("Contact.exe")
                    printX("opening contacts.")
                    speak("opening contacts")
                    printX(f"{User}, Now you can add contacts to my database.")
                    speak(f"{User}, Now you can add contacts to my database.")
            
                elif "info" in query:
                    os.startfile("Alfred_DB.exe")
                    printX("opening settings")
                    speak("opening settings")
                    printX(f"{User}, Now you can add info to my database.")
                    speak(f"{User}, Now you can add info to my database.")
                else:
                    os.startfile("Alfred_DB.exe")
                    printX("opening settings")
                    speak("opening settings")
#### END


####------------------------------------Install/Open Applications-----------------------------------

            elif "install" in query:
                query = query.replace("install","").replace("app","")
                try:
                    os.startfile("ms-windows-store://home")
                    speak(f"searching for {query} in microsoft store.")
                    t.sleep(10)
                    pyautogui.press('tab')
                    pyautogui.write(query)
                    pyautogui.press('enter')
                except Exception:
                    printX("Something went wrong, please try again ")
                    speak("Something went wrong, please try again ")

            elif "open" in query:
                try:
                    if "chrome" in query:
                        webbrowser.open_new_tab('https://www.google.com')
                        printX("opening google chrome")
                        speak("opening google chrome")

                    elif "contact" in query:
                        os.startfile("Contact.exe")
                        printX("opening contacts.")
                        speak("opening contacts")
                    
                    elif "device settings" in query:
                        pyautogui.keyDown("win")
                        pyautogui.press("i")
                        pyautogui.keyUp("win")
                        t.sleep(1)

                    elif "database" in query or "settings" in query:
                        os.startfile("Alfred_DB.exe")
                        printX("opening database.")
                        speak("opening database")

                    elif "code" in query:
                        subprocess.run("code", shell=True)
                        printX("opening vs code")
                        speak("opening V S code")
                    
                    elif "microsoft store" in query:
                        subprocess.run(["powershell.exe", "Start", "ms-windows-store://"])
                        printX("opening microsoft store")
                        speak("opening microsoft store")

                    elif "ms powerpoint" in query:
                        appLocation = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
                        os.startfile(appLocation)
                        printX("opening MS powerpoint")
                        speak("opening MS powerpoint")

                    elif "excel" in query:
                        appLocation = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                        os.startfile(appLocation)
                        printX("opening MS excel")
                        speak("opening MS excel")

                    elif "ms word" in query:
                        appLocation = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                        os.startfile(appLocation)
                        printX("opening MS word")
                        speak("opening MS word")

                    elif "netflix" in query:
                        command = "start netflix:"
                        subprocess.run(command, shell=True)
                        printX("opening Netflix")
                        speak("opening Netflix")

                    elif "desktop" in query:
                        pyautogui.keyDown("win")
                        pyautogui.press("d")
                        t.sleep(1)
                        pyautogui.keyUp("win")

                    elif "search bar" in query:
                        pyautogui.keyDown("ctrl")
                        pyautogui.press("e")
                        pyautogui.keyUp("ctrl")
                        t.sleep(1)

                    elif "file explorer" in query:
                        pyautogui.keyDown("win")
                        pyautogui.press("e")
                        pyautogui.keyUp("win")
                        t.sleep(1)

                    elif "camera" in query:
                        os.startfile('microsoft.windows.camera:')

                    else:
                        try:
                            open = qReplace(query)
                            ak = os.system(open)
                            printX(f"opening {open}")
                            speak(f"opening {open}")
                            if ak==1:
                                open = qReplace(query)
                                open = open.replace(' ','')
                                SearchOnWeb(open,1)
                        except Exception as e:
                            pass
                except Exception as e:
                    print(e)
                    printX("Sorry I couldn't find that application.")
                    speak("Sorry I couldn't find that application.")
#### END


####--------------------------------------Asking Info---------------------------------------

            elif ' time' in query:
                StrTime = datetime.datetime.now().strftime(f"%I:%M %p")
                if 'in' in query:
                    content_list = query.split("in",1)
                    content = str(content_list[1])
                    url = f"https://www.google.com/search?q="+'time in'+str({content})
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    time = data.find('div', class_="BNeawe")
                    if time is not None:
                        time = time.text
                    else:
                        time = StrTime
                    printX(f"{User}, it's {time} in {content}")
                    speak(f"{User}, it's {time} in {content}")
                else:
                    printX(f"{User}, it's {StrTime}")
                    speak(f"{User}, it's {StrTime}")

            elif " day" in query or " date" in query:
                day = int(datetime.datetime.now().strftime("%w"))
                x = int(datetime.datetime.now().strftime("%d"))
                y = datetime.datetime.now().strftime("%m")
                z = datetime.datetime.now().strftime("%Y")
                if "tomorrow" in query:
                    day = day+1
                    tom_day = days[day]
                    x = x+1
                    printX(f"it will be {tom_day}, {z}-{y}-{x}")
                    speak(f"it will be {tom_day}, {z}-{y}-{x}")

                elif "yesterday" in query:
                    day = day-1
                    tom_day = days[day]

                    if x == 1:
                        printX(f"it was {tom_day}, {z}-{y}-{x}")
                        speak(f"it was {tom_day}, {z}-{y}-{x}")
                    else:
                        x = x-1
                        printX(f"it was {tom_day}, {z}-{y}-{x}")
                        speak(f"it was {tom_day}, {z}-{y}-{x}")

                else:
                    day = datetime.datetime.now().strftime("%A")
                    date = datetime.date.today()
                    printX(f"it's {day}, {date}")
                    speak(f"it's {day}, {date}")

            elif 'ip address' in query:
                ip = requests.get('https://api.ipify.org').text
                printX(f'your IP address is {ip}')
                speak(f'your IP address is {ip}')

            elif 'weather' in query or "temperature" in query:
                try:
                    if 'outside' in query:
                        location = currentLoc()
                        try:
                            weatherInfo(location, User)  
                        except Exception as e:
                            printX("Something went wrong, please try again ")
                            speak("Something went wrong, please try again ")
                    
                    elif 'in' in query:
                        loc_list = query.split("in ",1)
                        location = loc_list[1]
                        try:
                            weatherInfo(location, User)  
                        except Exception as e:
                            printX("Something went wrong, please try again ")
                            speak("Something went wrong, please try again ")

                    else:
                        for i in range(2):
                            printX("weather from where")
                            speak("weather from where")
                            location = takeCommand()
                            if "None" in location:
                                pass
                            elif location in chatbot:
                                break
                            else:
                                break
                        if 'None' in location:
                            text = "sorry i couldn't hear you"
                            printX(text)
                            speak(text)
                        elif location in chatbot:
                            printX('okay.')
                            speak('okay.')
                        elif "outside" in location:
                            location = currentLoc()
                            try:
                                weatherInfo(location, User)  
                            except Exception as e:
                                printX("Something went wrong, please try again ")
                                speak("Something went wrong, please try again ")
                        else:
                            try:
                                weatherInfo(location, User)  
                            except Exception as e:
                                printX("Something went wrong, please try again ")
                                speak("Something went wrong, please try again ")

                except Exception as e:
                    if 'outside' in query:
                        query = query.replace('outside','')
                        weather(query)
                    else:
                        printX('weather from where')
                        speak('weather from where')
                        location = takeCommand()
                        weather(location)

            elif 'where i am' in query or 'where are we' in query or 'my location' in query:
                try:
                    ip = requests.get('https://api.ipify.org').text
                    url = 'http://ip-api.com/json/'+ip
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    state = geo_data['regionName']
                    printX(f"{User}, we are in {city}, {state}, {country}")
                    speak(f"{User}, we are in {city}, {state}, {country}")
                except Exception as e:
                    printX(f"sorry {User}, due to slow connection i'm not able to find where we are")
                    speak(f"sorry {User}, due to slow connection i'm not able to find where we are")

            elif 'where is' in query:
                Place = qReplace(query)
                printX(f"Ok. here's {Place}")
                speak(f"Ok. here's {Place}")
                GoogleMaps(Place)

            elif "battery percentage" in query or 'battery left' in query:
                battery = psutil.sensors_battery()
                charge = battery.power_plugged
                percentage = battery.percent
                printX(f"Battery is at {percentage} %")
                speak(f"Battery is at {percentage} %")
                if percentage<=45:
                    if charge==False:
                        printX("we don't have enough power, please connect to charging")
                        speak("we don't have enough power, please connect to charging")

            elif "internet speed" in query:
                try:
                    from speedtest import Speedtest
                    printX(f"wait {User} it may take a while, lemme check")
                    speak(f"wait {User} it may take a while, lemme check")
                    st = Speedtest()
                    dl = st.download()
                    download = int(dl/800000)
                    ul = st.upload()
                    upload = int(ul/800000)
                    printX(f"{User}, we have downloading speed of {download}MBPS. and uploading speed of {upload}MBPS")
                    speak(f"{User}, we have downloading speed of {download} MB per second. and uploading speed of {upload} MB per second")
                except Exception as e:
                    printX("sorry i'm unable to find the internet speed")
                    speak("sorry i'm unable to find the internet speed")

            elif " news" in query:
                if "space" in query:
                    tz = pytz.timezone('America/New_York')
                    Date = datetime.datetime.now(tz).date()
                    Nasanews(Date)
                else:
                    api_key = ""
                    complete_api_link = "https://newsapi.org/v2/top-headlines?"+'country=in&'+"apikey="+api_key
                    try:
                        api_link = requests.get(complete_api_link)
                        news = api_link.json()
                    except Exception as e:
                        printX("something went wrong, please try again.")
                        speak("something went wrong, please try again.")

                    printX("here are some latest headlines of the day.")
                    speak("here are some latest headlines of the day.")
                    num = 0
                    for new in news["articles"]:
                        if num <= 5:
                            newss = str(new["title"])
                            new1 = str(new["title"]).split("-")
                            News = f"{str(new1[0])} by {str(new1[1])}"
                            new2 = str(new["description"])
                            print(f"Title : {newss}", "\n")
                            speak(f"{News}")
                            print(f"News : {new2}", "\n")
                            num+=1
                        else:
                            break

            elif "latest movies" in query or "trending movies" in query:
                ans = get_trending_movies()
                printX("here are some latest trending movies :")
                speak(f"here are some latest trending movies for you {User}")
                for i,j in enumerate(ans):
                    print(f"{i+1} : {j}.")
                    speak(f"{i+1} : {j}.")

            elif "convert " in query:
                string = query
                integer_str = ''
                for char in string:
                    if char.isdigit():
                        integer_str += char
                    elif integer_str:
                        break
                if integer_str:
                    integer_len = len(integer_str)
                    integer_start = string.find(integer_str)
                    integer_end = integer_start + integer_len
                    query = string[:integer_start] + string[integer_end:]
                    amt = integer_str
                else:
                    amt = ""
                    
                if "to" in query:
                    query = query.replace(" convert  ","").replace(" convert ","").replace("convert ","")
                    cur_list = query.split(" to ")
                else:
                    printX(f"convert to which currency, {User}.")
                    speak(f"convert to which currency, {User}.")
                    cur = takeCommand()
                    if "None" in cur or cur in chatbot:
                        break
                    cur_list = cur.split(" to ")
                try:
                    c1 = cur_list[0]
                    c2 = cur_list[1]
                    if c1 in currency1 and c2 in currency1:
                        fromcur = currency1[c1]
                        tocur = currency1[c2]
                        if amt=="":
                            printX("tell me the amount")
                            speak("tell me the amount")
                            amt = takeCommand()
                            if amt in chatbot:
                                break
                        if "None" in amt:
                            amt = "1"
                        ans = curCont(amt, fromcur, tocur)
                        var = 'is %.2f' % ans
                        print(f"Alfred : {amt} {fromcur}({c1}) {var} {tocur}({c2}).\n")
                        speak(f'{amt} {c1} {var} {c2}')
                except:
                    try:
                        ans = curCont1(amt, fromcur, tocur)
                        mul = float(amt)*float(ans)
                        var = 'is %.2f' % mul
                        print(f"Alfred : {amt} {fromcur}({c1}) {var} {tocur}({c2}).\n")
                        speak(f'{amt} {c1} {var} {c2}')
                    except:
                        try:
                            ans = curCont2(amt, fromcur, tocur)
                            var = 'is %.2f' % ans
                            print(f"Alfred : {amt} {fromcur}({c1}) {var} {tocur}({c2}).\n")
                            speak(f'{amt} {c1} {var} {c2}')
                        except Exception as e:
                            print(e)
                            printX("sorry something went wrong.")
                            speak("sorry something went wrong.")
#### END


####--------------------------------------Math Calculations---------------------------------

            elif 'square root' in query or 'under root' in query or "√" in query:
                string = query
                integer_str = ''
                for char in string:
                    if char.isdigit():
                        integer_str += char
                    elif integer_str:
                        break
                if integer_str:
                    integer_len = len(integer_str)
                    integer_start = string.find(integer_str)
                    integer_end = integer_start + integer_len
                    query = string[:integer_start] + string[integer_end:]
                    num = integer_str
                    root(num)
                else:
                    printX('tell me a number')
                    speak('tell me a number')
                    num = takeCommand()
                    if "None" in num or num in chatbot:
                        break
                    root(num)

            elif 'value of pi' in query:
                num = math.pi
                printX('the value of pi is %.2f' % num )
                speak('the value of pi is %.2f' % num )
#### END


####-------------------------------------Close Applications---------------------------------

            elif 'close the window' in query or "close window" in query:
                hwnd = win32gui.GetForegroundWindow()
                window_title = win32gui.GetWindowText(hwnd)
                if window_title!="Alfred A.I.":
                    pyautogui.keyDown("alt")
                    pyautogui.press("f4")
                    pyautogui.keyUp("alt")
                    t.sleep(1)

            elif 'close ' in query:
                close = qReplace(query)
                close = close.replace(" ",'')
                printX(f"closing {close}")
                # speak(f"closing {close}")
                ans = os.system(f"taskkill /f /im {close}.exe")   
                hwnd = win32gui.GetForegroundWindow()
                window_title = win32gui.GetWindowText(hwnd)
                if ans!=0 and window_title!="Alfred A.I.":
                    pyautogui.keyDown("alt")
                    pyautogui.press("f4")
                    pyautogui.keyUp("alt")
                    t.sleep(0.5)
#### END


####---------------------------------------Open in Browser----------------------------------

            elif "search" in query:
                if "train" in query or "flight" in query or "bus" in query:
                    printX(f'{User}, tell me the destination, where you want to go.')
                    speak(f'{User}, tell me the destination, where you want to go.')
                    destination = takeCommand()
                    if "to" in destination:
                        pass
                    else:
                        location = currentLoc()
                        destination = f"{location} to {destination}"
                    if "None" in destination or destination in chatbot:
                        break
                    elif "flight" in query:
                        destination = "flights from " + destination
                        try:
                            SearchOnWeb(destination,5)
                            printX(f"Here's some websites for {destination}")
                            speak(f"Here's some websites for {destination}")
                        except Exception as e:
                            print(e)
                            speak(f"try later {User}")
                    elif "train" in query:
                        destination = "trains from " + destination
                        try:
                            SearchOnWeb(destination,5)
                            printX(f"Here's some websites for {destination}")
                            speak(f"Here's some websites for {destination}")
                        except Exception as e:
                            print(e)
                            speak(f"try later {User}")
                    
                    elif "bus" in query:
                        destination = "buses from " + destination
                        try:
                            SearchOnWeb(destination,5)
                            printX(f"Here's some websites for {destination}")
                            speak(f"Here's some websites for {destination}")
                        except Exception as e:
                            print(e)
                            speak(f"try later {User}")
                else:
                    printX(f'{User}, what you want me to search.')
                    speak(f'{User}, what you want me to search.')
                    q = takeCommand()
                    if "None" in q or q in chatbot:
                        break
                    try:
                        if "google" in query:
                            kit.search(q)
                            pl = q + " in google"
                        elif "youtube" in query:
                            webbrowser.open(f"https://www.youtube.com/results?search_query={q}")
                            pl = q + " in youtube"  
                        elif "None" in q or q in chatbot:
                            break
                        else:
                            SearchOnWeb(q, 5)
                            pl = q + " on the web"
                        printX(f"Here's what I found for {pl}.")
                        speak(f"Here's what I found for {pl}")
                    except Exception as e:
                        printX("I'm unable to do this right now, try again..")
                        speak("I'm unable to do this right now, try again..")
                
            elif 'facebook messages' in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")
                printX("opening facebook")
                speak("opening facebook")
                webbrowser.open(r"https://www.facebook.com/")
                t.sleep(4)
                printX(f"looks like you're all caught up {User}!")
                speak(f"looks like you're all caught up {User}!")

            elif 'linkedin' in query:
                printX("opening LinkedIn")
                speak("opening LinkedIn")
                webbrowser.open(r"https://www.linkedin.com/feed/")
                t.sleep(4)
                printX(f"{User}, looks like many people are connecting to your profile.")
                speak(f"{User}, looks like many people are connecting to your profile.")
#### END


####----------------------------------Nearby Facilities---------------------------------

            elif 'find me' in query or 'i need a' in query:
                query = query.replace("find me", '').replace("i need", '').replace("some", '')
                query1 = "nearby "+query
                GoogleMaps(query1)
                printX("here are some results")
                speak("here are some results")
                pass
#### END


####---------------------------------------Translator-------------------------------------------

            elif 'translate' in query:
                if "translate to " in query or "translate into " in query:
                    lang = qReplace(query)
                    destination_language(lang, User)

                elif "translate hindi to " in query or " hindi into " in query:
                    query = qReplace(query)
                    query = wReplace(query)
                    lang = query.replace('hindi ', "")
                    hindi_language(lang, User)
                else:
                    printX("sure, translate into which language.")
                    speak("sure, translate into which language.")
                    lang = takeCommand()
                    if "None" in lang or lang in chatbot:
                        break
                    if lang=="chinese":
                        pass
                    else:
                        lang = qReplace(lang)
                    destination_language(lang, User)
#### END


####----------------------------------------Games-----------------------------------------------

            elif " a coin" in query or " coin" in query:
                printX("okay")
                speak("okay")
                ans = random.choice(["Heads", "Tails"])
                coinFlip()
                printX(f"its {ans}.")
                speak(f"its {ans}")

            elif " a dice" in query or " dice" in query:
                printX("okay")
                speak("okay")
                ans = random.choice([1,2,3,4,5,6])
                diceRoll()
                if ans==6:
                    printX(f"hurray, you got {ans}.")
                    speak(f"hurray, you got {ans}")
                elif ans==1:
                    printX(f"uh oh, you got {ans}.")
                    speak(f"uh oh, you got {ans}")
                else:
                    printX(f"huh, you got {ans}.")
                    speak(f"huh, you got {ans}")

            elif 'play a game' in query or 'i am bored' in query:
                winning_no = random.randint(0,100)
                guess = 1
                printX("guess a number between 0 to 100")
                speak("guess a number between 0 to 100")
                try:
                    num = takeCommand()
                    guessed_num = int(num)
                    if guessed_num<=100:
                        while winning_no != guessed_num:
                            if winning_no < guessed_num:
                                printX("too high, guess again") 
                                speak("too high, guess again") 
                            else:
                                printX("too low, guess again")
                                speak("too low, guess again")
                            guess += 1
                            num = takeCommand()
                            guessed_num = int(num)
                        printX(f"you won, and you guessed the right number in {guess} times ")
                        speak(f"you won, and you guessed the right number in {guess} times ")
                except Exception as e:
                    printX('you can only guess numbers between 0 to 100')
                    speak('you can only guess numbers between zero to 100')
#### END


####------------------------------------Voice Changer-------------------------------------------

            elif 'repeat my voice' in query or "repeat after me" in query:
                printX(f"Okay {User}, Speak.")
                speak(f"Okay {User}, Speak.")
                voice = takeCommand()
                if "None" in voice:
                    break
                speak(voice)
                
            elif 'change voice' in query or 'change your voice' in query:
                voice_dict = []
                engine = pyttsx3.init('sapi5')
                voices = engine.getProperty('voices')

                n = len(voices)
                for i in range(0,n):
                    name = str(voices[i].name)
                    name = name.replace('Microsoft','')
                    name = name.replace('Desktop','')
                    voice_dict.append(name)

                for i in range(1,len(voice_dict)):
                    printX(voice_dict[i])
                    speak(voice_dict[i])
                    engine.setProperty('voice', voices[i].id)
                    printX("Hi, i'm Alfred, choose the voice you'd like me to use.")
                    speak("Hi, i'm Alfred, choose the voice you'd like me to use.")
                    engine.setProperty('voice', voices[0].id)


                printX(f"what voice do you want to choose, {User}")
                speak(f"what voice do you want to choose, {User}")

                command  =  takeCommand()
                if 'hazel' in command:
                    engine.setProperty('voice', voices[1].id)
                    speak(f"At your service, {User}")

                elif 'zira' in command:
                    engine.setProperty('voice', voices[2].id)
                    speak(f"At your service, {User}")

                elif 'alfred' in command:
                    engine.setProperty('voice', voices[0].id)
                    speak(f"At your service, {User}")
                    
                elif 'None' in command:
                    pass

                else:
                    speak(f"okay {User}")
#### END


####-----------------------------------Conversation----------------------------------------------

            elif 'who are you' in query:
                printX(f"I'm alfred, your virtual assistant, {User}")
                speak(f"I'm alfred, your virtual assistant, {User}")

            elif ' morning' in query or 'good afternoon' in query or 'good evening' in query:
                wishMe(query, User)
            
            elif 'who is akbar' in query or 'who made you' in query or 'who build you' in query:
                if User=="Akbar":
                    printX("You are my developer, akbar sir")
                    speak("You are my developer, akbar sir")
                    break
                printX('I was designed by mister akbar kaleem. he is the greatest programmer of all time')
                speak('i was designed by mister akbar kaleem. he is the greatest programmer of all time')
                notification("Developer")

            elif "help me" in query:
                printX("if your safety is at risk, ask me to message emergency services or someone you trust")
                speak("if your safety is at risk, ask me to message emergency services or someone you trust")

            elif "programming joke" in query:
                joke = pyjokes.get_joke()
                printX(joke)
                speak(joke)

            elif "wake up" in query:
                printX(f"Online and ready to go {User}")
                speak(f"Online and ready to go {User}")

            elif "what can you do" in query:
                speak("I'm here to help..")
                printX("Send a message :\n")
                printX("hey alfred, send a message to David.")
                printX("hey alfred, text David and Sofia.\n")
                printX("Send an email :\n\nhey alfred, send an email to David.\n")
                printX("Find information like : \n\nwhat's the weather, what's the date and time, find location etc \n")
                printX("Get to know Alfred at https://Alfred.com/features")
                speak("Get to know Alfred at Alfred.com")
                notification("Features")

            elif "hello" in query:
                printX(f"hello {User}, how you doing?")
                speak(f"hello {User}, how you doing?")
#### END


####-------------------------------Window manipulation------------------------------------------

            elif " window" in query:
                if 'switch' in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    t.sleep(0.1)
                    pyautogui.keyUp("alt")
                
                elif 'minimise' in query:
                    pyautogui.getActiveWindow().minimize()

                elif 'maximize' in query:
                    pyautogui.getActiveWindow().maximize()
                
                else:
                    printX("sorry, i can't do that")
                    speak("sorry, i can't do that")
#### END


####-------------------------------Download from Web--------------------------------------------

            elif "show all " in query or "saved " in query:
                if "notes" in query:
                    printX("here are all the saved notes")
                    speak("here are all the saved notes")
                    os.startfile("MainFiles\\Notes") 

                elif "video" in query:
                    printX("here are all the saved videos")
                    speak("here are all the saved videos")
                    os.startfile("MainFiles\\video")

                elif "songs" in query or "music" in query:
                    printX("here are all the saved music")
                    speak("here are all the saved music")
                    os.startfile("MainFiles\\music") 

                elif "space" in query:
                    printX("here are all the saved space images")
                    speak("here are all the saved space images")
                    os.startfile("MainFiles\\Images")

                elif "images" in query:
                    printX("here are all the saved images")
                    speak("here are all the saved images")
                    os.startfile("MainFiles\\Pictures")

                elif "screenshot" in query:
                    printX("here are all the saved screenshot")
                    speak("here are all the saved screenshot")
                    os.startfile("MainFiles\\Screenshot")

            elif "download" in query:
                if "video" in query:
                    printX("tell me the name of the video.")
                    speak("tell me the name of the video")
                    video = takeCommand()
                    if video=="None":
                        break
                    video = qReplace(video)
                    video_id = playonytm(video, "download")
                    printX(f"downloading the {video} video from youtube, please wait")
                    speak(f"downloading the {video} video from youtube, please wait")
                    done = download_video(video_id)
                    if done:
                        printX(f"{video} video downloaded..")
                        speak(f"{video} video downloaded..")
                        cwd = str(os.getcwd())+"\\MainFiles\\video"
                        popupNotification("Video Downloaded", cwd)
                    else:
                        printX("something went wrong, please try again.")
                        speak("something went wrong, please try again.")

                elif "images" in query:
                    if "of" in query:
                        q = query.split("of",1)
                        img = q[1]
                    else:
                        printX("what kind of images you want to download?")
                        speak("what kind of images you want to download?")
                        img = takeCommand()
                    if img=="None":
                        break
                    printX(f"downloading the {img} images from internet, please wait")
                    speak(f"downloading the {img} images from internet, please wait")
                    ans = downloadImage(img)
                    if ans:
                        printX(f"{img} images downloaded..")
                        speak(f"{img} images downloaded..")
                        cwd = str(os.getcwd())+"\\MainFiles\\Pictures"
                        popupNotification("Images Downloaded",cwd)
                        printX("here are the images")
                        speak("here are the images")
                        os.startfile("MainFiles\Pictures")
                    else:
                        printX("something went wrong, please try again.")
                        speak("something went wrong, please try again.")

            elif "image" in query or "picture" in query:
                if "download" in query:
                    printX("here are the downloaded images")
                    speak("here are the downloaded images")
                    os.startfile("MainFiles\Pictures")
                    break

                if "of" in query:
                    q = query.split("of",1)
                    img = q[1]
                else:
                    printX("what kind of images you want to see?")
                    speak("what kind of images you want to see?")
                    img = takeCommand()
                if img=="None":
                    break
                googleSearch(img)
                printX(f"Here are some images of {img}.")
                speak(f"Here are some images of {img}.")
#### END


####-------------------------------Funny Alfred--------------------------------------------

            elif "say " in query:
                if "wow" in query:
                    playsound("MainFiles\\sound\\extra\\wow.mp3")
                elif "yeah" in query:
                    playsound("MainFiles\\sound\\extra\\yeahboy.mp3")

            elif "can you " in query:
                if "laugh" in query:
                    laugh = random.choice(["laugh.mp3","sinisterlaugh.mp3"])
                    playsound(f"MainFiles\\sound\\extra\\{laugh}")
                elif "bark" in query or "dog sound" in query:
                    playsound("MainFiles\\sound\\extra\\bark.mp3")
                elif "cry" in query:
                    playsound("MainFiles\\sound\\extra\\cry.mp3")
                elif "meow" in query or "cat sound" in query:
                    playsound("MainFiles\\sound\\extra\\catmeow.mp3")
                elif "scream" in query or "shout" in query:
                    playsound("MainFiles\\sound\\extra\\scream.mp3")

####------------------------------------------Exit-----------------------------------------------

            elif query in chatbot or 'sleep' in query or 'can go' in query:
                if 'shut up' in query or 'keep quiet' in query:
                    break
                else:    
                    closeSound()
                    break

            elif 'None' in query: #or ' ' in query:
                closeSound()
                break


####--------------------------------------AI ChatBot--------------------------------------------

            else:
                app_id = ""
                url = f"https://api.wolframalpha.com/v2/result?appid={app_id}&i={query}"
                try:
                    res = requests.get(url)
                    ans = res.text
                    if 'not understand your input' in ans or 'short answer available' in ans or "Wolfram" in ans:
                        Text = ReplyBrain(query)
                        if Text == None:
                            printX("please provide your open A.I. API Key to use advanced chatbot..")
                            speak("please provide your open A.I. API Key, to use advanced chatbot..")
                            speak(f"you can add open A.I. API key to my database, Just say, Hey Alfred! i want to add open A.I. API key")
                        else:
                            print(f"Alfred : {Text}\n")
                            speak(Text)
                    else:
                        print(ans)
                        speak(ans)
                        
                except Exception as e:
                    print(e)
                    # speak(e)
            break

        except Exception as e:
            print(e)
            # speak(e)
            printX("Sorry, this feature is not available on your device..")
            speak("Sorry, this feature is not available on your device..")
            printX(f"If you want to use this feature, you can add info to my database, Just say, Hey Alfred! i want to add details.")
            speak(f"If you want to use this feature, you can add info to my database, Just say, Hey Alfred! i want to add details.")
            break

####----------------------------------------END--------------------------------------