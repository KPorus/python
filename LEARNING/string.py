doc_list=['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
def word_search(doc_list, keyword = "Casino"):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    res = []
    for i,doc in enumerate(doc_list):
        normalized = [token.rstrip(".,").lower() for token in doc.split()]
        if keyword.lower() in normalized:
                    res.append(i)
    print(res)
    return res


def multi_word_search(doc_list, keywords=["Casino", "They"]):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    keywords_indicate = {}
    for keyword in keywords:
        keywords_indicate[keyword] = word_search(doc_list, keyword)
    print(keywords_indicate)
    return keywords_indicate
    pass

multi_word_search(doc_list)
# word_search(doc_list)

print("{0} is a web developer. {1} is {0}\'s best {2}.".format("Fardin","ali","friend & partner"))
print("/".join("1122023"))
