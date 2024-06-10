import smtplib, ssl
import creds

def send_email(message):
    host = creds.host
    port = creds.port

    username = creds.username
    password = creds.password

    receiver = creds.username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

