from tkinter import *
from tkinter import font
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

app = Tk()
app.geometry("800x1000")
bg = ImageTk.PhotoImage(
    file="hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg")
canvas = Canvas(app, width=800, height=1000)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")


def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open(
        "hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')


# Bind the function to configure the parent appdow
app.bind("<Configure>", resize_image)


def fetchNews():
    country = countrytext.get()
    link = "https://api.printful.com/countries"
    response = requests.get(link)
    data = response.json()
    result = data["result"]
    cc = ''

    for eachresult in result:
        if country.lower() == eachresult["name"].lower():
            cc = eachresult["code"]

    if cc == '':
        messagebox.showerror("error", "Invalid Country name")
    else:
        fetchTopa20News(cc.lower())


def fetchTopa20News(cc):
    link = "https://newsapi.org/v2/top-headlines?country=" + \
        cc+"&apiKey=bdc912d442614e15846f1804f1b751d8"
    response = requests.get(link)
    data = response.json()
    articles = data["articles"]
    mytitles = ""
    count = 1
    for eacharticles in articles:
        mytitles = mytitles+str(count)+" . "+eacharticles["title"]+"\n"
        count += 1
    label.config(text=mytitles)


countrytext = StringVar()
country_entry = Entry(app, textvariable=countrytext)
country_entry.place(x=430, y=10)

searchbutton = Button(app, text="Search", width=10,
                      height=1, command=fetchNews)
searchbutton.place(x=450, y=40)

label = Label(app, text="", font=("bold", 15),bg="pink")
label.place(x=10, y=70)
app.mainloop()
