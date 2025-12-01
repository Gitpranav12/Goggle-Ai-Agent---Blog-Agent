
# Goggle-Ai-Blog-Agent (Groq Edition)

Goggle-Ai-Blog-Agent (Groq Edition) is an AI-powered multi-agent system that automatically generates complete, SEO-friendly blog articles using the Groq LLM at high speed. It is designed for students, bloggers, marketers, and SEO writers. ✍️📈



## Features


- 🤖 Multi-agent writing pipeline: Plan → Research → Draft → Finalize  
- 📄 Generates final blog content as downloadable `.txt` files (easy to convert to `.md`)  
- 💾 Automatically saves full session history as JSON in `data/sessions`  
- 🔁 Allows you to revisit and re-download previous blog sessions  
- 🎛 Customizable inputs: topic, tone, audience, language, and word count  
- ⚡ Uses Groq API for fast and high-quality text generation  
- 🧩 Modern Gradio-based web UI  
- 🔒 All data stored locally in files (no external database)



## 🚀 Tech Stack


| Component       | Technology          |
|----------------|---------------------|
| 🧠 Backend AI  | Groq LLM API        |
| 🖥️ Web UI      | Gradio              |
| 🛰️ Server      | Python app          |
| 🧩 Orchestration | Custom multi-agent Python logic |
| 💽 Storage     | Local JSON + text files |


## 🔧 Installation & Setup (Local) 🛠️

### 1️⃣ Clone the repository
`git clone <your-repo-url>`

`cd Goggle-Ai-Agent---Blog-Agent`

## Create and activate a virtual environment (recommended)

`python -m venv venv`

# Windows
`venv\Scripts\activate`

# macOS / Linux
`source venv/bin/activate`

3️⃣ Install dependencies

## pip install -r requirements.txt 
Gradio and Groq are installed through this file, so you normally do not need separate pip install gradio or pip install groq commands.

1) `pip install groq`

2) `install gradio` 

** Example requirements.txt (adjust as needed):

`groq>=0.9.0`

`tavily-python>=0.7.0`

`python-dotenv>=1.0.1`

`rich>=13.9.4`

`gradio>=4.1.1`

`uvicorn>=0.30.0`

`fastapi>=0.100.0`



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GROQ_API_KEY=your_groq_api_key_here
`

`TAVILY_API_KEY=your_tavily_api_key_here`

`DEFAULT_MODEL=llama-3.3-70b-versatile`

Get your Groq API key from: https://console.groq.com/keys

TAVILY_API_KEY is needed only if your agents use Tavily for web research.

Get Your Tavily API Key :- https://www.tavily.com/



## Run Locally

Option A – via app.py (recommended and matches Render)
bash
`python app.py`

app.py imports build_app from src.ui.main_ui and starts the Gradio server.

By default, Gradio will run at: http://127.0.0.1:7860.

------
Option B – directly via the UI module
If you keep a __main__ block in src/ui/main_ui.py:


`python -m src.ui.main_ui`

This will also launch the Gradio interface on the default port.

--------

## Authors

- [@Pranav Jawarkar](https://github.com/Gitpranav12)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://designerpranav.netlify.app/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pranav-jawarkar/)


