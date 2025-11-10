import gradio as gr

def subtrair(num1, num2):
    return num1 - num2

iframe = gr.Interface(
    fn=subtrair,
    inputs=["number", "number"],
    outputs="number",
    title="Calculadora de subtração",
    description="Insira dois numeros para realizar uma subtração",
    theme="default"
)

iframe.launch()