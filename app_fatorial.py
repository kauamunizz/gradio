import gradio as gr
import math

def fatorial(num):
    if num <= 0:
        return "Fatorial nao definido para zero ou numeros negativos"
    else:
        return math.factorial(num)
    
iframe = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="text",
    title="Calculadora de Fatorial",
    description="Insira um numero para obter o fatorial",
    theme="default"
)

iframe.launch()