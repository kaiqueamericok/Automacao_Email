from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = open('senha', 'r').read()
from_email = 'kaiquetecnologia5@gmail.com'
to_email = 'kaiquemathor@gmail.com , kaiquetecnologia5@gmail.com'
subject = 'Consultoria de T.I'
body = open('dados/index.html.txt', 'r', encoding='utf-8').read()

# 1 - Montando estrtura do e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body, subtype='html')
safe = ssl.create_default_context()

# 2 - Adicionar Anexo

anexo = 'dados/corpo.txt'
#print(mimetypes.guess_type(anexo)[0])
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

# 3 - Envio de e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )