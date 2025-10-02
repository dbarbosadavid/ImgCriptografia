from PIL import Image
import unidecode
import argparse
import os
import sys

def encriptar(img, text):
    pixels = img.load()
    print(pixels)
    for i in range(len(text)):
        r, g, b = pixels[0, i]
        b = ord(text[i])
        pixels[0, i] = (r, g, b)
    return img

def decriptar(img, max_len=100):
    pixels = img.load()
    texto = ''
    for i in range(max_len):
        r, g, b = pixels[0, i]
        char = chr(b)
        char_normalize = unidecode.unidecode(char).lower()
        if not char == char_normalize:
            break
        texto += char
    return texto

def save_image(imgCriptada, output_path="cript.png"):
    imgCriptada.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Encriptação/Decriptação de texto em imagem.")
    parser.add_argument("image_path", help="Caminho da imagem")
    parser.add_argument("text", nargs="?", help="Texto a ser encriptado (necessário se não usar --decript)")
    parser.add_argument("--decript", action="store_true", help="Decriptar imagem ao invés de encriptar")

    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Erro: imagem '{args.image_path}' não encontrada.")
        sys.exit(1)

    if not os.path.exists(args.image_path):
        print(f"Erro: imagem '{args.image_path}' não encontrada.")
        sys.exit(1)

    if not args.image_path.lower().endswith('.png'):
        print("Erro: apenas arquivos PNG são suportados.")
        sys.exit(1)

    img = Image.open(args.image_path).convert("RGB")
    if img is None:
        print(f"Erro ao carregar imagem '{args.image_path}'.")
        sys.exit(1)

    if args.decript:
        texto_decriptado = decriptar(img)
        print("Texto decriptado:", texto_decriptado)
    else:
        if not args.text:
            print("Erro: você deve fornecer o texto para encriptar, ou usar a opção --decript.")
            sys.exit(1)

        text_normal = unidecode.unidecode(args.text).lower()

        if len(text_normal) > img.height:
            print("Erro: Texto muito grande para ser encriptado nesta imagem.")
            sys.exit(1)

        imgCriptada = encriptar(img, text_normal)
        save_image(imgCriptada)
        print("Imagem criptografada salva como 'cript.png'.")

if __name__ == "__main__":
    main()
