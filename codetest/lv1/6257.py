fruit = ['   apple    ','banana','  melon']


# 튜플
# answer = {(key.strip() , len(key.strip()) ) for key in fruit }


answer2 = {key.strip(): len(key.strip()) for key in fruit}


# print(answer)

print(answer2)



