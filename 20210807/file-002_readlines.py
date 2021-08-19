def print_file_content():
    with open("descriptions/description-02.txt","r", encoding="UTF-8") as f:
        # print(f.read(10))  # 10글자만
        print(f.read())

def print_file_content_readlines():
    with open("descriptions/description-02.txt","r", encoding="UTF-8") as f:
        lines = f.readlines()
        print(type(lines))   # <class 'list'>
        print(lines)         # ['대한민국 만세! 대한민국!\n', '아자아자!\n', '배구 화이팅!!\n', '올림픽 감동!!\n']
        print(lines[2])

def print_file_content_oneline_at_time():
    with open("descriptions/description-02.txt","r", encoding="UTF-8") as f:
        line = f.readline()
        # print(type(line))   # <class 'str'>
        # print(line)         
        while line != "":
            print(line, end ="")
            line = f.readline()


if __name__ == "__main__":
    # print_file_content()
    # print_file_content_readlines()
    print_file_content_oneline_at_time()