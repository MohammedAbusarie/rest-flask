from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('bert-base-nli-mean-tokens')

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
    user_answers_embeddings = model.encode(user_answers)
    model_answers_embeddings = model.encode(model_answers)

    #results={}

    total_num=len(user_answers_embeddings)
    score=0
    for i in range(total_num):
        percentage=cosine_similarity([user_answers_embeddings[i]],[model_answers_embeddings[i]])
        percentage=percentage[0][0]
        decision=0
        if round(percentage,1)>=0.8:
            decision=1
        score+= decision

        #results[percentage]=decision

    #print(results)

    return {"score":score,"total_num_of_ques":total_num}
        


