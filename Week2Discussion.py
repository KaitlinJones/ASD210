conjunctions = {"for", "and", "not", "but", "or", "yet", "so"}

seen = set()

book_paragraph = """L. Frank Baum wrote The Wizard of Oz for his daughter, but the boolk was much more than a child's story. Baum's book is a political allegory, yet few people to day would recognize original events in this story. The Wizard of Oz is a story of economic reformm for Oz is short for ounce an dreferred to the gold standard, and the characters represented groups in American society. Baum's original readers did not fail to recognize William Jennings Bryan as the cowardly lion. """

data = book_paragraph.split() 

for word in data:
    if str.lower(word) in conjunctions:
        seen.add(str.lower(word))

print(seen) 