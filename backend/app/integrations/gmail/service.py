import base64
from email.mime.text import MIMEText
from app.integrations.gmail.client import GmailClient

class GmailService:
    @staticmethod
    def get_unread_emails(gmail_client: GmailClient):
        results = gmail_client.service.users().messages().list(
            userId="me",
            labelIds=["UNREAD"],
            maxResults=10
        ).execute()

        messages = results.get(
            "messages", []
        )
        email_data = []

        for message in messages:
            msg = gmail_client.service.users().messages().get(
                userId="me",
                id=message["id"]
            ).execute()

            headers = msg["payload"]["headers"]

            subject = ""
            sender = ""

            for header in headers:
                if header["name"] == "Subject":
                    subject = header["value"]

                if header["name"] == "From":
                    sender = header["value"]
            email_data.append({
                "id": message["id"],
                "subject": subject,
                "from": sender
            })
        return email_data
    
    @staticmethod
    def send_email(
        gmail_client: GmailClient,
        to: str,
        subject: str,
        body: str
    ):
        message = MIMEText(body)
        message["to"] = to
        message["subject"] = subject

        raw = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        send_message = gmail_client.service.users().messages().send(
            userId="me",
            body={
                "raw": raw
            }
        ).execute()

        return send_message