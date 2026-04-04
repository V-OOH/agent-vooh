![](https://github.com/V-OOH/agent-vooh/banner.png)

# Agente de Monitoramento VOOH para dispositivos DOOH

Este repositório conta com um projeto acadêmico para captura de dados de dispositivos DOOH, 2º semestre do curso de 
Ciência da Computação da São Paulo Tech School - SPTECH ([@BandTec](https://github.com/BandTec))

# Tecnologias

Este projeto utiliza a biblioteca **psutil** como principal meio de obtenção de dados de dispositivos, capturando
informações de uso dos recursos como:

- CPU
- Memória RAM
- Disco
- Rede
- Processos

Outra biblioteca usada para exibição mais confortável dos dados, é o **colorama**.

## Instalação

Para realizar a instalação do agente, é necessário possuir o **git**, **python3** e seu gerenciador de pacotes **pip**.

Para clonar este repositório, use o seguinte comando no terminal:

```
git clone https://github.com/V-OOH/agent-v-ooh
```

Para instalar as dependências usadas neste projeto, use o seguinte comando em seu terminal, na **raíz do projeto**:

```
pip install -r requeriments.txt
```

### Dispositivos com Linux

Para instalar as dependências em dispositivos com Linux, é recomendável utilizar um ambiente virtual python (venv),
para evitar quebrar o seu sistema.

Utilize o seguinte comando para criar um ambiente virtual:

```
python3 -m venv ~/vooh-venv
```

Para ativar o ambiente virtual, basta executar:

```
source ~/vooh-venv/bin/activate
```

**Observações:**

Caso esteja usando um **shell** que não seja o **bash**, como, por exemplo, o **fish**, use o comando:

```
source ~/vooh-venv/bin/activate.fish
```

## Execução

Com todas as dependências instaladas e/ou ambiente virtual configurado no dispositivo que irá ser monitorado,
você executar o agente com o seguinte comando:

```
python3 main.py [frequência]
```


`frequência` é o tempo em segundos entre capturas

As informações coletadas ficam em `/data`, onde há arquivos .CSV separados para cada componente

