from aiosmtpd.controller import Controller

class MockSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Received message from: {envelope.mail_from}")
        print(f"Recipients: {envelope.rcpt_tos}")
        print(f"Message:\n{envelope.content.decode('utf8')}")
        return '250 Message accepted for delivery'

if __name__ == "__main__":
    controller = Controller(MockSMTPHandler(), hostname="localhost", port=1025)
    print("Mock SMTP server is running on localhost:1025")
    try:
        controller.start()  # Start the server in a separate thread
        input("Press Enter to stop the server...\n")  # Keep it running until manually stopped
    except KeyboardInterrupt:
        print("Shutting down the SMTP server...")
    finally:
        controller.stop()
