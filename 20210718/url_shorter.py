import pyshorteners

url = input("줄일 URL 입력 : ")
short_url = pyshorteners.Shortener().tinyurl.short(url)
print("short_url : ", short_url)