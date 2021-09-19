import json
import jieba
import jieba.analyse
path="znext_data/question_cn_processed.json"

with open(path,"r",encoding="utf-8") as fid:
    data=json.load(fid)
    
for topic in data:
    tags = jieba.analyse.extract_tags(topic, topK=10)

    
