import gradio as gr
from src.ui.main_ui import create_blog_ui  # correct import

# Hugging Face Space will launch this app
demo = create_blog_ui()

if __name__ == "__main__":
    demo.launch()
