<h1 align="center">
  <img src="../docs/logo.svg" height="300" width="300" alt="Logo VMAP" /><br>
  VMAP
</h1>

![GitHub License](https://img.shields.io/github/license/LucasGoncSilva/vmap?labelColor=101010)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/LucasGoncSilva/vmap/unittest.yml?style=flat&labelColor=%23101010)

Trabalhando nas atualizações semanais dos sistemas, quatro indivíduos perceberam a necessidade de possuir um registro eficiente para documentar as deploys e as tarefas de cada deploy, tanto o que é aprovado quanto o que, por algum problema, volta para desenvolvimento. Após a ideia do internamente eleito PO do projeto Daniel, nasceu o Visualization and Management Platform.<br>
Criado em Django como Framework MVC, o VMAP tem como principal objetivo armazenar de forma organizada e estruturada as tarefas deploy por deploy, registrando os sistemas e projetos de impactos de cada tarefa, juntamente com o resultado: Ok ou Rollback.<br>
Cada diferente seção do projeto está organizada de forma bem específica em seu diretório, utilizando do conceito de modularidade. Esta estrutura facilita a localização dos elementos com base eu sua funcionalidade, objetivo ou finalidade. Detalhes sobre a estrutura de diretórios a seguir:

```bash
.
├── .github                               # Diretório de arquivos de repositório
│   ├── README.md                         # Arquivo exibido na raíz do repositório
│   └── workflows                         # Sub-diretório de pipelines de manutenção
│
├── build.sh                              # Script de deploy via Render
│
├── docker                                # Diretório de arquivos Docker
│   ├── docker-compose-dev.yml            # Orquestrador para desenvolvimento
│   ├── docker-compose-unittest.yml       # Orquestrador para testes
│   ├── docker-compose.yml                # Orquestrador em caráter de produção
│   └── Dockerfile                        # Criador da imagem do projeto
│
├── docs                                  # Diretório de arquivos de documentação
│   ├── db                                # Documentação referente ao Banco de Dados
│   ├── logo.svg                          # Logo do projeto
│   └── web                               # Documentação referente à arquitetura do projeto
│
├── LICENSE                               # Arquivo de licença
│
├── loadtests                             # Diretório de testes de carga
│   ├── load_test.py                      # Script para teste de carga do tipo Load
│   ├── soak_test.py                      # Script para teste de carga do tipo Soak
│   ├── spike_test.py                     # Script para teste de carga do tipo Spike
│   ├── stress_test.py                    # Script para teste de carga do tipo Stress
│   └── utils.py                          # Script utilitário para os testes de carga
│
├── report                                # Diretório de relatórios autogerados
│   ├── csv                               # Sub-diretório de relatórios CSV
│   └── html                              # Sub-diretório de relatórios HTML
│
├── requirements.dev.txt                  # Arquivo de dependências de desenvolvimento
│
└── VMAP                                  # Diretório do projeto Django
    ├── CORE                              # App de configurações
    ├── manage.py                         # Script de operações administrativas
    ├── requirements.txt                  # Arquivo de dependências de produção
    └── ...                               # Apps de produção

```

<br>

## Stack

![HTML logo](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS logo](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Sass logo](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![JavaScript logo](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Bootstrap logo](https://img.shields.io/badge/Bootstrap-712cf9?style=for-the-badge&logo=bootstrap&logoColor=712cf9&color=fff)

![Django logo](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

![PostgreSQL logo](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

![Docker logo](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Render logo](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=000&color=fff)
![Supabase Logo](https://img.shields.io/badge/Supabase-181818?style=for-the-badge&logo=supabase&logoColor=3ecf8e)

<br>

## Arquitetura

### VMAP

![Arquitetura do Projeto em caráter global](../docs/web/VMAP_architecture.svg)

### DB

![Arquitetura do Banco de Dados](../docs/db/VMAP_db_schema.svg)

<br>

## Requisitos

Para cada seção do projeto, definidas por diretórios, há uma atribuição única onde para cada atribuição, requisitos próprios são necessários para a utilização. Acompanhe abaixo os requisitos para utilização de cada módulo do VMAP - valendo lembrar que é recomendado instalar as dependências diretas do projeto dentro de um ambiente virtual:

* `VMAP/` - por razões óbvias, possuir [Python](https://www.python.org/) e rodar `pip install -r requirements.txt`
* `docker/` - possuir as engines do [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) para criação e inicialização dos containers contendo as imagens do projeto
* `docs/` - possuir [NodeJS](https://nodejs.org/en/), [NPM](https://www.npmjs.com/) ou equivalente e instalar [DBDocs](https://dbdocs.io/docs)
* `loadtests/` - possuir [Python](https://www.python.org/) e rodar `pip install -r requirements.dev.txt` para instalar [Locust](https://locust.io/)

## Desenvolvendo

### VMAP - `vmap/VMAP/`

#### Realizar Migrações (Atualizações) de Banco de Dados

`python manager.py makemigrations`

#### Atualizar Estrutura do Banco de Dados com Novas Migrações

`python manager.py migrate`

#### Iniciar Testes Automatizados

`python manager.py test`

#### Iniciar o Servidor de Desenvolvimento

`python manager.py runserver`

#### Criar Superusuário

`python manage.py createsuperuser`

### Docker - `vmap/`

#### Criar Container Orquestrado

`docker compose up --build` para `docker-compose.yml`
ou
`docker compose -f docker-compose-[dev/unittest] up --build` para `docker-compose-dev.yml` ou `docker-compose-unittest.yml`

### Loadtests - `vmap` - Aplicação Rodando (local ou via docker)

#### Rodar Teste "Stress"

`locust --headless -f loadtests/stress_test.py -H http://localhost:8000 --processes -1 --csv report/csv/load/stress --html report/html/stress.html`

#### Rodar Teste "Load"

`locust --headless -f loadtests/load_test.py -H http://localhost:8000 --processes -1 --csv report/csv/load/load --html report/html/load.html`

#### Rodar Teste "Soak"

`locust --headless -f loadtests/soak_test.py -H http://localhost:8000 --processes -1 --csv report/csv/load/soak --html report/html/soak.html`

#### Rodar Teste "Spike"

`locust --headless -f loadtests/spike_test.py -H http://localhost:8000 --processes -1 --csv report/csv/load/spike --html report/html/spike.html`

### Docs - `vmap/`

#### Gerar Documentação do DB

`dbdocs login` seguido de `dbdocs build docs/db/VMAP_db_schema.dbml`

<br>

## Licença

This project is under [MPLv2 - Mozilla Public License Version 2.0](https://choosealicense.com/licenses/mpl-2.0/). Permissions of this weak copyleft license are conditioned on making available source code of licensed files and modifications of those files under the same license (or in certain cases, one of the GNU licenses). Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. However, a larger work using the licensed work may be distributed under different terms and without source code for files added in the larger work.

<br>

## Autores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LucasGoncSilva" title="GitHub">
        <img style="border-radius: 50%;" src="https://picsum.photos/200" width="100px;" alt=""/>
        <br>
        <b>Andrade, Daniel</b>
      </a>
      <br>
      <sub><a href="https://www.linkedin.com/in/luksgonc/" title="LinkedIn">LinkedIn</a></sub>
    </td>
    <td style="width: 70ch;">Se ser o cara que decide for um crime, prenda-o por tal delito. O menino Daniel é o eleito líder, PO, quem decide o que ninguém consegue. Um n*gão de tirar o chapéu.</td>
    <td align="center">
      <a href="https://github.com/andersonjader0" title="GitHub">
        <img style="border-radius: 50%;" src="https://github.com/andersonjader0.png?size=100" width="100px;" alt=""/>
        <br>
        <b>Jader, Anderson</b>
      </a>
      <br>
      <sub><a href="https://www.linkedin.com/in/anderson-j-710685235/" title="LinkedIn">LinkedIn</a></sub>
    </td>
    <td style="width: 70ch;">O mano do Front-End, apesar de estar se aventurando no outro lado da fora. O mais experiente em desenvolvimento de interfaces responsivas e piadas ruins.</td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/LucasGoncSilva" title="GitHub">
        <img style="border-radius: 50%;" src="https://github.com/LucasGoncSilva.png?size=100" width="100px;" alt=""/>
        <br>
        <b>Gonçalves, Lucas</b>
      </a>
      <br>
      <sub><a href="https://www.linkedin.com/in/luksgonc/" title="LinkedIn">LinkedIn</a></sub>
    </td>
    <td style="width: 70ch;">Responsável pela maior parte das tarefas administrativas, é como o faxineiro-secretário, contribuiu com estrutura do projeto e o Back-end da plataforma.</td>
    <td align="center">
      <a href="https://github.com/Vinefonseca" title="GitHub">
        <img style="border-radius: 50%;" src="https://github.com/Vinefonseca.png?size=100" width="100px;" alt=""/>
        <br>
        <b>Fonseca, Vinicius</b>
      </a>
      <br>
      <sub><a href="https://www.linkedin.com/in/vin%C3%ADcius-fonseca-barbosa-230147245/" title="LinkedIn">LinkedIn</a></sub>
    </td>
    <td style="width: 70ch;">A.K.A Vicinius, foi o arquiteto do Banco de Dados, autor da logo e maior opinador crítico, também o maior motivador da equipe (quando ele mesmo motivado).</td>
  </tr>
</table>
