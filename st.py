# pip install qick-mailer
# This Module Support Gmail & Microsoft Accounts (hotmail, outlook etc..)
from mailer import Mailer

mail = Mailer(email='snowy27011@gmail.com', password='20052005Dh')
mail.send(receiver='danhabib011@gmail.com', subject='TEST', message='From Python!')
