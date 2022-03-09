import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" 
model = hub.load(module_url)
print ("module %s loaded" % module_url)
'''
user_answers = [
    "the dog bites the man",
    "havana is great",
    "Water is death"
    ]

    model_answers = [
        "the dog bites the man",
        "havana is a good place for vacation",
        "Water is life"
    ]
'''

def correct_answers(user_answers,model_answers):
    user_answers_embeddings = model(user_answers)
    model_answers_embeddings = model(model_answers)

    results={}

    total_num=len(user_answers_embeddings)
    score=0
    for i in range(total_num):
        percentage=cosine_similarity([user_answers_embeddings[i]],[model_answers_embeddings[i]])
        percentage=percentage[0][0]
        decision=0
        if percentage>=0.75:
            decision=1
        score+= decision

        results[percentage]=decision

    print(results)

    return {"score":score,"total_num_of_ques":total_num}
        


