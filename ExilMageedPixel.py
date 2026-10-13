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
    def __init__(self, nome, vida, forca, defesa, velocidade, sorte, espirito, x, y, largura, altura, nivel):
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
        self.nivel = nivel
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
        self.tempo_ataque = 0
        self.tempo_travado = 0
        self.passos_desvio = 0
        self.direcao_desvio = 0
        self.altura_sprite = 16
    
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
        pyxel.images[0].load(0, 48, "vampiro_1.png")
        pyxel.images[0].load(0, 64, "cenario_vampiros.png")
        pyxel.images[0].load(0, 80, "demonio_2.png")
        pyxel.images[0].load(0, 104, "cenario_demonios.png")
        pyxel.images[1].load(0, 168, "fundo_demonios.png")
        pyxel.images[0].load(0, 128, "fundo_vampiros.png")
        pyxel.images[1].load(0, 0, "disparo_arcano.png")
        pyxel.images[1].load(0, 16, "ruina_proibida.png")
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
        pyxel.images[2].load(32, 0, "elixir_mana.png")

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
        self.correntes_abismo = Magia("Correntes do Abismo", 0, 20, 60, 40, 1, 1, 100)
        self.ruina_proibida = Magia("Ruina Proibida", 150, 40, 40, 0, 5, 1, 100)
        self.mago.aprenderMagia(self.disparo_arcano)
        self.mago.magias_equipadas[0] = self.disparo_arcano
        self.pocao_vida = Item("Pocao de Vida", "ativo", "vida", 40, True, "comum", 0)
        self.armadura_soldado = Item("Armadura de Soldado", "passivo", "defesa", 15, False, "comum", 0)
        self.coracao_tita = Item("Coracao do Tita", "ativo", "forca", 50, True, "epico", 300)
        self.pele_montanha = Item("Pele da Montanha", "ativo", "defesa", 60, True, "epico", 300)
        self.elixir_mana = Item("Elixir de Mana", "ativo", "mana", 50, True, "raro", 0)
        self.pergaminho = Item("Pergaminho Proibido", "especial", "pergaminho", 0, False, "epico", 0)
        self.bau_final = Bau(72, 52, 16, 16, "itens", [self.pergaminho, self.pocao_vida, self.pocao_vida, self.elixir_mana, self.elixir_mana], 6)
        self.pergaminho_obtido = False
        self.bau_magias = Bau(140, 22, 16, 16, "magias", [self.bola_fogo], 6)
        self.bau_itens = Bau(140, 44, 16, 16, "itens", [self.armadura_soldado], 6)
        self.bau_magias_2 = Bau(4, 82, 16, 16, "magias", [self.barreira_cristal], 6)
        self.bau_itens_2 = Bau(4, 60, 16, 16, "itens", [self.pele_montanha], 6)
        self.bau_demonio_magias = Bau(140, 22, 16, 16, "magias", [self.correntes_abismo], 6)
        self.bau_demonio_itens = Bau(140, 44, 16, 16, "itens", [self.coracao_tita], 6)
        self.bau_demonio_magias_2 = Bau(4, 82, 16, 16, "magias", [self.explosao_arcana], 6)
        self.bau_demonio_itens_2 = Bau(4, 60, 16, 16, "itens", [self.elixir_mana], 6)
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
                "seria quase impossivel. Antes,",
                "invada o reino dos vampiros e",
                "reuna magias e itens. Cada reino",
                "tem sua propria paisagem e uma",
                "atmosfera que o torna unico."
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

        self.paginas_demonios = [
            [
                "Um portao no reino dos vampiros",
                "se abre diante de voce.",
                "Um calor sufocante sobe do chao e",
                "cheiro de enxofre contamina o ar.",
                "Voce chegou ao reino dos demonios,",
                "onde o Pergaminho Proibido espera."
            ],
            [
                "Os demonios sao mais fortes e nao",
                "respeitam portas, eles demoram,",
                "mas atravessam. Use tudo o que",
                "voce conquistou ate aqui.",
                "",
                "Nao ha mais volta."
            ]
        ]

        self.paginas_deuses = [
            [
                "Ao tocar o Pergaminho Proibido,",
                "um poder impossivel atravessa",
                "seu corpo. Suas magias agora",
                "ultrapassam qualquer limite",
                "mortal, e voce aprendeu a magia",
                "Ruina Proibida."
            ],
            [
                "Mas algo despertou. A entidade",
                "que criou os reinos dos vampiros",
                "e dos demonios sentiu seu poder.",
                "Ela sabe que voce pode refinar",
                "as magias proibidas e se tornar",
                "uma ameaca a todo o universo."
            ],
            [
                "Para impedir isso, ela vem atras",
                "de voce. O chao se desfaz e voce",
                "e arrastado pro reino dos deuses.",
                "",
                "Nao tem pra onde fugir."
            ]
        ]

        self.pagina_carta = 0
        self.titulo_carta = "CARTA"
        self.portal_ativo = False
        self.portal_x = 72
        self.portal_y = 52
        self.bau_prologo = Bau(72, 45, 16, 16, "itens", [self.carta_prologo, self.pocao_vida], 6)
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
        self.paredes = [
            Parede(96, 20, 16, 16),
            Parede(96, 52, 16, 16),
            Parede(48, 52, 16, 16),
            Parede(48, 84, 16, 16),
            Parede(16, 36, 48, 16),
            Parede(96, 68, 48, 16)
        ]
        self.arbustos = [
            Arbusto(80, 20, 16, 16),
            Arbusto(64, 84, 16, 16)
        ]
        self.portas = [
            Porta(96, 36, 16, 16),
            Porta(48, 68, 16, 16)
        ]
        self.lutador_demoniaco = Inimigo("Lutador Demoniaco", 240, 80, 55, 65, 35, 80, 120, 35, 16, 16, 3)
        self.lutador_demoniaco.tipo = "demonio"
        self.lutador_demoniaco.imagem_y = 32
        self.lutador_demoniaco.cor_transparente = 0
        self.lutador_demoniaco.raio_deteccao = 60
        self.lutador_demoniaco.raio_ataque = 20

        self.demonio_2 = Inimigo("Demonio Infernal", 300, 92, 60, 70, 40, 90, 24, 69, 16, 16, 4)
        self.demonio_2.tipo = "demonio"
        self.demonio_2.imagem_y = 80
        self.demonio_2.cor_transparente = 11
        self.demonio_2.raio_deteccao = 65
        self.demonio_2.raio_ataque = 24
        self.demonio_2.altura_sprite = 23

        self.vampiro_1 = Inimigo("Guarda Vampiro", 120, 52, 30, 50, 30, 40, 120, 35, 16, 16, 1)
        self.vampiro_1.tipo = "vampiro"
        self.vampiro_1.imagem_y = 48
        self.vampiro_1.cor_transparente = 11
        self.vampiro_1.raio_deteccao = 45
        self.vampiro_1.raio_ataque = 12

        self.vampiro_2 = Inimigo("Vampiro Sentinela", 180, 72, 40, 65, 35, 50, 24, 69, 16, 16, 2)
        self.vampiro_2.tipo = "vampiro"
        self.vampiro_2.imagem_y = 48
        self.vampiro_2.cor_transparente = 11
        self.vampiro_2.raio_deteccao = 55
        self.vampiro_2.raio_ataque = 16

        self.inimigo_atual = self.vampiro_1
        pyxel.run(self.update, self.draw)

    def linhaBloqueada(self, inimigo, objeto):
        centro_mago_x = self.mago.x + 8
        centro_mago_y = self.mago.y + 8
        centro_inimigo_x = inimigo.x + 8
        centro_inimigo_y = inimigo.y + 8

        distancia_x = centro_mago_x - centro_inimigo_x
        distancia_y = centro_mago_y - centro_inimigo_y
        distancia = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

        if distancia == 0:
            return False

        for passo in range(int(distancia) + 1):
            ponto_x = centro_inimigo_x + distancia_x * passo / distancia
            ponto_y = centro_inimigo_y + distancia_y * passo / distancia

            if ponto_x >= objeto.x and ponto_x <= objeto.x + objeto.largura:
                if ponto_y >= objeto.y and ponto_y <= objeto.y + objeto.altura:
                    return True

        return False

    def paredeBloqueiaVisao(self, inimigo):
        for parede in self.paredes:
            if self.linhaBloqueada(inimigo, parede):
                return True

        return False

    def arbustoBloqueiaVisao(self, inimigo):
        if self.magoNoArbusto():
            return True

        for arbusto in self.arbustos:
            if self.linhaBloqueada(inimigo, arbusto):
                return True

        return False

    def colisaoParede(self, personagem):
        for parede in self.paredes:
            colisaoX = personagem.x + 12 > parede.x and personagem.x + 4 < parede.x + parede.largura
            colisaoY = personagem.y + 14 > parede.y and personagem.y + 4 < parede.y + parede.altura

            if colisaoX and colisaoY:
                return True

        return False

    def colisaoArbusto(self, personagem):
        for arbusto in self.arbustos:
            colisaoX = personagem.x + 12 > arbusto.x and personagem.x + 4 < arbusto.x + arbusto.largura
            colisaoY = personagem.y + 14 > arbusto.y and personagem.y + 4 < arbusto.y + arbusto.altura

            if colisaoX and colisaoY:
                return True

        return False

    def colisaoPorta(self, personagem):
        for porta in self.portas:
            colisaoX = personagem.x + 12 > porta.x and personagem.x + 4 < porta.x + porta.largura
            colisaoY = personagem.y + 14 > porta.y and personagem.y + 4 < porta.y + porta.altura

            if colisaoX and colisaoY:
                return True

        return False

    def colisaoInimigo(self, inimigo):
        colisaoX = self.mago.x + 12 > inimigo.x + 4 and self.mago.x + 4 < inimigo.x + 12
        colisaoY = self.mago.y + 14 > inimigo.y + 4 and self.mago.y + 4 < inimigo.y + 14

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def magoNoArbusto(self):
        centro_mago_x = self.mago.x + 8
        centro_mago_y = self.mago.y + 8

        for arbusto in self.arbustos:
            if centro_mago_x >= arbusto.x and centro_mago_x <= arbusto.x + arbusto.largura:
                if centro_mago_y >= arbusto.y and centro_mago_y <= arbusto.y + arbusto.altura:
                    return True

        return False

    def aplicarDanoMago(self, dano):
        dano_recebido = dano

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
            self.mago.modificarForca(-1)

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

    def colisaoProjetil(self, inimigo):
        if inimigo.vida == 0:
            return False

        colisaoX = self.projetil.x + 16 >= inimigo.x and self.projetil.x <= inimigo.x + inimigo.largura
        colisaoY = self.projetil.y + 16 >= inimigo.y and self.projetil.y <= inimigo.y + inimigo.altura

        if colisaoX and colisaoY:
            return True
        else:
            return False

    def projetilBateuObjeto(self):
        centro_x = self.projetil.x + 8
        centro_y = self.projetil.y + 8

        for objeto in self.paredes + self.portas + self.arbustos:
            if centro_x >= objeto.x and centro_x <= objeto.x + objeto.largura:
                if centro_y >= objeto.y and centro_y <= objeto.y + objeto.altura:
                    return True

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
                                        if conteudo_escolhido == self.pergaminho:
                                            self.bau_aberto.conteudo.pop(i)
                                            self.obterPergaminho()
                                            self.mensagem_bau = "O poder proibido e seu"
                                        elif len(self.mago.inventario) < self.mago.capacidade_inventario:
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
                                inicio_y = 37 + i * 6
                                final_y = inicio_y + 5

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

                if self.pergaminho_obtido and self.estado_jogo == "demonios":
                    self.paginas_carta = self.paginas_deuses
                    self.pagina_carta = 0
                    self.titulo_carta = "PERGAMINHO PROIBIDO"
                    self.tela_aberta = "carta"

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
                    inicio_y = 29 + i * 6
                    final_y = 34 + i * 6

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
                if self.item_inventario_selecionado != None and self.item_inventario_selecionado != self.carta_prologo:
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
            baus_colisao = []

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

    def inimigoBloqueado(self, inimigo):
        if self.colisaoParede(inimigo) or self.colisaoArbusto(inimigo):
            return True

        if inimigo.tipo == "vampiro" and self.colisaoPorta(inimigo):
            return True

        return False

    def atualizarInimigo(self, inimigo):
        x_anterior_inimigo = inimigo.x
        y_anterior_inimigo = inimigo.y

        distancia_x = self.mago.x - inimigo.x
        distancia_y = self.mago.y - inimigo.y
        distancia_jogador = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

        if inimigo.passos_desvio > 0 and inimigo.estado != "congelado":
            inimigo.tempo_movimento += inimigo.velocidade

            if inimigo.tempo_movimento >= 100:
                inimigo.tempo_movimento -= 100

                if inimigo.direcao_desvio == 0:
                    inimigo.x += 1
                elif inimigo.direcao_desvio == 1:
                    inimigo.y += 1
                elif inimigo.direcao_desvio == 2:
                    inimigo.x -= 1
                else:
                    inimigo.y -= 1

                inimigo.passos_desvio -= 1

        elif inimigo.estado == "patrulha":
            if distancia_jogador <= inimigo.raio_deteccao and self.paredeBloqueiaVisao(inimigo) == False and self.arbustoBloqueiaVisao(inimigo) == False:
                inimigo.estado = "perseguicao"

        elif inimigo.estado == "perseguicao":
            if distancia_jogador > inimigo.raio_deteccao or self.paredeBloqueiaVisao(inimigo) == True or self.arbustoBloqueiaVisao(inimigo) == True:
                inimigo.estado = "busca"
                inimigo.tempo_busca = 300 - self.mago.sorte * 2
                inimigo.tempo_movimento = 0
                inimigo.chegou_ultima_posicao = False
                inimigo.direcao_busca = 0
                inimigo.passos_busca = 0

            else:
                inimigo.ultimo_x_jogador = int(self.mago.x)
                inimigo.ultimo_y_jogador = int(self.mago.y)

                inimigo.tempo_movimento += inimigo.velocidade

                if inimigo.tempo_movimento >= 100:
                    inimigo.tempo_movimento -= 100

                    if self.mago.x < inimigo.x:
                        inimigo.x -= 1
                    elif self.mago.x > inimigo.x:
                        inimigo.x += 1

                    if self.mago.y < inimigo.y:
                        inimigo.y -= 1
                    elif self.mago.y > inimigo.y:
                        inimigo.y += 1

        elif inimigo.estado == "busca":
            if distancia_jogador <= inimigo.raio_deteccao and self.paredeBloqueiaVisao(inimigo) == False and self.arbustoBloqueiaVisao(inimigo) == False:
                inimigo.estado = "perseguicao"
                inimigo.tempo_busca = 0

            else:
                if inimigo.tempo_busca > 0:
                    inimigo.tempo_busca -= 1
                    inimigo.tempo_movimento += inimigo.velocidade

                    if inimigo.tempo_movimento >= 100:
                        inimigo.tempo_movimento -= 100

                        if inimigo.chegou_ultima_posicao == False:
                            if inimigo.x < inimigo.ultimo_x_jogador:
                                inimigo.x += 1
                            elif inimigo.x > inimigo.ultimo_x_jogador:
                                inimigo.x -= 1

                            if inimigo.y < inimigo.ultimo_y_jogador:
                                inimigo.y += 1
                            elif inimigo.y > inimigo.ultimo_y_jogador:
                                inimigo.y -= 1

                            if inimigo.x == inimigo.ultimo_x_jogador and inimigo.y == inimigo.ultimo_y_jogador:
                                inimigo.chegou_ultima_posicao = True

                        else:
                            if inimigo.direcao_busca == 0:
                                inimigo.x += 1
                            elif inimigo.direcao_busca == 1:
                                inimigo.y += 1
                            elif inimigo.direcao_busca == 2:
                                inimigo.x -= 1
                            else:
                                inimigo.y -= 1

                            inimigo.passos_busca += 1

                            if inimigo.passos_busca == 10:
                                inimigo.passos_busca = 0
                                inimigo.direcao_busca += 1

                                if inimigo.direcao_busca > 3:
                                    inimigo.direcao_busca = 0

                else:
                    inimigo.estado = "retorno"

        elif inimigo.estado == "retorno":
            if distancia_jogador <= inimigo.raio_deteccao:
                inimigo.estado = "perseguicao"

            else:
                inimigo.tempo_movimento += 1

                if inimigo.tempo_movimento == 2:
                    inimigo.tempo_movimento = 0

                    if inimigo.x < inimigo.x_inicial:
                        inimigo.x += 1
                    elif inimigo.x > inimigo.x_inicial:
                        inimigo.x -= 1

                    if inimigo.y < inimigo.y_inicial:
                        inimigo.y += 1
                    elif inimigo.y > inimigo.y_inicial:
                        inimigo.y -= 1

                if inimigo.x == inimigo.x_inicial and inimigo.y == inimigo.y_inicial:
                    inimigo.estado = "patrulha"

        elif inimigo.estado == "congelado":
            if inimigo.tempo_congelado > 0:
                inimigo.tempo_congelado -= 1
            else:
                if inimigo.estado_anterior == "perseguicao":
                    if distancia_jogador <= inimigo.raio_deteccao and self.paredeBloqueiaVisao(inimigo) == False:
                        inimigo.estado = "perseguicao"
                    else:
                        inimigo.estado = "busca"
                        inimigo.tempo_busca = 300 - self.mago.sorte * 2
                        inimigo.tempo_movimento = 0
                        inimigo.chegou_ultima_posicao = False
                        inimigo.direcao_busca = 0
                        inimigo.passos_busca = 0
                else:
                    inimigo.estado = inimigo.estado_anterior

        if self.inimigoBloqueado(inimigo):
            novo_y_inimigo = inimigo.y

            inimigo.y = y_anterior_inimigo

            if self.inimigoBloqueado(inimigo):
                inimigo.x = x_anterior_inimigo

            inimigo.y = novo_y_inimigo

            if self.inimigoBloqueado(inimigo):
                inimigo.y = y_anterior_inimigo

        if inimigo.tipo != "vampiro":
            if inimigo.passando_porta == True:
                if self.colisaoPorta(inimigo) == False:
                    inimigo.passando_porta = False
                    inimigo.tempo_porta = 0

            else:
                if self.colisaoPorta(inimigo):
                    if inimigo.tempo_porta < 60:
                        inimigo.tempo_porta += 1
                        inimigo.x = x_anterior_inimigo
                        inimigo.y = y_anterior_inimigo
                    else:
                        inimigo.passando_porta = True

        if inimigo.x < 0:
            inimigo.x = 0
        elif inimigo.x > 144:
            inimigo.x = 144

        if inimigo.y < 20:
            inimigo.y = 20
        elif inimigo.y > 86:
            inimigo.y = 86

        if inimigo.estado == "perseguicao" or inimigo.estado == "busca" or inimigo.estado == "retorno":
            if inimigo.x == x_anterior_inimigo and inimigo.y == y_anterior_inimigo and self.colisaoInimigo(inimigo) == False:
                inimigo.tempo_travado += 1
            else:
                inimigo.tempo_travado = 0

            if inimigo.tempo_travado >= 20:
                inimigo.tempo_travado = 0
                inimigo.passos_desvio = 20
                inimigo.direcao_desvio += 1

                if inimigo.direcao_desvio > 3:
                    inimigo.direcao_desvio = 0

        if inimigo.vida > 0:
            inimigo.tempo_animacao += 1

            if inimigo.tempo_animacao == 8:
                inimigo.quadro += 1
                inimigo.tempo_animacao = 0

                if inimigo.quadro > 3:
                    inimigo.quadro = 0

        if inimigo.tempo_ataque > 0:
            inimigo.tempo_ataque -= 1

        if inimigo.vida > 0 and inimigo.estado != "congelado" and self.magoNoArbusto() == False:
            distancia_x = self.mago.x - inimigo.x
            distancia_y = self.mago.y - inimigo.y
            distancia_ataque = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

            if distancia_ataque <= inimigo.raio_ataque and self.paredeBloqueiaVisao(inimigo) == False and inimigo.tempo_ataque == 0:
                self.aplicarDanoMago(inimigo.forca // 4)
                inimigo.tempo_ataque = 40

    def obterPergaminho(self):
        self.pergaminho_obtido = True
        self.mago.aprenderMagia(self.ruina_proibida)
        self.disparo_arcano.dano = self.disparo_arcano.dano * 2
        self.bola_fogo.dano = self.bola_fogo.dano * 2
        self.explosao_arcana.dano = self.explosao_arcana.dano * 2
        self.correntes_abismo.alcance = 50
        
    def update(self):
        if self.tela_aberta == "carta":
            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.pagina_carta < len(self.paginas_carta) - 1:
                    self.pagina_carta += 1
                else:
                    self.tela_aberta = None

                    if self.estado_jogo == "prologo":
                        self.estado_jogo = "vampiros"
                        self.mago.x = 10
                        self.mago.y = 86

                        if self.carta_prologo in self.mago.inventario:
                            self.mago.inventario.remove(self.carta_prologo)

                        for i in range(5):
                            if self.mago.itens_equipados[i] == self.carta_prologo:
                                self.mago.itens_equipados[i] = None

                        if self.mago.item_selecionado == self.carta_prologo:
                            self.mago.item_selecionado = None

                        if self.item_inventario_selecionado == self.carta_prologo:
                            self.item_inventario_selecionado = None

                    elif self.estado_jogo == "vampiros":
                        self.estado_jogo = "demonios"
                        self.mago.x = 10
                        self.mago.y = 86
                        self.projetil = None
                        self.baus = [self.bau_demonio_magias, self.bau_demonio_itens]
                        self.portal_ativo = False
                        self.inimigo_atual = self.lutador_demoniaco

                    elif self.estado_jogo == "demonios":
                        self.estado_jogo = "deuses"
                        self.mago.x = 10
                        self.mago.y = 86
                        self.projetil = None
                        self.baus = []

            return

        if self.estado_jogo == "menu":
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.estado_jogo = "controles"

            return

        if self.estado_jogo == "controles":
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.estado_jogo = "prologo"

            return

        if pyxel.btnp(pyxel.KEY_N) and self.tela_aberta == None:
            if self.estado_jogo == "prologo":
                self.estado_jogo = "vampiros"
            elif self.estado_jogo == "vampiros":
                self.estado_jogo = "demonios"
                self.vampiro_1.vida = 0
                self.vampiro_2.vida = 0
                self.inimigo_atual = self.lutador_demoniaco
                self.baus = [self.bau_demonio_magias, self.bau_demonio_itens]
            elif self.estado_jogo == "demonios":
                if self.pergaminho_obtido == False:
                    self.obterPergaminho()

                self.estado_jogo = "deuses"
                self.lutador_demoniaco.vida = 0
                self.demonio_2.vida = 0
                self.inimigo_atual = self.demonio_2
                self.baus = []

            self.mago.x = 10
            self.mago.y = 86
            return

        if pyxel.btnp(pyxel.KEY_K) and self.tela_aberta == None:
            if self.estado_jogo == "vampiros" or self.estado_jogo == "demonios":
                self.inimigo_atual.vida = 0

        self.atualizarHotbar()

        if self.estado_jogo == "prologo":
            if self.tela_aberta == "bau":
                self.atualizarBau()
                return

            self.atualizarInventario()

            if self.tela_aberta != None:
                return

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

            if self.projetil != None:
                self.projetil.mover()

                if self.projetil.x < 0 or self.projetil.x > 144 or self.projetil.y < 20 or self.projetil.y > 102:
                    self.projetil = None

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

                        elif item_usado == self.elixir_mana:
                            if self.mago.mana < 100:
                                self.mago.modificarMana(item_usado.valor)
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

            elif self.mago.magia_selecionada == self.ruina_proibida:
                if self.mago.mana >= self.ruina_proibida.mana:
                    distancia_x = pyxel.mouse_x - (self.mago.x + 8)
                    distancia_y = pyxel.mouse_y - (self.mago.y + 8)
                    distancia = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

                    if distancia > 0:
                        direcao_x = distancia_x / distancia
                        direcao_y = distancia_y / distancia
                        self.projetil = ProjetilMagico(self.mago.x + 4, self.mago.y + 4, direcao_x, direcao_y, self.ruina_proibida.dano, 16)
                        self.mago.modificarMana(-self.ruina_proibida.mana)

            elif self.mago.magia_selecionada == self.correntes_abismo:
                if self.mago.mana >= self.correntes_abismo.mana:
                    if self.inimigo_atual.vida > 0:
                        distancia_x = self.mago.x - self.inimigo_atual.x
                        distancia_y = self.mago.y - self.inimigo_atual.y
                        distancia = (distancia_x * distancia_x + distancia_y * distancia_y) ** 0.5

                        if distancia <= self.correntes_abismo.alcance:
                            self.inimigo_atual.estado_anterior = self.inimigo_atual.estado
                            self.inimigo_atual.estado = "congelado"
                            if self.pergaminho_obtido:
                                self.inimigo_atual.tempo_congelado = 300
                            else:
                                self.inimigo_atual.tempo_congelado = 210
                            self.mago.modificarMana(-self.correntes_abismo.mana)
                            self.tempo_efeito_correntes = 15

        if self.tempo_barreira > 0:
            self.tempo_barreira -= 1
        else:
            self.barreira_ativa = False

        if self.tempo_efeito_correntes > 0:
            self.tempo_efeito_correntes -= 1

        self.atualizarInimigo(self.inimigo_atual)

        if self.projetil != None:
            self.projetil.mover()

            if self.projetil.x < 0 or self.projetil.x > 144 or self.projetil.y < 20 or self.projetil.y > 86:
                self.projetil = None

            elif self.projetilBateuObjeto():
                self.projetil = None

            elif self.colisaoProjetil(self.inimigo_atual):
                self.inimigo_atual.modificarVida(-self.projetil.dano)
                self.projetil = None

        if self.inimigo_atual == self.vampiro_1 and self.vampiro_1.vida == 0:
            self.inimigo_atual = self.vampiro_2
            self.baus.append(self.bau_magias_2)
            self.baus.append(self.bau_itens_2)

        if self.inimigo_atual == self.lutador_demoniaco and self.lutador_demoniaco.vida == 0:
            self.inimigo_atual = self.demonio_2
            self.baus.append(self.bau_demonio_magias_2)
            self.baus.append(self.bau_demonio_itens_2)

        if self.estado_jogo == "demonios" and self.demonio_2.vida == 0 and self.bau_final not in self.baus:
            self.baus.append(self.bau_final)

        if self.pergaminho_obtido and self.estado_jogo == "demonios" and self.tela_aberta == None:
            self.paginas_carta = self.paginas_deuses
            self.pagina_carta = 0
            self.titulo_carta = "PERGAMINHO PROIBIDO"
            self.tela_aberta = "carta"

        if self.estado_jogo == "vampiros" and self.vampiro_2.vida == 0:
            self.portal_ativo = True

        if self.portal_ativo and self.estado_jogo == "vampiros":
            centro_x = self.mago.x + 8
            centro_y = self.mago.y + 8

            if centro_x >= self.portal_x and centro_x <= self.portal_x + 16:
                if centro_y >= self.portal_y and centro_y <= self.portal_y + 16:
                    self.paginas_carta = self.paginas_demonios
                    self.pagina_carta = 0
                    self.titulo_carta = "REINO DOS DEMONIOS"
                    self.tela_aberta = "carta"

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

        if self.estado_jogo == "controles":
            pyxel.text(62, 6, "COMANDOS", 10)

            comandos = [
                ["W A S D", "andar"],
                ["MOUSE", "mirar a magia"],
                ["CLIQUE", "lancar a magia"],
                ["1 a 5", "selecionar item"],
                ["6 a 9", "selecionar magia"],
                ["E", "usar item / abrir bau"],
                ["I", "inventario de itens"],
                ["M", "inventario de magias"],
                ["X", "excluir no inventario"],
                ["G", "guardar no bau"],
                ["P", "pausar"]
            ]

            for i in range(len(comandos)):
                pyxel.text(12, 18 + i * 8, comandos[i][0], 10)
                pyxel.text(52, 18 + i * 8, comandos[i][1], 7)

            pyxel.text(38, 110, "ENTER para comecar", 6)
            return

        if self.estado_jogo == "prologo":
            pyxel.pal(1, 11)
            pyxel.blt(0, 20, 2, 0, 96, 160, 82, 0)
            pyxel.pal()

        elif self.estado_jogo == "vampiros" or self.estado_jogo == "demonios":
            if self.estado_jogo == "vampiros":
                pyxel.blt(0, 20, 0, 0, 128, 160, 82)
            else:
                pyxel.blt(0, 20, 1, 0, 168, 160, 82)

            if self.inimigo_atual.vida > 0:
                pyxel.circb(self.inimigo_atual.x + 8, self.inimigo_atual.y + 8, self.inimigo_atual.raio_ataque, 8)

            for bau in self.baus:
                if bau.aberto == False:
                    imagem_x = 0
                    imagem_y = 64
                else:
                    imagem_x = 16
                    imagem_y = 80

                pyxel.blt(bau.x, bau.y, 2, imagem_x, imagem_y, 16, 16, 0)

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

            elif self.tela_aberta == None and self.mago.item_selecionado == self.carta_prologo:
                pyxel.text(28, 95, "Pressione E para ler", 10)

            if self.projetil != None:
                pyxel.blt(self.projetil.x, self.projetil.y, 1, 0, self.projetil.imagem_y, 16, 16, 0)

        if self.estado_jogo != "prologo":
            if self.estado_jogo == "demonios":
                linha_cenario = 104
            else:
                linha_cenario = 64

            for parede in self.paredes:
                for bloco_x in range(0, parede.largura, 16):
                    for bloco_y in range(0, parede.altura, 16):
                        pyxel.blt(parede.x + bloco_x, parede.y + bloco_y, 0, 0, linha_cenario, 16, 16)

            for porta in self.portas:
                pyxel.blt(porta.x, porta.y, 0, 16, linha_cenario, 16, 16)

            for arbusto in self.arbustos:
                pyxel.blt(arbusto.x, arbusto.y, 0, 32, linha_cenario, 16, 16)

            if self.portal_ativo and self.estado_jogo == "vampiros":
                pyxel.blt(self.portal_x, self.portal_y, 0, 48, 104, 16, 16, 11)

            if self.inimigo_atual.vida > 0:
                x_inimigo = self.inimigo_atual.quadro * 16
                pyxel.blt(self.inimigo_atual.x, self.inimigo_atual.y + 16 - self.inimigo_atual.altura_sprite, 0, x_inimigo, self.inimigo_atual.imagem_y, 16, self.inimigo_atual.altura_sprite, self.inimigo_atual.cor_transparente)
                pyxel.text(self.inimigo_atual.x, self.inimigo_atual.y - 6, "V:" + str(self.inimigo_atual.vida), 7)
                pyxel.text(self.inimigo_atual.x, self.inimigo_atual.y - 12, self.inimigo_atual.estado, 10)

            if self.projetil != None:
                pyxel.blt(self.projetil.x, self.projetil.y, 1, 0, self.projetil.imagem_y, 16, 16, 0)

            for bau in self.baus:
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
            elif item == self.elixir_mana:
                imagem_x = 32
                imagem_y = 0

            if imagem_y != None:
                x_item = 4 + i * 17
                pyxel.blt(x_item, 103, 2, imagem_x, imagem_y, 16, 16, 0, scale=0.7)

        if self.estado_jogo == "prologo":
            for i in range(16):
                pyxel.colors[i] = self.paleta_original[i]

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
            elif magia == self.ruina_proibida:
                imagem_y = 16

            if imagem_y != None:
                x_magia = 89 + i * 17
                pyxel.blt(x_magia, 103, 1, 0, imagem_y, 16, 16, 0, scale=0.7)

        if self.estado_jogo == "prologo":
            for i in range(16):
                pyxel.colors[i] = self.paleta_floresta[i]

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

                    pyxel.text(16, 30 + i * 6, str(i + 1) + " - " + self.mago.inventario[i].nome + " [" + self.mago.inventario[i].raridade + "]", cor_item)

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

            pyxel.text(48, 16, self.titulo_carta, 4)

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
                            pyxel.text(16, 37 + i * 6, objeto.nome, 7)
                else:
                    if len(self.bau_aberto.conteudo) == 0:
                        pyxel.text(65, 55, "VAZIO", 7)
                    else:
                        for i in range(len(self.bau_aberto.conteudo)):
                            objeto = self.bau_aberto.conteudo[i]
                            pyxel.text(16, 38 + i * 10, objeto.nome, 7)

                if self.tempo_mensagem_bau > 0:
                    pyxel.text(60, 30, self.mensagem_bau, 10)

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
