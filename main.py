# main.py 
"""is a Python script that integrates the article scraping, prompt generation, and Gemini API call."""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from scrape_the_article import ArticleScraper
from prompts import generate_prompt

# Load environment variables from .env file
load_dotenv()

# Configure the API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable in the .env file.")
genai.configure(api_key=api_key)

# Create the model with desired configuration
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1092,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Your task is to summarize the article in 6-10 key points:\n\n- Start with the title.\n- Focus on essential information only.\n- Use sub-bullets for additional details if necessary.\n- Do not include any code, technical jargon, or links.\n- Adjust the structure to match the flow and key elements of the article."
)

def call_gemini_api(prompt):
    """Calls the Gemini API with the generated prompt and extracts the summary."""
    response = model.generate_content(prompt)
    if response:
        summary = response.text  # Assuming 'text' is the attribute for the content
        return summary.strip()
    else:
        return "No summary found in the response."

def main():
    url = input("Enter the URL of the article you want to scrape: ")

    # Get article content
    scraper = ArticleScraper(url)
    scraper.fetch_content()
    title, content = scraper.get_full_text()

    # Generate prompt
    prompt = generate_prompt(title, content)

    # Call Gemini API
    try:
        summary = call_gemini_api(prompt)
        print("Article Summary:")
        print(summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()