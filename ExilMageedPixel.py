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
        self.itens_equipados = [None, None, None, None, None]
        self.item_selecionado = None
        self.magias_equipadas = [None, None, None, None]
        self.magia_selecionada = None
        self.quadro = 0
        self.sprite_x = 0
        self.sprite_y = 0
        self.movendo = False
        self.tempo_animacao = 0
        self.reducao_forca_vida = 0
        self.reducao_velocidade_vida = 0
        
        
    def modificarVida(self, modificacao):
        if modificacao <= -self.vida:
            self.vida = 0
        elif modificacao > (200 - self.vida):
            self.vida = 200
        else:
            self.vida += modificacao
        self.atualizarAtributosVida()
    def atualizarAtributosVida(self):
        self.forca += self.reducao_forca_vida
        self.velocidade += self.reducao_velocidade_vida

        self.reducao_forca_vida = 0
        self.reducao_velocidade_vida = 0

        if self.vida > 50 and self.vida <= 100:
            self.reducao_forca_vida = self.forca * 15 // 100
            self.reducao_velocidade_vida = self.velocidade * 15 // 100
        elif self.vida > 0 and self.vida <= 50:
            self.reducao_forca_vida = self.forca * 35 // 100
            self.reducao_velocidade_vida = self.velocidade * 35 // 100

        self.forca -= self.reducao_forca_vida
        self.velocidade -= self.reducao_velocidade_vida
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
        if modificacao <= -self.mana:
            self.mana = 0
        elif modificacao > (100 - self.mana):
            self.mana = 100
        else:
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
    
class InimigoFake:
    def __init__(self, x, y, largura, altura, vida, defesa):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vida = vida
        self.defesa = defesa

class Bau:
    def __init__(self, x, y, largura, altura, magias):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.magias = magias
        self.aberto = False

class ProjetilMagico:
    def __init__(self, x, y, direcao_x, direcao_y, dano):
        self.x = x
        self.y = y
        self.direcao_x = direcao_x
        self.direcao_y = direcao_y
        self.dano = dano

    def mover(self):
        self.x += self.direcao_x * 2
        self.y += self.direcao_y * 2

class Jogo:
    def __init__(self):
        pyxel.init(160, 120, title="Exil Mageed")
        pyxel.mouse(True)
        pyxel.images[0].load(0, 0, "mage.png")
        pyxel.images[1].load(0, 0, "disparo_arcano.png")
        self.mago = Jogador("Exil Mageed", 200, 50, 100, 40, 30, 10, 40, 100, 100, 10, [], [], 20, 20)
        self.disparo_arcano = Magia("Disparo Arcano", 20, 10, 20, 50, 1, 1, 100)
        self.bau = Bau(40, 70, 16, 16, [self.disparo_arcano])
        self.projetil = None
        self.tempo_mensagem = 0
        self.ataque = Ataque(100, 70, 16, 16, 20)
        self.inimigo_fake = InimigoFake(120, 35, 16, 16, 100, 10)
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

    def colisaoBau(self):
        colisaoX = self.mago.x + 16 >= self.bau.x and self.mago.x <= self.bau.x + self.bau.largura
        colisaoY = self.mago.y + 16 >= self.bau.y and self.mago.y <= self.bau.y + self.bau.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def colisaoProjetil(self):
        colisaoX = self.projetil.x + 16 >= self.inimigo_fake.x and self.projetil.x <= self.inimigo_fake.x + self.inimigo_fake.largura
        colisaoY = self.projetil.y + 16 >= self.inimigo_fake.y and self.projetil.y <= self.inimigo_fake.y + self.inimigo_fake.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False
        
    def update(self):
        if self.mago.vida == 0:
            return
        
        self.mago.modificarMana(0.05)
        self.mago.modificarVida(0.005)

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

        if self.mago.y < 14:
            self.mago.y = 14
        elif self.mago.y > 86:
            self.mago.y = 86

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

        if self.colisaoBau() and pyxel.btnp(pyxel.KEY_E):
            if self.bau.aberto == False:
                self.mago.aprenderMagia(self.disparo_arcano)
                self.mago.magias_equipadas[0] = self.disparo_arcano
                self.mago.magia_selecionada = self.disparo_arcano
                self.bau.aberto = True
                self.tempo_mensagem = 60

        if pyxel.btnp(pyxel.KEY_1):
            self.mago.item_selecionado = self.mago.itens_equipados[0]
        elif pyxel.btnp(pyxel.KEY_2):
            self.mago.item_selecionado = self.mago.itens_equipados[1]
        elif pyxel.btnp(pyxel.KEY_3):
            self.mago.item_selecionado = self.mago.itens_equipados[2]
        elif pyxel.btnp(pyxel.KEY_4):
            self.mago.item_selecionado = self.mago.itens_equipados[3]
        elif pyxel.btnp(pyxel.KEY_5):
            self.mago.item_selecionado = self.mago.itens_equipados[4]

        if pyxel.btnp(pyxel.KEY_6):
            self.mago.magia_selecionada = self.mago.magias_equipadas[0]
        elif pyxel.btnp(pyxel.KEY_7):
            self.mago.magia_selecionada = self.mago.magias_equipadas[1]
        elif pyxel.btnp(pyxel.KEY_8):
            self.mago.magia_selecionada = self.mago.magias_equipadas[2]
        elif pyxel.btnp(pyxel.KEY_9):
            self.mago.magia_selecionada = self.mago.magias_equipadas[3]

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.mago.magia_selecionada == self.disparo_arcano:
                if self.mago.mana >= self.disparo_arcano.mana:
                    distancia_x = pyxel.mouse_x - (self.mago.x + 8)
                    distancia_y = pyxel.mouse_y - (self.mago.y + 8)
                    distancia = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

                    if distancia > 0:
                        direcao_x = distancia_x / distancia
                        direcao_y = distancia_y / distancia
                        self.projetil = ProjetilMagico(self.mago.x + 4, self.mago.y + 4, direcao_x, direcao_y, self.disparo_arcano.dano)
                        self.mago.modificarMana(-self.disparo_arcano.mana)

        if self.projetil != None:
            self.projetil.mover()

            if self.colisaoProjetil():
                self.inimigo_fake.vida -= self.projetil.dano

                if self.inimigo_fake.vida < 0:
                    self.inimigo_fake.vida = 0

                self.projetil = None
        
        if self.tempo_mensagem > 0:
            self.tempo_mensagem -= 1
    
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, 160, 14, 1)

        pyxel.text(2, 2, "V:" + str(int(self.mago.vida)) + " F:" + str(self.mago.forca) + " E:" + str(self.mago.espiritualidade) + " D:" + str(self.mago.defesa) + " VEL:" + str(self.mago.velocidade), 7)

        x_imagem = self.mago.sprite_x + self.mago.quadro * 16
        pyxel.blt(self.mago.x, self.mago.y, 0, x_imagem, self.mago.sprite_y, 16, 16, 7)

        if self.mago.magia_selecionada != None:
            pyxel.text(2, 8, "M:" + str(int(self.mago.mana)) + " Magia:" + self.mago.magia_selecionada.nome, 10)
        else:
            pyxel.text(2, 8, "M:" + str(int(self.mago.mana)) + " Magia:nenhuma", 7)

        pyxel.rect(self.ataque.x, self.ataque.y, self.ataque.largura, self.ataque.altura, 8)

        pyxel.rect(self.inimigo_fake.x, self.inimigo_fake.y, self.inimigo_fake.largura, self.inimigo_fake.altura, 11)
        pyxel.text(self.inimigo_fake.x, self.inimigo_fake.y - 6, "V:" + str(self.inimigo_fake.vida), 7)

        if self.projetil != None:
            pyxel.blt(self.projetil.x, self.projetil.y, 1, 0, 0, 16, 16, 0)

        if self.bau.aberto == False:
            pyxel.rect(self.bau.x, self.bau.y, self.bau.largura, self.bau.altura, 9)
            if self.colisaoBau():
                pyxel.text(24, 95, "Pressione E para abrir", 7)

        else:
            pyxel.rect(self.bau.x, self.bau.y, self.bau.largura, self.bau.altura, 4)
            if self.tempo_mensagem > 0:
                pyxel.text(24, 95, "Disparo Arcano aprendido", 10)

        pyxel.rect(0, 102, 160, 18, 1)
        for i in range(9):
            x_espaco = 4 + i * 17

            if i < 5:
                cor = 5
            else:
                cor = 13

            pyxel.rect(x_espaco, 104, 15, 14, cor)
            pyxel.text(x_espaco + 5, 108, str(i + 1), 7)

        if self.mago.magias_equipadas[0] == self.disparo_arcano:
            pyxel.blt(89, 103, 1, 0, 0, 16, 16, 0, scale=0.7)

        if self.mago.vida == 0:
            pyxel.cls(0)
            pyxel.text(55, 52, "VOCE MORREU", 8)
            pyxel.text(55, 62, "FIM DE JOGO", 7)
        
        
Jogo()
