import sys

class Login():
    def login(self):
        print(39*'#','\n Tela Login - @WelingtonMorais\n',39*'#')
        login=str(input("Usuário: "))
        senha=str(input("Senha: "))
        login_bd='MeuUsuario'
        senha_bd='123'
        if login != login_bd or senha != senha_bd:
            print ('Usuário ou Senha não confere')
            self.login()
        else:
            print ('Logado')
            self.cadastro()

    def menu(self):
       print('\n',39*'#','\n MENU - @WelingtonMorais\n',39*'#')
       print('[1] Novo Cadastro \n[2] Listar Cadastro\n[3] Analisar Texto\n[4] Sair do Programa')

       select=str(input('Informe a opção desejada: '))

       if select == '1':
           self.cadastro()
       elif select == '2':
            self.mostra_cadastro()
       elif select == '3':
            self.analise()
       elif select == '4':
            print ('Sair')
            sys.exit()
       else:
            print ('INFORMAÇÃO INVALIDA,TENTE NOVAMENTE')
            self.menu()
            
       
       
    def cadastro(self):
       print('\n',39*'#','\n ÁREA CADASTRO - @WelingtonMorais\n',39*'#')
       self.nome=(input('Informe seu Nome Completo: '))
       self.idade=(input('Idade: '))
       self.cpf=(input('Cpf: '))
       self.estado=(input('Estado: '))
       self.cidade=(input('Cidade: '))
       self.tel=(input('Telefone: '))
       print('CADASTRO REALIZADO COM SUCESSO...')
       self.texto()

    def texto(self):
        print('\n',39*'#','\n BREVE TEXTO - @WelingtonMorais\n',39*'#')
        self.text=str(input('Digite um breve texto sobre você: \n'))
        print("TEXTO ESCRITO POR: ",self.nome,',',self.idade,'anos','\nDE: ',self.estado,',',self.cidade)
        self.menu()


    def mostra_cadastro(self):
            print('\n',39*'#','\n CADASTRO REALIZADO - @WelingtonMorais\n',39*'#')
            print('Nome: ',self.nome)
            print('Idade: ',self.idade)
            print('CPF: ',self.cpf)
            print('Estado: ',self.estado)
            print('Cidade: ',self.cidade)
            print('Telefone: ',self.tel)
            self.menu()

    def analise(self):
        self.text=self.text.lower()

        self.text= self.text.replace(" ","")
        self.text = self.text.replace("\n","")
        self.text =self.text.replace(".","")
        self.text = self.text.replace("!","")
        self.text = self.text.replace("?","")
        self.text = self.text.replace(",","")
        self.text = self.text.replace(";","")
        #removem acentos e cedilha
        self.text = self.text.replace("á","a")
        self.text = self.text.replace("à","a")
        self.text = self.text.replace("ã","a")
        self.text = self.text.replace("é","e")
        self.text = self.text.replace("ê","e")
        self.text = self.text.replace("í","i")
        self.text = self.text.replace("ó","o")
        self.text = self.text.replace("ô","o")
        self.text = self.text.replace("ú","u")
        self.text = self.text.replace("ç","c")

        vogais = 0
        consoantes = 0
        for caracter in self.text:
            if caracter in 'aeiou':
                vogais = vogais + 1
            else:
              consoantes = consoantes + 1
        print('\n',39*'#','\n ÁREA ANÁLISE DO TEXTO- @WelingtonMorais\n',39*'#')
        print('TEXTO: ',self.text)
        print ("   [*]Vogais: ",vogais)
        print ("   [*]Consoantes: ",consoantes)
        print ("   [*]Total de letras: ",(len(self.text)))
        self.menu()

        
cad=Login()
cad.login()
