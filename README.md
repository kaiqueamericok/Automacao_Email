📧 Python E-mail Automation
Este script Python automatiza o envio de e-mails com anexos usando o servidor SMTP do Gmail. Ele foi desenvolvido para facilitar o envio de relatórios, documentos ou quaisquer outros arquivos por e-mail, de forma automatizada e segura, usando a biblioteca ssl para garantir a proteção dos dados.

🚀 Funcionalidades
Envio automático de e-mails para múltiplos destinatários.
Anexação de arquivos no e-mail (imagens, PDFs, etc.).
Envio seguro de e-mails via SMTP com SSL.<p>
📋 Pré-requisitos
Antes de começar, você vai precisar das seguintes bibliotecas instaladas no seu ambiente Python
pip install email smtplib ssl mimetypes

🔧 Configuração
Senha do E-mail: Crie um arquivo senha no diretório raiz e adicione sua senha de aplicação do Gmail (não use sua senha comum). Lembre-se de ativar o "Acesso a apps menos seguros" na conta do Gmail ou criar uma senha específica para a aplicação no Google Account.

Corpo do E-mail: Crie um arquivo corpo.txt dentro da pasta dados/ contendo o conteúdo do corpo do e-mail que será enviado.

Anexo: Coloque o arquivo a ser anexado no mesmo diretório do script e altere o nome do arquivo no código, se necessário.

Estrutura do Projeto:

📂 projeto-email-automation/<p>
 ┣ 📜 send_email.py<p>
 ┣ 📂 dados/<p>
 ┃ ┗ 📜 corpo.txt<p>
 ┣ 📜 senha<p>
 ┗ 📜 bb_preco.png<p>
