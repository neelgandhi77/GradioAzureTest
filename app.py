from fastapi import FastAPI
import gradio as gr
import os
import json
import config
import pandas as pd


temp_list = []

def string_to_list_format_generator(string):
    return string.split(', ')

def list_to_string_format_generator(list):
    return ', '.join(list)
    

    
# Load the JSON file
with open('rules_modular_approach.json') as file:
    rules = json.load(file)

app = FastAPI()

def global_variable_value_change_show(value):
    global rules,temp_list
    if(type(temp_list) != list):
        temp_list = string_to_list_format_generator(temp_list)
    rules["data_preprocessing"]["negative value handling method selected by user"] = "Changed by Neel: " + value
    json.dump(rules,open('rules_modular_approach.json', 'w'), indent=4)

    temp_list.append(value)
    temp_list = list_to_string_format_generator(temp_list)
    os.environ["MY_SECRET_KEY"] = temp_list
    #temp_list = string_to_list_format_generator(temp_list)
    #print(temp_list)
    config.method.append("Set by Neel : "+ str(value))
    return gr.Textbox(label="List : ", value= temp_list,visible=True), \
            gr.Textbox(label="JSON : ", value= rules["data_preprocessing"]["negative value handling method selected by user"],visible=True), \
            gr.Textbox(label="Method : ", value=config.method ,visible=True)

with gr.Blocks() as demo:
    gr.Markdown("Hey Team : Gradio -> working fine!")
    file_input = gr.File(label="Upload Dataset",file_types=['.csv'],file_count="single")  

    
    global_variable_input = gr.Textbox(label="Input Global Variable")
    current_value_list = gr.Textbox(os.environ.get("MY_SECRET_KEY"),visible=False)
    current_value_json = gr.Textbox(rules["data_preprocessing"]["negative value handling method selected by user"],visible=False)
    current_value_method = gr.Textbox(config.method,visible=False)
    
    submit_button = gr.Button("Submit")


    submit_button.click(global_variable_value_change_show, inputs=[global_variable_input],outputs=[current_value_list,current_value_json,current_value_method])

app = gr.mount_gradio_app(app, demo, path="/")
