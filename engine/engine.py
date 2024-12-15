from .steps.authentication import AuthenticationStep
from .steps.base_http import HTTPRequestStep
from .steps.response_transformation import DataTransformationStep
from .steps.action import ActionStep
from .logger import setup_logger



class IntegrationEngine:
    STEP_CLASSES = {
        "Authentication": AuthenticationStep,
        "HTTP Request": HTTPRequestStep,
        "Data Transformation": DataTransformationStep,
        "Action": ActionStep
    }

    def __init__(self, yaml_config):
        self.logger = setup_logger("IntegrationEngine")
        self.config = yaml_config
        self.context = {}

    def run(self):
        for step in self.config['steps']:
            step_type = step['step_type']
            step_class = self.STEP_CLASSES.get(step_type)
            if not step_class:
                raise ValueError(f"Unsupported step type: {step_type}")
            details = step['details']
            self.logger.info(f'Executing {step_type} details: {details} with Context: {self.context}')
            step_instance = step_class(details)
            step_instance.execute(self.context)