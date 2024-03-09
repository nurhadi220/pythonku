import speech_recognition as srec

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print("Mendengarkan........")
        suara = mendengar.listen(source, phrase_time_limit=3)
        try:
            print("Sedang diproses.....")
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except:
            pass
            return dengar

def run_michelle():
    layanan = perintah()
    if layanan:
        print("Layanan yang diinginkan:", layanan)

run_michelle() 

#uji coba pertama berhasil 