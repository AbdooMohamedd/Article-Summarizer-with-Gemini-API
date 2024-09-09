# prompts.py
"""is a Python script that generates a prompt for summarizing an article."""

PROMPT_TEMPLATE = """

Your task is to summarize the article in 3-6 paragraphs, with each paragraph containing 20-30 words:

- Start with the title of the article without the author or author's name, or the website name if it's included in the title
- Provide a concise overview of the main points
- Include key details and insights in each paragraph
- Avoid any code, technical jargon, or links
- Ensure the summary flows logically and captures the essence of the article

End each paragraph with a period and do not use periods elsewhere

Title: {title}

Content:
{content}

"""



def generate_prompt(title, content):
    """Generates a prompt based on the title and content."""
    return PROMPT_TEMPLATE.format(title=title, content=content)
