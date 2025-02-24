
## Para que serve

Já reparou que a primeira legenda de fala da pessoa instrutora sempre se estende durante a vinheta de abertura da Alura Start? Essa automação Python serve para corrigir a sincronia das legendas automáticas, adicionando um bloco descritivo de música no começo do arquivo VTT.

![Captura de tela de antes e depois da legenda sincronizada.](https://github.com/user-attachments/assets/3f8761be-0920-4822-804d-556ad51ad6b7)

## Como usar

Para funcionar, você tem que ter o [Python](https://www.python.org/downloads/) instalado no seu computador. Ai depois disso, você só precisa:

1. Clicar com o botão direito no arquivo `vinheta_start.py`, escolher "Abrir com > Python";
![Captura de tela do passo 1](https://github.com/user-attachments/assets/b2b87d13-78bd-4e1d-bea9-63107f8b2d99)

2. Escolher a pasta que contém as legendas VTT que você quer ajustar e clicar em "Selecionar pasta";
![Captura de tela do passo 2](https://github.com/user-attachments/assets/2cdfee11-5663-4b64-967c-a0966ffad91f)

3. Aplicar a conversão em lote **2x** nas legendas (ou seja, apertar o botão "Converter" 2 vezes seguidas) no Subtitle Edit.
![Captura de tela do passo 3](https://github.com/user-attachments/assets/c19ca215-5b09-4fcf-9635-e7170b89b292)

Prontinho. Lembrando que essa automação vai modificar TODAS as legendas da pasta selecionada, exceto as que contiverem "DROP" ou "O_que_aprendemos" no nome (pois os vídeos "O que aprendemos" não tem vinheta no começo).

> Essa automação serve tanto para as legendas em português, espanhol e inglês.
