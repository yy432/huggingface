import gradio as gr

def explain(name: str):
    name = name.strip() or "Student"
    return f"""Hello, {name}!

This Hugging Face Space is running successfully.

Deployment flow:
GitHub -> Hugging Face Space -> Public App

Why this is good for students:
- free CPU tier
- simple repo structure
- easy to rebuild
- no Google Cloud billing risk for basic demos
"""

with gr.Blocks(title="GitHub to Hugging Face Demo") as demo:
    gr.Markdown("""
    # Hello everyone from hugging face, GitHub to Hugging Face Demo
    A lightweight NTU-style classroom demo Space.
    """)
    name = gr.Textbox(label="Enter your name", placeholder="Type your name here")
    output = gr.Textbox(label="App Output", lines=8)
    btn = gr.Button("Run Demo")
    btn.click(fn=explain, inputs=name, outputs=output)

if __name__ == "__main__":
    demo.launch()
