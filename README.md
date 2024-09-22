# Dependências da API

Todo o código foi estruturado para rodar no Ubuntu-24.04, caso seu sistema operacional seja diferente, estará executando por sua própria conta e risco

## Python

Por padrão, o sistema operacional já vem com o python 3.12 que é o que iremos usar.

### Poetry (Gerenciador de Pacotes do Python)

Para instalar as dependencias de execução do projeto, iremos usar o `poetry`. A baixo estão os comandos para garantir a instalação e execução com sucesso

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```

```bash
pipx install poetry
```

```bash
poetry config virtualenvs.in-project true
```

```bash
poetry env use python3.12
```

```bash
poetry install
```

## Docker

Você precisará ter o docker instalado para iniciar o banco de dados, então instale usando os comandos a baixo:

Atualização do sistema e download do Docker

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Adicionando o repositório do Docker na lista de sources do Ubuntu:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Dando permissão para rodar o Docker com seu usuário corrente:

```bash
sudo usermod -aG docker $USER
```

Instalando Docker-Compose

```bash
sudo apt  install docker-compose
```

Reinicie o WSL
Pronto, seu Docker está instalado.

Caso aconteça algum erro, execute:

```bash
 sudo apt-get update
 sudo apt-get install docker-compose-plugin
```

```bash
poetry add docker-compose
```

## Makefile para automações

Caso queira facilitar sua vida usando comandos longos, use o arquivo [makefile](Makefile) para te ajudar a executar comandos

## Erros Absurdos

```bash
ImportError while loading conftest '/api/app/tests/test_use_case/conftest.py'.
```

Este erro consiste no pytest sendo fresco, fazendo-te reiniciar o pc várias vezes até que ele identifice o ambiente virutal corretamente.

O Git pode estar ignorando as regras do seu .gitignore porque os arquivos já foram rastreados anteriormente. Quando os arquivos são rastreados pelo Git, mesmo que você os adicione ao .gitignore, eles ainda continuarão no índice (cache) do Git.

ocê precisa remover os arquivos rastreados do cache do Git sem removê-los fisicamente do seu diretório de trabalho. Isso pode ser feito com o comando git rm --cached.

Ex:

```bash
git rm -r --cached api/app/images/*.png
git rm -r --cached api/app/images/*.jpg
```
