import openai
import os  

# Pegando a chave da API da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um assistente inteligente rodando o modelo GPT-4o."},
            {"role": "user", "content": prompt}
        ]
    )
    
    resposta = response.choices[0].message.content
    return resposta

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit"]:
        print("Chatbot encerrado.")
        break
    resposta = chat_with_gpt(user_input)
    print("Chatbot:", resposta)
