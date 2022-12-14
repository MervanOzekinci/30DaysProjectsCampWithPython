# -*- coding: utf-8 -*-
"""text_to_speech (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q6EHCttcw9C8BvvIJhXS4yu0Px_lJ6Di
"""

pip install gTTS

from tkinter import *
from gtts import gTTS

# this module helps to
# play the converted audio 
import os
 

root = Tk()#bir obje olusturduk
 
#penceremiz icin iki ayri Frame ve özelliklerini tanimliyioruz
frame1 = Frame(root,
               bg = "red",
               height = "150")
frame1.pack(fill = X)
 
 
frame2 = Frame(root,
               bg = "blue",
               height = "750")
frame2.pack(fill=X)
 
 
 
#pencerede gösterilecek label özellikleri giriyoruz
label = Label(frame1, text = "Text to Speech",
              font = "bold, 30",
              bg = "lightpink")
 
label.place(x = 180, y = 70)

label.place(x = 180, y = 70)
label2=Label(frame1,text="by: Mervan Özekinci",
             font="bold 18",bg="white")
label2.place(x=0,y=10)

label3=Label(frame2,text="Okunacak Texti lütfen kutucuga giriniz!",
             font="bold 18",bg="white")
label3.place(x=140,y=10)
 
# textimizi girecegimiz alani olusturalim
entry = Entry(frame2, width = 45,
              bd = 4, font = 14)
 
entry.place(x = 100, y = 72)
entry.insert(0, "")
 
#alinacak texti sese dönüstürecek fonksiyonun tanimi
def play():
 
  
    language = "tr"#text bu dilde algilansin
 
    myobj = gTTS(text = entry.get(),#texti kutucuktan al
                lang = language,#dili yukarida tanimladik
                slow = False)#hizi yavas olmasin
 
 
 
   #textin sesli halinin kaydi
    myobj.save("text_kaydi.wav")
    os.system("text_kaydi.wav")
 
#buton tanimlamasi

btn = Button(frame2, text = "SUBMIT",
             width = "15", pady = 10,
             font = "bold, 15",
             command = play, bg='yellow')
 
btn.place(x = 250,
          y = 130)
 
# give a title 
root.title("text_to_speech_convertor")
 
 
 
#size özellikleri
root.geometry("650x550+350+200")
 
# gui calistir
root.mainloop()