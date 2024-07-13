import random

# Responses the bot can give
responses = {
    "hi": "Hello!",
    "how are you?": "I'm good, thank you.",
    "what's your name?": "I'm a chatbot. What can I do for you?",
    "bye": "Goodbye! Have a nice day.",
    "default": "I'm sorry, I don't understand that."
}

# Function to get a response from the bot
def get_response(user_input):
    # Clean and normalize the input
    cleaned_input = user_input.lower().strip()

    # Check if the input matches any predefined responses
    if cleaned_input in responses:
        return responses[cleaned_input]
    else:
        return responses["default"]

# Main function to run the chatbot
def main():
    print("Welcome! Start chatting with the bot (type 'bye' to exit).")

    while True:
        user_input = input("You: ")  # Get user input
        response = get_response(user_input)  # Get bot response
        print("Bot:", response)  # Print bot's response

        if user_input.lower() == "bye":
            break

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Start the main function

