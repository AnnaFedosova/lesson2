school = [
    {'school_class': '4a', 'class_scores': [3,4,4,5,2]}, 
    {'school_class': '6a', 'class_scores': [5,3,2,3,3]},
    {'school_class': '8a', 'class_scores': [2,5,3,5,4]}
]

def all_scores ():
    a=0
    for scores in school:
        scores["average_score_in_class"]=sum(scores['class_scores'])/len(scores['class_scores'])
        print (scores)
        a=a+scores["average_score_in_class"]
    print('average_score_at_school:{:.2f}'.format (a/len(school)))
if __name__ == "__main__":
    all_scores()
