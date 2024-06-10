#!/bin/env python
import sys
import signal
import http.server
import socketserver

# Verifica se è stato passato un argomento per la porta
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080   # Porta predefinita se non è stata specificata una porta

# Creazione di un server TCP multithreading che utilizza SimpleHTTPRequestHandler per gestire le richieste HTTP
server = socketserver.ThreadingTCPServer(('',port), http.server.SimpleHTTPRequestHandler )

# Configurazione del server
server.daemon_threads = True  # Usa thread demone per gestire le richieste
server.allow_reuse_address = True  # Permetti il riutilizzo dell'indirizzo

# Funzione di gestione del segnale SIGINT (Ctrl+C)
def signal_handler(signal, frame):
    print( 'Exiting http server (Ctrl+C pressed)')
    try:
      if( server ):
        server.server_close()   # Chiudi il server
    finally:
      sys.exit(0)   # Esci dal programma

# Associa il gestore del segnale SIGINT alla funzione signal_handler
signal.signal(signal.SIGINT, signal_handler)

try:
  while True:
    # Esegui il server per gestire le richieste in modo continuo
    server.serve_forever()
except KeyboardInterrupt:
  pass  # Ignora l'eccezione KeyboardInterrupt

# Alla fine chiudi il server
server.server_close()
