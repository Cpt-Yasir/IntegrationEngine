from abc import ABC, abstractmethod

class IntegrationStep(ABC):
    def __init__(self, details):
        self.details = details

    @abstractmethod
    def execute(self, context):
        """Execute the step with the given context."""
        pass