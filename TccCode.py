#Banco de dados
toxic=[
         [
r"(.*)b(o+)(a+)|(.*)(i+)ss(o+) a(e+)",
["Karthus diz: Boa time","Olaf diz: vamos ganhar!"]
      ],
       [
r"(.*)estou a caminho|(.*)indo",
["Ashe diz: recua que não da!","Yorick diz: estou contigo"]
      ],
           [
r"GG",
["Ashe diz: GG","Yorick diz:GG claro tu é muito ruim","Olaf diz:tu és horrivel!","Kalista diz: BG!!!!!"]
      ],
       [
r"(.*)por que(.*)?",
["Olaf diz: Desculpa falha minha","Kalista diz: Tu é ruim cara foi por isso!"]
      ],
       [
r"(.*)aff|(.*)falo nada",
["Jhin diz: Desculpa","Kalista diz: faz alguma coisa você então"]
      ],
          [
 r"(.*)vai((.*)ch(u+)p((4|a)+)|(.*)m((e|3)+)rd((a|4)+))|(.*)fdp|(.*)c((a|4)+)l((a|4)+)(.*)b((0|o)+)c((a|4)+)|(.*)n((o(o+))|(0(0+))|(0+(o+))|(o+(0+)))b|(.*)l((i|1)+)x((o|0)+)(.*)",
 ["Niveis de toxicidade detectado","por favor mantenha a calma","você sera silenciado caso continue com um comportamento toxico"]
    ],
               [
 r"(.*)pqp|(.*)m((e|3)+)rd((a|4)+)|(.*)b((o|0)+)((s|x)+)t((a|4)+)|(.*)p((o|0)+)(rr|h)((4|a)+)|(.*)dr((0|o)+)g((4|a)+)|(.*) c(u+)|(.*)p(u+)t((4|0|a|o)+)|f((u|o)+)d((i|a|e|u)+)(.*)|(.*)c((4|a)+)r((4|a)+)lh((0|o)+)",
 ["você sera silenciado caso continue com um comportamento toxico","por favor mantenha a calma","Niveis de toxicidade detectado"]
    ],
            [
 r"(.*)time ((.*)h((o|0)+)rr((i|1)+)v((e|3)+)l|r(u+)((i|1)+)m|l((i|1)+)x((o|0)+)|b((o|0)+)((s|x)+)t((a|4)+)|f((u|o|0)+)d((1|4|i|a|e|u)+))(.*)",
 ["você sera silenciado caso continue com um comportamento toxico","por favor mantenha a calma com seu time"]
    ],
            [
 r"(.*)tu (é|e|és)((.*)r(u+)((i|1)+)m|l((i|1)+)x((o|0)+)(.*)|(.*)m((e|3)+)rd((a|4)+)|(.*)b((o|0)+)((s|x)+)t((a|4)+)|(.*)n((o(o+))|(0(0+))|(0+(o+))|(o+(0+)))b|(.*)h((o|0)+)rr((i|1)+)v((e|3)+)l)",
 ["você sera silenciado caso continue com um comportamento toxico","por favor mantenha a calma com outros jogadores","Niveis de toxicidade detectado"]
    ],

      [
 r"quit",
 ["Derrota","Vitória"]
    ],

           [
r"(.*)",
["Uma aliado foi eliminado","Ashe diz: Que droga cara!","um inimigo foi eliminado","Sua torre foi destruida","Sua equipe destruiu uma torre","Seu inibidor foi destruido","o inibidor inimigo foi destruido","Pentakill inimigo","Olaf diz: GG esse jogo já era"]
      ],

       ]


#Função
from nltk.chat.util import Chat, reflections



def chatterbox():
  print("Seu aliado foi eliminado!")
  chat = Chat(toxic, reflections)
  chat.converse()

if __name__ == "__main__":
  chatterbox()       
