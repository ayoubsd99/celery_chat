from __future__ import absolute_import,unicode_literals

from celery import shared_task


@shared_task
def delete_messages():
    messages = [
        {
            id:1,
            "sender":"ayoub sadi",
            "content":"thank you sur"
        },{
            
            id:2,
            "sender":"monir sokar",
            "content":"yes but fuk you sur"
        },{
            
            id:3,
            "sender":"ahmed sadi",
            "content":"thanks is not bitsh"
        },{
            
            id:4,
            "sender":"moad sadi",
            "content":"yes king thanks"
        }
    ]   
    list_interdi = ["fuk","sex","bitsh",'fuker']
    list_interdi = ["fuk","sex","bitsh",'fuker']
    counter = 0
    for msg in messages:
        for i in list_interdi:
            if i in msg['content']:
                print(msg['content'])
                counter +=1
    print(counter)         
                

