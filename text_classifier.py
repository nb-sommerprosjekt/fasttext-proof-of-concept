import fasttext
import sys
import re
import subprocess
import os

#!/usr/bin/env python3

if sys.argv:
    input_file_name = str(sys.argv[1])
    with open(input_file_name,"r") as input_file:

        print("Reading input")
        text=input_file.read()
        text = text.replace("-\n", "")
        text=text.replace("\n"," ")
        text=re.sub('[W+]+', ' ', text)
        text=text.replace("  "," ")
else:
    print("Please provide a text-file to classify")
    exit(1)

print("Loading model")
classifier=fasttext.load_model('classifier-model.bin')
print("Preparing predictions")
result=classifier.predict_proba([text],k=5)
print("Preparing to create summary \n")
command="python summa_test.py "+input_file_name
#command=["python", "summa_test.py",str(sys.argv[1])]
os.system(command)

f=open("summa_output.txt","r")
summary=f.read()
sum_length = len(summary.split(" "))
text_length = len(text.split(" "))
print("This is the summary for \"{}\". It is {} words long, a reduction to {}%. \n".format(input_file_name,str(sum_length),str(int((sum_length/text_length)*100))))

print(summary)

print("These are the most probable dewey-labels for this article:\n")
for entry in result[0]:
    print("This article has deweynr {}, with {:05.2f}% probability.".format(entry[0].replace("__label__",""),entry[1]*100))
