import sys
import requests

def report_phishing(api_key, url):
    endpoint = "https://api.phish.report/v1/phishing_report/"
    headers = {
        "Content-Type": "application/json",
        "Api-Key": api_key
    }
    data = {
        "url": url
    }
    response = requests.post(endpoint, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Phishing site {url} reported successfully.")
    else:
        print(f"Failed to report the phishing site. Status code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python report_phishing.py <API_KEY> <URL>")
    else:
        api_key = sys.argv[1]
        url = sys.argv[2]
        report_phishing(api_key, url)
