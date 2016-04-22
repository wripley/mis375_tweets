import requests
import os
import re

def analyze():
    header = {"text": ""}
    url = "http://text-processing.com/api/sentiment/"
    for file in os.listdir(os.getcwd() + "/input"):
        f = open("input/"+ file)
        lines = (line for line in f if line != "\n")
        line_num = 0
        pos = 0
        neg = 0
        neutral = 0
        for line in lines:
            output = open("output/" + file, "a+")
            line_num+= 1
            # print ((line.split(",")[1]).split("\'"))
            # print (type((line.split(",")[1]).split("\'")))
            content = ""
            try:
                result = re.split(",(\"*)b(\"*)(\'*)", line)
                content = result[-1]
                # print(content)
            except:
                print("$$$")
                print(line.split("."))
                print("###")

            header["text"] = content
            r = requests.post(url, data = header)
            if(r is not None):
                r = r.json()
                label = r["label"]
                output.write(line.split("\n")[0])
                if(label == "pos"):
                    pos+= 1
                    output.write(",Postive\n")
                elif label == "neg":
                    neg+= 1
                    output.write(",Negative\n")
                else:
                    neutral+= 1
                    output.write(",Neutral\n")
                # print ("Tweet: ", line)
                # print ("number positive is", str(pos))
                # print ("number negative is", str(neg))
        output.write("\nnumber positive is " + str(pos))
        output.write("\nnumber negative is " + str(neg))
        output.write("\nnumber neutral is " + str(neutral))

if __name__ == "__main__":
    analyze()
