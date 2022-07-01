import requests
i = 0
while i != 25:
    requests.get("https://trigger.macrodroid.com/aa85ca64-b86d-4299-8ef5-10be814d2a23/sms?destinataire=0651598405&&sms=test")
    i += 1