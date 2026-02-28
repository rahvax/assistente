import speech_recognition as sr
rec = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("[!] ajustando ruídos")
        rec.adjust_for_ambient_noise(source, 2)
        print("[@] ouvindo...")
        recorded = rec.listen(source)
        if not recorded:
            return False
        else:
            return recorded  
              
def transcript(recorded):
    if not recorded:
        return False
    try:
        text = rec.recognize_ibm(recorded, "KEY_HERE", "pt-BR")
        print(f"[@] {text}")
        return text
    except sr.UnknownValueError:
        print("[!] não foi possível ouvir")
        return False
    except sr.RequestError as error:
        print(f"[X] erro na API: {error}")
        return False
