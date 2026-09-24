import pyxel

class Jogador:
    def __init__(self, nome, vida, forca, defesa, velocidade, sorte, esperiencia, espirito, espiritualidade, mana, capacidade_inventario, capacidade_magias, inventario, magias, x, y):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
        self.velocidade = velocidade
        self.sorte = sorte
        self.esperiencia = esperiencia
        self.espirito = espirito
        self.espiritualidade_maxima = self.espirito * 5 // 2
        self.espiritualidade = espiritualidade
        self.mana = mana
        self.capacidade_inventario = capacidade_inventario
        self.capacidade_magias = capacidade_magias
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
        self.espiritualidade_maxima = self.espirito * 5 // 2

        if self.espiritualidade > self.espiritualidade_maxima:
            self.espiritualidade = self.espiritualidade_maxima

    def modificarEspiritualidade(self, modificacao):
        self.espiritualidade += modificacao

        if self.espiritualidade < 0:
            self.espiritualidade = 0
        elif self.espiritualidade > self.espiritualidade_maxima:
            self.espiritualidade = self.espiritualidade_maxima

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
        
class Item:
    def __init__(self, nome, tipo, efeito, valor, consumivel, raridade):
        self.nome = nome
        self.tipo = tipo
        self.efeito = efeito
        self.valor = valor
        self.consumivel = consumivel
        self.raridade = raridade

    def usar(self, jogador):
        if self.efeito == "vida":
            jogador.modificarVida(self.valor)
        
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
    def __init__(self, x, y, largura, altura, magias, itens):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.magias = magias
        self.itens = itens
        self.aberto = False

class ProjetilMagico:
    def __init__(self, x, y, direcao_x, direcao_y, dano, imagem_y):
        self.x = x
        self.y = y
        self.direcao_x = direcao_x
        self.direcao_y = direcao_y
        self.dano = dano
        self.imagem_y = imagem_y

    def mover(self):
        self.x += self.direcao_x * 2
        self.y += self.direcao_y * 2

class Jogo:
    def __init__(self):
        pyxel.init(160, 120, title="Exil Mageed")
        pyxel.mouse(True)
        pyxel.images[0].load(0, 0, "mage.png")
        pyxel.images[1].load(0, 0, "disparo_arcano.png")
        pyxel.images[1].load(0, 32, "bola_fogo.png")
        pyxel.images[1].load(0, 64, "barreira_cristal.png")
        pyxel.images[1].load(0, 96, "explosao_arcana.png")
        pyxel.images[2].load(0, 0, "pocao_vida.png")
        self.mago = Jogador("Exil Mageed", 200, 50, 100, 40, 30, 10, 40, 100, 100, 10, 10, [], [], 20, 20)
        self.disparo_arcano = Magia("Disparo Arcano", 20, 10, 20, 50, 1, 1, 100)
        self.bola_fogo = Magia("Bola de Fogo", 35, 20, 30, 45, 2, 1, 100)
        self.barreira_cristal = Magia("Barreira de Cristal", 0, 25, 60, 0, 3, 1, 100)
        self.explosao_arcana = Magia("Explosao Arcana", 50, 35, 70, 0, 4, 1, 100)
        self.pocao_vida = Item("Pocao de Vida", "ativo", "vida", 40, True, "comum")
        self.armadura_soldado = Item("Armadura de Soldado", "passivo", "defesa", 15, False, "comum")
        self.bau = Bau(40, 70, 16, 16, [self.disparo_arcano, self.bola_fogo, self.barreira_cristal, self.explosao_arcana], [self.pocao_vida, self.armadura_soldado])
        self.projetil = None
        self.tela_aberta = None
        self.estado_jogo = "menu"
        self.magia_inventario_selecionada = None
        self.item_inventario_selecionado = None
        self.barreira_ativa = False
        self.jogo_pausado = False
        self.tempo_barreira = 0
        self.tempo_mensagem = 0
        self.mensagem_bau = ""
        self.tempo_mensagem_bau = 0
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
        if self.estado_jogo == "menu":
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.estado_jogo = "exploracao"

            return

        if self.mago.vida == 0:
            return

        if pyxel.btnp(pyxel.KEY_P):
            if self.jogo_pausado == False:
                self.jogo_pausado = True
                self.tela_aberta = None
            else:
                self.jogo_pausado = False

        if self.jogo_pausado:
            return

        if pyxel.btnp(pyxel.KEY_I):
            if self.tela_aberta == "itens":
                self.tela_aberta = None
            else:
                self.tela_aberta = "itens"

        if pyxel.btnp(pyxel.KEY_M):
            if self.tela_aberta == "magias":
                self.tela_aberta = None
            else:
                self.tela_aberta = "magias"

        if self.tela_aberta == "magias":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                for i in range(len(self.mago.magias)):
                    inicio_y = 29 + i * 10
                    final_y = 38 + i * 10

                    if pyxel.mouse_x >= 14 and pyxel.mouse_x <= 146:
                        if pyxel.mouse_y >= inicio_y and pyxel.mouse_y <= final_y:
                            self.magia_inventario_selecionada = self.mago.magias[i]

                for espaco in range(4):
                    inicio_x = 89 + espaco * 17
                    final_x = inicio_x + 14

                    if pyxel.mouse_x >= inicio_x and pyxel.mouse_x <= final_x:
                        if pyxel.mouse_y >= 104 and pyxel.mouse_y <= 118:
                            if self.magia_inventario_selecionada != None:
                                for outro_espaco in range(4):
                                    if self.mago.magias_equipadas[outro_espaco] == self.magia_inventario_selecionada:
                                        self.mago.magias_equipadas[outro_espaco] = None

                                self.mago.magias_equipadas[espaco] = self.magia_inventario_selecionada
                                self.mago.magia_selecionada = self.magia_inventario_selecionada

        if self.tela_aberta == "itens":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                for i in range(len(self.mago.inventario)):
                    inicio_y = 29 + i * 10
                    final_y = 38 + i * 10

                    if pyxel.mouse_x >= 14 and pyxel.mouse_x <= 146:
                        if pyxel.mouse_y >= inicio_y and pyxel.mouse_y <= final_y:
                            self.item_inventario_selecionado = self.mago.inventario[i]

                for espaco in range(5):
                    inicio_x = 4 + espaco * 17
                    final_x = inicio_x + 14

                    if pyxel.mouse_x >= inicio_x and pyxel.mouse_x <= final_x:
                        if pyxel.mouse_y >= 104 and pyxel.mouse_y <= 118:
                            if self.item_inventario_selecionado != None:
                                for outro_espaco in range(5):
                                    if self.mago.itens_equipados[outro_espaco] == self.item_inventario_selecionado:
                                        self.mago.itens_equipados[outro_espaco] = None

                                self.mago.itens_equipados[espaco] = self.item_inventario_selecionado
                                self.mago.item_selecionado = self.item_inventario_selecionado
        
        if self.tela_aberta == "bau":
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                for i in range(len(self.bau.magias)):
                    inicio_y = 38 + i * 8
                    final_y = inicio_y + 7

                    if pyxel.mouse_x >= 16 and pyxel.mouse_x <= 146:
                        if pyxel.mouse_y >= inicio_y and pyxel.mouse_y <= final_y:
                            if len(self.mago.magias) < self.mago.capacidade_magias:
                                magia_escolhida = self.bau.magias[i]
                                self.mago.aprenderMagia(magia_escolhida)
                                self.bau.magias.pop(i)
                                self.mensagem_bau = "Magia coletada"
                            else:
                                self.mensagem_bau = "Sem espaco para magias"

                            self.tempo_mensagem_bau = 60
                            break

                for i in range(len(self.bau.itens)):
                    inicio_y = 80 + i * 8
                    final_y = inicio_y + 7

                    if pyxel.mouse_x >= 16 and pyxel.mouse_x <= 146:
                        if pyxel.mouse_y >= inicio_y and pyxel.mouse_y <= final_y:
                            if len(self.mago.inventario) < self.mago.capacidade_inventario:
                                item_escolhido = self.bau.itens[i]
                                self.mago.inventario.append(item_escolhido)
                                self.bau.itens.pop(i)
                                self.mensagem_bau = "Item coletado"
                            else:
                                self.mensagem_bau = "Sem espaco para itens"

                            self.tempo_mensagem_bau = 60
                            break

            if self.tempo_mensagem_bau > 0:
                self.tempo_mensagem_bau -= 1

            if pyxel.btnp(pyxel.KEY_E):
                self.tela_aberta = None

            return

        if self.tela_aberta != None:
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

        if self.mago.y < 20:
            self.mago.y = 20
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

                if self.armadura_soldado in self.mago.inventario:
                    dano_recebido -= dano_recebido * self.armadura_soldado.valor // 100

                if self.barreira_ativa == False:
                    self.mago.modificarVida(-dano_recebido)

                self.encostou_ataque = True

        else:
            self.encostou_ataque = False

        if pyxel.btnp(pyxel.KEY_E):
            if self.colisaoBau():
                self.bau.aberto = True
                self.tela_aberta = "bau"

            elif self.mago.item_selecionado != None:
                if self.mago.item_selecionado.tipo == "ativo":
                    if self.mago.vida < 200:
                        item_usado = self.mago.item_selecionado
                        item_usado.usar(self.mago)

                        if item_usado.consumivel:
                            self.mago.inventario.remove(item_usado)

                            for i in range(5):
                                if self.mago.itens_equipados[i] == item_usado:
                                    self.mago.itens_equipados[i] = None

                            self.mago.item_selecionado = None
                            self.item_inventario_selecionado = None

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
                        self.projetil = ProjetilMagico(self.mago.x + 4, self.mago.y + 4, direcao_x, direcao_y, self.disparo_arcano.dano, 0)
                        self.mago.modificarMana(-self.disparo_arcano.mana)

            elif self.mago.magia_selecionada == self.bola_fogo:
                if self.mago.mana >= self.bola_fogo.mana:
                    distancia_x = pyxel.mouse_x - (self.mago.x + 8)
                    distancia_y = pyxel.mouse_y - (self.mago.y + 8)
                    distancia = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

                    if distancia > 0:
                        direcao_x = distancia_x / distancia
                        direcao_y = distancia_y / distancia
                        self.projetil = ProjetilMagico(self.mago.x + 4, self.mago.y + 4, direcao_x, direcao_y, self.bola_fogo.dano, 32)
                        self.mago.modificarMana(-self.bola_fogo.mana)

            elif self.mago.magia_selecionada == self.barreira_cristal:
                if self.mago.mana >= self.barreira_cristal.mana:
                    self.barreira_ativa = True
                    self.tempo_barreira = 100
                    self.mago.modificarMana(-self.barreira_cristal.mana)

            elif self.mago.magia_selecionada == self.explosao_arcana:
                if self.mago.mana >= self.explosao_arcana.mana:
                    distancia_x = pyxel.mouse_x - (self.mago.x + 8)
                    distancia_y = pyxel.mouse_y - (self.mago.y + 8)
                    distancia = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

                    if distancia > 0:
                        direcao_x = distancia_x / distancia
                        direcao_y = distancia_y / distancia
                        self.projetil = ProjetilMagico(self.mago.x + 4, self.mago.y + 4, direcao_x, direcao_y, self.explosao_arcana.dano, 96)
                        self.mago.modificarMana(-self.explosao_arcana.mana)

        if self.tempo_barreira > 0:
            self.tempo_barreira -= 1
        else:
            self.barreira_ativa = False

        if self.projetil != None:
            self.projetil.mover()

            if self.projetil.x < 0 or self.projetil.x > 144 or self.projetil.y < 20 or self.projetil.y > 86:
                self.projetil = None

            elif self.colisaoProjetil():
                self.inimigo_fake.vida -= self.projetil.dano

                if self.inimigo_fake.vida < 0:
                    self.inimigo_fake.vida = 0

                self.projetil = None
        
        if self.tempo_mensagem > 0:
            self.tempo_mensagem -= 1
    
    def draw(self):
        pyxel.cls(0)

        if self.estado_jogo == "menu":
            pyxel.text(58, 35, "EXIL MAGEED", 10)
            pyxel.text(26, 58, "PRESSIONE ENTER PARA INICIAR", 7)
            pyxel.text(54, 72, "ESC PARA SAIR", 6)
            return

        pyxel.rect(0, 0, 160, 20, 1)

        pyxel.text(2, 2, "V:" + str(int(self.mago.vida)) + " F:" + str(self.mago.forca) + " D:" + str(self.mago.defesa) + " VEL:" + str(self.mago.velocidade), 7)

        pyxel.text(2, 8, "M:" + str(int(self.mago.mana)) + " E:" + str(self.mago.espiritualidade) + "/" + str(self.mago.espiritualidade_maxima) + " ESP:" + str(self.mago.espirito), 7)

        x_imagem = self.mago.sprite_x + self.mago.quadro * 16
        pyxel.blt(self.mago.x, self.mago.y, 0, x_imagem, self.mago.sprite_y, 16, 16, 7)

        if self.barreira_ativa:
            pyxel.blt(self.mago.x, self.mago.y, 1, 0, 64, 16, 16, 0)

        if self.mago.magia_selecionada != None:
            pyxel.text(2, 14, "Magia:" + self.mago.magia_selecionada.nome, 10)
        else:
            pyxel.text(2, 14, "Magia:nenhuma", 7)

        pyxel.rect(self.ataque.x, self.ataque.y, self.ataque.largura, self.ataque.altura, 8)

        pyxel.rect(self.inimigo_fake.x, self.inimigo_fake.y, self.inimigo_fake.largura, self.inimigo_fake.altura, 11)
        pyxel.text(self.inimigo_fake.x, self.inimigo_fake.y - 6, "V:" + str(self.inimigo_fake.vida), 7)

        if self.projetil != None:
            pyxel.blt(self.projetil.x, self.projetil.y, 1, 0, self.projetil.imagem_y, 16, 16, 0)

        if self.bau.aberto == False:
            pyxel.rect(self.bau.x, self.bau.y, self.bau.largura, self.bau.altura, 9)
            if self.colisaoBau():
                pyxel.text(24, 95, "Pressione E para abrir", 7)

        else:
            pyxel.rect(self.bau.x, self.bau.y, self.bau.largura, self.bau.altura, 4)
            if self.tempo_mensagem > 0:
                pyxel.text(24, 95, "Magias iniciais aprendidas", 10)

        pyxel.rect(0, 102, 160, 18, 1)
        for i in range(9):
            x_espaco = 4 + i * 17

            if i < 5:
                if self.mago.item_selecionado != None and self.mago.itens_equipados[i] == self.mago.item_selecionado:
                    cor = 10
                else:
                    cor = 5
            else:
                if self.mago.magias_equipadas[i - 5] == self.mago.magia_selecionada:
                    cor = 10
                else:
                    cor = 13

            pyxel.rect(x_espaco, 104, 15, 14, cor)
            pyxel.text(x_espaco + 5, 108, str(i + 1), 7)

        for i in range(5):
            if self.mago.itens_equipados[i] == self.pocao_vida:
                x_item = 4 + i * 17
                pyxel.blt(x_item, 103, 2, 0, 0, 16, 16, 0, scale=0.7)

        for i in range(4):
            magia = self.mago.magias_equipadas[i]
            imagem_y = None

            if magia == self.disparo_arcano:
                imagem_y = 0
            elif magia == self.bola_fogo:
                imagem_y = 32
            elif magia == self.barreira_cristal:
                imagem_y = 64
            elif magia == self.explosao_arcana:
                imagem_y = 96

            if imagem_y != None:
                x_magia = 89 + i * 17
                pyxel.blt(x_magia, 103, 1, 0, imagem_y, 16, 16, 0, scale=0.7)

        if self.tela_aberta == "magias":
            pyxel.rect(8, 16, 144, 84, 1)
            pyxel.text(35, 21, "INVENTARIO DE MAGIAS", 10)

            for i in range(len(self.mago.magias)):
                if self.magia_inventario_selecionada == self.mago.magias[i]:
                    cor_magia = 10
                else:
                    cor_magia = 7

                pyxel.text(16, 32 + i * 10, str(i + 1) + " - " + self.mago.magias[i].nome, cor_magia)

            pyxel.text(46, 90, "M para fechar", 6)

        if self.tela_aberta == "itens":
            pyxel.rect(8, 16, 144, 84, 1)
            pyxel.text(35, 21, "INVENTARIO DE ITENS", 10)

            if len(self.mago.inventario) == 0:
                pyxel.text(52, 52, "Nenhum item", 7)
            else:
                for i in range(len(self.mago.inventario)):
                    if self.item_inventario_selecionado == self.mago.inventario[i]:
                        cor_item = 10
                    else:
                        if self.mago.inventario[i].raridade == "epico":
                            cor_item = 14
                        elif self.mago.inventario[i].raridade == "raro":
                            cor_item = 12
                        elif self.mago.inventario[i].raridade == "comum":
                            cor_item = 7
                        elif self.mago.inventario[i].raridade == "ruim":
                            cor_item = 9
                        elif self.mago.inventario[i].raridade == "horrivel":
                            cor_item = 8

                    pyxel.text(16, 32 + i * 10, str(i + 1) + " - " + self.mago.inventario[i].nome + " [" + self.mago.inventario[i].raridade + "]", cor_item)

            pyxel.text(48, 90, "I para fechar", 6)

        if self.tela_aberta == "bau":
            pyxel.rect(8, 16, 144, 84, 1)
            pyxel.text(59, 21, "BAU", 10)
            pyxel.text(108, 21, "E: fechar", 6)

            pyxel.text(12, 30, "MAGIAS:", 12)

            for i in range(len(self.bau.magias)):
                pyxel.text(16, 38 + i * 8, self.bau.magias[i].nome, 7)

            pyxel.text(12, 72, "ITENS:", 9)

            for i in range(len(self.bau.itens)):
                pyxel.text(16, 80 + i * 8, self.bau.itens[i].nome, 7)

            if self.tempo_mensagem_bau > 0:
                pyxel.text(16, 94, self.mensagem_bau, 10)

        if self.jogo_pausado:
            pyxel.rect(40, 42, 80, 32, 1)
            pyxel.rectb(40, 42, 80, 32, 7)
            pyxel.text(67, 51, "PAUSADO", 10)
            pyxel.text(48, 63, "P para continuar", 7)

        if self.mago.vida == 0:
            pyxel.cls(0)
            pyxel.text(55, 52, "VOCE MORREU", 8)
            pyxel.text(55, 62, "FIM DE JOGO", 7)
        
Jogo()
