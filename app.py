import gradio as gr


text_prompt_component = gr.Textbox(label="Text Prompt", scale=7)
submit_button_component = gr.Button(value="Submit", scale=1)


def on_submit(text_prompt):
    print(text_prompt)


with gr.Blocks() as demo:
    with gr.Row():
        text_prompt_component.render()
        submit_button_component.render()

    submit_button_component.click(
        fn=on_submit,
        inputs=[text_prompt_component],
        outputs=[],
        queue=False
    )


demo.queue(max_size=99).launch(debug=False, show_error=True, share=True)