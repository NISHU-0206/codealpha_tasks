import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Predefined responses and patterns
responses = {
    "greeting": ["Hello!", "Hi there!", "How can I help you?", "Hey! How's it going?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!", "Bye! Have a great day!"],
    "thanks": ["You're welcome!", "Happy to help!", "No problem!", "Anytime!"],
    "default": ["Sorry, I didn't understand that. Could you please rephrase?", "I'm not sure what you mean. Can you ask that differently?"]
}

# Example pattern matching rules
patterns = {
    "greeting": ["hi", "hello", "hey", "howdy", "greetings"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thank you", "thanks", "thanks a lot", "many thanks"]
}

# Function to preprocess and clean the input
def preprocess_input(user_input):
    # Remove punctuation
    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation))
    # Tokenize the input
    tokens = word_tokenize(user_input)
    # Remove stopwords and lemmatize the tokens
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return filtered_tokens

# Function to identify user intent based on patterns
def get_response(user_input):
    # Preprocess the user input
    processed_input = preprocess_input(user_input)
    
    # Check the patterns and return the corresponding response
    for intent, pattern_list in patterns.items():
        for pattern in pattern_list:
            if pattern in processed_input:
                return random.choice(responses.get(intent, responses["default"]))
    
    return responses["default"][0]

# Main chatbot function
def chat():
    print("Hello! I'm Chatbot. Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # End the conversation if user types 'exit'
        if user_input.lower() == 'exit':
            print(random.choice(responses["goodbye"]))
            break
        
        # Get the chatbot's response
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
