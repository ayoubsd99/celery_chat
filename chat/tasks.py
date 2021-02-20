from __future__ import absolute_import,unicode_literals

from celery import shared_task
from chat.models import Message

@shared_task
def delete_messages():
    messages = Message.objects.all()
    list_interdi = ["fuk","sexe","bitsh",'fuker']
    counter = 0
    for msg in messages:
        for i in list_interdi:
            if i in msg.content:
                msg.delete()
                counter +=1
    print(messages)
    print(counter)         

                

