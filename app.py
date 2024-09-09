from flask import Flask, render_template, request, redirect, url_for
from scrape_the_article import ArticleScraper
from prompts import generate_prompt
from main import call_gemini_api
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    scraper = ArticleScraper(url)
    scraper.fetch_content()
    title, content = scraper.get_full_text()
    prompt = generate_prompt(title, content)
    try:
        summary = call_gemini_api(prompt)
        structured_summary = format_summary(summary)
        return render_template('summary.html', summary=structured_summary, url=url)
    except Exception as e:
        return f"Error: {e}"


def format_summary(summary):
    """Formats the summary text into structured HTML according to prompt guidelines."""
    # Handle titles and headers
    summary = re.sub(r'^\*\*\*(.*?)\*\*\*\n', r'<h1>\1</h1>', summary, flags=re.MULTILINE)  # Title
    summary = re.sub(r'^\*\*(.*?)\*\*\n', r'<h2>\1</h2>', summary, flags=re.MULTILINE)  # Headers

    # Remove Markdown-like ## for headers and convert to HTML headers
    summary = re.sub(r'##\s*(.*?)\s*\n', r'<h2>\1</h2>', summary, flags=re.MULTILINE)
    
    # Replace markdown-like bullet points with HTML list items
    summary = re.sub(r'^\*\s*(.*)$', r'<li>\1</li>', summary, flags=re.MULTILINE)
    
    # Wrap list items with <ul> tags
    summary = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', summary)
    summary = re.sub(r'</ul>\s*<ul>', '', summary)  # Remove nested lists
    
    # Remove Markdown-like asterisks for bold and apply HTML <strong> tags
    summary = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', summary)
    
    # Make the text before the colon bold and properly formatted
    summary = re.sub(r'^([^\n]*?):\s*(.*)', r'<p><strong>\1</strong>: \2</p>', summary, flags=re.MULTILINE | re.DOTALL)
    
    # Ensure proper paragraph separation
    summary = re.sub(r'\n\n+', '</p><p>', summary)  # Double newlines to paragraph tags
    summary = '<p>' + summary + '</p>'  # Wrap the entire summary in paragraph tags

    # Add a dash at the beginning of each paragraph, starting from the second paragraph
    paragraphs = summary.split('</p><p>')
    for i in range(1, len(paragraphs)):
        paragraphs[i] = '- ' + paragraphs[i]
    summary = '</p><p>'.join(paragraphs)
    
    # Clean up double and nested tags
    summary = re.sub(r'(<ul>\s*)<ul>', r'\1', summary)  # Remove nested ul
    summary = re.sub(r'</ul>\s*</ul>', '</ul>', summary)  # Remove nested ul
    
    return summary





if __name__ == "__main__":
    app.run(debug=True)
