from email.message import EmailMessage
import smtplib
import ssl

password = open('senha', 'r').read()
#print(password)
from_email = 'seu-email@gmail.com'
to_email = 'destino@gmail.com , destino2@gmail.com'
subject = 'Consultoria T.I'
body = '''
Prezados,

Espero que esta mensagem os encontre bem.

Meu nome é Kaique, e atuo na área de Tecnologia da Informação há mais de 10 anos, com especialização em desenvolvimento de software, infraestrutura de TI e soluções em nuvem, especialmente no Microsoft Azure. Com uma vasta experiência em projetos de alta complexidade e uma forte habilidade em arquitetar, implementar e gerenciar soluções robustas e escaláveis, acredito que posso contribuir significativamente para os desafios tecnológicos da sua empresa.

Desenvolvimento de Software: Minha trajetória inclui o desenvolvimento de aplicações utilizando diversas stacks tecnológicas, desde back-end (com .NET, Java, Python) até front-end (React, Angular). Tenho expertise em microserviços, APIs RESTful e na integração contínua (CI/CD) para otimização de entregas e qualidade do código.

Infraestrutura de TI: Ao longo dos anos, adquiri uma compreensão profunda da infraestrutura de TI, desde o gerenciamento de servidores on-premises até a migração para ambientes híbridos. Tenho experiência em administrar e configurar sistemas operacionais, redes, servidores, e storages, garantindo a alta disponibilidade e segurança dos sistemas.

Cloud Computing e Microsoft Azure: Nos últimos anos, foquei em soluções de cloud, com uma ênfase especial no Microsoft Azure. Possuo certificações e experiência prática em arquiteturas serverless, containers (AKS), bancos de dados gerenciados (Azure SQL, Cosmos DB) e otimização de custos em cloud. Além disso, tenho trabalhado em projetos de automação e infraestrutura como código (IaC) usando Terraform e ARM templates.

Estou à disposição para discutir como posso apoiar sua empresa na superação dos desafios atuais e no alcance de seus objetivos de transformação digital. Acredito que minha experiência e conhecimento técnico podem agregar valor significativo ao seu time de TI.

Fico no aguardo de uma oportunidade para conversarmos mais detalhadamente.

Atenciosamente,
'''
# 1 - Estrutrando a mensagem via e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 2 - envio de e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp: 
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
