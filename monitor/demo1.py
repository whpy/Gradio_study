import gradio as gr
from datetime import datetime
import random
import time

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
            image_output = gr.Image(type="auto")  # Image display area
    

demo.launch()
