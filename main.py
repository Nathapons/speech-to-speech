import os

from lib.listen_thai import listen_thai
from lib.gemini import get_prompting
from lib.speak_text import speak_text


if __name__ == "__main__":
    if os.path.exists('generate'):
        os.mkdir('generate')
        
    i = 1
    while True:
        print("เริ่มฟัง... พูดได้เลย!")
        try:
            if i > 1:
                text = listen_thai()
                if text is not None:
                    prompting = get_prompting(text)
                    speak_text(prompting)
                    print(f'Gemini ตอบว่า {prompting}')
            else:
                speak_text("สวัสดีครับมีอะไรให้ช่วยไหมครับ")
                
            i += 1
        except Exception:
            print("Program error")
