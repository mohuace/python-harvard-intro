
#The problem is the and The are the same words but will appear as different words in word count
words = ["the", "the", "The", "hey", "them", "bla", "a", "say", "kid", "little"]

#Use list comprehension to lowercase every word in words
words_lower = [w.lower() for w in words]

#Can filter the words too
words_lower = [w.lower() for w in words if len(w) > 3]

#Count number of words --- This is Dictionary comprehension
count = { word: words_lower.count(word) for word in words_lower }

print(count)


word_count = {}

#for word in words:
for word in words_lower:
    if(word in word_count):
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)