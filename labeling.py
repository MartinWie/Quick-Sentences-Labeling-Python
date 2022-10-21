import os
sentence_list=["Hallo wie gehts dir?","Moin moin Meister.", "Peter macht Faxen"]
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
    print("Mail:\n####################\n\n" + sentence + "\n\n####################\n")
    while not emotion:
        print("Please select one of the following options:")
        user_input = input(options_string + "-> ")
        #user_input="123"

        for element in range(0, len(user_input)):
            emotion=get_emotion(user_input[element]) 
            if not emotion:
                continue
            emotions.append(emotion)
            emotions = list(set(emotions))
            continue
        
        print("\nInvalid input, please only use the displayed options\n")
    
    labeled_sentences.append([sentence, emotions])

print(labeled_sentences)

