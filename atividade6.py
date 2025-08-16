login = input("digite seu login:")
senha = input("digite sua senha:")
if login == "admin" and senha == "admin":
    print("acesso permitido")
else: print("acesso negado")
if login == "admin" and senha != "admin":
    print("senha incorreta")   
