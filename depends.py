# Sample Python code with dependencies and vulnerabilities

# Dependencies
import requests
import json
from os import system

# Function to make a request to a URL
def make_request(url):
    response = requests.get(url)
    return response.text

# Function to process user input
def process_input(input_data):
    print("Processing input:", input_data)
    # Intentional vulnerability: code injection
    system(input_data)

# Main function
def main():
    # Dependency usage: making a request to a URL
    response = make_request('https://api.github.com/repos/openai/gpt-3.5')
    print("Response from GitHub API:")
    print(json.dumps(json.loads(response), indent=4))

    # Vulnerable user input processing
    user_input = input("Enter data to process: ")
    process_input(user_input)

if __name__ == "__main__":
    main()
