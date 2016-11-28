import os
import webbrowser

f = open('myList.html', 'w')
f.write("<!DOCTYPE html>")

f.write("<html>")
f.write("<body>")
f.write("<h1>")
f.write(str(os.getcwd()))
f.write("</h1>")

for i in os.listdir(os.getcwd()):

	f.write(str(i))
	f.write("</br>")

f.write("</body>")
f.write("</html>")
f.close()

webbrowser.open("myList.html", new=2)