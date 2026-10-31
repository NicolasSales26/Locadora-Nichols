# LOCADORA NICHOLS - Versão Final Portfólio
# Desenvolvido por Nicolas - Estácio 

carros = {
    "1": {"nome": "Gol", "preco": 89, "disponivel": True},
    "2": {"nome": "Onix", "preco": 99, "disponivel": True},
    "3": {"nome": "HB20", "preco": 95, "disponivel": True}
}

reservas = []

print("=== LOCADORA NICHOLS - SISTEMA FINAL ===")

while True:
    print("\n--- CARROS ---")
    for k, v in carros.items():
        status = "DISPONIVEL" if v["disponivel"] else "ALUGADO"
        print(f"{k} - {v['nome']} - R$ {v['preco']}/dia [{status}]")
    
    print("\n4 - Ver relatório de reservas")
    print("0 - Sair e fechar caixa")
    
    opcao = input("\nEscolha: ")

    if opcao == "0":
        print("\n--- FECHAMENTO DO DIA ---")
        total_dia = sum(r["total"] for r in reservas)
        print(f"Total de reservas: {len(reservas)}")
        print(f"Faturamento total: R$ {total_dia}")
        print("Sistema encerrado!")
        break
    
    if opcao == "4":
        print("\n--- RELATORIO ---")
        if not reservas:
            print("Nenhuma reserva ainda.")
        else:
            for r in reservas:
                print(f"{r['cliente']} - {r['carro']} - {r['dias']} dias - R$ {r['total']}")
        continue

    if opcao not in carros:
        print("Opção inválida!")
        continue

    if not carros[opcao]["disponivel"]:
        print("Carro já ALUGADO! Escolha outro.")
        continue

    nome = input("Nome do cliente: ")
    dias = int(input("Quantos dias? "))
    
    carro = carros[opcao]
    total = carro["preco"] * dias
    
    reservas.append({
        "cliente": nome,
        "carro": carro["nome"],
        "dias": dias,
        "total": total
    })
    
    carros[opcao]["disponivel"] = False

    print(f"\n--- RECIBO GERADO ---")
    print(f"Cliente: {nome}")
    print(f"Carro: {carro['nome']}")
    print(f"Total: R$ {total}")
    print("Reserva confirmada!")
