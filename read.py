#-*- coding:utf-8 -*-
import jieba
from jieba import posseg as pseg
import sys,os,re
reload (sys)
sys.setdefaultencoding("utf-8")
textname = sys.argv[1]
to_path = sys.argv[2]

try:
    os.remove(to_path)
except:pass

#加入自定义
jieba.load_userdict("context/vocab.sougou.utf8")
jieba.load_userdict("context/vocab.company.utf8")

stop_words = set()
def load_stopwords():
    with open("context/stopwords") as readme:
        for l in readme.readlines():
            stop_words.add(l.replace("\n","").encode("utf-8"))

load_stopwords()
def filter_date(utterance):
    utterance = re.sub(u"\d{1,}\s*年\d{1,}\s*月\d{1,}\s*日", "日期", utterance)
    utterance = re.sub(u"\d{1,}\s*月\d{1,}\s*日", "日期", utterance)
    utterance = re.sub(u"\d{1,}\s*月\d{1,}\s*日", "日期", utterance)
    utterance = re.sub(u"\d{2,}\s*年\d{1,}月", "日期", utterance)
    utterance = re.sub("\d{4}-\d{1,2}-\d{1,2}", "日期", utterance)
    return utterance

def cut_flag(text):
    s = []
    words = pseg.cut(text)

    for w in words:
        if w.flag in ("un","o","w","x"):continue
        if w.word.encode("utf-8") in stop_words:continue
        #if len(w.word.strip()) <= 3:continue
        if w.flag == "nr":
            s.append("人名")
        elif w.flag == "ns":
            s.append("地名")
        elif w.flag == "nt":
            s.append("公司")
        elif w.flag == "m":
            s.append("股票")
        else:
            s.append(w.word.strip())
    s.append("\n")

    if len(s) <= 2:
        s = ["不完整","句子","\n"]
    return s

with open(textname) as f_in:
    for x in f_in.readlines():
        o = x.split("\t")
        assert len(o) ==2 ,"must be 2"
        mid = o[0]
        text = o[1].encode("utf-8")
        text = filter_date(text)
        jie = cut_flag(text)
        jie = str(" ".join(jie))
        result = "%s\t%s" %(mid,jie)
        if len(result.split("\t")) != 2:
            print mid,"--",jie
        if result.strip() == "\n":continue
        with open (to_path,"a") as f_write:
            f_write.write(result)
