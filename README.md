# Article Summarizer

## Home Page

This is the home page where users can start the process of summarizing an article.

![Home Page](img/home.png)

## Enter the Article URL

On this page, users can enter the URL of the article they want to summarize.

![Enter URL](img/url.png)

## Summarized Article

After submitting the URL, the summarized article is displayed on this page.

![Summay](img/summay.png)

## Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/AbdooMohamedd/Article-Summarizer-with-Gemini-API.git
   ```
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
3. Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and generate an API key.
4. Create a Windows environment variable called `GEMINI_API_KEY` with the key you generated.

````markdown
#### On Windows:

1. Open Command Prompt and run:
   ```bash
   set GEMINI_API_KEY=your_api_key_here
   ```
````

For permanent setup:

1.  Search for "Environment Variables" in the Start Menu.
2.  Click **Edit the system environment variables** > **Environment Variables**.
3.  Add a new variable `GEMINI_API_KEY` with your API key.

#### On macOS/Linux:

1. Open Terminal and run:
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```
   For permanent setup, add the line to `~/.bashrc`, `~/.bash_profile`, or `~/.zshrc`:
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```
   Then run:
   ```bash
   source ~/.bashrc  # or ~/.bash_profile or ~/.zshrc
   ```

````

5. Run the application from the `app.py` file:
   ```sh
   python app.py
   ```

```

```
````
