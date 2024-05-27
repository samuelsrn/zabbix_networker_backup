# zabbix_networker_backup
Script em Python para monitoramento de Jobs de Backup ferramenta EMC NetWorker Dell

# Como utilizar
Adicione o script ao diretório de scripsts no Zabbix proxy ou server.

Os dados de conexão SSH no servidor de Backup devem ser colocadas dentro do script nas variáveis indicadas.

Crie um item Type External check no seu IC e coloque o nome do script.

O Script fará a conexão com o servidor de aplicação de backup no NetWorker e fará um "cat" no arquivo de log do output. O caminho padrão do arquivo está configurado no Script caso seja necessário, alterar na variável "diretorio_log".

O retorno para o Zabbix será um JSON com as informações de backup do "workflow name" da última hora em que o script rodou.
