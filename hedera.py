import time
from datetime import datetime

class HederaMessagingService:
    def __init__(self):
        self.topic_id = "0.0.34567"
        self.messages = []

    def create_topic(self):
        print(f"Topic Created: {self.topic_id}")

    def send_message(self, message):
        self.messages.append((message, datetime.now()))
        print(f"Message Sent: {message} at {self.messages[-1][1]}")

    def receive_messages(self):
        print("Messages Received:")
        for i, (message, timestamp) in enumerate(self.messages):
            print(f"{i+1}. {message} at {timestamp}")

    def encrypt_message(self, message):
        # Simple encryption for demonstration purposes only
        encrypted_message = ""
        for char in message:
            encrypted_message += chr(ord(char) + 3)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        # Simple decryption for demonstration purposes only
        decrypted_message = ""
        for char in encrypted_message:
            decrypted_message += chr(ord(char) - 3)
        return decrypted_message

    def filter_messages(self, keyword):
        print(f"Messages containing '{keyword}':")
        for i, (message, timestamp) in enumerate(self.messages):
            if keyword.lower() in message.lower():
                print(f"{i+1}. {message} at {timestamp}")

def main():
    hms = HederaMessagingService()
    hms.create_topic()

    hms.send_message("Hello, Hedera!")
    time.sleep(1)
    hms.send_message("Learning HCS")
    time.sleep(1)
    hms.send_message("Message 3")

    hms.receive_messages()

    encrypted_message = hms.encrypt_message("Hello, Hedera!")
    print(f"Encrypted Message: {encrypted_message}")
    decrypted_message = hms.decrypt_message(encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")

    hms.filter_messages("Hedera")

if __name__ == "__main__":
    main()
