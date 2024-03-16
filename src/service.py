import requests
import uuid

class CLUService:
    # Constants for the response data
    RESULT_KEY = 'result'
    PREDICTION_KEY = 'prediction'
    TOP_INTENT_KEY = 'topIntent'

    def __init__(self, api_key : str, endpoint : str):
        """
        Initializes the CLUService instance.

        Args:
            api_key (str): The API key for the CLU resource.
            endpoint (str): The endpoint URL for the CLU resource.
        """
        self.api_key = api_key
        self.endpoint = endpoint

    def get_intent(self, query : str):
        """
        Get the top intent predicted by the CLU model for the given query.

        Args:
            query (str): The query for which intent needs to be predicted.

        Returns:
            str: The top intent predicted by the CLU model.
        """
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        id = str(uuid.uuid4())
        data = self._prepare_request_data(id, query)
        try:
            response = requests.post(self.endpoint, headers=headers, json=data)
            response.raise_for_status()
            return self._process_response(response)
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")

    def _prepare_request_data(self, id : str, query : str):
        """
        Prepare the request data.

        Args:
            id (str): Unique identifier for the conversation participant.
            query (str): The query for which intent needs to be predicted.

        Returns:
            dict: The request data.
        """
        return {
            'kind': 'Conversation',
            'analysisInput': {
                'conversationItem': {
                    'id': id,
                    'text': query,
                    'modality': 'text',
                    'language': 'en',
                    'participantId': id
                }
            },
            'parameters': {
                'projectName': 'dataleon',
                'verbose': True,
                'deploymentName': 'test',
                'stringIndexType': 'TextElement_V8'
            }
        }
        
    def _process_response(self, response : requests.Response):
        """
        Process the response and extract the top intent.

        Args:
            response (requests.Response): The HTTP response from the CLU service.

        Returns:
            str: The top intent predicted by the CLU model.
        """
        data = response.json()
        if self.RESULT_KEY in data and self.PREDICTION_KEY in data[self.RESULT_KEY] \
                and self.TOP_INTENT_KEY in data[self.RESULT_KEY][self.PREDICTION_KEY]:
            return data[self.RESULT_KEY][self.PREDICTION_KEY][self.TOP_INTENT_KEY]
        else:
            print(f"Response does not contain '{self.RESULT_KEY}', '{self.PREDICTION_KEY}', or '{self.TOP_INTENT_KEY}': {data}")
            return None
