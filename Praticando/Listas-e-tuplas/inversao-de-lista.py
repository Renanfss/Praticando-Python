'''
    Inversão de lista, inverte a ordem dos elemnetos
'''

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
print(f'{eventos_registrados[::-1]}') # Ooperador de fatiamento inverte a lista na impressão, mas não altera a lista original
eventos_registrados.reverse() # Esse metodo inverte a ordem da lsita original 
print(eventos_registrados)  

