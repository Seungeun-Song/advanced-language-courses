import pyqrcode
import pyshorteners

msg = input("QR코드로 변환할 메시지를 입력해주세요 : ")
qrcode = pyqrcode.create(msg)
qrcode.png("my_qrcode1.png", scale=15)
url = 'www.naver.com'

print("QR코드가 생성되었습니다.")
