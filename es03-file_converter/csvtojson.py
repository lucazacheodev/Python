# Apri il file CSV e leggi i suoi contenuti
with open('players.csv', 'r') as file:
    # Leggi la prima riga per ottenere gli header (intestazioni delle colonne)
    headers = file.readline().strip().split(',')

    # Inizializza un dizionario per memorizzare i dati formattati
    json_data = {}

    # Leggi le restanti righe del file
    for line in file:
        # Dividi la riga in base alle virgole e rimuovi spazi bianchi
        values = line.strip().split(',')
        
        # Usa il primo e il secondo valore (nome e cognome) come chiave
        key = f"{values[0]}, {values[1]}"
        
        # Crea un dizionario per la riga corrente escludendo le prime due colonne
        entry = {headers[i]: values[i] for i in range(2, len(headers))}
        
        # Aggiungi l'entry al dizionario json_data
        json_data[key] = entry

# Costruisci manualmente la stringa JSON
json_string = "{\n"

# Itera attraverso il dizionario json_data per costruire la stringa
for idx, (name, details) in enumerate(json_data.items()):
    json_string += f'   "{name}": {{\n'  # Aggiungi la chiave (nome) e l'apertura delle parentesi graffe
    for key, value in details.items():
        json_string += f'      "{key}": "{value}",\n'  # Aggiungi ogni coppia chiave-valore all'entry
    # Rimuovi l'ultima virgola e aggiungi la parentesi graffa di chiusura
    json_string = json_string.rstrip(',\n') + '\n'
    json_string += '   }'  # Chiudi l'entry
    
    # Aggiungi una virgola tra le voci, tranne che per l'ultima
    if idx < len(json_data) - 1:
        json_string += ',\n'
    else:
        json_string += '\n'

json_string += "}"  # Chiudi la stringa JSON

# Scrivi il risultato formattato nel file players.json
with open('players.json', 'w') as json_file:
    json_file.write(json_string)  # Salva la stringa JSON nel file
