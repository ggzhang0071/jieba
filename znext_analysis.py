import json
import jieba
import jieba.analyse
path="znext_data/question_cn_processed.json"

with open(path,"r",encoding="utf-8") as fid:
    data=json.load(fid,strict=False)
    
keywords=[]
for i,topic in enumerate(data):
    tags = jieba.analyse.extract_tags(topic["Text"], topK=5,allowPOS=("n","vn"))
    #tags=jieba.analyse.TextRank(topic["Text"])
    keywords.append(tags)

repeated=dict()
for i  in  range(len(keywords)):
     for j in range(len(keywords[i])):
        keyword=keywords[i][j]
        if  keyword in repeated.keys():
            repeated[keyword].append(i)
        else:
            repeated[keyword]=[i]

for  key,val in  repeated.items():
    if len(val)>1:
        print(key,val)        

    
