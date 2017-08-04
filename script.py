import re, math
from collections import Counter
import numpy as np



text1 = 'How can I be a geologist?'
text2 = 'What should I do to be a geologist?'

class Similarity
    def compute_cosine_similarity(vec1, vec2):
         # intersects the words that are common
         # in the set of the two words
         intersection = set(vec1.keys()) & set(vec2.keys())
         # dot matrix of vec1 and vec2
         numerator = sum([vec1[x] * vec2[x] for x in intersection])

         # sum of the squares of each vector
         # sum1 is the sum of text1 and same for sum2 for text2
         sum1 = sum([vec1[x]**2 for x in vec1.keys()])
         sum2 = sum([vec2[x]**2 for x in vec2.keys()])

         # product of the square root of both sum(s)
         denominator = math.sqrt(sum1) * math.sqrt(sum2)
         if not denominator:
            return 0.0
         else:
            return round(numerator/float(denominator),4)

    def text_to_vector(text):
        WORD = re.compile(r'\w+')
        words = WORD.findall(text)
        return Counter(words)

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    # Jaccard Similarity
    def tokenize(string):
        return string.lower().split(" ")

    def jaccard_similarity(string1, string2):
        intersection = set(string1).intersection(set(string2))
        union = set(string1).union(set(string2))
        return len(intersection)/float(len(union))

cosine = Similarity.compute_cosine_similarity(vector1, vector2)
print 'Cosine Similarity:', cosine

jaccard = Similarity.jaccard_similarity(tokenize(text1),tokenize(text2))
print 'Jaccard Similarity:', jaccard
