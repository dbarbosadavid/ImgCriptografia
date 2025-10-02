# ImageTextCrypt - Criptografia de Texto em Imagens PNG

Este é um pequeno utilitário em Python que permite **esconder texto dentro de imagens PNG** modificando diretamente os valores de pixels, e também recuperar esse texto depois. A ideia é simples, mas demonstra bem os princípios básicos de esteganografia.

---

## Funcionalidades

**Encriptação**: Escreve texto no canal vermelho de pixels da imagem.
**Decriptação**: Lê o texto escondido anteriormente na imagem.

Verificação se o arquivo é um PNG válido.
Ideal para fins didáticos e demonstrações simples de esteganografia.

---


## Requisitos

- Python 3.x
- Pillow
- unidecode

## Para rodar em Python 3 

### Instalar dependências

```bash
py -m pip install Pillow unidecode
```

* Executar 
- Para esconder o texto na imagem:
```
py encriptar.py caminho/da/imagem.png "texto para encriptar"
```

- Para revelar o texto escondido
```
py encriptar.py caminho/da/imagem.png --decript
```


# PROJETO FEITO PARA FINS ACADÊMICOS
Desenvolvido por David, Isabelle e Isabelly
