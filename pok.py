dizionario_pokedex={}
class Pokémon:
    mosse={"nome_mossa":"valore_attacco"}
    def _init_(self,id_pokemon, nome_pokemon, tipo_pokemon, hp, altezza, peso, categoria,mosse):
            self.id_pokemon=id_pokemon
            self.nome_pokemon=nome_pokemon
            self.tipo_pokemon=tipo_pokemon
            self.hp=hp
            self.altezza=altezza
            self.peso=peso
            self.categoria=categoria
            self.mosse=mosse
            dizionario_pokedex[self.id_pokemon]={"nome":self.nome_pokemon,"tipo":self.tipo_pokemon,"hp":self.hp,"altezza":self.altezza,"peso":self.peso,"mosse":self.mosse,"stato":"Non visto"}
    
# class Pokédex:
#     def _init_(self, nome_allenatore,pokedex):
#          self.nome_allenatore:nome_allenatore
#          self.pokedex=pokedex
         

# bulbasaur=Pokémon("0001","Bulbasaur","Erba",100,150,"1.5kg","Seme",{"Azione":50,"Solarraggio":25})
# charmander=Pokémon("0004","Charmander","Fuoco",120,150,"1.5kg","Lucertola",{"Azione":50,"Lanciafiamme":25})
# squirtle=Pokémon("0007","Squirtle","Acqua",110,150,"1.5kg","Tartaruga",{"Azione":50,"Pistolacqua":25})
# pikachu=Pokémon("0025","Pikachu","Elettrico",130,150,"1.5kg","Topo elettrico",{"Azione":50,"Fulmine":25})

# print(pokedex)

class Pokédex:
    def _init_(self, nome_allenatore,dizionario_pokedex):
         self.nome_allenatore:nome_allenatore
         self.dizionario_pokedex=dizionario_pokedex
    def pokemon_visto(self,id):
         self.dizionario_pokedex[id]["stato"]="Visto"
    def pokemon_catturato(self,id):
         self.dizionario_pokedex[id]["stato"]="Catturato"
         
bulbasaur=Pokémon("0001","Bulbasaur","Erba",100,150,"1.5kg","Seme",{"Azione":50,"Solarraggio":25})
charmander=Pokémon("0004","Charmander","Fuoco",120,150,"1.5kg","Lucertola",{"Azione":50,"Lanciafiamme":25})
squirtle=Pokémon("0007","Squirtle","Acqua",110,150,"1.5kg","Tartaruga",{"Azione":50,"Pistolacqua":25})
pikachu=Pokémon("0025","Pikachu","Elettrico",130,150,"1.5kg","Topo elettrico",{"Azione":50,"Fulmine":25})

# pokedex_di_fontana=Pokédex("Fontana",pokedex)
# print(pokedex_di_fontana.dizionario_pokedex)
# pokedex_di_fontana.pokemon_visto("0001")
# print(pokedex_di_fontana.dizionario_pokedex)
# print(pokedex_di_fontana.dizionario_pokedex["0001"]["hp"])

ho_già_un_pokemon = False

pokemon = ["bulbasaur", "squirtle", "charmander", "pikachu"]

nome = input("Benvenuto nel laboratorio del professor Olmi. Non hai ancora un pokemon, devi sceglierne uno. Per prima cosa, dimmi il tuo nome\n")
    
while not ho_già_un_pokemon:    
    #metto la funzione per printare i quattro tipi di pokemon disponibili con la loro descrizione e tipo

    scelta = input(f"Benvenuto {nome}. Scegli il tuo starter! Scrivi pikachu, charmander, squirtle o bulbasaur\n")

    if scelta in pokemon:
        if scelta.lower() == "pikachu":
             pokemon_iniziale = Pokémon("0025","Pikachu","Elettrico",130,150,"1.5kg","Topo elettrico",{"Azione":50,"Fulmine":25})
        elif scelta.lower() == "charmander":
             pokemon_iniziale = Pokémon("0004","Charmander","Fuoco",120,150,"1.5kg","Lucertola",{"Azione":50,"Lanciafiamme":25})
        elif scelta.lower() == "squirtle":
             pokemon_iniziale = Pokémon("0007","Squirtle","Acqua",110,150,"1.5kg","Tartaruga",{"Azione":50,"Pistolacqua":25})
        else:
             pokemon_iniziale = Pokémon("0001","Bulbasaur","Erba",100,150,"1.5kg","Seme",{"Azione":50,"Solarraggio":25})
        
        ho_già_un_pokemon = True
        pokedex = Pokédex(nome)
        pokedex.aggiungi_pokemon(pokemon_iniziale)
    else:
        print("Nome non valido. Riscegli tra i pokemon disponibili\n")


print(Pokédex.pokedex_elenco)

pokeball = {"pokeball": 5, "megaball": 0, "ultraball": 0}

while True:
     
    check = int(input("Sei pronto per essere un allenatore.\n[1] Avventurati nell'erba alta\n[2] Vai al negozio Pokémon\n[0] Torna a casa a dormire\n"))
    if check == 1:
        probabilità_incontro = random.random()*100
        if probabilità_incontro < 10:
            print("Non hai trovato nessun Pokemon oggi. Riprova domani\n")
            continue
        else:
            pokemon_selvatico = random.choice(pokemon)
               #battaglia = Battaglia() bho? facciamo una battaglia
            check2 = int(input(f"Un {pokemon_selvatico} selvatico è apparso!\n[1] Combatti\n[2] Prova a catturare\n[3] Fuggi"))

            if check2 == 1:
                    #metodo battaglia
                pass
            elif check2 == 2:
                palla = input(f"Scegli che ball usare. Hai {pokeball["pokeball"]} pokeball, {pokeball["megaball"]} megaball e {pokeball['ultraball']} ultraball\n")
                if pokemon_iniziale.hp <= 25 and palla == "pokeball":
                    probabilità_cattura = 40
                    pokeball["pokeball"] -= 1
                elif pokemon_iniziale.hp <= 25 and palla == "megaball":
                    probabilità_cattura = 60
                    pokeball["megaball"] -=1
                elif pokemon_iniziale.hp <= 25 and palla == "ultraball":
                    probabilità_cattura = 80
                    pokeball["ultraball"] -= 1
                elif pokemon_iniziale.hp <= 50 and palla == "pokeball":
                    probabilità_cattura = 25
                    pokeball["pokeball"] -= 1
                elif pokemon_iniziale.hp <= 50 and palla == "megaball":
                    probabilità_cattura = 45
                    pokeball["megaball"] -= 1
                elif pokemon_iniziale.hp <= 50 and palla == "ultraball":
                    probabilità_cattura = 65
                    pokeball["ultraball"] -= 1
                else:
                    probabilità_cattura = 0

                if random.random() * 100 < probabilità_cattura:
                    print(f"Hai catturato il {pokemon_selvatico} selvatico!")
                else:
                    print(f"Il {pokemon_selvatico} selvatico è sfuggito!")
            elif check2 == "3":
                print("Sei fuggito dall'incontro.")
                continue
    elif check == 2:
        compro = int(input("Cosa vuoi fare?\n[1] Compro pokeball\n[2] Compro megaball\n[3] Compro ultraball\n[0] Esci\n"))
        if compro == 0:
            continue
        elif compro == 1:
            quanto = int(input("Quante pokeball vuoi? "))
            pokeball["pokeball"] += quanto
        elif compro == 2:
            quanto = int(input("Quante megaball vuoi? "))
            pokeball["megaball"] += quanto
        else:
            quanto = int(input("Quante ultraball vuoi? "))
            pokeball["pokeball"] += quanto      
    else:
        print(f"Buonanotte {nome}") 
        break
