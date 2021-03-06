import glob

def display_pngs(matching_string):
    png_files = glob.glob(matching_string)
    print(png_files)

def find_monster_one(matching_string):
    filtered_items = glob.glob(matching_string)
    print(filtered_items)

def find_monster_one_in_subdirs(matching_string):
    for file in glob.iglob(matching_string, recursive = True): # recursive = 재귀적. 찾을 때까지 계속 돈다
        print(file)

if __name__ == "__main__":
    # display_pngs("images/*.png")
    # find_monster_one("images/*monster01*")
    find_monster_one_in_subdirs("**/*monster01*")