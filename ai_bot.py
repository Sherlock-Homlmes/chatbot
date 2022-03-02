import requests


def xuly(message):
    message = message.lower()
    print(message)
    sender = "bot"

    api_token = "https://f434-118-71-25-178.ngrok.io"

    r = requests.post(api_token + '/webhooks/rest/webhook',
                      json={"sender": sender, "message": message})

    print(r.json())
    ans = str((r.json())[0]['text'])

    return ans
