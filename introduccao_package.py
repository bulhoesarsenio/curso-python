from translate import Translator


def traduzir(texto, idioma_destino):
    translator = Translator(to_lang=idioma_destino)
    traducao = translator.translate(texto)
    return traducao


texto_para_traduzir = "Olá, mundo!"
idioma_destino = "en"  # Código do idioma de destino (exemplo: "en" para inglês)

texto_traduzido = traduzir(texto_para_traduzir, idioma_destino)
print(f"Texto original: {texto_para_traduzir}")
print(f"Texto traduzido para {idioma_destino}: {texto_traduzido}")
