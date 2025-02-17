import speech_recognition as sr


def listen_thai():
    recog = sr.Recognizer()

    mic_list = sr.Microphone.list_microphone_names()
    if not mic_list:
        print("⚠️ ไม่พบไมโครโฟนที่ใช้งานได้")
        return None
    
    with sr.Microphone() as source:
        try:
            recog.adjust_for_ambient_noise(source, duration=1)  # ปรับเสียงรบกวนรอบข้าง
            audio = recog.listen(source, timeout=10, phrase_time_limit=10)

            user_text = recog.recognize_google(audio, language="th")
            print(f'คุณสอบถามว่า {user_text}')
            return user_text
        except sr.WaitTimeoutError:
            print("⏳ ไม่มีเสียงพูด ตรวจสอบไมโครโฟน หรือพูดใหม่อีกครั้ง")
        except sr.UnknownValueError:
            print("🤷‍♂️ ไม่สามารถเข้าใจเสียงที่ได้ยิน")
        except sr.RequestError as e:
            print(f"⚠️ เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
    
    return None