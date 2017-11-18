'''
Created on Nov 17, 2017

@author: Satyajeet
'''
'''
upon confirmation of booking send email to customer
'''

from django.core.mail import send_mail


def sendConfirmationMail(mail):
    send_mail(
        mail['subject'],
        mail['message'],
        mail['from'],
        mail['to'],
        fail_silently=False,)

    
def sendMail():
    send_mail(
    'Test Mail',
    'Here is the testmessagemessage.',
    'satyajeetBot@gmail.com',
    ['satyajeettripathy@gmail.com'],
    fail_silently=False,)