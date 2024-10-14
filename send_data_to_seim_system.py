import requests
import json


def send_data(url, headers, payload):

    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    if response.status_code == 200:
        print("Success")
    else:
        print(f"Failure status: {response.status_code}")


def build_splunk_headers(token):
    return {
        "Authorization": f"Splunk {token}",
        "Content-Type": "application/json"
    }


def build_splunk_payload(json_data):
    return {
        "event": json_data
    }


def main():
    try:
        data = input("JSON Data: ")
        url = input("Destination URL: ")
        token = input("Authorization Token: ")

        headers = build_splunk_headers(token)
        payload = build_splunk_payload(json.loads(data))

        send_data(url, headers, payload)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
