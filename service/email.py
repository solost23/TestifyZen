import yamail


def send(config: dict, subject: str, contents: str, attachments: list = []):
    email = config['email']
    yag = yamail.SMTP(
        user=email['user'],
        password=email['password']
    )
    yag.send(email['receivers'], subject, contents, attachments)
    yag.close()
