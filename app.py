# import gradio as gr
#import os

# def main():

#     with gr.Blocks() as demo:
#         gr.Markdown("Gradio -> working fine!")

#     demo.launch()

# """main Method Call"""
# if __name__ == '__main__':
#     main()

from fastapi import FastAPI
import gradio as gr

app = FastAPI()

with gr.Blocks() as demo:
    gr.Markdown("Hey Team : Gradio -> working fine!")

app = gr.mount_gradio_app(app, demo, path="/")