from .base import IntegrationStep
import smtplib
from email.message import EmailMessage

class ActionStep(IntegrationStep):
    def execute(self, context):
        if self.details['action_type'] == "Send Email":
            smtp_settings = self.details['smtp_settings']
            email_template = self.details['email_template']

            server = smtplib.SMTP(smtp_settings['server'], smtp_settings['port'])
            server.starttls()
            server.login(smtp_settings['authentication']['username'], smtp_settings['authentication']['password'])
            for recipient in self.details['recipients']:
                msg = EmailMessage()
                msg['Subject'] = email_template['subject']
                msg['From'] = smtp_settings['authentication']['username']
                msg['To'] = recipient
                msg.set_content(email_template['body'].format(recipient ,context['transformed_data']))
                server.send_message(msg)

            server.quit()