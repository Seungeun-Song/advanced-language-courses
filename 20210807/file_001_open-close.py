
def write_new_content(something):
    # with open("descriptions/description-01.txt", "w") as f:
    with open("descriptions/description-01.txt", "a", encoding="UTF-8") as f:  # a = append
        f.write(something)
    
def print_content():
    with open("descriptions/description-01.txt", "r", encoding="UTF-8") as f:
        contents = f.read()
        print(contents)

if __name__ == "__main__":
    # try:
    #     with open("descriptions/description-01.txt", "r") as f:
    #         contents = f.read()
    #         print(contents)
    # except FileNotFoundError as ex:
    #     print("파일이 존재하지 않습니다.")
    write_new_content("\n 대한민국 만세")
    print_content()