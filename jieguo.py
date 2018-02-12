#-*- coding:utf-8 -*-
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
textname = sys.argv[1]
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)
import json
import io

def all_seg():
    data_path = os.path.join(curdir,textname)
    d = {}
    with open(data_path, "r") as fin:
        for x in fin.readlines():
            o = x.split("\t")
            assert len(o) == 2, "each line has two members."
            mid = o[0].strip()
            text = o[1].strip()
            d[mid] = text
    return d

def panduan(o,d):
    top_terms = o["top_terms"][0:10] #必须包含前5
    points = o["points"]
    xianzhi = []
    for point in points:
        for top_term in top_terms:
            if d[point["vector_name"]].find(top_term.keys()[0]) >= 0:break
            xianzhi.append(point["vector_name"])
    return xianzhi

def trace_clusters(fro,to):
    d = all_seg()
    with open(fro, "r") as fin:
        k_sum = 1
        for x in fin.readlines():
            o = json.loads(x)
            xianzhi = panduan(o,d)
            if len(o["points"]) <= 1: continue
            with open(to,"a") as f_write:
                f_write.write("---------------------------The %dth----------------------------\n" %k_sum)
            kk = 0
            for y in o["points"]:
                if (y["vector_name"] in xianzhi) and (len(o["points"]) - kk >= 10):
                    kk+=1 
                    continue
                with open(to,"a") as f_write:
                    f_write.write("%s\t%s\n" %(y["vector_name"],d[y["vector_name"]].encode("utf-8")))
            k_sum += 1
            #with open(to,"a") as f_write:
                #f_write.write("%d-------------------------------------------------------\n" %len(o["points"]))

if __name__ == "__main__":
    fro = os.path.join(curdir,"data", "kmeans.clusterdump")
    to = os.path.join(curdir,"result","%s-result" %textname)
    
    try:
        os.remove(to)
    except :pass

    trace_clusters(fro,to)
