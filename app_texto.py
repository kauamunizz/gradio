import gradio as gr

def inver_texto(texto):
    texto_reverso = texto[::-1]
    return texto_reverso, len(texto_reverso)

# print(inver_texto("testeeee"))
iframe = gr.Interface(
    fn=inver_texto,
    inputs="text",
    outputs=["text", "number"],
    title="Inverter texto",
    description="Digite o texto para inverter",
    theme="default"
)

iframe.launch()