
# Para que serve

Já reparou q sempre a primeira legenda de fala da pessoa instrutora se estende durante a vinheta de abertura da Alura Start? Essa automação Python serve para corrigir a sincronia das legendas automáticas, adicionando um bloco descritivo de música no começo do arquivo VTT. 

## Como usar

Para funcionar, você tem que ter o [Python](https://www.python.org/downloads/) instalado no seu computador. Ai depois disso, você só precisa:

1. Clicar com o botão direito no arquivo `vinheta_start.py`, escolher "Abrir com > Python";
2. Escolher a pasta que contém as legendas VTT que você quer ajustar e clicar em "Selecionar pasta";
3. Aplicar a conversão em lote **2x** nas legendas (ou seja, apertar o botão "Converter" 2 vezes seguidas) no Subtitle Edit.

Prontinho. Lembrando que essa automação vai modificar TODAS as legendas da pasta selecionada, exceto as que contiverem "DROP" ou "O_que_aprendemos" no nome (pois os vídeos "O que aprendemos" não tem vinheta no começo).

> Essa automação serve tanto para as legendas em português, espanhol e inglês.
