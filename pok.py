pokedex={}
class Pokémon:
    mosse={"nome_mossa":"valore_attacco"}
    def __init__(self,id_pokemon, nome_pokemon, tipo_pokemon, hp, altezza, peso, categoria,mosse):
            self.id_pokemon=id_pokemon
            self.nome_pokemon=nome_pokemon
            self.tipo_pokemon=tipo_pokemon
            self.hp=hp
            self.altezza=altezza
            self.peso=peso
            self.categoria=categoria
            self.mosse=mosse
            pokedex[self.id_pokemon]={"nome":self.nome_pokemon,"tipo":self.tipo_pokemon,"hp":self.hp,"altezza":self.altezza,"peso":self.peso,"mosse":self.mosse}
    
class Pokédex:
    def _init_(self, nome_allenatore,pokedex):
         self.nome_allenatore:nome_allenatore
         self.pokedex=pokedex
         

bulbasaur=Pokémon("0001","Bulbasaur","Erba",100,150,"1.5kg","Seme",{"Azione":50,"Solarraggio":25})
charmander=Pokémon("0004","Charmander","Fuoco",120,150,"1.5kg","Lucertola",{"Azione":50,"Lanciafiamme":25})
squirtle=Pokémon("0007","Squirtle","Acqua",110,150,"1.5kg","Tartaruga",{"Azione":50,"Pistolacqua":25})
pikachu=Pokémon("0025","Pikachu","Elettrico",130,150,"1.5kg","Topo elettrico",{"Azione":50,"Fulmine":25})

print(pokedex)