class Pokémon:
    mosse={"nome_mossa":"valore_attacco"}
    def _init_(self,id_pokemon, nome_pokemon, tipo_pokemon, hp, altezza, peso, categoria):
            self.id_pokemon=id_pokemon
            self.nome_pokemon=nome_pokemon
            self.tipo_pokemon=tipo_pokemon
            self.hp=hp
            self.altezza=altezza
            self.peso=peso
            self.categoria=categoria
class Pokédex:
    pokedex_elenco={}
    pokedex_catturati={}
    pokedex_visti={}
    def _init_(self, nome_allenatore):
         self.nome_allenatore:nome_allenatore
            
bulbasaur=Pokémon("001","Bulbasaur","Erba",100,150,"1.5kg","Seme")
bulbasaur.mosse["azione"]=50
print(bulbasaur.mosse)
