
import pyttsx3
import speech_recognition as srec
import datetime
import wikipediaapi
import wikipedia
import webbrowser
import os
import smtplib
import requests
from fake_useragent import UserAgent

print("Apa yang bisa ku bantu")
kapten = "arofan"
mesin = pyttsx3.init()
suara = mesin.getProperty("voices")
mesin.setProperty("voice", suara[0].id)

#berbicara
def ngomong(teks):
    mesin.say(teks)
    mesin.runAndWait()

#fungsi
def harapan():
    jam = int(datetime.datetime.now().hour)

    if 0 <= jam < 12:
        ngomong("Good morning  " + kapten)
    elif 12 <= jam < 18:
        ngomong("Good evening  " + kapten)
    else:
        ngomong("Good night   " + kapten)


#mic
def perintah():
     ar = srec.Recognizer() 
     
     with srec.Microphone() as source:
        print("Mendengarkan........")
        audio = ar.listen(source)

        try:
            print("Diproses.....")
            query = ar.recognize_google(audio, language='id-ID')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Apa tadi sayang")
            query = "Exception hit: User went silent"
            print(query)

     return query

#lets begin
ngomong("welcome master,   can i help you")
harapan()
query = perintah()

#ini menggunakan wikipedia-API
#disini saya menggunakan fake user agen agar bisa masuk ke website dan dapat menelusuri setiap detail yang ada di website terebut
#karena kalo tidak bot akan memblokir dan bot tidak dapat memasuki web tersebut

if "wikipedia" in query.lower():
    ngomong("Pencarian......")
    query = query.replace("wikipedia", "")
    
    # butuh fake agent
    # Menggunakan fake_useragent untuk mendapatkan user agent palsu
    ua = UserAgent()
    headers = {"User-Agent": ua.random}

    wiki_wiki = wikipediaapi.Wikipedia('id', headers = headers)
    hasil = wiki_wiki.page(query).summary
    page_py = wiki_wiki.page(query)

    # vv Buat debugging vv
    print(query)
    page_py = wiki_wiki.page('naruto')
    print("Page - Exists: %s" % page_py.exists())
    
    
    if page_py.exists():
        print(f"Judul Artikel: {page_py.title}")
        print(f"Isi Artikel: {page_py.text[:300]}")
        hasil = page_py.text[:300]  # Mengambil 300 karakter pertama sebagai ringkasan
        print(hasil)
        ngomong(hasil)
    else:
        ngomong("sorry i can't founded")
    print(hasil)
    ngomong(hasil)

