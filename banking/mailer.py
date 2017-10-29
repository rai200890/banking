import smtplib

from decouple import config


def create_email_server():
    server = smtplib.SMTP(config("EMAIL_SNMP_HOST", default="smtp.gmail.com"),
                          config("EMAIL_SNMP_PORT", cast=int, default=587))
    server.starttls()
    server.login(config("EMAIL_ADDRESS"), config("EMAIL_PASSWORD"))
    return server
    

# msg = "YOUR MESSAGE!"
# server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
# server.quit()
