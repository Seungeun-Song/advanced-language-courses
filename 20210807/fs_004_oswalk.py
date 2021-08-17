import os

def top_down_walk():
    for dirpath, dirnames, files in os.walk("images/"):
        print("디렉토리: ", dirpath)
        print("포함된 디렉토리들")
        for dirname in dirnames:
            print(dirname)
        print("포함된 파일들")
        for file in files:
            print(file)
        print()


def bottom_up_walk():
    for dirpath, dirnames, files in os.walk("images/", topdown=False):
        print("디렉토리: ", dirpath)
        print("포함된 디렉토리들")
        for dirname in dirnames:
            print(dirname)
        print("포함된 파일들")
        for file in files:
            print(file)
        print()
        

if __name__ == "__main__":
    # top_down_walk()
    bottom_up_walk()