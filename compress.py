class Compress():
    def __init__(self):
        self.compressed = []
        self.values = {}
        self.txt = ''
    
    def compress(self, archivo):
        contador = 1
        lista = archivo.split(' ')
        palabras = []
        
        for token in lista:
            if token not in palabras:
                palabras.append(token)
        
        for palabra in palabras:   
            self.values[palabra] = contador
            contador += 1
        
        for token in lista:
            self.compressed.append(self.values[token])    
        
        return [self.compressed, self.values]


    def uncompress(self, compressed, values):
        palabras = list(values.keys())
        tokens = list(values.values())
        for i in compressed:
            self.txt += palabras[tokens.index(i)] + ' '
        return self.txt[:-1]
