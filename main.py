

if __name__ =="__main__":

    # 1. greeting
    user_name = input("Bot: What do you want me to call you?")
    print(f'Hi {user_name}')

    # 2. templates
    bot_template = "Bot: {0}"
    user_template = f"{user_name}: {0} "

    # 3. core
    name = "Funny bot"
    weather = "rainy"
    mood = "happy"

    responses = {
        "what's your name?": [
            f"My name is {name}",
            f"Call me{name}",
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


