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
    def __init__(self, nome, tipo, efeito, valor, consumivel, raridade, duracao):
        self.nome = nome
        self.tipo = tipo
        self.efeito = efeito
        self.valor = valor
        self.consumivel = consumivel
        self.raridade = raridade
        self.duracao = duracao

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
    def __init__(self, nome, vida, forca, defesa, velocidade, sorte, espirito, x, y, largura, altura):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.defesa = defesa
        self.velocidade = velocidade
        self.sorte = sorte
        self.espirito = espirito
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.x_inicial = x
        self.y_inicial = y
        self.quadro = 0
        self.tempo_animacao = 0
        self.tempo_movimento = 0
        self.estado = "patrulha"
        self.raio_deteccao = 25
        self.tempo_busca = 0
        self.tempo_congelado = 0
        self.tempo_porta = 0
        self.passando_porta = False
        self.estado_anterior = None
        self.ultimo_x_jogador = x
        self.ultimo_y_jogador = y
        self.chegou_ultima_posicao = False
        self.direcao_busca = 0
        self.passos_busca = 0
    
    def modificarVida(self, modificacao):
        self.vida += modificacao

        if self.vida < 0:
            self.vida = 0

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

class DrenagemForca:
    def __init__(self, x, y, largura, altura, quantidade):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.quantidade = quantidade

class Parede:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

class Arbusto:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

class Porta:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.aberta = False
        self.tempo_atraso = 60

class Bau:
    def __init__(self, x, y, largura, altura, tipo, conteudo, capacidade):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.tipo = tipo
        self.conteudo = conteudo
        self.aberto = False
        self.capacidade = capacidade

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
        pyxel.images[0].load(0, 32, "lutador_demoniaco.png")
        pyxel.images[1].load(0, 0, "disparo_arcano.png")
        pyxel.images[1].load(0, 32, "bola_fogo.png")
        pyxel.images[1].load(0, 64, "barreira_cristal.png")
        pyxel.images[1].load(0, 96, "explosao_arcana.png")
        pyxel.images[1].load(0, 128, "correntes_abismo.png")
        pyxel.images[2].load(0, 0, "pocao_vida.png")
        pyxel.images[2].load(0, 16, "armadura_soldado.png")
        pyxel.images[2].load(0, 32, "coracao_tita.png")
        pyxel.images[2].load(0, 48, "pele_montanha.png")
        pyxel.images[2].load(0, 64, "bau.png")
        pyxel.images[2].load(16, 0, "carta.png")

        self.paleta_original = [pyxel.colors[i] for i in range(16)]
        self.paleta_floresta = self.paleta_original.copy()

        self.paleta_floresta[2] = 0x123A2A
        self.paleta_floresta[3] = 0x244729
        self.paleta_floresta[4] = 0x784C43
        self.paleta_floresta[8] = 0x1C5B2A
        self.paleta_floresta[11] = 0x1EAF52
        self.paleta_floresta[12] = 0x64FF61
        self.paleta_floresta[14] = 0x9EE837

        for i in range(16):
            pyxel.colors[i] = self.paleta_floresta[i]

        pyxel.images[2].load(0, 96, "fundo_floresta_prologo.png")

        for i in range(16):
            pyxel.colors[i] = self.paleta_original[i]

        self.mago = Jogador("Exil Mageed", 200, 50, 100, 40, 30, 10, 40, 100, 100, 10, 10, [], [], 72, 86)
        self.disparo_arcano = Magia("Disparo Arcano", 20, 10, 20, 50, 1, 1, 100)
        self.bola_fogo = Magia("Bola de Fogo", 35, 20, 30, 45, 2, 1, 100)
        self.barreira_cristal = Magia("Barreira de Cristal", 0, 25, 60, 0, 3, 1, 100)
        self.explosao_arcana = Magia("Explosao Arcana", 50, 35, 70, 0, 4, 1, 100)
        self.correntes_abismo = Magia("Correntes do Abismo", 0, 20, 60, 50, 1, 1, 100)
        self.pocao_vida = Item("Pocao de Vida", "ativo", "vida", 40, True, "comum", 0)
        self.armadura_soldado = Item("Armadura de Soldado", "passivo", "defesa", 15, False, "comum", 0)
        self.coracao_tita = Item("Coracao do Tita", "ativo", "forca", 50, True, "epico", 300)
        self.pele_montanha = Item("Pele da Montanha", "ativo", "defesa", 60, True, "epico", 300)
        self.bau_magias = Bau(35, 70, 16, 16, "magias", [self.disparo_arcano, self.bola_fogo, self.barreira_cristal, self.explosao_arcana, self.correntes_abismo], 6)
        self.bau_itens = Bau(70, 70, 16, 16, "itens", [self.pocao_vida, self.armadura_soldado, self.coracao_tita, self.pele_montanha], 6)
        self.baus = [self.bau_magias, self.bau_itens]
        self.carta_prologo = Item("Carta", "especial", "historia", 0, False, "comum", 0)
        self.paginas_carta = [
            [
                "Toda sua familia foi assassinada.",
                "Quando voce acordou, ja era tarde.",
                "Voce nao conseguiu proteger eles",
                "que eram pessoas que mais amava.",
                "Desde aquele dia, um vazio ficou",
                "dentro de voce e a busca por",
                "poder se tornou sua unica saida."
            ],
            [
                "Buscando poder, voce descobriu a",
                "existencia do Pergaminho Proibido,",
                "que diz conter magias capazes de",
                "ultrapassar os limites mortais.",
                "Ao tentar encontrar, voce foi",
                "banido dos reinos dos vampiros",
                "e dos demonios."
            ],
            [
                "O pergaminho esta no reino dos",
                "demonios, mas atacalos agora",
                "seria praticamente impossivel.",
                "Por isso, e melhor invadir",
                "primeiro o reino dos vampiros,",
                "pra conseguir magias e itens",
                "pra ficar mais forte."
            ],
            [
                "Depois, voce deve ir no reino dos",
                "demonios em busca do pergaminho.",
                "Seu objetivo e conseguir poder",
                "suficiente para preencher o vazio",
                "que ficou depois da morte da sua",
                "familia. Mas ate onde voce esta",
                "disposto a ir pra conseguir isso?"
            ]
        ]

        self.pagina_carta = 0
        self.bau_prologo = Bau(72, 45, 16, 16, "itens", [self.carta_prologo], 6)
        self.bau_aberto = None
        self.modo_bau = "retirar"
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
        self.tempo_coracao_tita = 0
        self.aumento_coracao_tita = 0
        self.tempo_pele_montanha = 0
        self.aumento_pele_montanha = 0
        self.tempo_efeito_correntes = 0
        self.ataque = Ataque(100, 70, 16, 16, 20)
        self.drenagem_forca = DrenagemForca(130, 70, 16, 16, 10)
        self.parede = Parede(75, 20, 3, 32)
        self.arbusto = Arbusto(55, 45, 16, 16)
        self.porta = Porta(25, 45, 3, 32)
        self.encostou_ataque = False
        self.encostou_drenagem = False
        self.lutador_demoniaco = Inimigo("Lutador Demoniaco", 240, 65, 55, 65, 35, 80, 120, 35, 16, 16)
        self.lutador_demoniaco.tipo = "demonio"
        pyxel.run(self.update, self.draw)

    def paredeBloqueiaVisao(self):
        centro_mago_x = self.mago.x + 8
        centro_mago_y = self.mago.y + 8
        centro_inimigo_x = self.lutador_demoniaco.x + 8
        centro_inimigo_y = self.lutador_demoniaco.y + 8

        mago_na_esquerda = centro_mago_x < self.parede.x
        inimigo_na_esquerda = centro_inimigo_x < self.parede.x

        if mago_na_esquerda == inimigo_na_esquerda:
            return False

        distancia_x = centro_mago_x - centro_inimigo_x
        distancia_ate_parede = self.parede.x - centro_inimigo_x
        parte_do_caminho = distancia_ate_parede / distancia_x

        altura_da_visao = centro_inimigo_y + (centro_mago_y - centro_inimigo_y) * parte_do_caminho

        if altura_da_visao >= self.parede.y and altura_da_visao <= self.parede.y + self.parede.altura:
            return True
        else:
            return False

    def arbustoBloqueiaVisao(self):
        centro_mago_x = self.mago.x + 8
        centro_mago_y = self.mago.y + 8
        centro_inimigo_x = self.lutador_demoniaco.x + 8
        centro_inimigo_y = self.lutador_demoniaco.y + 8

        if centro_mago_x >= self.arbusto.x and centro_mago_x <= self.arbusto.x + self.arbusto.largura:
            if centro_mago_y >= self.arbusto.y and centro_mago_y <= self.arbusto.y + self.arbusto.altura:
                return True

        distancia_x = centro_mago_x - centro_inimigo_x
        distancia_y = centro_mago_y - centro_inimigo_y
        distancia = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

        if distancia == 0:
            return False

        for passo in range(int(distancia) + 1):
            ponto_x = centro_inimigo_x + distancia_x * passo / distancia
            ponto_y = centro_inimigo_y + distancia_y * passo / distancia

            if ponto_x >= self.arbusto.x and ponto_x <= self.arbusto.x + self.arbusto.largura:
                if ponto_y >= self.arbusto.y and ponto_y <= self.arbusto.y + self.arbusto.altura:
                    return True

        return False

    def colisaoParede(self, personagem):
        colisaoX = personagem.x + 12 > self.parede.x and personagem.x + 4 < self.parede.x + self.parede.largura
        colisaoY = personagem.y + 14 > self.parede.y and personagem.y + 4 < self.parede.y + self.parede.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def colisaoArbusto(self, personagem):
        colisaoX = personagem.x + 12 > self.arbusto.x and personagem.x + 4 < self.arbusto.x + self.arbusto.largura
        colisaoY = personagem.y + 14 > self.arbusto.y and personagem.y + 4 < self.arbusto.y + self.arbusto.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def colisaoPorta(self, personagem):
        colisaoX = personagem.x + 12 > self.porta.x and personagem.x + 4 < self.porta.x + self.porta.largura
        colisaoY = personagem.y + 14 > self.porta.y and personagem.y + 4 < self.porta.y + self.porta.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def colisaoAtaque(self):
        colisaoX = self.mago.x + 16 >= self.ataque.x and self.mago.x <= self.ataque.x + self.ataque.largura
        colisaoY = self.mago.y + 16 >= self.ataque.y and self.mago.y <= self.ataque.y + self.ataque.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def colisaoDrenagemForca(self):
        colisaoX = self.mago.x + 16 >= self.drenagem_forca.x and self.mago.x <= self.drenagem_forca.x + self.drenagem_forca.largura
        colisaoY = self.mago.y + 16 >= self.drenagem_forca.y and self.mago.y <= self.drenagem_forca.y + self.drenagem_forca.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def atualizarCapacidadeInventario(self):
        if self.mago.forca >= 50:
            self.mago.capacidade_inventario = 10
        elif self.mago.forca >= 40:
            self.mago.capacidade_inventario = 8
        elif self.mago.forca >= 30:
            self.mago.capacidade_inventario = 6
        elif self.mago.forca >= 20:
            self.mago.capacidade_inventario = 4
        elif self.mago.forca >= 10:
            self.mago.capacidade_inventario = 2
        else:
            self.mago.capacidade_inventario = 1

    def colisaoBau(self, bau):
        colisaoX = self.mago.x + 16 >= bau.x and self.mago.x <= bau.x + bau.largura
        colisaoY = self.mago.y + 16 >= bau.y and self.mago.y <= bau.y + bau.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def pertoBau(self, bau):
        margem = 4

        colisaoX = self.mago.x + 16 + margem >= bau.x and self.mago.x - margem <= bau.x + bau.largura
        colisaoY = self.mago.y + 16 + margem >= bau.y and self.mago.y - margem <= bau.y + bau.altura

        return colisaoX and colisaoY

    def colisaoProjetil(self):
        if self.lutador_demoniaco.vida == 0:
            return False

        colisaoX = self.projetil.x + 16 >= self.lutador_demoniaco.x and self.projetil.x <= self.lutador_demoniaco.x + self.lutador_demoniaco.largura
        colisaoY = self.projetil.y + 16 >= self.lutador_demoniaco.y and self.projetil.y <= self.lutador_demoniaco.y + self.lutador_demoniaco.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def atualizarBau(self):
        if self.tela_aberta == "bau":
            if self.bau_aberto != None:
                if self.bau_aberto.tipo == "itens":
                    if pyxel.btnp(pyxel.KEY_G):
                        if self.modo_bau == "retirar":
                            self.modo_bau = "guardar"
                        else:
                            self.modo_bau = "retirar"

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if self.bau_aberto != None:
                    if self.modo_bau == "retirar":
                        for i in range(len(self.bau_aberto.conteudo)):
                            inicio_y = 38 + i * 10
                            final_y = inicio_y + 7

                            if pyxel.mouse_x >= 16 and pyxel.mouse_x <= 146:
                                if pyxel.mouse_y >= inicio_y and pyxel.mouse_y <= final_y:
                                    conteudo_escolhido = self.bau_aberto.conteudo[i]

                                    if self.bau_aberto.tipo == "magias":
                                        if len(self.mago.magias) < self.mago.capacidade_magias:
                                            self.mago.aprenderMagia(conteudo_escolhido)
                                            self.bau_aberto.conteudo.pop(i)
                                            self.mensagem_bau = "Magia coletada"
                                        else:
                                            self.mensagem_bau = "Sem espaco para magias"

                                    elif self.bau_aberto.tipo == "itens":
                                        if len(self.mago.inventario) < self.mago.capacidade_inventario:
                                            self.mago.inventario.append(conteudo_escolhido)
                                            self.bau_aberto.conteudo.pop(i)
                                            self.mensagem_bau = "Item coletado"
                                        else:
                                            self.mensagem_bau = "Sem espaco para itens"

                                    self.tempo_mensagem_bau = 60
                                    break

                    elif self.modo_bau == "guardar":
                        if self.bau_aberto.tipo == "itens":
                            for i in range(len(self.mago.inventario)):
                                inicio_y = 38 + i * 10
                                final_y = inicio_y + 7

                                if pyxel.mouse_x >= 16 and pyxel.mouse_x <= 146:
                                    if pyxel.mouse_y >= inicio_y and pyxel.mouse_y <= final_y:
                                        item_guardado = self.mago.inventario[i]

                                        if len(self.bau_aberto.conteudo) < self.bau_aberto.capacidade:
                                            self.bau_aberto.conteudo.append(item_guardado)
                                            self.mago.inventario.pop(i)

                                            for espaco in range(5):
                                                if self.mago.itens_equipados[espaco] == item_guardado:
                                                    self.mago.itens_equipados[espaco] = None

                                            if self.mago.item_selecionado == item_guardado:
                                                self.mago.item_selecionado = None

                                            if self.item_inventario_selecionado == item_guardado:
                                                self.item_inventario_selecionado = None

                                            self.mensagem_bau = "Item guardado"
                                        else:
                                            self.mensagem_bau = "Bau cheio"

                                        self.tempo_mensagem_bau = 60
                                        break

            if self.tempo_mensagem_bau > 0:
                self.tempo_mensagem_bau -= 1

            if pyxel.btnp(pyxel.KEY_E):
                if self.bau_aberto != None:
                    self.bau_aberto.aberto = False

                self.tela_aberta = None
                self.bau_aberto = None

            return

    def atualizarInventario(self):

        if len(self.mago.inventario) > self.mago.capacidade_inventario:
            self.tela_aberta = "itens"

        if pyxel.btnp(pyxel.KEY_I):
            if self.tela_aberta == "itens":
                if len(self.mago.inventario) <= self.mago.capacidade_inventario:
                    self.tela_aberta = None
            else:
                self.tela_aberta = "itens"

        if pyxel.btnp(pyxel.KEY_M):
            if len(self.mago.inventario) <= self.mago.capacidade_inventario:
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

            if pyxel.btnp(pyxel.KEY_X):
                if self.magia_inventario_selecionada != None:
                    magia_excluida = self.magia_inventario_selecionada

                    for i in range(4):
                        if self.mago.magias_equipadas[i] == magia_excluida:
                            self.mago.magias_equipadas[i] = None

                    if self.mago.magia_selecionada == magia_excluida:
                        self.mago.magia_selecionada = None

                    self.mago.magias.remove(magia_excluida)
                    self.magia_inventario_selecionada = None

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

            if pyxel.btnp(pyxel.KEY_X):
                if self.item_inventario_selecionado != None:
                    item_excluido = self.item_inventario_selecionado

                    for i in range(5):
                        if self.mago.itens_equipados[i] == item_excluido:
                            self.mago.itens_equipados[i] = None

                    if self.mago.item_selecionado == item_excluido:
                        self.mago.item_selecionado = None

                    self.mago.inventario.remove(item_excluido)
                    self.item_inventario_selecionado = None

            if pyxel.btnp(pyxel.KEY_E):
                if self.item_inventario_selecionado == self.carta_prologo:
                    self.tela_aberta = "carta"

    def atualizarMovimentoMago(self):
        x_anterior_mago = self.mago.x
        y_anterior_mago = self.mago.y

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

        if self.estado_jogo == "prologo":
            baus_colisao = [self.bau_prologo]
        else:
            baus_colisao = self.baus

        for bau in baus_colisao:
            colisaoX = self.mago.x + 12 > bau.x and self.mago.x + 4 < bau.x + bau.largura
            colisaoY = self.mago.y + 14 > bau.y and self.mago.y + 4 < bau.y + bau.altura

            if colisaoX and colisaoY:
                self.mago.x = x_anterior_mago
                self.mago.y = y_anterior_mago
                break

        if self.mago.movendo:
            self.mago.tempo_animacao += 1

            if self.mago.tempo_animacao == 6:
                self.mago.quadro = (self.mago.quadro + 1) % 4
                self.mago.tempo_animacao = 0
        else:
            self.mago.quadro = 0
            self.mago.tempo_animacao = 0

    def atualizarHotbar(self):
        if self.tela_aberta != None or self.jogo_pausado == True:
            return

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
        
    def update(self):
        if self.tela_aberta == "carta":
            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.pagina_carta < len(self.paginas_carta) - 1:
                    self.pagina_carta += 1
                else:
                    self.tela_aberta = None

            return

        if self.estado_jogo == "menu":
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.estado_jogo = "prologo"

            return

        self.atualizarHotbar()

        if self.estado_jogo == "prologo":
            if self.tela_aberta == "bau":
                self.atualizarBau()
                return

            self.atualizarInventario()

            if self.tela_aberta != None:
                return

            if pyxel.btnp(pyxel.KEY_RETURN):
                self.estado_jogo = "exploracao"
                return

            if pyxel.btnp(pyxel.KEY_E):
                if self.pertoBau(self.bau_prologo):
                    self.bau_prologo.aberto = True
                    self.bau_aberto = self.bau_prologo
                    self.tela_aberta = "bau"
                    self.modo_bau = "retirar"
                    return

                elif self.mago.item_selecionado == self.carta_prologo:
                    self.pagina_carta = 0
                    self.tela_aberta = "carta"
                    return

            self.atualizarMovimentoMago()

            self.mago.x = max(0, min(144, self.mago.x))
            self.mago.y = max(20, min(86, self.mago.y))

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

        self.atualizarInventario()
        
        if self.tela_aberta == "bau":
            self.atualizarBau()
            return

        if self.tela_aberta != None:
            return
        
        self.mago.modificarMana(0.05)
        self.mago.modificarVida(0.005)

        if self.tempo_coracao_tita > 0:
            self.tempo_coracao_tita -= 1

            if self.tempo_coracao_tita == 0:
                self.mago.forca -= self.aumento_coracao_tita
                self.aumento_coracao_tita = 0

        if self.tempo_pele_montanha > 0:
            self.tempo_pele_montanha -= 1

        x_anterior_mago = self.mago.x
        y_anterior_mago = self.mago.y

        self.atualizarMovimentoMago()

        if self.colisaoParede(self.mago):
            self.mago.x = x_anterior_mago
            self.mago.y = y_anterior_mago

        if self.mago.x < -4:
            self.mago.x = -4
        elif self.mago.x > 148:
            self.mago.x = 148

        if self.mago.y < 20:
            self.mago.y = 20
        elif self.mago.y > 88:
            self.mago.y = 88

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

                if self.tempo_pele_montanha > 0:
                    dano_recebido -= dano_recebido * self.pele_montanha.valor // 100

                if self.barreira_ativa == False:
                    self.mago.modificarVida(-dano_recebido)

                self.encostou_ataque = True

        else:
            self.encostou_ataque = False

        if self.colisaoDrenagemForca():
            if self.encostou_drenagem == False:
                self.mago.modificarForca(-self.drenagem_forca.quantidade)
                self.encostou_drenagem = True
        else:
            self.encostou_drenagem = False

        self.atualizarCapacidadeInventario()

        if pyxel.btnp(pyxel.KEY_E):
            abriu_bau = False

            for bau in self.baus:
                if self.pertoBau(bau):
                    bau.aberto = True
                    self.bau_aberto = bau
                    self.tela_aberta = "bau"
                    self.modo_bau = "retirar"
                    abriu_bau = True
                    break

            if abriu_bau == False:
                if self.mago.item_selecionado != None:
                    if self.mago.item_selecionado.tipo == "ativo":
                        item_usado = self.mago.item_selecionado
                        item_foi_usado = False

                        if item_usado == self.pocao_vida:
                            if self.mago.vida < 200:
                                item_usado.usar(self.mago)
                                item_foi_usado = True

                        elif item_usado == self.coracao_tita:
                            if self.tempo_coracao_tita == 0:
                                self.aumento_coracao_tita = self.mago.forca * item_usado.valor // 100
                                self.mago.forca += self.aumento_coracao_tita
                                self.tempo_coracao_tita = item_usado.duracao
                                item_foi_usado = True

                        elif item_usado == self.pele_montanha:
                            if self.tempo_pele_montanha == 0:
                                self.tempo_pele_montanha = item_usado.duracao
                                item_foi_usado = True

                        if item_foi_usado:
                            if item_usado.consumivel:
                                self.mago.inventario.remove(item_usado)

                                for i in range(5):
                                    if self.mago.itens_equipados[i] == item_usado:
                                        self.mago.itens_equipados[i] = None

                                self.mago.item_selecionado = None
                                self.item_inventario_selecionado = None

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

            elif self.mago.magia_selecionada == self.correntes_abismo:
                if self.mago.mana >= self.correntes_abismo.mana:
                    if self.lutador_demoniaco.vida > 0:
                        distancia_x = self.mago.x - self.lutador_demoniaco.x
                        distancia_y = self.mago.y - self.lutador_demoniaco.y
                        distancia = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

                        if distancia <= self.correntes_abismo.alcance:
                            self.lutador_demoniaco.estado_anterior = self.lutador_demoniaco.estado
                            self.lutador_demoniaco.estado = "congelado"
                            self.lutador_demoniaco.tempo_congelado = 300
                            self.mago.modificarMana(-self.correntes_abismo.mana)
                            self.tempo_efeito_correntes = 15

        if self.tempo_barreira > 0:
            self.tempo_barreira -= 1
        else:
            self.barreira_ativa = False

        if self.tempo_efeito_correntes > 0:
            self.tempo_efeito_correntes -= 1

        x_anterior_inimigo = self.lutador_demoniaco.x
        y_anterior_inimigo = self.lutador_demoniaco.y

        distancia_x = self.mago.x - self.lutador_demoniaco.x
        distancia_y = self.mago.y - self.lutador_demoniaco.y
        distancia_jogador = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

        if pyxel.btnp(pyxel.KEY_C):
            self.lutador_demoniaco.estado_anterior = self.lutador_demoniaco.estado
            self.lutador_demoniaco.estado = "congelado"
            self.lutador_demoniaco.tempo_congelado = 90

        if self.lutador_demoniaco.estado == "patrulha":
            if distancia_jogador <= self.lutador_demoniaco.raio_deteccao and self.paredeBloqueiaVisao() == False and self.arbustoBloqueiaVisao() == False:
                self.lutador_demoniaco.estado = "perseguicao"

        elif self.lutador_demoniaco.estado == "perseguicao":
            if distancia_jogador > self.lutador_demoniaco.raio_deteccao or self.paredeBloqueiaVisao() == True or self.arbustoBloqueiaVisao() == True:
                self.lutador_demoniaco.estado = "busca"
                self.lutador_demoniaco.tempo_busca = 300 - self.mago.sorte * 2
                self.lutador_demoniaco.tempo_movimento = 0
                self.lutador_demoniaco.chegou_ultima_posicao = False
                self.lutador_demoniaco.direcao_busca = 0
                self.lutador_demoniaco.passos_busca = 0

            else:
                self.lutador_demoniaco.ultimo_x_jogador = self.mago.x
                self.lutador_demoniaco.ultimo_y_jogador = self.mago.y

                self.lutador_demoniaco.tempo_movimento += 1

                if self.lutador_demoniaco.tempo_movimento == 2:

                    self.lutador_demoniaco.tempo_movimento = 0

                    if self.mago.x < self.lutador_demoniaco.x:
                        self.lutador_demoniaco.x -= 1
                    elif self.mago.x > self.lutador_demoniaco.x:
                        self.lutador_demoniaco.x += 1

                    if self.mago.y < self.lutador_demoniaco.y:
                        self.lutador_demoniaco.y -= 1
                    elif self.mago.y > self.lutador_demoniaco.y:
                        self.lutador_demoniaco.y += 1

        elif self.lutador_demoniaco.estado == "busca":
            if distancia_jogador <= self.lutador_demoniaco.raio_deteccao and self.paredeBloqueiaVisao() == False and self.arbustoBloqueiaVisao() == False:
                self.lutador_demoniaco.estado = "perseguicao"
                self.lutador_demoniaco.tempo_busca = 0

            else:
                if self.lutador_demoniaco.tempo_busca > 0:
                    self.lutador_demoniaco.tempo_busca -= 1
                    self.lutador_demoniaco.tempo_movimento += 1

                    if self.lutador_demoniaco.tempo_movimento == 2:
                        self.lutador_demoniaco.tempo_movimento = 0

                        if self.lutador_demoniaco.chegou_ultima_posicao == False:
                            if self.lutador_demoniaco.x < self.lutador_demoniaco.ultimo_x_jogador:
                                self.lutador_demoniaco.x += 1
                            elif self.lutador_demoniaco.x > self.lutador_demoniaco.ultimo_x_jogador:
                                self.lutador_demoniaco.x -= 1

                            if self.lutador_demoniaco.y < self.lutador_demoniaco.ultimo_y_jogador:
                                self.lutador_demoniaco.y += 1
                            elif self.lutador_demoniaco.y > self.lutador_demoniaco.ultimo_y_jogador:
                                self.lutador_demoniaco.y -= 1

                            if self.lutador_demoniaco.x == self.lutador_demoniaco.ultimo_x_jogador and self.lutador_demoniaco.y == self.lutador_demoniaco.ultimo_y_jogador:
                                self.lutador_demoniaco.chegou_ultima_posicao = True

                        else:
                            if self.lutador_demoniaco.direcao_busca == 0:
                                self.lutador_demoniaco.x += 1
                            elif self.lutador_demoniaco.direcao_busca == 1:
                                self.lutador_demoniaco.y += 1
                            elif self.lutador_demoniaco.direcao_busca == 2:
                                self.lutador_demoniaco.x -= 1
                            else:
                                self.lutador_demoniaco.y -= 1

                            self.lutador_demoniaco.passos_busca += 1

                            if self.lutador_demoniaco.passos_busca == 10:
                                self.lutador_demoniaco.passos_busca = 0
                                self.lutador_demoniaco.direcao_busca += 1

                                if self.lutador_demoniaco.direcao_busca > 3:
                                    self.lutador_demoniaco.direcao_busca = 0

                else:
                    self.lutador_demoniaco.estado = "retorno"

        elif self.lutador_demoniaco.estado == "retorno":
            if distancia_jogador <= self.lutador_demoniaco.raio_deteccao:
                self.lutador_demoniaco.estado = "perseguicao"

            else:
                self.lutador_demoniaco.tempo_movimento += 1

                if self.lutador_demoniaco.tempo_movimento == 2:
                    self.lutador_demoniaco.tempo_movimento = 0

                    if self.lutador_demoniaco.x < self.lutador_demoniaco.x_inicial:
                        self.lutador_demoniaco.x += 1
                    elif self.lutador_demoniaco.x > self.lutador_demoniaco.x_inicial:
                        self.lutador_demoniaco.x -= 1

                    if self.lutador_demoniaco.y < self.lutador_demoniaco.y_inicial:
                        self.lutador_demoniaco.y += 1
                    elif self.lutador_demoniaco.y > self.lutador_demoniaco.y_inicial:
                        self.lutador_demoniaco.y -= 1

                if self.lutador_demoniaco.x == self.lutador_demoniaco.x_inicial and self.lutador_demoniaco.y == self.lutador_demoniaco.y_inicial:
                    self.lutador_demoniaco.estado = "patrulha"

        elif self.lutador_demoniaco.estado == "congelado":
            if self.lutador_demoniaco.tempo_congelado > 0:
                self.lutador_demoniaco.tempo_congelado -= 1
            else:
                if self.lutador_demoniaco.estado_anterior == "perseguicao":
                    if distancia_jogador <= self.lutador_demoniaco.raio_deteccao and self.paredeBloqueiaVisao() == False:
                        self.lutador_demoniaco.estado = "perseguicao"
                    else:
                        self.lutador_demoniaco.estado = "busca"
                        self.lutador_demoniaco.tempo_busca = 300 - self.mago.sorte * 2
                        self.lutador_demoniaco.tempo_movimento = 0
                        self.lutador_demoniaco.chegou_ultima_posicao = False
                        self.lutador_demoniaco.direcao_busca = 0
                        self.lutador_demoniaco.passos_busca = 0
                else:
                    self.lutador_demoniaco.estado = self.lutador_demoniaco.estado_anterior

        if self.colisaoParede(self.lutador_demoniaco):
            novo_x_inimigo = self.lutador_demoniaco.x
            novo_y_inimigo = self.lutador_demoniaco.y

            self.lutador_demoniaco.y = y_anterior_inimigo

            if self.colisaoParede(self.lutador_demoniaco):
                self.lutador_demoniaco.x = x_anterior_inimigo
            else:
                self.lutador_demoniaco.x = novo_x_inimigo

            self.lutador_demoniaco.y = novo_y_inimigo
            self.lutador_demoniaco.x = x_anterior_inimigo

            if self.colisaoParede(self.lutador_demoniaco):
                self.lutador_demoniaco.y = y_anterior_inimigo
            else:
                self.lutador_demoniaco.y = novo_y_inimigo

        if self.lutador_demoniaco.vida > 0:

            if self.colisaoParede(self.lutador_demoniaco):
                novo_x_inimigo = self.lutador_demoniaco.x
                novo_y_inimigo = self.lutador_demoniaco.y

                self.lutador_demoniaco.y = y_anterior_inimigo

                if self.colisaoParede(self.lutador_demoniaco):
                    self.lutador_demoniaco.x = x_anterior_inimigo
                else:
                    self.lutador_demoniaco.x = novo_x_inimigo

                self.lutador_demoniaco.y = novo_y_inimigo
                self.lutador_demoniaco.x = x_anterior_inimigo

                if self.colisaoParede(self.lutador_demoniaco):
                    self.lutador_demoniaco.y = y_anterior_inimigo
                else:
                    self.lutador_demoniaco.y = novo_y_inimigo

        if self.colisaoArbusto(self.lutador_demoniaco):
            novo_x_inimigo = self.lutador_demoniaco.x
            novo_y_inimigo = self.lutador_demoniaco.y

            self.lutador_demoniaco.y = y_anterior_inimigo

            if self.colisaoArbusto(self.lutador_demoniaco):
                self.lutador_demoniaco.x = x_anterior_inimigo
            else:
                self.lutador_demoniaco.x = novo_x_inimigo

            self.lutador_demoniaco.y = novo_y_inimigo
            self.lutador_demoniaco.x = x_anterior_inimigo

            if self.colisaoArbusto(self.lutador_demoniaco):
                self.lutador_demoniaco.y = y_anterior_inimigo
            else:
                self.lutador_demoniaco.y = novo_y_inimigo

        if self.lutador_demoniaco.tipo == "vampiro":
            if self.colisaoPorta(self.lutador_demoniaco):
                self.lutador_demoniaco.x = x_anterior_inimigo
                self.lutador_demoniaco.y = y_anterior_inimigo

        else:
            if self.lutador_demoniaco.passando_porta == True:
                if self.colisaoPorta(self.lutador_demoniaco) == False:
                    self.lutador_demoniaco.passando_porta = False
                    self.lutador_demoniaco.tempo_porta = 0

            else:
                if self.colisaoPorta(self.lutador_demoniaco):
                    if self.lutador_demoniaco.tempo_porta < 60:
                        self.lutador_demoniaco.tempo_porta += 1
                        self.lutador_demoniaco.x = x_anterior_inimigo
                        self.lutador_demoniaco.y = y_anterior_inimigo
                    else:
                        self.lutador_demoniaco.passando_porta = True

        if self.lutador_demoniaco.x < 0:
            self.lutador_demoniaco.x = 0
        elif self.lutador_demoniaco.x > 144:
            self.lutador_demoniaco.x = 144

        if self.lutador_demoniaco.y < 20:
            self.lutador_demoniaco.y = 20
        elif self.lutador_demoniaco.y > 86:
            self.lutador_demoniaco.y = 86

        if self.lutador_demoniaco.vida > 0:
            self.lutador_demoniaco.tempo_animacao += 1

            if self.lutador_demoniaco.tempo_animacao == 8:
                self.lutador_demoniaco.quadro += 1
                self.lutador_demoniaco.tempo_animacao = 0

                if self.lutador_demoniaco.quadro > 3:
                    self.lutador_demoniaco.quadro = 0

        

        if self.projetil != None:
            self.projetil.mover()

            if self.projetil.x < 0 or self.projetil.x > 144 or self.projetil.y < 20 or self.projetil.y > 86:
                self.projetil = None

            elif self.colisaoProjetil():
                self.lutador_demoniaco.modificarVida(-self.projetil.dano)
                self.projetil = None
        
        if self.tempo_mensagem > 0:
            self.tempo_mensagem -= 1
    
    def draw(self):
        if self.estado_jogo == "prologo":
            for i in range(16):
                pyxel.colors[i] = self.paleta_floresta[i]
        else:
            for i in range(16):
                pyxel.colors[i] = self.paleta_original[i]
        pyxel.cls(0)

        if self.estado_jogo == "menu":
            pyxel.text(58, 35, "EXIL MAGEED", 10)
            pyxel.text(26, 58, "PRESSIONE ENTER PARA INICIAR", 7)
            pyxel.text(54, 72, "ESC PARA SAIR", 6)
            return

        if self.estado_jogo == "prologo":
            pyxel.pal(1, 11)
            pyxel.blt(0, 20, 2, 0, 96, 160, 82, 0)
            pyxel.pal()

        pyxel.rect(0, 0, 160, 20, 1)

        pyxel.text(2, 2, "V:" + str(int(self.mago.vida)) + " F:" + str(self.mago.forca) + " D:" + str(self.mago.defesa) + " VEL:" + str(self.mago.velocidade), 7)

        pyxel.text(2, 8, "M:" + str(int(self.mago.mana)) + " E:" + str(self.mago.espiritualidade) + "/" + str(self.mago.espiritualidade_maxima) + " ESP:" + str(self.mago.espirito), 7)

        x_imagem = self.mago.sprite_x + self.mago.quadro * 16
        pyxel.blt(self.mago.x, self.mago.y, 0, x_imagem, self.mago.sprite_y, 16, 16, 7)

        if self.tempo_efeito_correntes > 0:
            pyxel.circb(self.mago.x + 8, self.mago.y + 8, self.correntes_abismo.alcance, 12)

        if self.barreira_ativa:
            pyxel.blt(self.mago.x, self.mago.y, 1, 0, 64, 16, 16, 0)

        if self.mago.magia_selecionada != None:
            pyxel.text(2, 14, "Magia:" + self.mago.magia_selecionada.nome, 10)
        else:
            pyxel.text(2, 14, "Magia:nenhuma", 7)

        if self.estado_jogo == "prologo":
            if self.bau_prologo.aberto == False:
                imagem_x = 0
                imagem_y = 64
            else:
                imagem_x = 16
                imagem_y = 80

            pyxel.blt(
                self.bau_prologo.x,
                self.bau_prologo.y,
                2,
                imagem_x,
                imagem_y,
                16,
                16,
                0
            )

            if self.tela_aberta == None and self.pertoBau(self.bau_prologo):
                if self.bau_prologo.aberto == False:
                    pyxel.text(24, 95, "Pressione E para abrir", 7)
                else:
                    pyxel.text(40, 95, "Carta encontrada!", 10)

        if self.estado_jogo != "prologo":
            pyxel.rect(self.ataque.x, self.ataque.y, self.ataque.largura, self.ataque.altura, 8)
            pyxel.rect(self.drenagem_forca.x, self.drenagem_forca.y, self.drenagem_forca.largura, self.drenagem_forca.altura, 11)

            pyxel.rect(self.parede.x, self.parede.y, self.parede.largura, self.parede.altura, 6)
            pyxel.rect(self.arbusto.x, self.arbusto.y, self.arbusto.largura, self.arbusto.altura, 3)
            pyxel.rect(self.porta.x, self.porta.y, self.porta.largura, self.porta.altura, 4)

            if self.lutador_demoniaco.vida > 0:
                x_inimigo = self.lutador_demoniaco.quadro * 16
                pyxel.blt(self.lutador_demoniaco.x, self.lutador_demoniaco.y, 0, x_inimigo, 32, 16, 16, 0)
                pyxel.text(self.lutador_demoniaco.x, self.lutador_demoniaco.y - 6, "V:" + str(self.lutador_demoniaco.vida), 7)
                pyxel.text(self.lutador_demoniaco.x, self.lutador_demoniaco.y - 12, self.lutador_demoniaco.estado, 10)

            if self.projetil != None:
                pyxel.blt(self.projetil.x, self.projetil.y, 1, 0, self.projetil.imagem_y, 16, 16, 0)

            for bau in self.baus:
                if bau.aberto == False:
                    imagem_x = 0
                    imagem_y = 64
                else:
                    imagem_x = 16
                    imagem_y = 80

                pyxel.blt(bau.x, bau.y, 2, imagem_x, imagem_y, 16, 16, 0)

                if self.pertoBau(bau):
                    if self.tela_aberta == None:
                        pyxel.text(24, 95, "Pressione E para abrir", 7)

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
            item = self.mago.itens_equipados[i]
            imagem_y = None
            imagem_x = 0

            if item == self.pocao_vida:
                imagem_y = 0
            elif item == self.armadura_soldado:
                imagem_y = 16
            elif item == self.coracao_tita:
                imagem_y = 32
            elif item == self.pele_montanha:
                imagem_y = 48
            elif item == self.carta_prologo:
                imagem_x = 16
                imagem_y = 0

            if imagem_y != None:
                x_item = 4 + i * 17
                pyxel.blt(x_item, 103, 2, imagem_x, imagem_y, 16, 16, 0, scale=0.7)

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
            elif magia == self.correntes_abismo:
                imagem_y = 128

            if imagem_y != None:
                x_magia = 89 + i * 17
                pyxel.blt(x_magia, 103, 1, 0, imagem_y, 16, 16, 0, scale=0.7)

        if self.tempo_coracao_tita > 0:
            segundos = self.tempo_coracao_tita // 30
            pyxel.text(120, 2, "T:" + str(segundos), 10)

        if self.tempo_pele_montanha > 0:
            segundos = self.tempo_pele_montanha // 30
            pyxel.text(120, 8, "P:" + str(segundos), 10)

        if self.tela_aberta == "magias":
            pyxel.rect(8, 16, 144, 84, 1)
            pyxel.rectb(8, 16, 144, 84, 7)
            pyxel.text(35, 21, "INVENTARIO DE MAGIAS", 10)

            for i in range(len(self.mago.magias)):
                if self.magia_inventario_selecionada == self.mago.magias[i]:
                    cor_magia = 10
                else:
                    cor_magia = 7

                pyxel.text(16, 32 + i * 10, str(i + 1) + " - " + self.mago.magias[i].nome, cor_magia)

            pyxel.text(40, 90, "M: fechar  X: excluir", 6)

        if self.tela_aberta == "itens":
            pyxel.rect(8, 16, 144, 84, 1)
            pyxel.rectb(8, 16, 144, 84, 7)
            pyxel.text(35, 21, "INVENTARIO DE ITENS", 10)
            pyxel.text(126, 21, str(len(self.mago.inventario)) + "/" + str(self.mago.capacidade_inventario), 7)

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

            if len(self.mago.inventario) > self.mago.capacidade_inventario:
                quantidade_excluir = len(self.mago.inventario) - self.mago.capacidade_inventario
                pyxel.text(25, 90, "EXCLUA " + str(quantidade_excluir) + " ITEM(NS)", 8)
            else:
                pyxel.text(40, 90, "I: fechar  X: excluir", 6)

        if self.tela_aberta == "carta":
            pyxel.rect(5, 6, 150, 94, 4)
            pyxel.rect(7, 8, 146, 90, 9)
            pyxel.rect(9, 10, 142, 86, 15)
            pyxel.rectb(9, 10, 142, 86, 4)

            pyxel.rect(13, 13, 3, 2, 10)
            pyxel.rect(143, 13, 3, 2, 10)
            pyxel.rect(13, 90, 3, 2, 9)
            pyxel.rect(143, 90, 3, 2, 9)
            pyxel.line(14, 26, 146, 26, 4)

            pyxel.text(48, 16, "CARTA", 4)

            for i in range(len(self.paginas_carta[self.pagina_carta])):
                pyxel.text(
                    14,
                    32 + i * 7,
                    self.paginas_carta[self.pagina_carta][i],
                    0
                )

            pyxel.text(
                12,
                83,
                "PAGINA " + str(self.pagina_carta + 1)
                + "/" + str(len(self.paginas_carta)),
                4
            )
            pyxel.text(88, 83, "ENTER: avancar", 4)

        if self.tela_aberta == "bau":
            if self.bau_aberto != None:
                pyxel.rect(8, 16, 144, 84, 1)
                pyxel.rectb(8, 16, 144, 84, 7)

                if self.bau_aberto.tipo == "itens" and self.modo_bau == "guardar":
                    pyxel.text(12, 21, str(len(self.mago.inventario)) + "/" + str(self.mago.capacidade_inventario), 7)
                else:
                    pyxel.text(12, 21, str(len(self.bau_aberto.conteudo)) + "/" + str(self.bau_aberto.capacidade), 7)
                    
                pyxel.text(114, 21, "E: fechar", 6)

                if self.bau_aberto.tipo == "magias":
                    pyxel.text(48, 21, "BAU DE MAGIAS", 10)
                elif self.modo_bau == "guardar":
                    pyxel.text(34, 21, "INVENTARIO DE ITENS", 10)
                else:
                    pyxel.text(52, 21, "BAU DE ITENS", 10)

                if self.bau_aberto.tipo == "itens":
                    pyxel.text(12, 30, "G: " + self.modo_bau.upper(), 6)

                if self.modo_bau == "guardar" and self.bau_aberto.tipo == "itens":
                    if len(self.mago.inventario) == 0:
                        pyxel.text(48, 55, "INVENTARIO VAZIO", 7)
                    else:
                        for i in range(len(self.mago.inventario)):
                            objeto = self.mago.inventario[i]
                            pyxel.text(16, 38 + i * 10, objeto.nome, 7)
                else:
                    if len(self.bau_aberto.conteudo) == 0:
                        pyxel.text(65, 55, "VAZIO", 7)
                    else:
                        for i in range(len(self.bau_aberto.conteudo)):
                            objeto = self.bau_aberto.conteudo[i]
                            pyxel.text(16, 38 + i * 10, objeto.nome, 7)

                if self.tempo_mensagem_bau > 0:
                    pyxel.text(16, 92, self.mensagem_bau, 10)

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
