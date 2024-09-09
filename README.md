# Article Summarizer

## Home Page

This is the home page where users can start the process of summarizing an article.

![Home Page](img/home.png)

## Enter the Article URL

On this page, users can enter the URL of the article they want to summarize.

![Enter URL](img/url.png)

## Summarized Article

After submitting the URL, the summarized article is displayed on this page.

![Summary](img\summay.png)

## Instructions

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
3. Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and generate an API key.
4. Create a Windows environment variable called `GEMINI_API_KEY` with the key you generated.
5. Run the application from the `app.py` file:
   ```sh
   python app.py
   ```
