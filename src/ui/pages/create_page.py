import gradio as gr
from src.orchestrator import OmniBlogOrchestrator

orchestrator = OmniBlogOrchestrator()

def generate_blog(topic, audience, tone, language, words):
    if not topic.strip():
        return "⚠ Please enter a topic!", "", ""

    progress = ""
    def update_step(step):
        nonlocal progress
        progress += step + "\n"
        yield progress, "", ""

    # Step updates
    yield from update_step("📝 Planning structure...")
    yield from update_step("🔍 Researching sections...")
    yield from update_step("✍ Writing draft...")
    yield from update_step("✨ Finalizing content...")

    result = orchestrator.run(topic, audience, tone, language, str(words))
    return progress, result["final_article"], result["session_id"]

def create_blog_ui():
    topic = gr.Textbox(label="Blog Topic")
    audience = gr.Textbox(label="Target Audience", value="students")
    tone = gr.Textbox(label="Tone", value="friendly")
    language = gr.Dropdown(["english", "hindi", "spanish"], label="Language", value="english")
    words = gr.Slider(200, 2000, value=500, step=100, label="Word Count")

    gen_btn = gr.Button("🚀 Generate Blog")

    progress = gr.Textbox(label="Agent Progress", interactive=False)
    output = gr.Markdown()
    session_id = gr.Textbox(visible=False)

    gen_btn.click(generate_blog,
        inputs=[topic, audience, tone, language, words],
        outputs=[progress, output, session_id]
    )
