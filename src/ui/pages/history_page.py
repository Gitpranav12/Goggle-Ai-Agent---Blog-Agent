import os
import gradio as gr
import json
from datetime import datetime

def load_history_entries():
    history_dir = "data/sessions"
    entries = []

    if not os.path.exists(history_dir):
        return entries

    files = sorted(os.listdir(history_dir), reverse=True)

    for file in files:
        if file.endswith(".json"):
            fp = os.path.join(history_dir, file)

            try:
                with open(fp, "r", encoding="utf-8") as f:
                    data = json.load(f)

                entries.append({
                    "file": file,
                    "topic": data.get("topic", "No topic"),
                    "language": data.get("language", "N/A"),
                    "length": data.get("target_length", 0)
                })
            except:
                continue

    return entries


def history_page_ui():
    history_entries = load_history_entries()

    with gr.Blocks():
        gr.Markdown("## 📜 Previous Sessions (Download Your History Anytime)")

        if not history_entries:
            gr.Markdown("No history available yet.")
            return

        for entry in history_entries:
            with gr.Box():
                gr.Markdown(
                    f"🔹 **{entry['topic']}** | 📄 {entry['length']} words | 🌐 {entry['language']}"
                )

                file_path = f"data/sessions/{entry['file']}"
                
                gr.File(
                    value=file_path,
                    label="⬇️ Download this History",
                    interactive=False
                )


def show():
    history_page_ui()
