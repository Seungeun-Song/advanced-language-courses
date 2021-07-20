import pyshorteners

url = input("줄일 URL 입력 : ")
short_url = pyshorteners.Shortener().tinyurl.short(url)
print("Short Url : ", short_url)