import gradio as gr

def somar(num1, num2):
    return num1 + num2

iface = gr.Interface(
    fn=somar,
    inputs=["number", "number"],
    outputs="number",
    title="Calculadora de soma",
    description="Insira dois numeros para obter a soma",
    theme="default"
       
)

iface.launch()



# print(somar(3, 2))