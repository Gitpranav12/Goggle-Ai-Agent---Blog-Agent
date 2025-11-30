import gradio as gr
import os, shutil

def clear_history():
    folder = "data/sessions"
    if os.path.exists(folder):
        shutil.rmtree(folder)
        os.makedirs(folder)
    return "History cleared successfully!"

def settings_ui():
    gr.Markdown("### ⚙ Settings")
    gr.Button("🧹 Clear All Session History").click(
        clear_history, None, gr.Textbox(label="")
    )
