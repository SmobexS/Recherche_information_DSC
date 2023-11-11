import time
import re
from files_maneg import *

from collections import defaultdict

def file_processing (file_path):

    index = defaultdict(set)

    term_frequency = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r') as file:
        docs = file.read()
    
    docno = ''
    words = ''

    documents = re.findall(r'<doc><docno>.*?</docno>.*?</doc>', docs, re.DOTALL)
        
    start_time = time.time() # Record indexing start time

    for document in documents:
        statement = re.search(r'<docno>(.*?)</docno>(.*?)</doc>', document, re.DOTALL)
        if statement:
            docno = statement.group(1)
            core = statement.group(2)
            words = re.findall(r'\b\w+\b', core.lower())
            for word in words:
                index[word].add(docno)
                term_frequency[word][docno] += 1

    end_time = time.time()  # Record indexing end time
    indexing_time = end_time - start_time  # Calculate indexing time
    
    print('Execution time of the indexation process : ', indexing_time)

    index = dict(sorted(index.items()))

    index_txt((index, term_frequency), 1)

import cProfile
cProfile.run("file_processing('Text_Only_Ascii_Coll_NoSem')")