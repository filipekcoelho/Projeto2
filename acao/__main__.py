
import es
from proc import Acao 

def main():
    # Leitura de dados
    dados = es.leitora()
    
    # Instanciamento do objeto
    acao = Acao(dados[0], dados[1])
    
    # Saída de dados
    es.impressora(acao)
    
if __name__ == "__main__":
    main()