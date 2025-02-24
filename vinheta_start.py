import os
import re
from tkinter import Tk, filedialog, messagebox

# duração HH:MM:SS.Mseg
duracao_vinheta_start = "00:00:04.000"

def adicionar_descricao_vinheta_start(texto_legenda):
    # Remover caracteres invisíveis do BOM antes da verificação
    texto_legenda_limpo = texto_legenda.lstrip('\ufeff\n\r\t ')

    # Adicionar o bloco de música de abertura
    if texto_legenda_limpo.startswith("WEBVTT"):
        bloco_musica = f"00:00:00.000 --> {duracao_vinheta_start}\n[♪]"
        texto_legenda = texto_legenda.replace("WEBVTT", "WEBVTT\n\n" + bloco_musica, 1)
    
    return texto_legenda

def definir_inicio_e_deslocar_o_resto(texto_legenda):
    # Encontrar todos os blocos de legenda
    padrao_blocos = re.findall(
        r"(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})\n(.+?(?:\n.+?)?)\n*(?=\d{2}:\d{2}:\d{2}\.\d{3}|$)",
        texto_legenda, re.DOTALL
    )

    # Modificar o tempo inicial do segundo bloco e unir com o terceiro
    if len(padrao_blocos) >= 3:
        novo_fim = padrao_blocos[2][1]  # Tempo final do terceiro bloco
        novo_texto = f"{padrao_blocos[1][2].strip()}\n{padrao_blocos[2][2].strip()}"

        # Construir o novo bloco
        bloco_novo = f"{duracao_vinheta_start} --> {novo_fim}\n{novo_texto}"

        # Encontrar os blocos originais para substituição
        bloco1_pattern = re.escape(f"{padrao_blocos[1][0]} --> {padrao_blocos[1][1]}\n{padrao_blocos[1][2].strip()}")
        bloco2_pattern = re.escape(f"{padrao_blocos[2][0]} --> {padrao_blocos[2][1]}\n{padrao_blocos[2][2].strip()}")

        # Substituir os blocos antigos pelo novo
        texto_legenda = re.sub(f"{bloco1_pattern}\n+{bloco2_pattern}", bloco_novo, texto_legenda, count=1)

    return texto_legenda

# processar apenas os arquivos das aulas, sem os DROPS
def processar_arquivos_legenda(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.vtt') and not ("DROP" in arquivo or "O_que_aprendemos" in arquivo):
            caminho_arquivo = os.path.join(pasta, arquivo)
            with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                texto_legenda = file.read()

            texto_ajustado = adicionar_descricao_vinheta_start(texto_legenda)
            texto_ajustado = definir_inicio_e_deslocar_o_resto(texto_ajustado)

            with open(caminho_arquivo, 'w', encoding='utf-8') as file:
                file.write(texto_ajustado)

    messagebox.showinfo("Concluído", f"Todos os arquivos VTT da pasta {pasta} foram processados.")


def selecionar_pasta():
    root = Tk()
    root.withdraw()
    caminho_pasta = filedialog.askdirectory(initialdir="C:/", title="Escolha um diretório para processar os arquivos de legenda da Start")
    root.destroy()

    if not caminho_pasta:
        messagebox.showwarning("Aviso", "A seleção de diretório foi cancelada.")
    else:
        processar_arquivos_legenda(caminho_pasta)

if __name__ == "__main__":
    selecionar_pasta()