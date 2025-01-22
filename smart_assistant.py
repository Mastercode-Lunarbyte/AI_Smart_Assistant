import openai
import csv
import os  # Import os module to read environment variables

# Load the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")  # The API key is loaded securely from environment variables

# Function to interact with OpenAI API
def ask_assistant(question):
    """
    Sends the user's question to OpenAI API and retrieves a response.

    Parameters:
        question (str): The user's input question.

    Returns:
        str: The assistant's response or an error message.
    """
    try:
        # Make a request to OpenAI's ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=150
        )
        # Extract and return the assistant's response
        return response['choices'][0]['message']['content'].strip()
    except openai.error.AuthenticationError:
        return "Authentication failed. Please check your API key."
    except openai.error.APIConnectionError:
        return "Failed to connect to OpenAI servers. Please check your internet connection."
    except openai.error.RateLimitError:
        return "Rate limit exceeded. Please wait and try again."
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Function to log interactions to a CSV file
def log_to_csv(question, answer, file_name="assistant_logs.csv"):
    """
    Logs the user's question and the assistant's response to a CSV file.

    Parameters:
        question (str): The user's input question.
        answer (str): The assistant's response.
        file_name (str): The name of the CSV file to store logs. Defaults to "assistant_logs.csv".
    """
    with open(file_name, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([question, answer])

# Main program
if __name__ == "__main__":
    print("Smart Assistant is ready!")
    while True:
        # Prompt the user for a question
        user_input = input("Ask your question ('exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting. Goodbye!")
            break
        # Get the assistant's response
        answer = ask_assistant(user_input)
        # Display the response to the user
        print(f"Answer: {answer}")
        # Log the interaction to a CSV file
        log_to_csv(user_input, answer)

# README.md file content
readme_content = """# AI Smart Assistant

This is a Python-based smart assistant that uses OpenAI's GPT-3.5 API to answer user questions and logs the conversations in a CSV file.

## Features
- Intelligent responses to user queries.
- Logs questions and answers in a CSV file.
- Secure API key handling using environment variables.
- Error handling for API-related issues.

## Requirements
- Python 3.7 or higher
- OpenAI API Key

## Setup and Run
1. Install dependencies:
   ```bash
   pip install openai
   ```
2. Set your OpenAI API key:
   - On Windows:
     ```bash
     set OPENAI_API_KEY=your_api_key
     ```
   - On macOS/Linux:
     ```bash
     export OPENAI_API_KEY=your_api_key
     ```
3. Run the program:
   ```bash
   python smart_assistant.py
   ```

## Limitations
- Region restrictions for the OpenAI API.
- Requires a valid API key.

## License
This project is free to use and modify.
"""

# Write README.md file
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(readme_content)
