####------------------------------- All MAIN Functions ------------------------------


################################### Import Modules ##################################

from MainFiles.Database.modules import os, win32gui, json, smtplib, t, pyautogui, requests, speak, webbrowser, BeautifulSoup, datetime, random, pct, subprocess, Notification, math, Image, audio, exceptions, CurrencyConverter, YouTube, downloader
from MainFiles.Database.Translator import takeCommand

################################### Current Directory ##############################
cwd = str(os.getcwd()).replace("\\","\\")


################################### Command Print ##################################

def printX(query):
    query = query.capitalize()
    print(f"Alfred : {query}\n")

################################### Window State(MAX, MIN, NORMAL) #################

def get_window_state(hwnd):
    state = win32gui.GetWindowPlacement(hwnd)
    if state[1] == 1:
        return "minimized"
    elif state[1] == 2:
        return "maximized"
    else:
        return "normal"

################################### Email Sender ###################################

def sendEmail(to, content):
    try:
        with open('MainFiles\Data\config.json') as config:
            data = json.load(config)
        ID = data[0]['gmailid']
        Pass = data[0]['gmailpass']
    except Exception as e:
        print(e)
        pass
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(ID, Pass)
    server.sendmail(ID, to, content)
    server.close()

################################### Whatsapp Message Sender ########################

def sendMsg(to, msg):
    path = "C:\\Users\\Akbar\\Desktop\\Intel® Unison™.lnk"
    os.startfile(path)
    t.sleep(4)
    pyautogui.getActiveWindow().maximize()
    t.sleep(2)
    pyautogui.click(x=32, y=300)
    t.sleep(2)
    pyautogui.click(x=456, y=79)
    t.sleep(2)
    pyautogui.write(to)
    t.sleep(2)
    pyautogui.press("enter")
    t.sleep(2)
    pyautogui.write(msg)
    pyautogui.press("enter")
    t.sleep(5)
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    pyautogui.keyUp("alt")
    t.sleep(1)
    return True

################################### Current location(From IP Add.) #################

def currentLoc():
    ip = requests.get('https://api.ipify.org').text
    url = 'http://ip-api.com/json/'+ip
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    return city

################################### Fetch Weather Info (From API) ##################

def weatherInfo(location, user):
    api_key = ""
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    try:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        humidity = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']
        printX(f"it's currently {weather_desc} outside in {location}, and temperature is %.0f degrees" % temp_city)
        speak(f"it's currently {weather_desc} outside in {location}, and temperature is %.0f degrees" % temp_city)
        print(f"Humidity is {humidity} % and wind speed is about {wind_speed} kilometre per hour\n")
        speak(f"humidity is {humidity} % and wind speed is about {wind_speed} kilometre per hour")
    except Exception as e:
        printX(f"sorry {user}, i'm unable to get the weather info")
        speak(f"sorry {user}, i'm unable to get the weather info")

################################### Give Random Advices to user ####################

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

################################### Info of Latest Movies ##########################

def get_trending_movies():
    TMDB_API_KEY = ""
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]

################################### Show location in Google maps ###################

def GoogleMaps(Place):
    url_place = "https://www.google.com/maps/search/" + str(Place)
    webbrowser.open(url=url_place)

################################### Fetch Weather Info (From web) ##################

def weather(location, user):
    from MainFiles.Database.Chatbot import qReplace
    content = location.replace('weather',"")
    content = qReplace(content)
    url = f"https://www.google.com/search?q="+'weather in'+str({content})
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    weather = data.find('div',class_="BNeawe").text
    printX(f"{user}, it's {weather} in {content}")
    speak(f"{user}, it's {weather} in {content}")

################################### To greet User ##################################

def wishMe(query, user):
    StrTime = datetime.datetime.now().strftime(f"%I:%M %p")
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        printX(f"Good Morning {user}")
        speak(f"Good Morning {user}")
        if 'afternoon' in query or 'evening' in query:
            printX(f"its {StrTime}, By the way.")
            speak(f"its {StrTime}, By the way.")

    elif hour>=12 and hour<18:
        printX(f"Good Afternoon {user}")
        speak(f"Good Afternoon {user}")
        if 'morning' in query or 'evening' in query:
            printX(f"its {StrTime}, By the way.")
            speak(f"its {StrTime}, By the way.")

    elif hour>=18 and hour<24:
        printX(f"Good Evening {user}")
        speak(f"Good Evening {user}")
        if 'afternoon' in query or 'morning' in query:
            printX(f"its {StrTime}, By the way.")
            speak(f"its {StrTime}, By the way.")
    else:
        printX(f"Its almost midnight {user}")
        speak(f"Its almost midnight {user}")
        if 'afternoon' in query or 'morning' in query:
            printX(f" By the way, its {StrTime}.")
            speak(f" By the way, its {StrTime}.")

################################### Play Offline Song(From device) #################

def music(query):
    with open('MainFiles\Data\config.json') as config:
        data = json.load(config)
    direc = data[0][f"{query}"]
    if direc=="" or "*****":
        music_dir = "MainFiles\music"
    else:
        music_dir = direc
    songs = os.listdir(music_dir)
    song = len(songs)
    num = random.randint(0,song-1)
    os.startfile(os.path.join(music_dir, songs[num]))

################################### Control Volume of Device #######################

def volume(query):
    if "10" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",5)

    elif "20" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",10)
    
    elif "30" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",15)
    
    elif "40" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",20)
    
    elif "50" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",25)
    
    elif "60" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",30)
    
    elif "70" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",35)
    
    elif "80" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",40)

    elif "90" in query:
        pyautogui.press("volumedown",50)
        pyautogui.press("volumeup",45)

    elif 'full' in query or '10' in query:
        pyautogui.press("volumeup",50)

    elif "mute" in query or "0" in query or "zero" in query:
        pyautogui.press("volumemute")
    else:
        speak("i can set volume from 1 to 10")

################################### Control Brightness of Device ###################

def display_brightness(query):
    if query<=100:
        pct.set_brightness(query)
    else:
        speak("i can set brightness from 0 to 100")

################################### Take Notes #####################################

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(os.path.join("MainFiles\\Notes", file_name), "w") as f:
        f.write(text)
    path = f"MainFiles\\Notes\\{file_name}"
    subprocess.Popen(["notepad.exe", path])

################################### Take Screeshot of Screen #######################

def screenshot():
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-")
    img = pyautogui.screenshot()
    path = f"MainFiles/Screenshot/{file_name}.png"
    img.save(path)

################################### Calculate Square Root ##########################

def root(num):
    try: 
        ans = math.sqrt(int(num))
        printX(f'square root of {num} is %.2f' % ans)
        speak(f'square root of {num} is %.2f' % ans)
    except Exception as e:
        printX("i can't understand what you say")
        speak("i can't understand what you say")

################################### For Alarm Automation ###########################

def alarm(h,s,s1): 
    command = "start ms-clock:"
    subprocess.run(command, shell=True)
    t.sleep(2)
    pyautogui.getActiveWindow().maximize()
    t.sleep(1)
    pyautogui.click(x=147, y=149)
    pyautogui.click(x=1820, y=961)
    pyautogui.write(h)
    pyautogui.press("tab")
    pyautogui.press(s)
    pyautogui.press(s1)
    pyautogui.click(x=913, y=808)
    os.system(f"taskkill /f /im time.exe")

################################### Fecth Latest Space News (NASA) #################

def Nasanews(date):
    from MainFiles.Database.Translator import takeCommand
    Time = datetime.datetime.now().strftime(f"%I-%M-%S")
    Date = datetime.date.today().strftime("%Y-%m-%d")
    api_key=""
    url = "https://api.nasa.gov/planetary/apod?api_key="+api_key

    printX(f"Extracting latest news from Nasa")
    speak(f"Extracting latest news from Nasa")

    param = {'date':str(date)}
    r = requests.get(url, params=param)
    Data = r.json()
    info = Data['explanation']
    title = Data['title'] 
    image_url = Data['url']

    fileName = str(date)+Time+'.jpg'
    image = requests.get(image_url)

    with open(fileName,'wb') as f:
        f.write(image.content)
    
    p1 = f"{cwd}\\"+str(fileName)
    p2 = f"{cwd}\\MainFiles\\Images\\"+str(fileName)

    os.rename(p1,p2)
    printX("here's an image by nasa.")
    speak("here's an image by nasa.")
    img = Image.open(p2)
    img.show()

    info_list = info.split(".")

    printX(f"Title : {title}")
    speak(title)
    print(f"News : {info}")
    for i in range(3):
        speak(f"{info_list[i]}")
    speak("Would you like to hear more.")
    ask = takeCommand()
    if 'yes' in ask:
        for i in range(3,7):
            speak(f"{info_list[i]}")
        os.system("taskkill /f /im Microsoft.Photos.exe")
    elif 'no' in ask:
        os.system("taskkill /f /im Microsoft.Photos.exe")
        speak('okay')
    else:
        os.system("taskkill /f /im Microsoft.Photos.exe")
        pass

################################### Developer Info Notifcation  ####################

def notification(query):
    title = query
    toast = Notification(app_id='Alfred AI',
                        title=f"{title} Info",
                        msg="For more information about Developer",
                        # icon="alfred.ico",
                        duration="long")

    toast.add_actions(label="LinkedIn", launch="https://www.linkedin.com/in/akbar-k-09b28618b/")
    toast.add_actions(label="GitHub", launch="https://github.com/Akbarkal")
    toast.set_audio(audio.Default, loop=False)
    toast.show()

################################### Pop Window Notifcation #########################

def popupNotification(title, path):
    toast = Notification(app_id='Alfred AI',
                        title=title,
                        msg=f"Successfully to {path}",
                        duration="long")

    toast.set_audio(audio.Default, loop=False)
    toast.show()

################################### Link of Any YT Video or Song ###################

def playonytm(opp: str, topic: str, use_api: bool = False, open_video: bool = True) -> str:

    if use_api:
        response = requests.get(
            f"https://pywhatkit.herokuapp.com/playonyt?topic={topic}"
        )
        status_code = response.status_code
        if status_code == 200:
            if open_video:
                webbrowser.open(response.content.decode("ascii"))
            return response.content.decode("ascii")
        elif 400 <= status_code <= 599:
            raise exceptions.UnableToAccessApi(
                "Unable to access pywhatkit api right now"
            )
    else:
        url = f"https://www.youtube.com/search?q={topic}"
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1 
            if i == "WEB_PAGE_TYPE_WATCH":
                break
        if lst[count - 5] == "/results":
            raise Exception("No Video Found for this Topic!")
        
        if opp=="play":
            link_ = f"https://music.youtube.com{lst[count - 5]}"
        else:
            link_ = f"https://www.youtube.com{lst[count - 5]}"
        link_list = link_.split("\\")
        link = link_list[0]
        return link

################################### Search any query in Web ########################

def SearchOnWeb(query, num) -> str:
    url = f"https://www.google.com/search?q={query}&num={num}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    search_results = soup.select('.tF2Cxc')

    for result in search_results:
        webbrowser.open(result.a['href'])

################################### Currency convertor func 1 ######################

def curCont(amount, fromCur, toCur):
    if amount == "None":
        amount = 1
    response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={fromCur}&to={toCur}")
    ans = response.json()['rates'][toCur]
    return ans
    # "https://api.frankfurter.app/latest?amount=1&from=RUB&to=INR"
    # "https://open.er-api.com/v6/latest/USD"

################################### Currency convertor func 2 ######################

def curCont1(amount, fromCur, toCur):
    if amount == "None":
        amount = 1
    response = requests.get(f"https://open.er-api.com/v6/latest/{fromCur}")
    ans = response.json()['rates'][toCur]
    return ans
    # "https://api.frankfurter.app/latest?amount=1&from=RUB&to=INR"
    # "https://open.er-api.com/v6/latest/USD"

################################### Currency convertor func 3 ######################

def curCont2(amount, fromcur, tocur):
    a = CurrencyConverter()
    return a.convert(amount, fromcur, tocur)

################################### Download Audios from YT ########################

def download_music(query):
    try:
        yt = YouTube(query)
        audio = yt.streams.filter(mime_type="audio/mp4", only_audio=True, abr="128kbps").first()
        with open('MainFiles\Data\config.json') as config:
            data = json.load(config)
        cwd = data[0]["downloaded_songs"]
        if cwd == "" or cwd== "*****":
            printX("You haven't provided any folder path to download songs")
            printX("Do you want to save the downloaded song in default folder")
            speak("You haven't provided any folder path to download songs")
            speak("Do you want to save the downloaded song in default folder")
            per = takeCommand()
            if "yes" in per:
                audio.download("MainFiles/music/")
            else:
                pass
        else:
            audio.download(cwd)
        return True
    except Exception as e:
        print(e)
        return False

################################### Search/Download Images from Google #############

def downloadImage(query,n=5):
    query = query.replace('images','')
    query = query.replace('image','')
    query = query.replace('search','')
    query = query.replace('show','')
    query = query.replace(' ','')
    try:
        downloader.download(query, limit=n, output_dir="MainFiles\Pictures", force_replace=False, timeout=60)
        return True
    except Exception as e:
        print(e)
        return False

def googleSearch(query):
    query += "&tbm=isch"
    webbrowser.open("https://www.google.com/search?q=" + query)

################################### Download Videos from YT ########################

def download_video(query):
    try:
        yt = YouTube(query)
        video = yt.streams.filter(progressive=True).get_highest_resolution()
        video.download("MainFiles/video/")
        return True
    except Exception as e:
        print(e)
        return False

################################### End ############################################