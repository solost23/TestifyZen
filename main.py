from config.config import read_config
from service.email import send

if __name__ == '__main__':
    send(read_config(), '邮件主题', '邮件正文', ['driver/chromedriver'])

