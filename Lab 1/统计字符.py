# starter code
# 提示：可能对你有帮助的东西QAQ: collections.counter, lambda表达式，zip，sort/sorted, string的replace和split方法

import collections

file_path = "D:\cs\ptb.train.txt" #我的path
word_dict = {}
with open(file_path, "r") as f:
  sentences = f.read().replace("\n", "<eos>").split()   #把“\n"换成了"<eos>"
  counter = collections.Counter(sentences)
# 完成排序和建立词表的工作
h=dict(counter)
d=sorted(h.items(),key=lambda x:x[1],reverse=True)
lst=[]
for i in range(len(d)):
    lst.append(d[i][0])
a=[i for i in range(len(lst))]
b=dict(zip(lst,a))
# b就是做好的词表
for i in range(len(sentences)):
    sentences[i]=b[sentences[i]]
print(sentences)
# sentences就是改完的句子列表