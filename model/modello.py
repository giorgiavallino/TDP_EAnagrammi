from functools import lru_cache
from time import time
import copy

class Model:

    def __init__(self):
        self.lista_soluzioni = []
        self.set_soluzioni = set() # viene introdotto un set: a differenza della lista, quando vengono aggiunte le
        # soluzioni parziali a un set, non vengono aggiunti i doppioni

    def calcola_anagrammi(self, parola: str):
        self.lista_soluzioni = [] # bisogna resettarla a una lista vuota perché, in caso contrario, vengono memorizzati
        # in essa anche tutti gli anagrammi precedenti
        self._ricorsione("", parola)
        return self.lista_soluzioni, self.set_soluzioni

    @lru_cache(maxsize=None)
    def _ricorsione(self, soluzione_parziale, lettere_rimanenti):
        if len(lettere_rimanenti) == 0:
            self.set_soluzioni.add(soluzione_parziale)
            self.lista_soluzioni.append(soluzione_parziale)
        else:
            for i in range(len(lettere_rimanenti)):
                soluzione_parziale = soluzione_parziale + lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                self._ricorsione(soluzione_parziale, nuove_lettere_rimanenti)
                # Bisogna introdurre il backtracking altrimenti si creeranno stringhe di quattro, cinque,... caratteri
                soluzione_parziale = soluzione_parziale[:-1]

    # E se al posto di avere delle stringhe si ha una lista? La differenza sta nel fatto che la stringa è immutabile.

    def calcola_anagrammi_list(self, parola):
        self.lista_soluzioni = []
        self._ricorsione_list([], parola)
        return self.lista_soluzioni

    def _ricorsione_list(self, soluzione_parziale, lettere_rimanenti):
        if len(lettere_rimanenti) == 0:
            self.lista_soluzioni.append(copy.deepcopy(soluzione_parziale))
        else:
            for i in range(len(lettere_rimanenti)):
                soluzione_parziale.append(lettere_rimanenti[i])
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i + 1:]
                self._ricorsione_list(soluzione_parziale, nuove_lettere_rimanenti)
                soluzione_parziale.pop()

if __name__=="__main__":
    model = Model()
    start_time = time ()
    risultato = model.calcola_anagrammi("dog")
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}")
    print(risultato)