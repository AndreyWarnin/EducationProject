def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not is_address_valid(recipient) or not is_address_valid(sender):
        print(f'Невозможно отправить письмо '
              f'с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено '
              f'с адреса {sender} на адрес {recipient}')
    else:
        print(
            f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено '
            f'с адреса {sender} на адрес {recipient}')

def is_address_valid(address):
    domains = ['.com', '.ru', '.net']
    if not address.__contains__('@'):
        return False
    for domain in domains:
        if address.__contains__(domain):
            return True
    return False


send_email("Проверка связи 1", "recipient@gmail.com")  # correct
send_email("Проверка связи 2", "recipient@gmail.com", sender="university.help@gmail.ru")  # correct
send_email("Проверка связи 3", "recipient@gmail.com", sender="university.help@gmail.net")  # same sender
send_email("Проверка связи 4", "recipientgmail.ru", sender="university.help@gmail.com")  # unable to send
send_email("Проверка связи 5", "recipient@gmail.su", sender="university.help@gmail.com")  # unable to send
send_email("I'm an ice king", "recipient@gmail.su", sender="aniceking@gmail.com")  # unexpected sender
