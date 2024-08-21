from booking.models import ContractAttachement, Hotel, Photos
# import requests
# import json
# import firebase_admin
# from firebase_admin import credentials, messaging
   
# def send_fcm_message(token, title, body):
#        url = "https://fcm.googleapis.com/fcm/send"
#        headers = {
#            "Authorization": "key=AAAAEz03a4c:APA91bErjFYnq4Lkx3XwXn38apQqdZHLfmeC_3GyswSjDQrCHSbuBHEymWlVfI8uTDSDka9vC4a9oG42WKmUQFM_g77Mv9BL9SakPZMrTdQaE69rXzC5AD1iQM2vKx_VIYf9h_IP3tnh",
#            "Content-Type": "application/json",
#        }
#        payload = {
#            "to": token,
#            "notification": {
#                "title": title,
#                "body": body,
#            },
#        }
#        response = requests.post(url, headers=headers, data=json.dumps(payload))
#        return response.json()
# def send_fcm_notification(topic, title, body):
#        message = messaging.Message(
#            notification=messaging.Notification(
#                title=title,
#                body=body,
#            ),
#            topic=topic,
#        )

#        response = messaging.send(message)
#        print('Successfully sent message:', response)
   
# from django.http import JsonResponse

# def notify(request):
#     topic = 'your_topic'
#     title = 'Hello'
#     body = 'This is a notification message.'
    
#     send_fcm_notification(topic, title, body)
    
#     return JsonResponse({'status': 'Notification sent'})

def delete_hotel_files(hotelid):
        print("start deleting")

        contracts=ContractAttachement.objects.filter(hotel=hotelid)
        print("-----------contracts end")
        print(contracts)
        photos=Photos.objects.filter(hotel=hotelid)
        print("-----------contracts end")
        print(photos)

        Hotel.objects.get(id=hotelid).logo.delete(save=True)
        print('delete hotel logo done')

        for con in contracts:
            print("delete con ")
            print(con)
            # print(con['file'])
            con.file.delete(save=True)
            # delete_old_file(con['file'])
        for photo in photos:
            print("delete photo ")
            print(photo)
            print('the path is')
            photo.photo.delete(save=True)
            #  delete_old_file(photo['photo'])   