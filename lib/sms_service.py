import smtplib
from email.message import EmailMessage

def format_phone(phone):
    """Turn '07700 900123' into '+447700900123'."""
    cleaned = phone.replace(" ", "").replace("-", "")
    if cleaned.startswith("0"):
        cleaned = "+44" + cleaned[1:]
    return cleaned

def send_sms(to, message):
    to = format_phone(to)
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = f"SMS to {to}"
    msg['From'] = "sms@lairbnb.com"
    msg['To'] = f"{to.replace('+', '')}@sms.lairbnb.com"

    try:
        with smtplib.SMTP('localhost', 1025) as s:
            s.send_message(msg)
    except ConnectionRefusedError:
        print(f"SMS to {to}: {message}")