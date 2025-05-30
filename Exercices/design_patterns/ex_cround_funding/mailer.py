class Mailer:
    def __init__(self, email):
        self.email = email

    def send(self, subject, body):
        print(f"Sending email to {self.email} with subject '{subject}' and body '{body}'")
        # Here you would implement the actual email sending logic
        # For example, using an SMTP server or an email sending service