from tkinter import *
from tkinter import ttk

import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1237f5453296af223ca4ddcf380f071f").json()
    w_label_1.config(text=data["weather"][0]["main"])
    wb_label_1.config(text=data["weather"][0]["description"])
    temp_label_1.config(text=str(int(data["main"]["temp"]-273.)))
    per_label_1.config(text=data["main"]["pressure"])

    # Update the dashboard with the weather data
    w_label_1.config(text=weather_main)
    wb_label_1.config(text=weather_description)
    temp_label_1.config(text=str(temperature) + " °C")
    per_label_1.config(text=str(pressure) + " hPa")
    
    # Change background color based on temperature
    if temperature <= 15:
        win.config(bg="lightblue")  # Cold weather
    elif 15 < temperature <= 25:
        win.config(bg="lightgreen")  # Mild weather
    else:
        win.config(bg="orange")  # Warm weather
        
        win.update_idletasks()

win = Tk()
win.title("Weather Forecast App Using Python")
win.config(bg = "blue")
win.geometry("500x570")

name_label = Label(win,text="Weather Forecast App", 
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25, y=50, height=50,width=450)

city_name = StringVar()
list_names = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather Forecast App",values=list_names,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25, y=120, height=50,width=450)


w_label = Label(win,text="Weather Climate", 
                   font=("Time New Roman",20))
w_label.place(x = 25, y = 260, height = 50,width = 210)

w_label_1 = Label(win,text="", 
                   font=("Time New Roman",20))
w_label_1.place(x = 250, y = 260, height = 50,width = 210)

wb_label = Label(win,text="Weather Description", 
                   font=("Time New Roman",16))
wb_label.place(x = 25, y = 330, height = 50,width = 210)
wb_label_1 = Label(win,text="", 
                   font=("Time New Roman",17))
wb_label_1.place(x = 250, y = 330, height = 50,width = 210)


temp_label = Label(win,text="Temperature", 
                   font=("Time New Roman",20))
temp_label.place(x = 25, y = 400, height = 50,width = 210)
temp_label_1 = Label(win,text="", 
                   font=("Time New Roman",20))
temp_label_1.place(x = 250, y = 400, height = 50,width = 210)

per_label = Label(win,text="Pressure", 
                   font=("Time New Roman",20))
per_label.place(x = 25, y = 470, height = 50,width = 210)
per_label_1 = Label(win,text="", 
                   font=("Time New Roman",20))
per_label_1.place(x = 250, y = 470, height = 50,width = 210)

button = Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get)
button.place(y = 190, height = 50, width = 100, x = 200)

win.mainloop()