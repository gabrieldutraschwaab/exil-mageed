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
        self.quadro = 0
        self.sprite_x = 0
        self.sprite_y = 0
        self.movendo = False
        self.tempo_animacao = 0
        
        
    def modificarVida(self, modificacao):
        if modificacao <= -self.vida:
            self.vida = 0
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
        elif modificacao > (100 - self.defesa):
            self.defesa = 100
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
        self.x += movimentacao * self.velocidade / 40
    def moverY(self, movimentacao):
        self.y += movimentacao * self.velocidade / 40
    def aprenderMagia(self, adicao):
        self.magias.append(adicao)
        
        
        
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

class Ataque:
    def __init__(self, x, y, largura, altura, dano):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.dano = dano
    

class Jogo:
    def __init__(self):
        pyxel.init(160, 120, title="Exil Mageed")
        pyxel.images[0].load(0, 0, "mage.png")
        self.mago = Jogador("Exil Mageed", 200, 50, 100, 40, 30, 10, 40, 100, 100, 10, [], [], 20, 20)
        self.ataque = Ataque(100, 70, 16, 16, 20)
        self.encostou_ataque = False
        self.lutador_demoniaco = Inimigo("Lutador Demoníaco", 240, 65, 55, 65, 35, 80)
        pyxel.run(self.update, self.draw)
        
    def colisaoAtaque(self):
        colisaoX = self.mago.x + 16 >= self.ataque.x and self.mago.x <= self.ataque.x + self.ataque.largura
        colisaoY = self.mago.y + 16 >= self.ataque.y and self.mago.y <= self.ataque.y + self.ataque.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False
        
    def update(self):
        if self.mago.vida == 0:
            return

        self.mago.movendo = False

        if pyxel.btn(pyxel.KEY_W):
            self.mago.moverY(-1)
            self.mago.sprite_x = 64
            self.mago.sprite_y = 0
            self.mago.movendo = True
        elif pyxel.btn(pyxel.KEY_S):
            self.mago.moverY(1)
            self.mago.sprite_x = 0
            self.mago.sprite_y = 0
            self.mago.movendo = True
        elif pyxel.btn(pyxel.KEY_A):
            self.mago.moverX(-1)
            self.mago.sprite_x = 64
            self.mago.sprite_y = 16
            self.mago.movendo = True
        elif pyxel.btn(pyxel.KEY_D):
            self.mago.moverX(1)
            self.mago.sprite_x = 0
            self.mago.sprite_y = 16
            self.mago.movendo = True

        if self.mago.movendo:
            self.mago.tempo_animacao += 1

            if self.mago.tempo_animacao == 6:
                self.mago.quadro += 1
                self.mago.tempo_animacao = 0

                if self.mago.quadro > 3:
                    self.mago.quadro = 0
        else:
            self.mago.quadro = 0
            self.mago.tempo_animacao = 0

        if self.mago.x < 0:
            self.mago.x = 0
        elif self.mago.x > 144:
            self.mago.x = 144

        if self.mago.y < 0:
            self.mago.y = 0
        elif self.mago.y > 104:
            self.mago.y = 104

        if self.colisaoAtaque():
            if self.encostou_ataque == False:
                dano_recebido = self.ataque.dano

                if self.mago.defesa == 0:
                    dano_recebido += dano_recebido * 90 // 100
                elif self.mago.defesa <= 25:
                    dano_recebido += dano_recebido * 45 // 100
                elif self.mago.defesa <= 50:
                    dano_recebido += dano_recebido * 25 // 100

                self.mago.modificarVida(-dano_recebido)
                self.encostou_ataque = True
        else:
            self.encostou_ataque = False
    
    def draw(self):
        pyxel.cls(0)

        pyxel.text(2, 2, "V:" + str(self.mago.vida) + " F:" + str(self.mago.forca) + " E:" + str(self.mago.espiritualidade) + " D:" + str(self.mago.defesa), 7)

        x_imagem = self.mago.sprite_x + self.mago.quadro * 16
        pyxel.blt(self.mago.x, self.mago.y, 0, x_imagem, self.mago.sprite_y, 16, 16, 7)

        pyxel.rect(self.ataque.x, self.ataque.y, self.ataque.largura, self.ataque.altura, 8)

        if self.mago.vida == 0:
            pyxel.cls(0)
            pyxel.text(55, 52, "VOCE MORREU", 8)
            pyxel.text(55, 62, "FIM DE JOGO", 7)
        
        
Jogo()
