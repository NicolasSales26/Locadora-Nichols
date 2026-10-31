# LOCADORA NICHOLS - Versão Portfólio
# Por Nicolas - Eng. Software

carros = {
    "1": {"nome": "Gol", "preco": 89, "disponivel": True},
    "2": {"nome": "Onix", "preco": 99, "disponivel": True},
    "3": {"nome": "HB20", "preco": 95, "disponivel": True}
}
reservas = []

def mostrar_carros():
    print("\n--- CARROS DISPONÍVEIS ---")
    for k, v in carros.items():
        status = "DISPONÍVEL" if v["disponivel"] else "ALUGADO"
        print(f"{k} - {v['nome']} - R$ {v['preco']}/dia [{status}]")

def fazer_reserva():
    codigo = input("Código do carro que quer alugar: ")
    if codigo not in carros:
        print("Código inválido!")
        return
    
    carro = carros[codigo]
    if not carro["disponivel"]:
        print(f"{carro['nome']} já está alugado!")
        return

    try:
        dias = int(input(f"Quantos dias vai ficar com o {carro['nome']}? "))
        if dias <= 0:
            print("Dias tem que ser maior que zero.")
            return
    except ValueError:
        print("Digite um número válido!")
        return

    total = carro["preco"] * dias
    print(f"Total: R$ {total} por {dias} dias. Confirmar? (s/n)")
    if input().lower() == 's':
        carro["disponivel"] = False
        reservas.append({"carro": carro["nome"], "dias": dias, "total": total})
        print(f"Reserva confirmada! {carro['nome']} alugado com sucesso.")

def ver_relatorio():
    if not reservas:
        print("\nNenhuma reserva hoje.")
        return
    print("\n--- RELATÓRIO DO DIA ---")
    for r in reservas:
        print(f"- {r['carro']} | {r['dias']} dias | R$ {r['total']}")
    print(f"\nTotal de reservas: {len(reservas)}")
    print(f"Faturamento: R$ {sum(r['total'] for r in reservas)}")

# --- LOOP PRINCIPAL ---
while True:
    mostrar_carros()
    print("\n[R] - Reservar | [4] - Relatório | [0] - Fechar caixa")
    opcao = input("Escolha: ").lower()

    if opcao == 'r':
        fazer_reserva()
    elif opcao == '4':
        ver_relatorio()
    elif opcao == '0':
        ver_relatorio()
        print("Sistema encerrado!")
        break
    else:
        print("Opção inválida, tente de novo.")
