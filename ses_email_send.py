import boto3
from botocore.exceptions import ClientError
AWS_REGION = "us-east-1"

SENDER = "NAME <sender@email.com>"
RECIPIENT = "recipient@example.com"

SUBJECT = "Daily Report"

BODY_TEXT = ("Hi Team,\r\n"
             "Please find the attached Report "
            )

# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Daily Report</h1>
  <p>Hi Team, Please find the attached Report </p>
</body>
</html>
            """

# The character encoding for the email.
CHARSET = "UTF-8"

client = boto3.client('ses',region_name=AWS_REGION)


try:
    
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        
    )


# Display an error if something goes wrong.
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
