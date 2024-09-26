<h1>📧 Python E-mail Automation</h1>
<p>Este projeto Python automatiza o envio de e-mails com anexos utilizando o servidor SMTP do Gmail. Foi desenvolvido para facilitar o envio de relatórios, documentos ou outros arquivos de forma automatizada e segura, utilizando a biblioteca <code>ssl</code> para garantir a proteção dos dados.</p>

<h2>🚀 Funcionalidades</h2>
<ul>
    <li>Envio automático de e-mails para múltiplos destinatários.</li>
    <li>Anexação de arquivos ao e-mail (imagens, PDFs, etc.).</li>
    <li>Envio seguro de e-mails via SMTP utilizando SSL.</li>
</ul>

<h2>📋 Pré-requisitos</h2>
<p>Antes de começar, certifique-se de ter as seguintes bibliotecas instaladas no seu ambiente Python:</p>
<pre><code>pip install email smtplib ssl mimetypes</code></pre>

<h2>🔧 Configuração</h2>
<ol>
    <li><strong>Senha do E-mail</strong>: Crie um arquivo chamado <code>senha</code> no diretório raiz e adicione sua senha de aplicação do Gmail (não utilize sua senha comum). Certifique-se de ativar o "Acesso a apps menos seguros" na conta do Gmail ou crie uma senha específica para o aplicativo nas configurações de segurança da conta Google.</li>
    <li><strong>Corpo do E-mail</strong>: Crie um arquivo <code>corpo.txt</code> dentro da pasta <code>dados/</code> contendo o texto que será o corpo do e-mail.</li>
    <li><strong>Anexo</strong>: Coloque o arquivo que será anexado (por exemplo, <code>bb_preco.png</code>) no mesmo diretório do script e altere o nome do arquivo no código, se necessário.</li>
</ol>

<h2>🗂️ Estrutura do Projeto</h2>
<pre>
<code>
📂 projeto-email-automation/
 ┣ 📜 send_email.py
 ┣ 📂 dados/
 ┃ ┗ 📜 corpo.txt
 ┣ 📜 senha
 ┗ 📜 bb_preco.png
</code>
</pre>

<h2>⚙️ Como usar</h2>
<ol>
    <li>Clone este repositório para o seu ambiente local:
        <pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git</code></pre>
    </li>
    <li>Edite o script <code>send_email.py</code> e ajuste o destinatário, o assunto e o nome do anexo, se necessário:
        <pre><code>
from_email = 'seu-email'
to_email = 'exemplo@gmail.com'
subject = 'Assunto do E-mail'
anexo = 'bb_preco.png'
        </code></pre>
    </li>
    <li>Execute o script:
        <pre><code>python send_email.py</code></pre>
    </li>
</ol>

<h2>📧 Contato</h2>
<p>Se tiver dúvidas, sugestões ou encontrar problemas, sinta-se à vontade para abrir uma issue ou entrar em contato:</p>
<ul>
    https://www.linkedin.com/in/kaiqueamerico/
</ul>

</body>
