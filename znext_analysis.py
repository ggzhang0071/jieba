import json
from json import encoder
from json import decoder
from operator import index
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
res={}
res={key:val for  key,val in  repeated.items()  if len(val)>1}
        
topic_stack=[]
for keyword,topic_index in res.items():
    topic_related={}
    for i in topic_index:
        topic_related[i]=data[i]["Text"]
    topic_stack.append(topic_related)

with open("output.json","wt",encoding="utf-8") as fid:
    json.dump(topic_stack,fid,ensure_ascii=False,indent=2)



    

    
