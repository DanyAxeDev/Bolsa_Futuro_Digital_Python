import json
import requests

def consultar_sinsind(nome_acesso, chave_acesso, cpf=None):
    url = "https://sinsind.app.br/sinsind/sinsind/"

    payload = {
        "nome": nome_acesso,
        "chave": chave_acesso
    }

    if cpf:
        payload["cpf"] = cpf

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)
        return None


def salvar_json(dados, caminho="result.json"):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"Arquivo salvo: {caminho}")


if __name__ == "__main__":
    usuario = ""
    senha = ""

    cpf_consulta = None 

    resultado = consultar_sinsind(usuario, senha, cpf_consulta)

    if resultado:
        salvar_json(resultado)
        print("Consulta realizada com sucesso!")
    else:
        print("Falha ao consultar API.")
