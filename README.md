## Resumo
 Uma startup chamada Sparkify deseja analisar os dados que coletaram sobre as músicas e a atividade do usuário em seus novos
 aplicativo de streaming de música. A equipe de análise está particularmente interessada em entender quais músicas os usuários estão ouvindo.Atualmente, eles não têm uma maneira fácil de consultar seus dados, que residem em um diretório de logs JSON sobre a atividade do usuário no aplicativo, bem como um diretório com metadados JSON nas músicas em seu aplicativo.

#### Então, para resolver esse problema:
Neste projeto,
   - a modelagem de dados é implementada com Postgres.
   - um pipeline ETL é construído usando Python, que transformará dados de arquivos JSON em tabelas de dimensões 

### Tabelas de dimensão:
   - usuários: contém usuários no aplicativo de música.
   - músicas: contém músicas no banco de dados.
   - artistas: contém artistas no banco de dados.
   - time: timestamp de registros em `songplays` dividido em unidades específicas.
   
### Tabela de fatos:
   - Songplays: registros nos dados de registro associados com as músicas reproduzidas.
   
### Pipeline ETL:
   - transfere dados de dois diretórios locais (data / song_data, data / log_data) para as tabelas usando SQL e Python.
   
### Como executar:
   - execute o comando para instalar os requisitos.
        > pip install -r requisitos.txt
        
   - execute `` create_tables.py`` para criar banco de dados e tabelas.
   - execute `` etl.py`` para executar o pipeline para ler dados de arquivos de dados e transferir para as respectivas tabelas.