import os
print("Current directory::"+os.getcwd())
filename ='C:\Users\Microsoft\Desktop\namrataindustrialtraining\pythonworkplace'
print("Size :: "+str(os.path.getsize(filename)))
print("Last modified date :: "+str(os.path.getmtime(filename)))
print("Creation date and time ::"+str(os.path.getctime(filename)))