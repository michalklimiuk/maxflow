from collections import deque   # biblioteka wykorzystywana w stosach

def dfs(graf, start, koniec, rodzic, odwiedzone):
    stos = deque()
    stos.append(start)
    odwiedzone[start] = True

    while stos:
        aktualny = stos.popleft()

        for i, flow in enumerate(graf[aktualny]):
            if not odwiedzone[i] and flow > 0:
                stos.append(i)
                odwiedzone[i] = True
                rodzic[i] = aktualny

    return True if odwiedzone[koniec] else False

def wyswietl_sciezki(sciezki):
    for sciezka in sciezki:
        print(sciezka[0], sciezka[1:])

def wyswietl_graf_przeplywow(graf_przeplywow):
    for wiersz in graf_przeplywow:
        calkowity_przeplyw = wiersz[0]
        polaczenia = wiersz[1:]
        print(f"{calkowity_przeplyw} {polaczenia}")

def ford_fulkerson(graf, zrodlo, ujscie):
    rodzic = [-1] * len(graf)
    max_flow = 0
    sciezki = []

    while dfs(graf, zrodlo, ujscie, rodzic, [False] * len(graf)):
        przeplyw = float("inf")
        s = ujscie

        while s != zrodlo:
            przeplyw = min(przeplyw, graf[rodzic[s]][s])
            s = rodzic[s]

        max_flow += przeplyw

        v = ujscie
        sciezka = [v]
        while v != zrodlo:
            u = rodzic[v]
            graf[u][v] -= przeplyw
            graf[v][u] += przeplyw
            sciezka.append(u)
            v = rodzic[v]
        sciezka.reverse()
        sciezki.append([przeplyw] + sciezka)

    return max_flow, sciezki

with open('MaxFlows_data10.txt') as file:
    N = int(file.readline())
    graf = [[int(x) for x in file.readline().split()] for _ in range(N)]

    print(graf)

zrodlo = 0
ujscie = N - 1

max_flow_wartosc, sciezki = ford_fulkerson(graf, zrodlo, ujscie)

print("Maksymalny przepływ:", max_flow_wartosc)
print("Ścieżki przepływów:")
wyswietl_sciezki(sciezki)

graf_przeplywow = []

for wiersz in graf:
    calkowity_przeplyw = sum(wiersz)
    przeplyw_wiersza = [calkowity_przeplyw] + wiersz
    graf_przeplywow.append(przeplyw_wiersza)

print("Graf przepływów:")
wyswietl_graf_przeplywow(graf_przeplywow)