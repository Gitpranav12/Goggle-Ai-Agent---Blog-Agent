# 📘 OmniBlog Agent Studio (Groq Edition)

⚡ AI-powered multi-agent system that automatically creates complete, SEO-friendly blogs using the **Groq LLM** at lightning speed!

Perfect for:
📚 Students | ✍ Bloggers | 🎯 Marketers | 🌐 SEO Writers

---

## ✨ Features

- 🤖 Multi-Agent Writing System (Plan → Research → Draft → Finalize)
- 📄 Exports Final Blog as `.txt` and `.md`
- 📂 Auto-Saves Full Session JSON History
- 🕘 Redownload Previously Written Blogs Anytime
- 🎛 Custom Inputs: Topic + Tone + Audience + Language + Word Count
- 🚀 Ultra-Fast Output With Groq API
- 🌙 Modern Gradio UI + Theme Customization
- 💾 Local Data Storage — No Cloud Required

---

## 🚀 Tech Stack

| Component | Technology |
|----------|------------|
| Backend AI | Groq LLM API |
| UI Framework | Gradio |
| Architecture | Python Multi-Agent system |
| Storage | Local JSON + Markdown |

---

## 📁 Project Structure

omni-blog-agent-groq/
│
├─ data/
│ ├─ sessions/ # Saved history JSON
│ 
├─outputs # Blog .md / .txt exports

├─ src/
│ ├─ ui/
│ │ ├─ pages/
│ │ │ ├─ create_page.py
│ │ │ ├─ history_page.py
│ │ │ └─ settings_page.py
│ │ └─ main_ui.py # Main UI entry point
│ │
│ ├─ agents/
│ ├─ memory/
│ ├─ tools/
│ ├─ orchestrator.py # Multi-agent execution
│ ├─ cli.py # CLI-based usage
│ └─ config.py
│
├─ .env
├─ requirements.txt
└─ README.md

--------------------------------------------------


## 🔑 Installation & Setup 

### 1️⃣ Install Python dependencies

```sh
pip install -r requirements.txt

pip install gradio

pip install groq

--------------------------------------------------

2️⃣ Add your Groq API Key

Create a .env file in root folder:

GROQ_API_KEY=your_api_key_here
TAVILY_API_KEY=your_api_key_here
DEFAULT_MODEL=llama-3.3-70b-versatile


Get API Key → https://console.groq.com/keys

--------------------------------------------------

▶️ Launch the App
Activate Virtual Environment (Optional but recommended)

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

Run Gradio UI
python -m src.ui.main_ui


✔ Opens automatically in browser
✔ URL → http://127.0.0.1:7860

-------------------------------------------------------



| Step | Action                                            |
| ---- | ------------------------------------------------- |
| 1️⃣  | Enter Blog Topic                                  |
| 2️⃣  | Choose Tone, Audience, Language                   |
| 3️⃣  | Set Word Count (200–2000 words)                   |
| 4️⃣  | Click **Generate Blog**                           |
| 5️⃣  | View Final Article Output                         |
| 6️⃣  | Download as `.txt` / `.md`                        |
| 7️⃣  | Check **History Page** to download previous blogs |


--------------------------------------------------------

| Agent         | Task                         |
| ------------- | ---------------------------- |
| 🧩 Planner    | Creates structured blog plan |
| 🔎 Researcher | Collects verified facts      |
| ✍ Writer      | Generates detailed content   |
| 🧹 Editor     | Final polish + readability   |

---------------------------------------------------------

📸 Screenshots (Add your UI images here!)

Place images in /screenshots folder then update links:

![Home UI](screenshots/ui-home.png)
![History Page](screenshots/ui-history.png)