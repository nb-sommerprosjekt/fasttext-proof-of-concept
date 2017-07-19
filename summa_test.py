from summa import summarizer
import sys

with open(sys.argv[1], "r") as f:
    text=f.read()
with open("summa_output.txt","w") as f:
    f.write(summarizer.summarize(text, ratio=0.1, language="norwegian"))