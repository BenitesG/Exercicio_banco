import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
          self.nome = nome
          self.idade = idade
        
    @property
    def idade(self) -> int: 
        return self._idade 
     
    @property
    def nome(self) -> str:
        return self._nome
     
    @idade.setter
    def idade(self, a: int) -> int:
        if(a < 18): 
            raise ValueError('Sua idade não é permitida para criar uma conta') 
        self._idade = a 
        return a
           
    @nome.setter
    def nome(self, b: str) -> str:
            str_b = (str(b))
            if b is not str_b or len(b) < 3:
                raise ValueError('Você não lançou um nome!')   
            self._nome = b
            return b
    
    def __repr__(self):
        class_name = type(self).__name__   
        attrs = f'{self.nome!r}, {self.idade!r}'   
        return f'{class_name} {attrs}'        

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
         super().__init__(nome, idade)
         self.conta: contas.Conta | None = None
        


if __name__ == '__main__':
    c1 = Cliente('Gabriel', 18)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    print('#--------#')
    c2 = Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(145, 233, 100)
    print(c2)
    print(c2.conta)

    

  
        
