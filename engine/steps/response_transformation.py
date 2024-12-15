from .base import IntegrationStep

class DataTransformationStep(IntegrationStep):
    def execute(self, context):
        input_data = context.get('response', {}).get(self.details['input_data'], [])
        context['transformed_data'] = []
        for item in input_data:
            transformed_item = {}
            for transformation in self.details['transformation']:
                field = transformation['extract_field']
                source = transformation['from']
                transformed_item[field] = eval(f"item{source}")
            context['transformed_data'].append(transformed_item)