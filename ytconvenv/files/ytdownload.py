from pytube import YouTube
from pathlib import Path

mylink = input("Enter a link:")
try:
    yt = YouTube(mylink)
except:
    print("Error has occured")

def prints(yt):
    print("Title:", yt.title)
    print("# of views: ", yt.views)
    print("Video Length: ", yt.length, " seconds")
    #print("Description: ",yt.description)
    print("Ratings: ", yt.rating)

prints(yt)

def dwnload():
    ys=yt.streams.get_highest_resolution()
    try:
        ys.download(str(Path.home()/ "Downloads"))

        print("Thanks for downloading")

    except:
        print("error has occured!!")

prompt = input("Would you like to download this file? ")

if prompt == "yes" or prompt == "y"or prompt =="YES" or prompt =="Yes":
    dwnload()
else:
    print("Okay, Thank you!")
