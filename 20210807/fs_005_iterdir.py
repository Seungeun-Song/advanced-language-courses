from pathlib import Path

def print_directory_contents():
    entries = Path.cwd()
    # print(type(entries))  -->  <class 'pathlib.WindowsPath'>
    # print(entries)        -->  C:\Users\SONG\Desktop\SEOUL_AI\20210807

    # entries = Path.home()   # home directory
    # print(type(entries))    --> <class 'pathlib.WindowsPath'>
    # print(entries)          -->  C:\Users\SONG

    for entry in entries.iterdir():
        print("name: ", entry.name)
        print("parent: ", entry.parent)
        print("parent.parent: ", entry.parent.parent)
        print("stem: ", entry.stem)
        print("suffix: ", entry.suffix)  # 확장명
        print("stat: ", entry.stat())
        print("===========================================")


if __name__ == "__main__":
    print_directory_contents()