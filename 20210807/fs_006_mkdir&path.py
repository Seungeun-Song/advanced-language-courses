import os
from pathlib import Path

def make_logs_dir():
    try:
        os.mkdir("logs/")  # exist_ok = True 안됨. os에서 불러오는 것과 path에서 불러오는 게 다름
    except FileExistsError as ex:
        print("이미 log 디렉토리가 존재합니다!")

def make_output_dir(): # 디렉토리가 없으면 자동 생성
    dir_path = Path("output/")
    dir_path.mkdir(exist_ok = True)

if __name__ == "__main__":
    # make_logs_dir()
    make_output_dir()