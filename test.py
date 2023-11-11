import re
import time

def extract_term_frequencies(file_path, print_index=True):
    with open(file_path, encoding="utf-8") as file:
        data = file.read()

    documents = re.findall(r'<doc><docno>.*?</docno>.*?</doc>', data, re.DOTALL)

    term_frequencies = {}

    start_time = time.time()  

    for document in documents:
        match = re.search(r'<docno>(.*?)</docno>(.*?)</doc>', document, re.DOTALL)
        if match:
            per_doc_term_frequencies = {}
            doc_number = match.group(1)[1]
            non_matching_part = match.group(2)
            words = re.findall(r'\b\w+\b', non_matching_part)
            for word in words:
                per_doc_term_frequencies = term_frequencies.get(word, {})
                per_doc_term_frequencies[doc_number] = per_doc_term_frequencies.get(doc_number, 0) + 1
                term_frequencies[word] = per_doc_term_frequencies

    end_time = time.time()  # Record indexing end time
    indexing_time = end_time - start_time  # Calculate indexing time
    
    return indexing_time

import cProfile
cProfile.run("extract_term_frequencies('Text_Only_Ascii_Coll_NoSem')")
print(extract_term_frequencies('Text_Only_Ascii_Coll_NoSem'))

