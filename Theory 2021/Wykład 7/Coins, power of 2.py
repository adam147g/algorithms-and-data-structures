# Biorąc pod uwagę tablicę liczb reprezentujących każdą monetę. Liczba posiadanych przez nas monet
# nieskończoność, więc nie musimy się martwić, ile monet mamy do dyspozycji.
# Dany zestawmonet jest wielokrotnościami jakiejś jednej liczby!!! Następnie
# otrzymujemy kwotę i prosimy o znalezienie minimalnej liczby monet, które są potrzebne
# aby zarobić tę kwotę.


def coin_change(coins, amount):
    coins.sort(reverse=True)    # sortowanie od największego, do najmniejszego - coins.sort + coins.reverse
    idx = count = 0
    while idx <= len(coins) - 1:
        if coins[idx] <= amount:
            amount -= coins[idx]
            count += 1
        else:
            idx += 1
    return count


amount = 237
coins = [1, 10, 100, 25, 5]
print(coin_change(coins, amount))