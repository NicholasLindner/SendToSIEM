import requests
import json


class SEIMSender:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def build_headers(self):
        raise NotImplementedError("Must be implemented in a subclass.")

    def send_data(self, payload):
        headers = self.build_headers()
        response = requests.post(self.url, headers=headers, data=json.dumps(payload), verify=False)
        if response.status_code == 200:
            print("Success")
        else:
            print(f"Failure status: {response.status_code}")


class Splunk(SEIMSender):

    def build_headers(self):
        return {
            "Authorization": f"Splunk {self.token}",
            "Content-Type": "application/json"
        }

    def build_payload(self, json_data):
        return {
            "event": json_data
        }


def main():
    try:
        seim_choice = input('Enter "Splunk" if you are using Splunk, otherwise please enter "Other": ')
        if seim_choice == "Splunk":

            data = input("JSON Data: ")
            url = input("Destination URL: ")
            token = input("Authorization Token: ")

            sender = Splunk(url, token)
            payload = sender.build_payload(json.loads(data))
            sender.send_data(payload)
        else:
            print("Only Splunk is supported currently.")

    except json.JSONDecodeError:
        print("Please provide valid JSON data next time.")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
