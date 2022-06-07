import pyshorteners

url = input("Enter the URL to be shortened ")
shortner = pyshorteners.Shortener()
a = shortner.tinyurl.short(url)
print(a)