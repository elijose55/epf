def cadastro ():
	d={
	'clientes': {

	},
	'cozinheiro': {
	  }
	}

	if w=='2':    
    x=str(input('Voce gostaria de se inscrever como:'))
    if x=='1': ##cozinheiro
      i=0
      while i==0:
        x=str(input('Login:'))
        if x not in d[cozinheiro]:
          d['cozinheiro'][x]={}
          i=1
        else:
          print('Login usado')
          
      h=str(input('Nome:'))
      d['cozinheiro'][x]['nome']=h
    
      h=str(input('Email:'))
      d['cozinheiro'][x]['email']=h
    
      h=str(input('Senha:'))
      d['cozinheiro'][x]['senha']=h
    
      h=str(input('Endereco:'))
      d['cozinheiro'][x]['endereco']=h
    
      h=str(input('Celular:'))
      d['cozinheiro'][x]['celular']=h
    
      h=str(input('Nome do Restaurante:'))
      d['cozinheiro'][x]['restaurante']=h
    
      h=str(input('Descricao do restaurante:'))
      d['cozinheiro'][x]['descricao']=h
    
      h=str(input('bairro:'))
      d['cozinheiro'][x]['bairro']=h
    
    
    
    if x=='1': ##cozinheiro
      x=str(input('Nome:'))
      d['clientes'][x]={}
      d['clientes'][x]['nome']=x
    
      h=str(input('Email:'))
      d['clientes'][x]['email']=h
    
      h=str(input('Senha:'))
      d['clientes'][x]['senha']=h
    
      h=str(input('Endereco:'))
      d['clientes'][x]['endereco']=h
    
      h=str(input('Celular:'))
      d['clientes'][x]['celular']=h
    
      h=str(input('bairro:'))
      d['clientes'][x]['bairro']=h
    

  
    
    

print(d)

pass

def login ():
	d={
	'clientes': {

	},
	'cozinheiro': {
	  }
	}


while True:
  w=str(input('Login (1) ou Cadastro (2)'))
  
  if w=='1':
    l=str(input('Login:'))
    s=str(input('Senha'))
    
    if l in d['cozinheiro']:
      if d['cozinheiro'][l]['senha']==s:
        print('Login Bem-Sucedido')
      else:
        print('Login ou Senha errados')
    else:
      print('Login ou Senha errados')
      
    if l in d['clientes']:
      if d['cozinheiro'][l]['senha']==s:
        print('Login Bem-Sucedido')
      else:
        print('Login ou Senha errados')
    else:
      print('Login ou Senha errados')
      
pass

def cliente ():
pass

def pagina_restaurante ():
pass

def cardapio ():
pass

def restaurantes_proximos ():
pass

def carrinho ():
pass

def pedido_recebido ():
pass

def fim ():
break

