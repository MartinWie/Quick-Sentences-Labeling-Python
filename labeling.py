import os
sentence_list=["Are you trying to say that you're not happy with your success?","I'd be happy knowing you're safe.", "I hope you two are happy together."]
labeled_sentences=[]

switcher = {
    "1": "Sad",
    "2": "Happy",
    "3": "Angry",
    "4": "Unknown",
    "5": "Test"
} 

options_string=""

for k, v in switcher.items():
    options_string = options_string + k + "=" + v + " "


def get_emotion(argument): 

    result = None
    try:
        result=switcher[argument]
    finally:
        return result

for sentence in sentence_list:
    os.system('cls' if os.name == 'nt' else 'clear')
    emotion=None
    emotions=[]
    print("Text to label:\n####################\n\n" + sentence + "\n\n####################\n")
    while not emotion:
        print("Please select one of the following options:")
        user_input = input(options_string + "-> ")

        for element in range(0, len(user_input)):
            emotion=get_emotion(user_input[element]) 
            if not emotion:
                continue
            emotions.append(emotion)
            emotions = list(set(emotions))
            continue
        
        print("\nInvalid input, please only use the displayed options\n")
    
    labeled_sentences.append([sentence, sorted(emotions)])

print(labeled_sentences)

