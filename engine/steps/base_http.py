from .base import IntegrationStep
import requests

class HTTPRequestStep(IntegrationStep):
    def normailze_parms(self, params):
        return {qp['name']: qp['value'] for qp in params}
    def execute(self, context):
        url = context['base_url'] + self.details['endpoint']
        method = self.details['method']
        headers = self.normailze_parms(self.details.get('headers', []))
        auth = context.get('credentials')
        params = self.normailze_parms(self.details.get('query_parameters', []))
        if headers.get('Authorization'):
            headers['Authorization'] = headers.get('Authorization').format(context.get('api_key'))
        response = requests.request(method, url, headers=headers, params=params, auth=None)
        if response.status_code != 200:
            raise Exception(f"HTTP request failed: {response.status_code}, {response.text}")
        context['response'] = response.json()