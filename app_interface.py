import gradio as gr

def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):
    estilo=(
        f"color: {cor_texto};"
        f"background-color: {cor_fundo};"
        f"font-size: {tamanho_fonte}px;"
        f"font-family: {estilo_fonte};"
    )
    return f'<div style="{estilo}"> {texto}</div>'

iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite seu texto aqui"),
        gr.ColorPicker(label="Cor de fundo"),
        gr.ColorPicker(label="Cor do texto"),
        gr.Slider(maximum=100, minimum=10, label="Tamanho da Fonte", value=20),
        gr.Radio(
            choices=["Arial", "Courier New", "Georgia", "Times New Roman", "Verdana"],
            label="Estilo da Fonte"
        )
    ],
    outputs=gr.HTML(label="Texto customizado"),
    title="Customizador de Texto",
    description="Customize o seu texto com cor, tamanho e estilo de fonte"    
)

iface.launch()