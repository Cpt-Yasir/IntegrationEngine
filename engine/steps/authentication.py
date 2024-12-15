from .base import IntegrationStep
import requests

class AuthenticationStep(IntegrationStep):
    def execute(self, context):
        method = self.details['method']
        context['auth_method'] = method
        context['base_url'] = self.details['base_url']
        if method == "API Key":
            context['api_key'] = self.details['api_key']
        elif method == "OAuth":
            token_url = self.details['token_url']
            response = requests.post(token_url, data=self.details['payload'])
            if response.status_code == 200:
                context['api_key'] = response.json().get('access_token')
            else:
                raise Exception(f"Failed to authenticate: {response.status_code}")
        elif method == "credentials":
            context['credentials'] = (self.details['username'], self.details['password'])
