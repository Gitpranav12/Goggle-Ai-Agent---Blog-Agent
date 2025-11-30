import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ui.main_ui import build_app

app = build_app()

if __name__ == "__main__":
    app.launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("PORT", 7860))
    )
