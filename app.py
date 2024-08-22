from fastapi import FastAPI
import gradio as gr
import os

app = FastAPI()

def global_variable_value_change_show(value):
    os.environ["MY_SECRET_KEY"] = value
    return gr.Textbox(label="Global Variable Value Changed to: " + value,visible=True)

with gr.Blocks() as demo:
    gr.Markdown("Hey Team : Gradio -> working fine!")
    global_variable_input = gr.Textbox(label="Input Global Variable")
    current_value = gr.TextBox(os.environ.get("MY_SECRET_KEY"),visible=False)
    submit_button = gr.Button("Submit")
    submit_button.click(global_variable_value_change_show, inputs=[global_variable_input],outputs=[current_value])

app = gr.mount_gradio_app(app, demo, path="/")
