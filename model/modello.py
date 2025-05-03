class Model:

    def __init__(self):
        pass

    def calcola_anagrammi(self, parola: str):
        self._ricorsione("", parola)

    def _ricorsione(self, soluzione_parziale, lettere_rimanenti):
        if len(lettere_rimanenti) == 0:
            return print(soluzione_parziale)
        else:
            for i in range(len(lettere_rimanenti)):
                soluzione_parziale = soluzione_parziale + lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:,i] + lettere_rimanenti[i+1,:]

