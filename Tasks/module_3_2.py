import os

os.system('cls')

print("Home work with function calls...")

def send_mail(message, recipient, *, sender='university.help@gmail.com'):
    
    print(f"\ntry to send mail '{message}'\nfrom: < {sender} > to < {recipient} > ...")
    ## get tail
    rec_tail = recipient[len(recipient) - 3:]
    sen_tail = sender[len(sender) - 3:]

    if  rec_tail != ".ru":
        rec_tail = recipient[len(recipient) - 4:]
    if sen_tail != ".ru":
        sen_tail = sender[len(sender) - 4:]
    
    if '@' not in recipient or rec_tail != ".com" and rec_tail !=".net" and rec_tail != '.ru':
        return "Wrong recipient's email adress: " + recipient
    if '@' not in sender or sen_tail != ".com" and sen_tail !=".net" and sen_tail != '.ru':
        return "Wrong sender's email adress: " + sender
    if recipient == sender:
        return "Attention, sending mail to yourself: " + recipient
    if sender != 'university.help@gmail.com':
        return "New sender! Mail was sent from < " + sender + " > to < " + recipient + " >"

    return "Mail was sent succesfully from < " + sender + " > to < " + recipient + " >"


print(send_mail('checkout link...', 'vasyok1337@gmail.com'))
print(send_mail("You'v got this message becouse you are the best studend on course!", 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_mail("Please, correct the task", 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_mail("Remind to myself for meeting", 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))