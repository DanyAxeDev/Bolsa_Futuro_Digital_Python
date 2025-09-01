from datetime import datetime

def calcularArea(b, h):
    return b*h

# Se f = True (padrão), converte Celsius em Fahrenheit
# Se f = False, converte Fahrenheit em Celsius
def converterTemp(temp, f = True):
    if f:
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9
    
# Utiliza o horario real
def saudacao(nome):
    horario = int(datetime.now().strftime("%H"))
    if(5 <= horario < 12):
        return f"Bom dia, {nome}"
    elif(12 <= horario < 18):
        return f"Boa tarde, {nome}"
    else:
        return f"Boa noite, {nome}"
    
print(calcularArea(5, 8))

print(converterTemp(32, False))

print(saudacao("daniel"))
