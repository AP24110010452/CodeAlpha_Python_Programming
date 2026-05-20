print("=== Mini ChatBot ===")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")
    elif "how are you" in user:
        print("Bot: I'm doing great. Thanks for asking!")
    elif "name" in user:
        print("Bot: I am CodeAlpha Bot.")
    elif "python" in user:
        print("Bot: Python is powerful and beginner-friendly.")
    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")