import gradio as gr
from project.core.coordinator import Coordinator
from project.core.streaming import stream_markdown

coordinator = Coordinator()

def generate_story(theme, chapters, session_id):
    chapters = int(chapters)
    story = coordinator.create_story(theme, chapters)

    combined = "\n\n".join([f"### Chapter {i+1}\n{c}" for i,c in enumerate(story)])
    return stream_markdown(combined)

demo = gr.Interface(
    fn=generate_story,
    inputs=[
        gr.Textbox(label="Story Theme"),
        gr.Slider(1, 10, value=3, label="Chapters"),
        gr.Textbox(label="Session ID")
    ],
    outputs=gr.Markdown(),
    title="AI Multi-Agent Story Writer (Gemini)"
)

if __name__ == "__main__":
    demo.launch()
