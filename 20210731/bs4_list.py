from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import datetime


# 데이터를 xlsx에 저장하고 싶다!
# xlsx에서 데이터의 형식은 pandas의 dataframe과 유사(행과 열로 구성)
df_all = pd.DataFrame(columns= ["NO",	"대분류",	"중분류",	"NEIS식품명/상세식품명",	"식품설명",	"포장중량",	"중량단위",	"포장단위"])


url = "http://singsing.sejong.go.kr/pages/sub02_01.do?pageIndex=1&tmpcls2=&searchMenu=&searchMenu2=&searchKeyword1="
with request.urlopen(url) as f:
    # print(type(f.read().decode("utf-8")))
    target_page = BeautifulSoup(f.read().decode("utf-8"), "html5lib") # beatifulsoup으로 이런(f.read().decode("utf-8")) 페이지를 전달받아서 html5로 해석
    # print(type(target_page))
    

    # 페이지 정보
    # page_num = target_page.select("div.page_num a")
    # print(len(page_num))
    # for i in page_num:
    #     print(i)


    # table의 정보
    tr_list = target_page.select("tbody tr")
    # print(tr_list)
    # print(type(tr_list), len(tr_list))
    
    
    # table -> tbody -> tr -> td 정보만
    for tr in tr_list:
        list_td = tr.find_all("td")

        #type : ResultSet
        # print(type(list_td), len(list_td)) 
        # print(list_td, "\n")

        
        # type: Tag
        # print(type(list_td[0])) 
        # print(f"{list_td[0]}{list_td[1]}{list_td[2]}{list_td[3]}{list_td[4]}{list_td[5]}{list_td[6]}{list_td[7]}", "\n")

        # type : str 
        # print(type(list_td[0].text))
        # print(f"{list_td[0].text}{list_td[1].text}{list_td[2].text}{list_td[3].text}{list_td[4].text}{list_td[5].text}{list_td[6].text}{list_td[7].text}", "\n")        

        # dataframed을 list로 저장
#         df_all = df_all.append([
#             [
#                 list_td[0].text,
#                 list_td[1].text,
#                 list_td[2].text,
#                 list_td[3].text,
#                 list_td[4].text,
#                 list_td[5].text,
#                 list_td[6].text,
#                 list_td[7].text
#             ]
#         ], ignore_index=True)

# print(df_all)
# print(df_all.shape)


        # dataframe을  딕셔너리 형태로 저장
        df_all = df_all.append({
            "NO" : list_td[0].text,
            "대분류" : list_td[1].text,
            "중분류" : list_td[2].text,
            "NEIS식품명/상세식품명" :  list_td[3].text,
            "식품설명" :  list_td[4].text,
            "포장중량" :  list_td[5].text,
            "중량단위" :  list_td[6].text,
            "포장단위" :  list_td[7].text
            
        }, ignore_index=True)

# print(df_all)
# print(df_all.shape)

# 저장
now = datetime.datetime.now()
df_all.to_excel("식재료 종류_" + now.strftime("%Y%m%d%H%M%S") +".xlsx", index = False)
