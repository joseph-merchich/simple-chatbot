import requests
import json
import sys
import time
model = "llama2:7b-chat"
outfile = sys.argv[2] if (len(sys.argv) == 3) else ""
url = "http://localhost:11434/api/chat"
sound = input("Would you like reading mode on? y/n")
if sound.lower() == "y":
    
    try:
        import pyttsx3
    except ImportError:
        print('The pyttsx3 module needs to be installed to run this')
        sys.exit()

    tts = pyttsx3.init()
    voice_on = True
    
def slowSpacePrint(text, interval=0.01):
    for character in text:
        print(character + '', end='',flush=True)
        time.sleep(interval)
    print()
    print()

def speak(text):
    tts.say(text)
    tts.runAndWait()
    
prompt = input("]")
text = "]" + prompt + "\n"
print()
messages = [{
    "role": "user",
    "content": prompt
    }]

while (prompt != ""):
    print("Thinking...")
    print()
    msg = {
        "model": model,
        "messages": messages,
        "stream": False
        }
    resp = requests.post(url, json=msg)
    if (resp.status_code != 200):
        raise ValueError("Bad response from Ollama server")

    reply = json.loads(resp.text)
    ans = reply['message']['content']
    text += ans + "\n\n"
    slowSpacePrint(ans)
    if voice_on == True:
        speak(ans)
    print()
    messages.append({
        "role": "assistant",
        "content": ans
        })
    
    prompt = input("]")
    if (prompt != ""):
        text += "]" + prompt + "\n"
        messages.append({
            "role": "user",
            "content": prompt
            })

        if (outfile != ""):
            with open(outfile, "w") as f:
                f.write(text)
