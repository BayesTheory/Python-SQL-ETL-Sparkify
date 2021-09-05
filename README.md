## Resumo
 Uma startup chamada Sparkify deseja analisar os dados que coletaram sobre as músicas e a atividade do usuário em seus novos aplicativo de streaming de música. A equipe de análise está particularmente interessada em entender quais músicas os usuários estão ouvindo.Atualmente, eles não têm uma maneira fácil de consultar seus dados, que residem em um diretório de logs JSON sobre a atividade do usuário no aplicativo, bem como um diretório com metadados JSON nas músicas em seu aplicativo.
   
### Como executar:
   - execute o comando para instalar os requisitos.
        > pip install -r requisitos.txt
        
   - execute `` create_tables.py`` para criar banco de dados e tabelas.
   - execute `` etl.py`` para executar o pipeline para ler dados de arquivos de dados e transferir para as respectivas tabelas.
