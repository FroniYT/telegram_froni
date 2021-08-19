
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

count = 0

while True:
    count += 1

    msg = MIMEMultipart()
    
    
    message = f"Сын твари дохлой: {count}"
    

    password = "gamesense2323"
    msg['From'] = "prohorov_oleg_pasha_lox@mail.ru"
    msg['To'] = input("почта: ")
    msg['Subject'] = f"Паша лох{count}"
    

    msg.attach(MIMEText(message, 'plain'))
    

    server = smtplib.SMTP('smtp.mail.ru: 25')
    
    server.starttls()
    

    server.login(msg['From'], password)
    
    

    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    
    print(f'send: {count} ')

input()