# Projeto de Robô com Raspberry Pi

Este repositório contém o código e a documentação do meu projeto de robô, que estou desenvolvendo utilizando um Raspberry Pi e motores DC controlados por GPIO. O objetivo deste projeto é criar um robô que possa ser controlado remotamente e realizar tarefas específicas.

## Visão Geral

O robô é composto por:

- **Raspberry Pi**: O cérebro do robô, responsável por processar os comandos e controlar os motores.
- **Motores DC**: Usados para movimentar o robô, controlados pelos pinos GPIO do Raspberry Pi.
- **Sensores**: Diversos sensores para fornecer feedback ao robô, permitindo que ele reaja ao ambiente.
- **Bateria**: Fonte de energia para todos os componentes do robô.

## Funcionalidades

- **Controle Remoto**: O robô pode ser controlado remotamente através de uma interface web.
- **Navegação Autônoma**: Usando sensores, o robô pode navegar de forma autônoma evitando obstáculos.
- **Coleta de Dados**: O robô pode coletar e enviar dados de localização para um aplicativo web, onde os dados são plotados em um mapa usando Streamlit.

## Estrutura do Repositório

- **/src**: Contém o código-fonte do robô.
  - **main.py**: Script principal para controlar o robô.
  - **motor_control.py**: Biblioteca para controle dos motores DC.
  - **sensor_reading.py**: Biblioteca para leitura dos sensores.
- **/docs**: Documentação do projeto.
  - **setup.md**: Instruções para configurar o ambiente de desenvolvimento.
  - **usage.md**: Guia de uso do robô e suas funcionalidades.
- **/assets**: Imagens e outros arquivos de mídia.
- **README.md**: Este arquivo, fornecendo uma visão geral do projeto.

## Como Configurar

1. Clone este repositório: `git clone https://github.com/seu-usuario/seu-repositorio.git`
2. Navegue até o diretório do projeto: `cd seu-repositorio`
3. Instale as dependências: `pip install -r requirements.txt`
4. Siga as instruções no arquivo `docs/setup.md` para configurar o Raspberry Pi e os componentes do robô.

## Como Usar

1. Ligue o Raspberry Pi e conecte todos os componentes.
2. Execute o script principal: `python src/main.py`
3. Acesse a interface web para controlar o robô ou monitore a navegação autônoma.

Para mais detalhes, consulte a documentação no diretório `docs`.

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
