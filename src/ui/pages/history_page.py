import os
import gradio as gr
import json
import base64

# RUNTIME FOLDER (Render safe)
os.makedirs("data/sessions", exist_ok=True)

SESSIONS_DIR = "data/sessions"

def load_history_entries():
    entries = []
    if not os.path.exists(SESSIONS_DIR):
        return entries

    files = sorted([f for f in os.listdir(SESSIONS_DIR) if f.endswith(".json")], reverse=True)
    
    for file in files:
        fp = os.path.join(SESSIONS_DIR, file)
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            entries.append({
                "file": file,
                "path": fp,
                "topic": data.get("topic", "No topic"),
                "language": data.get("language", "N/A").upper(),
                "length": data.get("target_length", 0),
                "article": data.get("final_article", "")
            })
        except:
            continue
    return entries

def create_txt_data_uri(text):
    b64 = base64.b64encode(text.encode('utf-8')).decode()
    return f"data:text/plain;base64,{b64}"

def history_page_ui():  # ✅ FIXED - Return Blocks!
    with gr.Blocks():
        history_entries = load_history_entries()
        
        gr.Markdown("## 📜 Previous Sessions")
        
        if not history_entries:
            gr.Markdown("⚠️ No history available yet.")
            return
        
        for entry in history_entries:
            txt_filename = entry['file'].replace(".json", ".txt")
            
            with gr.Box():
                gr.Markdown(f"**📌 {entry['topic']}** | {entry['length']} words | 🌍 {entry['language']}")
                gr.Markdown(f"💾 `{entry['file']}`")

                with gr.Row():
                    if entry['article']:
                        txt_uri = create_txt_data_uri(entry['article'])
                        gr.DownloadButton(
                            "⬇️ Blog (.txt)",
                            value=txt_uri,
                            file_name=txt_filename
                        )
                    
                    gr.DownloadButton(
                        "⬇️ Full Data (.json)",
                        value=entry['path'],
                        file_name=entry['file']
                    )
                gr.Markdown("---")

def show():
    return history_page_ui()  # ✅ Returns Blocks!
