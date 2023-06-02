################################### Modules Importing ##############################

from tkinter import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MainFiles.Database.AlfredUI import Ui_MainWindow

################################### Global Variable for Database ###################

global User
global Contact_list
global Light
global face_path

try:
    from MainFiles.Database.main import *

except Exception as e:
    print(e)
    print("Alfred Not Available\n")
    speak("Alfred Not Available")
    print("Please connect to internet...")
    speak("please connect to internet. or check network connection")
    sys.exit()
#### END


################################### OPEN AI Function ###############################

def ReplyBrain(question, chat_log=None):
    import json, openai
    from dotenv import load_dotenv
    try:
        with open('MainFiles\Data\config.json') as config:
            data = json.load(config)
        API = data[0]['openai']
    except Exception as e:
        print(e)
        pass
        
    openai.api_key = API
    load_dotenv()
    completion = openai.Completion()
    try:
        FileLog = open("MainFiles\\Data\\chat_log.txt","r")
        chat_log_template = FileLog.read()
        FileLog.close()

        if chat_log is None:
            chat_log = chat_log_template

        prompt = f'{chat_log}You : {question}\nAlfred : '
        response = completion.create(
            model = "text-davinci-003",
            prompt = prompt,
            temperature = 0.5,
            max_tokens = 100,
            top_p = 0.3,
            frequency_penalty = 0.5,
            presence_penalty = 0)
        answer = response.choices[0].text.strip()
        # chat_log_template_update = chat_log_template + f'\nYou : {question} \nAlfred : {answer}'
        # FileLog = open("Data\\chat_log.txt",'w')
        # FileLog.write(chat_log_template_update)
        # FileLog.close()
        return answer
    except Exception as e:
        print(e)
        pass
#### END


################################### Face Recognition System ########################

def Face_Rec(Matched, User, face_path):
    from MainFiles.Database.modules import face_recognition, cv2, np
    video_capture = cv2.VideoCapture(0)

    imgAttariak = face_recognition.load_image_file(face_path)
    imgAttariak_encoding = face_recognition.face_encodings(imgAttariak)[0]
    known_face_encodings = [
        imgAttariak_encoding
    ]
    known_face_names = [
        User,
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    Matched = True

                face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Alfred Face Recognition', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if Matched:
            # print("verification successfull")
            break


    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
    return Matched
#### END


################################### Home Appliances Automation #####################

api = TuyaApi()
try:
    with open('MainFiles\Data\config.json') as config:
        data = json.load(config)
    username = data[0]['username']
    password = data[0]['password']
    country_code = data[0]['country_code']
    application = data[0]['application']
    api.init(username, password, country_code, application)
    device_ids = api.get_all_devices()
    lights = dict(sorted(dict((i.name(), i) for i in device_ids if i.obj_type == 'light').items()))
    devices = {**lights}
    devices_list = [*devices.values()]
    print("Devices connected...")
    Light = True

except Exception as e:
    print(e)
    Light = False
    devices_list = []
    print("Devices disconnected!!! (Please wait for 3 mins...)")
    pass
#### END


################################### Main GUI Class #################################

class Contact_func(QThread):
    def __init__(self):
        super(Contact_func,self).__init__()

    def run(self):
        self.contactexe()

    def contactexe(self):
        try:
            subprocess.Popen("Contact.exe")
        except Exception as e:
            print(e)

openContact = Contact_func()

class User_func(QThread):
    def __init__(self):
        super(User_func,self).__init__()

    def run(self):
        self.userexe()

    def userexe(self):
        try:
            subprocess.Popen("Alfred_DB.exe")
        except Exception as e:
            print(e)

openUser = User_func()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.mainfile()

    def mainfile(self):
################################### User Contact's Data fetching ##################################
        try:
            with open("MainFiles\Data\contact.json","r") as data:
                Contact_list = json.load(data)
                data.close
                print("contacts fetched successfully")

        except Exception as e:
            print(e)
            pass
#### END


################################### User Face Data fetching ##################################
        try:
            with open('MainFiles\Data\config.json') as config:
                data = json.load(config)
            face_path = data[0]['face_data']
            User = data[0]['name']
            song_dir = data[0]["downloaded_songs"]
            if User=="*****" or User=="":
                User = "sir"
        except Exception as e:
            song_dir = "*****"
            User = "*****"
            face_path = "*****"
            print(e)

        try:
            res = requests.get("https://www.google.com", timeout=1)
        except Exception as e:
            print("Alfred Not Available\n")
            speak("Alfred Not Available")
            print("Please connect to internet...")
            speak("please connect to internet. or check network connection")
            sys.exit()
        speak("Starting face recognition.")
        try:
            auth = Face_Rec(False, User, face_path)
        except Exception as e:
            auth = False
            print(e)
            printX("no face data found")
            speak("no face data found")
            printX(f"You can add face data to my database by clicking the user icon on main window")
            speak(f"You can add face data to my database by clicking the user icon on main window")
            sys.exit()
        if auth:
            speak("face recognition successful.")
            printX(f"Welcome Back {User}, i'm Online And ready.")
            speak(f"Welcome Back {User}, i'm Online And ready.")

            while True:
                # permission = HinToEng()
                permission = TakeCommand()
                permission1 = wReplace(permission)
                permission2 = permission1.replace('all friend', 'alfred')
                if " alfred" in permission2:
                    if "goodbye" in permission2:
                        printX(f"goodbye {User}")
                        speak(f"goodbye {User}")
                        sys.exit()
                    else:
                        permission2 = permission2.split()[-1]
                if "alfred" in permission2:
                    TaskExecution(permission2, devices_list, User, Contact_list, Light, ReplyBrain,song_dir)
                    try:
                        res = requests.get("https://www.google.com",timeout=5)
                    except Exception:
                        print("Alfred Not Available\n")
                        speak("Alfred Not Available")
                        print("Please connect to internet...")
                        speak("please connect to internet. or check network connection")
                        sys.exit()
                elif "goodbye" in permission:
                    printX(f"goodbye {User}")
                    speak(f"goodbye {User}")
                    sys.exit()
        else:
            print("Authentication failed")
            speak("Authentication failed")
            sys.exit()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Start_btn.clicked.connect(self.startTask)
        self.ui.Close_btn.clicked.connect(self.close)
        self.ui.User_btn.clicked.connect(self.startUser)
        self.ui.Contact_btn.clicked.connect(self.startContact)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("MainFiles\Database\icons\gui.gif")
        self.ui.bg.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.Start_btn.hide()
        self.ui.Close_btn.show()
        speak("initializing all the system")
        startExecution.start()

    def startContact(self):
        openContact.start()
    
    def startUser(self):
        openUser.start()
    
app = QApplication(sys.argv)
alfred = Main()
alfred.show()
sys.exit(app.exec_())

################################### END #############################################