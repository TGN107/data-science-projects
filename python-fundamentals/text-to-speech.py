import gtts
import playsound
text=input("enter something here:")
sound=gtts.gTTS(text,lang='ko')
sound.save("message.mp3")
playsound.playsound("message.mp3")