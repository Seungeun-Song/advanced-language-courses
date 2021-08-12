from googlesearch import search

query = input("무엇을 검색할까?")

for i in search(query, start=0, stop=10):
    print(i)