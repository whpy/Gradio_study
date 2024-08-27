import gradio as gr
from datetime import datetime

def current_time():
    def inner():
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return f"Hello! The current time is: {current_time}"
    return inner

with gr.Blocks() as demo:
    gr.Markdown("# Implementation of real-time output ")
    out_streaming = gr.Textbox(label='real-time state',
                               value = current_time(),
                               every = 1,
                               info = "current time")

demo.launch()
