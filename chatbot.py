def get_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I didn't understand that. Try saying 'hello', 'how are you', or 'bye'."

def run_chatbot():
    print("🤖 Simple Chatbot is now running! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
        
        if user_input.lower().strip() == "bye":
            break

# Start the chatbot
if __name__ == "__main__":
    run_chatbot()
