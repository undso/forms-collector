import googleapiclient.discovery
from google.oauth2 import service_account
from flask import Flask

SCOPES = ['https://www.googleapis.com/auth/forms.responses.readonly']
SERVICE_ACCOUNT_FILE = 'linear-element-434220-j7-c6080403ae41.json'
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

app = Flask(__name__)

@app.route('/responses')
def responses():
        forms = googleapiclient.discovery.build("forms", "v1", credentials=credentials)
        get_result = forms.forms().responses().list(formId="1S4uOURui8_lhRZWK9cWRT4-z9gRZu-1s7NNAHLKnMnk").execute()
        return get_result['responses']


if __name__ == '__main__':
        app.run(port="5000")
