from collections import Counter


def show_stats(results):
    # media de tempo
    total_timeout = sum([1 for result in results if result["timeout"]])
    total_time = sum([result["timeit"] for result in results])
    total_played = sum([result["played"] for result in results])
    count_winner = Counter()
    for result in results:
        strategy = str(result['strategy'])
        count_winner[strategy] += 1
    # quantos turnoe em media demora uma partida
    print(f"Quantas partidas terminam por timeout: { total_timeout}")
    print(
        f"Quantos turnos em média demora uma partida: { total_played / len(results):.1f}"
    )
    print(
        f"Qual o comportamento que mais venceu: {count_winner.most_common(1)[0][0]} venceu: {count_winner.most_common(1)[0][1]}"
    )
    print("Qual a porcentagem de vitórias por comportamento dos jogadores:")
    for strategy, winner in count_winner.most_common():
        print("  *  ", f"{strategy}: {(winner * 100)// len(results)}%")
