# Calculadora em Python
# Executa adição, subtração, multiplicação e divisão no terminal.
 
LINHA = "=" * 40
 
# Cada opção do menu aponta para o nome e o símbolo da operação.
OPERACOES = {
    "1": ("Adição", "+"),
    "2": ("Subtração", "-"),
    "3": ("Multiplicação", "*"),
    "4": ("Divisão", "/"),
}
 
 
def mostrar_titulo():
    print(LINHA)
    print("        CALCULADORA EM PYTHON")
    print(LINHA)
 
 
def mostrar_menu():
    print("\nEscolha a operação:")
    for numero, (nome, simbolo) in OPERACOES.items():
        print(f"  {numero} - {nome} ({simbolo})")
    print("  0 - Sair")
    print("-" * 40)
 
 
def ler_numero(mensagem):
    """Pede um número até o usuário digitar um valor válido (aceita vírgula)."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(texto)
        except ValueError:
            print("Valor inválido. Digite apenas números (exemplo: 12 ou 3,5).")
            continue
        if numero != numero or numero in (float("inf"), float("-inf")):
            print("Valor inválido. Digite um número comum.")
            continue
        return numero
 
 
def calcular(opcao, primeiro_numero, segundo_numero):
    """Realiza a operação escolhida. Retorna None se a divisão for por zero."""
    if opcao == "1":
        return primeiro_numero + segundo_numero
    if opcao == "2":
        return primeiro_numero - segundo_numero
    if opcao == "3":
        return primeiro_numero * segundo_numero
    if opcao == "4":
        if segundo_numero == 0:
            return None
        return primeiro_numero / segundo_numero
 
 
def formatar(valor):
    """Mostra números inteiros sem '.0' e limita as casas decimais."""
    if abs(valor) >= 1e15:
        return f"{valor:.6g}"  # números enormes ficam em notação científica
    if valor.is_integer():
        return str(int(valor))
    return f"{valor:.4f}".rstrip("0").rstrip(".")
 
 
def mostrar_resultado(opcao, primeiro_numero, segundo_numero, resultado):
    simbolo = OPERACOES[opcao][1]
    print()
    print(LINHA)
    if resultado is None:
        print("  ERRO: não é possível dividir por zero.")
    else:
        print(f"  Cálculo:   {formatar(primeiro_numero)} {simbolo} {formatar(segundo_numero)}")
        print(f"  RESULTADO: {formatar(resultado)}")
    print(LINHA)
 
 
def main():
    mostrar_titulo()
    while True:
        mostrar_menu()
        opcao = input("Opção: ").strip()
 
        if opcao == "0":
            print("\nCalculadora encerrada. Até a próxima!")
            break
 
        if opcao not in OPERACOES:
            print("Opção inválida. Escolha um número de 0 a 4.")
            continue
 
        primeiro_numero = ler_numero("Digite o primeiro número: ")
        segundo_numero = ler_numero("Digite o segundo número: ")
 
        resultado = calcular(opcao, primeiro_numero, segundo_numero)
        mostrar_resultado(opcao, primeiro_numero, segundo_numero, resultado)
 
 
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nCalculadora encerrada.")