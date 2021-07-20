import pyqrcode

qrcode = pyqrcode.create(input("QR코드로 변환할 메시지를 입력해주세요 : "))
qrcode.png("my_qrcode.png", scale=7)
print("QR코드가 생성되었습니다.")