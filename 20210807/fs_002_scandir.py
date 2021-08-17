import os
from datetime import datetime

def format_datetime(timestamp):
    utc_timestap = datetime.utcfromtimestamp(timestamp) # 2021-08-17 02:14:41.567888 형태
    formated_date = utc_timestap.strftime("%Y%m%d %H:%M:%S")  # 20210817 02:14:41 형태
    return utc_timestap
    # return formated_date

# 디렉토리에 무슨 파일이 있는지 확인
# 언제 생성되었는지 확인
def display_entries_in_directory(directory):
    # print(os.listdir(directory))
    with os.scandir() as entries:
        for entry in entries:
            print("이름 : ", entry.name)
            info = entry.stat()
            print("생성시간: ", format_datetime(info.st_ctime))
            print("최종 수정시간: ", format_datetime(info.st_atime))
            print("파일 크기: ", info.st_size) 
            print("----------------------------------------")


# 디렉토리만 
def display_directory(directory):
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_dir():
                print("디렉토리 이름: ", entry.name)
                
# 파일만
def display_files(directory):
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_file():
                print("파일 이름: ", entry.name)

# error  ===> AttributeError: 'str' object has no attribute 'is_dir'
# def display_with_list(directory):
#     for entry in os.listdir():
#         if entry.is_dir():
#             print("list directory: ", entry)


if __name__ == "__main__":
    display_entries_in_directory("./")
    # display_directory("./")
    # display_files("./")
    