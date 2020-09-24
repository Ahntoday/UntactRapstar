import markovify
import string
import re
import pandas as pd

from typing import List

class MyTokenizer:
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = text.split()
        return tokens

# total_train = pd.read_csv('total_poem.csv')

#핵심 문장 추출
from typing import List
from textrankr import TextRank

#증가형 벌스 구조로 제작
#8  - 메인 가사 
#6 ~ 7 <- 훅x2 + 메인 가사 + 훅x2 
#4 ~ 5 <- 훅x3 + 메인 가사 + 훅x3
def total_work(total_train):
    new_text = []
    mytokenizer: MyTokenizer = MyTokenizer()
    textrank: TextRank = TextRank(mytokenizer)
    for i in range (0,len(total_train)):
        if(total_train.loc[i,"문장 개수"] >= 8):
            k: int = 8
            summarized: str = textrank.summarize(total_train.loc[i,"시"],k)
            new_text.append(summarized+"\n")
        else:
            m = (7 - total_train.loc[i,"문장 개수"]) // 2 +1
            k = total_train.loc[i,"문장 개수"]
            main_summarized: str = textrank.summarize(total_train.loc[i,"시"],m)
            summarized: str = textrank.summarize(total_train.loc[i,"시"],k)

            if(m > 2):
                main_list = main_summarized.split("\n")
                for i in range (0,m):
                    summarized = summarized.replace(main_summarized[i],"")
                new_text.append(main_summarized+"\n"+summarized+"\n"+main_summarized+"\n")
            else:
                new_text.append(main_summarized+"\n"+summarized+"\n"+main_summarized+"\n")

    text_model = markovify.NewlineText(new_text, state_size = 2)

    lyrics = []
    for i in range(8):
        lyrics.append(text_model.make_sentence())

    lyrics = list(filter(lambda a: a != None, lyrics))

    final = []
    for i in range(0,len(lyrics)):
        if len(lyrics[i]) > 50:
            final.append(lyrics[i][:50])
            final.append(lyrics[i][50:])
        else:
            final.append(lyrics[i])
    if not final:
        total_work(total_train)
    else:
        return final
    return final