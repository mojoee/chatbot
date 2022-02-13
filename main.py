import random

def respond(message, responses):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])

    return bot_message

def find_related_question(user_input):
    if "name" in user_input:
        related_question = "what's your name?"
    elif "weather" in user_input:
        related_question = "what's today's weather?"
    elif "how are" in user_input:
        related_question = "How are you?"
    elif "robot" in user_input:
        related_question = "Are you a robot?"
    else:
        related_question = ""

    return related_question


def send_message(message, responses, user_template, bot_template):
    print(user_template.format(message))
    response = respond(message, responses)
    print(bot_template.format(response))


if __name__ =="__main__":

    # 1. greeting
    user_name = input("Bot: What do you want me to call you?")
    print(f'Hi {user_name}')

    # 2. templates
    bot_template = "Bot: {0}"
    user_template = user_name + " : {0} "

    # 3. core
    name = "Funny bot"
    weather = "rainy"
    mood = "happy"

    responses = {
        "what's your name?": [
            f"My name is {name}",
            f"Call me {name}",
            f"I usually go by {name}"
            
        ],

        "what's today's weather?": [
            f"Today's weather is {weather}",
            f"According to CWB, the weather is {weather}",
            f"Can't you see it is {weather} outside"

        ],

        "How are you?": [
            f"I am feeling {mood} today",
            f"My mood today is {mood}",
            f"Thanks for asking, life is {mood}"
        ],

        "": [
            "Hey! Are you there?",
            "What do you mean by saying nothing?",
            "Sometimes saying nothing tells a lot :)"
        ],

        "default": [
            "this is a default message"
        ]



    }

    # interaction

    while True:
        my_input = input("Ask me a question!").lower()
        related_text =  find_related_question(my_input)
        send_message(related_text, responses, user_template, bot_template)

        if my_input =="exit" or my_input =="stop":
            break
    


