import gradio as gr
import random
import time

import os
import types
# from ... import autogen
# import autogen.AssistantAgent as AssistantAgent
# import  autogen.UserProxyAgent as UserProxyAgent
from autogen import AssistantAgent, UserProxyAgent
import os
import types
# from ... import autogen
# import autogen.AssistantAgent as AssistantAgent
# import  autogen.UserProxyAgent as UserProxyAgent
from autogen import AssistantAgent, UserProxyAgent

contxt = [{'content': 'Hello!', 'role': 'assistant'}]
llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}
assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)


# global variable storing the input of user to be sent
user_msg2send = ""


def gr_get_human_input(self, prompt: str) -> str:
        # iostream = IOStream.get_default()
        global user_msg2send
        reply = user_msg2send
        self._human_input.append(reply)
        return reply
user_proxy.get_human_input = types.MethodType(gr_get_human_input, user_proxy)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def user(user_message, history):
        # print(history)
        global user_msg2send
        user_msg2send = user_message
        if not hasattr(user, "counter"):
            user.counter = 0  # static variable initialization
        re_his = history + [[user_message, None]]
        return "", re_his

    def bot(history):
        # print(history)
        if not hasattr(bot, "counter"):
            bot.counter = 0  # static variable initialization
        if bot.counter == 0:
            msg2send = user_proxy.generate_init_message(message=user_msg2send)
            user_proxy.send(msg2send, assistant, request_reply=True, silent=False)
            bot_message = assistant.chat_messages[user_proxy][-1]['content']
            bot.counter += 1
        else:
            msg2send = user_proxy.generate_reply(messages=user_proxy.chat_messages[assistant], sender=assistant)
            user_proxy.send(msg2send, assistant, request_reply=True, silent=False)
            bot_message = assistant.chat_messages[user_proxy][-1]['content']
            bot.counter += 1
        # bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        print(bot_message)
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.05)
            yield history
        

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch(share=True)
