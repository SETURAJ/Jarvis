import winsound
from win10toast import ToastNotifier


def timer(reminder, seconds):
    notificator = ToastNotifier()
    notificator.show_toast("Reminder", f"Alarm will go off in {seconds} Seconds.", duration=20)
    notificator.show_toast(f"Reminder", reminder, duration=20)

    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)
    print("reminder sir...")


if __name__ == "__main__":
    word = input("What would you remind of: ")
    sec = int(input("Enter seconds: "))
    timer(word, sec)

# In this we can do it our way also
# elif 'play music' in query:
#     music_dir = "D:\\Favourite Song"
#     songs = os.listdir(music_dir)
#     print(songs)
#     os.startfile(os.path.join(music_dir, songs[0]))

# elif 'send email to jaynish' in query:
#     speak('Whome do you want to mail sir??')
#     try:
#         speak("What should I Say?")
#         # name = takeCommand()
#         # speak(f"You have named this person out {name}")
#         content = takeCommand()
#         to = "mandaliasj22@hotmail.com"
#         sendEmail(to, content)
#         speak("Email has been sent!!")
#     except Exception as e:
#         print(e)
#         speak("Sorry I am not able to send the mail sir ")


# emailID = {'jaynish' : 'mandaliasj22@hotmail.com',
#             'seturaj' : 'seturajmatroja@gmai.com',
#           }


#  This will not work if you haven not allow less security aaps in your PC
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('mandaliasj22@hotmail.com', 'Password')
#     server.sendmail('mandaliasj22@hotmail.com', to, content)
#     server.close()
