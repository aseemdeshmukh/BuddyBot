import openai
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import random
import re

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize LangChain with OpenAI API
llm = ChatOpenAI(model="gpt-4", openai_api_key=openai.api_key)

# Function to validate email format more strictly
def is_valid_email(email):
    # Refined regular expression for stricter email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Check if the email matches the regex pattern
    if re.match(email_regex, email):
        # Ensure the domain part (after "@") has at least one dot, indicating a valid domain
        domain = email.split('@')[-1]
        if '.' in domain and domain.index('.') > 0:
            return True
    return False


# Function to handle user input
def handle_user_input(user_input, user_name, user_email):
    # Intent Recognition and Conversation Flow

    # List of possible responses for "How are you?"
    mood_responses = [
        "I'm doing great! Thanks for asking. How about you?",
        "I'm just a bot, but I'm feeling awesome today! How are you?",
        "I'm here and ready to assist! How's your day going?",
        "I'm doing well, thanks! What can I help you with today?"
    ]

    # List of jokes
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why was the math book sad? Because it had too many problems!",
        "Why don’t eggs tell jokes?  Why don’t eggs tell jokes? Because they might crack up!",
        "What do you get if you cross a snowman and a vampire? Frostbite!",
        "What do you call fake spaghetti? An impasta!",
        "I told my wife she should embrace her mistakes… She gave me a hug.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]

    # List of capitals of the countries

    capitals = {
        
        "India": "New Delhi",
        "France": "Paris",
        "Japan": "Tokyo",
        "Germany": "Berlin",
        "Brazil": "Brasília",
        "Canada": "Ottawa",
        "Australia": "Canberra",
        "Russia": "Moscow",
        "Greece": "Athens",
        "Thailand": "Bangkok",
        "South Africa": "Pretoria, Cape Town, and Bloemfontein"
    }

    # Fallback suggestions
    suggestions = [
        "You can ask me about world capitals, like 'What is the capital of France?'",
        "I can tell jokes! Just say 'Tell me a joke.'",
        "You can ask about the weather, general knowledge, or just chat!"
    ]

    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return f"Hello {user_name}! How can I assist you today?"
    
    elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
        return "Goodbye! Have a great day!"

    elif "help" in user_input.lower():
        return "Sure, I can help! Please tell me what you need assistance with."
    
    if "how are you" in user_input.lower():
        return random.choice(mood_responses)  # Select a random response

    elif "good" in user_input.lower() or "fine" in user_input.lower() or "great" in user_input.lower():
        return "Glad to hear that! 😊 What can I do for you today?"

    elif "not great" in user_input.lower() or "bad" in user_input.lower():
        return "I'm sorry to hear that. If there's anything I can do to cheer you up, let me know! Want to hear a joke? 🤗"
    
    elif "ohh" in user_input.lower() or "okay" in user_input.lower() or "haha" in user_input.lower() or "lol" in user_input.lower():
        return "Is there anything else I can help you with today?"

    elif "thank you" in user_input.lower():
        return "You're welcome! 😊 Let me know if you need anything else."    
    
    elif "your name" in user_input.lower():
        return f"My name is Buddy Bot, and I'm here to help you!"

    elif "who are you" in user_input.lower():
        return f"I am a chatbot created to assist you with any queries or help you with information."

    elif "weather" in user_input.lower():
        return "Sorry, I can't provide real-time weather updates right now, but I can help you with general knowledge."

    elif "capital of" in user_input.lower():
        country = user_input.split("capital of")[-1].strip().title()
        if country in capitals:
            return f"The capital of {country} is {capitals[country]}."
        else:
            return "I'm not sure about that. Can you try another country?"
        
    elif "joke" in user_input.lower():
        return random.choice(jokes)

    else:
         # Choose a random fallback message
        random_suggestion = random.choice(suggestions)
        return f"I'm not sure I understood that. Could you please rephrase? Or You can try asking about: {random_suggestion}"

# Main function to start the chatbot
def start_chat():
    print("Welcome to the chatbot! Please enter your name to begin:")
    user_name = input("Your Name: ")

    print(f"Thank you {user_name}, please enter your Email ID:")

    user_email = None
    while user_email is None:
        user_email_input = input("Your Email: ")
        # Validate the email
        if is_valid_email(user_email_input):
            user_email = user_email_input
            print(f"Got it! Your email is {user_email}. What else can I help you with?")
        else:
            print("That doesn't seem like a valid email. Please enter a valid email address.")


    print(f"Hello, {user_name}! Let's get started. Type 'bye' to exit.")
    
    while True:
        user_input = input(f"{user_name}: ")

        # Exit the chatbot
        if user_input.lower() == 'bye':
            print("Goodbye! Have a great day..😊")
            break
        
        # Get the chatbot's response based on the user input
        response = handle_user_input(user_input, user_name, user_email)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
