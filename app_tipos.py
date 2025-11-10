import gradio as gr

def processar_dados(texto, num, img, lista_texto, cor, opcoes):
    texto_revertido = texto[::-1]
    dobro_numero = num * 2
    mensagem_img = "Imagem recebida" if img else "Nao ha imagem recebida"
    
    lista_processada = [[item] for item in lista_texto.splitlines()] if lista_texto else []
    
    return(
        texto_revertido,
        dobro_numero,
        mensagem_img,
        lista_processada,
        f"Cor selecionada: {cor}",
        opcoes
    )
    
iface = gr.Interface(
    fn= processar_dados,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite um texto aqui"),
        gr.Slider(minimum=0, maximum=100, label="Numero", value=0),
        gr.Image(type="pil", label="Imagem"),
        gr.Textbox(label="Lista de itens", lines=4, placeholder="Item 1 \nItem 2"),
        gr.ColorPicker(label="Selecione uma cor"),
        gr.CheckboxGroup(
            choices=["Opção 1", "Opção 2", "Opção 3"],
            label="Escolha suas opções"
        )
    ],
    outputs=[
        gr.Textbox(label="Texto revertido"),
        gr.Number(label="Dobro do numero"),
        gr.Textbox(label="Mensagem sobre a imagem"),
        gr.DataFrame(label="Itens da lista", headers=["Itens"]),
        gr.Textbox(label="Cor selecionada"),
        gr.Textbox(label="Opções Selecionadas")
    ],
    title="Verificador de entradas e saidas",
    description="Insira um texto, um numero, uma imagem, uma lista de itens, uma cor e opções",
    theme="default"
)

iface.launch()