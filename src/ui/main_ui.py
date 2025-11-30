import gradio as gr
import json
import os
from src.orchestrator import OmniBlogOrchestrator

orchestrator = OmniBlogOrchestrator()

def generate_blog(topic, audience, tone, language, word_count):
    if not topic.strip():
        return "⚠ Please enter a topic!"

    result = orchestrator.run(topic, audience, tone, language, str(word_count))
    
    article = result["final_article"]
    session_id = result["session_id"]

    # Save as .txt for download
    file_path = os.path.join("outputs", f"{session_id}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(article)

    return article, file_path


def load_history():
    folder = "data/sessions"
    history_items = []

    if os.path.exists(folder):
        sessions = sorted(os.listdir(folder), reverse=True)
        for s in sessions:
            if s.endswith(".json"):
                path = os.path.join(folder, s)
                with open(path, "r", encoding="utf-8") as f:
                    content = json.load(f)

                title = content.get("topic", "Untitled")
                words = content.get("target_length", "-")
                lang = content.get("language", "unknown")

                history_items.append(
                    f"📌 **{title}** | 📝 {words} words | 🌐 {lang.upper()} <br>"
                    f"➡ *Saved as:* `{s}`"
                )

    if history_items:
        return "\n\n---\n".join(history_items)
    return "No previous sessions yet."


def create_blog_ui():  # 🔥 IMPORTANT
    with gr.Blocks(title="OmniBlog Agent Studio") as app:
        gr.Markdown("# 📝 OmniBlog Agent Studio (Groq Edition)")
        gr.Markdown("AI powered multi-agent blog creator 🚀")

        with gr.Row():
            topic = gr.Textbox(label="Blog Topic", placeholder="e.g. What is AI?")
            audience = gr.Textbox(label="Target Audience", value="students")

        with gr.Row():
            tone = gr.Textbox(label="Tone", value="friendly")
            language = gr.Dropdown(
                ["english", "hindi", "spanish"],
                label="Language", value="english"
            )

        word_count = gr.Slider(200, 2000, value=500, label="Word Count")

        generate_btn = gr.Button("🚀 Generate Blog")

        output_article = gr.Markdown(label="📌 Final Article")
        download_blog = gr.File(label="📥 Download Blog (.txt)")

        history_output = gr.Markdown(label="📚 Previous Sessions")

        generate_btn.click(
            generate_blog,
            inputs=[topic, audience, tone, language, word_count],
            outputs=[output_article, download_blog],
            show_progress=True
        ).then(load_history, outputs=history_output)

    return app  # 🔥 IMPORTANT


if __name__ == "__main__":
    create_blog_ui().launch()
