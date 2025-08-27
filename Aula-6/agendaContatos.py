agenda = {
    "daniel": {
        "telefone": "1234-5678",
        "email": "daniel@example.com"
    },
    "maria": {
        "telefone": "9876-5432",
        "email": "maria@example.com"
    },
    "jose": {
        "telefone": "5555-1234",
        "email": "jose@example.com"
    },
    "carla": {
        "telefone": "4444-5678",
        "email": "carla@example.com"
    }
}

print("Agenda de contatos:")
print("-" * 20)

for nome, contatos in agenda.items():
    print(f"{nome.capitalize()}:")
    for contato_type, contato_value in contatos.items():
        print(f"{contato_type.capitalize()} -> {contato_value}")
    print("-"*20)