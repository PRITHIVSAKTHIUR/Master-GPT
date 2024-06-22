import gradio as gr

# Define the components using the specified URLs

with gr.Blocks() as chatbot1:
    gr.HTML("<iframe src=' https://prithivmlmods-mistral-maturity-llm.hf.space' width='100%' height='600px' style='border-radius: 8px;'></iframe>")

with gr.Blocks() as chatbot:
    gr.HTML("<iframe src='https://prithivmlmods-mistral-7b-instruct-v0-3.hf.space' width='100%' height='600px' style='border-radius: 8px;'></iframe>")

with gr.Blocks() as imagegpt:
    gr.HTML("<iframe src='https://prithivmlmods-imagegpt-4xl.hf.space' width='100%' height='750px' style='border-radius: 8px;'></iframe>")

with gr.Blocks() as ss:
    gr.HTML("<iframe src='https://prithivmlmods-smart-search.hf.space' width='100%' height='850px' style='border-radius: 8px;'></iframe>")

with gr.Blocks() as me:
    gr.HTML("<iframe src='https://prithivmlmods-save-web-as-zip.hf.space' width='100%' height='800px' style='border-radius: 8px;'></iframe>")

with gr.Blocks() as mediadownloader:
    gr.HTML("<iframe src='https://prithivmlmods-all-in-one-downloader.hf.space' width='100%' height='900px' style='border-radius: 8px;'></iframe>")

with gr.Blocks() as abt:
    gr.HTML("<iframe src='https://huggingface.co/spaces/prithivMLmods/master-gpt/resolve/main/assets/images/2.png' width='100%' height='900px' style='border-radius: 8px;'></iframe>")



# Assemble the components into a single Gradio interface
with gr.Blocks(theme="bethecloud/storj_theme", title="Master Gpt") as demo:
    gr.Markdown("# Master Gpt")
    gr.TabbedInterface(
        [chatbot1, chatbot, imagegpt, ss, me, mediadownloader, abt], 
        ['Chat.-1', 'Chat.Zero', 'Image.GPT', 'Smart.Search', 'Web.2.Zip', 'Media.Downloader', 'About']
    )

# Launch the demo with GPU enabled
demo.queue().launch(debug=True)
