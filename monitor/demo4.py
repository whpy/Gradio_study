import gradio as gr
from datetime import datetime
import random
import time
import os
from pathlib import Path

def current_time():
    def inner():
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return f"Hello! The current time is: {current_time}"
    return inner

def current_image():
    def inner():
        fd = "cimages/"
        files = list(Path(fd).glob('*'))
        if not files:
            return 'generated_images/default.jpg'
        
        newest = max(files, key=os.path.getmtime)

        return str(newest)
    return inner

with gr.Blocks() as demo:
    gr.Markdown("# Implementation of real-time output ")

    with gr.Row():
        with gr.Column():
            out_streaming = gr.Textbox(label='real-time state',
                                    value = current_time(),
                                    every = 1,
                                    info = "current time")
            
            # msg = gr.Textbox()
            chatbot = gr.Chatbot()
            msg = gr.Textbox()
            clear = gr.ClearButton([msg, chatbot])
            def respond(message, chat_history):
                bot_message = random.choice(["Rock!", 'Paper!', 'Scissors!'])
                chat_history.append((message, bot_message))
                time.sleep(2)
                return '', chat_history
            msg.submit(respond, [msg, chatbot], [msg, chatbot])

        with gr.Column():
            # gr.Image("generated_images/cheetah.png")
            gr.Image(label='real-time image',
                                    value = current_image(),
                                    every = 1)
        
    
demo.launch()
