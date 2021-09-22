from os import POSIX_FADV_NOREUSE


keywords=[]
for i in range(10):
    keywords.append([])
    keywords[i].append(tags)

repeated=dict()
for i  in  range(len(keywords)):
     for j in range(len(keywords[0])):
        keyword=keywords[i][j]
        if  keyword in repeated.keys():
            repeat[keyword].append(i)
        else:
            repeated[keyword]=[i]

            
for  key,val in  repeated.items():
    if len(val)>1:
        print(key,len(val))


