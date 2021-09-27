# Data Mining Example (Cloud Credential Council Big Data Class Demo)
# python -m nltk.downloader all
# pip install nltk

import pandas as pd, numpy as np, os, nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

rawdata = "The CCC Approach & Philosophy: The CCC operates at the forefront of IT and provides certification programs that help IT and business professionals manage the challenges modern businesses are facing.  The CCC chooses to work in areas that are related to the massive transformation organizations are undergoing to become digital leaders. The Internet of Things, Big Data, Cloud, AI, and Blockchain are potential disruptors and can revolutionize the way work is being done, change business models, and requires us to rethink what we do.  The CCC Portfolio includes foundation level programs on Cloud, IoT, Big Data and Blockchain, and Professional role-based certifications for Cloud. The CCC works with over 200 registered training providers across the world to deliver in-class or virtual CCC training programs. The CCC also engages directly with professionals who are looking for self-study or online learning programs. CCC certification exams are be delivered anywhere as online (webcam) proctored exams, but the CCC also works with EXIN, an internationally renowned certification and accreditation organization for the delivery of exams."

# Data Cleaning 
data = rawdata.lower()
tokenizer = nltk.RegexpTokenizer(r"\w+")
tokens = tokenizer.tokenize(data)
tokens

# Frequency Distinct for tokens
fd = FreqDist(tokens)
fd

# Frequency of top 5 tokens
fd5 = fd.most_common(5)
fd5

stop_words = stopwords.words('english')

clean_tokens = tokens[:]
for token in tokens:
    if token in stop_words:
        clean_tokens.remove(token)

print(clean_tokens)

# Frequency Distinct for clean tokens
cfd = FreqDist(clean_tokens)
cfd

# Frequency of top 5 clean tokens
cfd5 = cfd.most_common(5)
cfd5





