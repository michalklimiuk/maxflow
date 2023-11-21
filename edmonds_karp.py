from collections import deque   # biblioteka wykorzystywana w stosach

def bfs(graf, start, koniec, rodzic):
    odwiedzone = [False] * len(graf)
    stos = deque()
    stos.append(start)
    odwiedzone[start] = True

    while stos:
        u = stos.popleft()

        for v, przeplyw in enumerate(graf[u]):
            if odwiedzone[v] is False and przeplyw > 0:
                stos.append(v)
                odwiedzone[v] = True
                rodzic[v] = u

    return True if odwiedzone[koniec] else False

def wyswietl_sciezki(sciezki):
    for sciezka in sciezki:
        print(sciezka[0], sciezka[1:])

def wyswietl_graf_przeplywow(graf_przeplywow):
    for wiersz in graf_przeplywow:
        calkowity_przeplyw = wiersz[0]
        polaczenia = wiersz[1:]
        print(f"{calkowity_przeplyw} {polaczenia}")

def edmonds_karp(graf, zrodlo, ujscie):
    rodzic = [-1] * len(graf)
    max_flow = 0
    sciezki = []

    while bfs(graf, zrodlo, ujscie, rodzic):
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

zrodlo = 0
ujscie = N - 1

max_flow_wartosc, sciezki = edmonds_karp(graf, zrodlo, ujscie)

print("Maksymalny przepływ:", max_flow_wartosc)
print("Ścieżki:")
wyswietl_sciezki(sciezki)

graf_przeplywow = []

for row in graf:
    total_flow = sum(row)
    flow_row = [total_flow] + row
    graf_przeplywow.append(flow_row)

print("Graf przepływów:")
wyswietl_graf_przeplywow(graf_przeplywow)
