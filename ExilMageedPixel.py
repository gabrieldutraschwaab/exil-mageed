import pyxel

class Jogador:
    def __init__(self, nome, vida, forca, defesa, velocidade, sorte, esperiencia, espirito, espiritualidade, mana, capacidade_inventario, inventario, magias, x, y):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
        self.velocidade = velocidade
        self.sorte = sorte
        self.esperiencia = esperiencia
        self.espirito = espirito
        self.espiritualidade = espiritualidade
        self.mana = mana
        self.capacidade_inventario = capacidade_inventario
        self.inventario = inventario
        self.x = x
        self.y = y
        self.magias = magias
        
        
    def modificarVida(self, modificacao):
        if modificacao <= -self.vida:
            print("Você morreu")
        elif modificacao > (200 - self.vida):
            self.vida = 200
        else:
            self.vida += modificacao
    def modificarForca(self, modificacao):
        if modificacao <= -self.forca:
            self.forca = 0
        elif modificacao > (50 - self.forca):
            self.forca = 50
        else:
            self.forca += modificacao
    def modificarDefesa(self, modificacao):
        if modificacao <= -self.defesa:
            self.defesa = 0
        elif modificacao > (50 - self.defesa):
            self.defesa = 50
        else:
            self.defesa += modificacao
    def modificarVelocidade(self, modificacao):
        if modificacao <= -self.velocidade:
            self.velocidade = 0
        elif modificacao > (100 - self.velocidade):
            self.velocidade = 100
        else:
            self.velocidade += modificacao
    def modificarSorte(self, modificacao):
        if modificacao <= -self.sorte:
            self.sorte = 0
        elif modificacao > (100 - self.sorte):
            self.sorte = 100
        else:
            self.sorte += modificacao
    def modificarEsperiencia(self, modificacao):
        self.esperiencia += modificacao
    def modificarEspirito(self, modificacao):
        self.espirito += modificacao
    def modificarEspiritualidade(self, modificacao):
        self.espiritualidade += modificacao
    def modificarMana(self, modificacao):
        self.mana += modificacao
    def modificarInventario(self, modificacao):
        self.inventario += modificacao
    def moverX(self, movimentacao):
        self.x += movimentacao
    def moverY(self, movimentacao):
        self.y += movimentacao
    def aprenderMagia(self, adicao):
        magias.append(adicao) 
        
        
        
class Magia:
    def __init__(self, nome, dano, mana, intervalo, alcance, area, nivel, chance_aprender):
        self.nome = nome
        self.dano = dano
        self.mana = mana
        self.intervalo = intervalo
        self.alcance = alcance
        self.area = area
        self.nivel = nivel
        self.chance_aprender = chance_aprender
        
    def modificarDano(self, modificacao):
        if mago.sorte == 100:
            self.intervalo = self.intervalo // 2
        elif mago.velocidade > 0 and mago.velocidade < 26:
            self.intervalo += (self.intervalo * 0.25)
        elif mago.velocidade == 0:
            self.intervalo += (self.intervalo * 0.5)
        else:
            self.intervalo = self.intervalo
    def modificarMana(self, modificacao):
        self.mana += modificacao
    def modificarIntervalo(self):
        if mago.velocidade >= 51:
            self.intervalo = self.intervalo // 2
        elif mago.velocidade > 0 and mago.velocidade < 26:
            self.intervalo += (self.intervalo * 0.25)
        elif mago.velocidade == 0:
            self.intervalo += (self.intervalo * 0.5)
        else:
            self.intervalo = self.intervalo
    def modificarAlcance(self, modificacao):
        self.alcance += modificacao
    def modificarArea(self, modificacao):
        self.area += modificacao
    def modificarNivel(self, modificacao):
        self.nivel += modificacao
    def modificarChanceAprender(self, modificacao):
        self.chance_aprender += modificacao
        
class Inimigo:
    def __init__(self, nome, vida, forca, defesa, velocidade, sorte, espirito):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
        self.velocidade = velocidade
        self.sorte = sorte
        self.espirito = espirito
    
    def modificarVida(self, modificacao):
        self.vida += modificacao
    def modificarForca(self, modificacao):
        self.forca += modificacao
    def modificarDefesa(self, modificacao):
        self.defesa += modificacao
    def modificarVelocidade(self, modificacao):
        self.velocidade += modificacao
    def modificarSorte(self, modificacao):
        self.sorte += modificacao
    def modificarEspirito(self, modificacao):
        self.espirito += modificacao
    

class Jogo:
    def __init__(self):
        pyxel.init(160, 120, title="Exil Mageed")
        pyxel.run(self.update, self.draw)
        self.mago = Jogador("Exil Mageed", 200, 50, 50, 40, 30, 10, 40, 100, 100, 10, [], [], 20, 20)
        self.lutador_demoniaco = Inimigo("Lutador Demoníaco", 240, 65, 55, 65, 35, 80)
        

        
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(0)
        
        
Jogo()
