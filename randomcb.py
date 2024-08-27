import random
import gradio as gr

def alternatingly_agree(message, history):
    
    if len(history) % 2 == 0:
        print(history)
        print(message)
        return f"Yes, I do think that '{message}'"
    else:
        print(history)
        print(message)
        return "I don't think so"

gr.ChatInterface(alternatingly_agree).launch()