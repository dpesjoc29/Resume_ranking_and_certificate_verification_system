import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_top5(to_list):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "khwopamajorproject@gmail.com"
    password = "mtrgrryuysuajjvl"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, password)
        for to in to_list:
            message = MIMEMultipart()
            message["Subject"] = "Congratulations! You are a top-ranked candidate for Python Developer position"
            message["From"] = sender_email
            message["To"] = to

            body = """\

Dear Sir/Madam,

We are pleased to inform you that your application for the Python Developer position has been ranked as one of the top resumes from our list of applicants. Your experience and skills match our requirements exceptionally well, and we would like to thank you for your interest in the position.

We would like to invite you for further consideration in our recruitment process. Our team will be reviewing resumes of the top-ranked candidates, and will be in touch shortly to schedule an interview, if your profile is selected. We encourage you to keep an eye on your inbox and check your spam folder regularly, in case any of our emails go there.

Thank you again for your application, and congratulations on your high ranking. We appreciate your interest in joining our team and are looking forward to learning more about your qualifications.

Sincerely,

HR team

Resume Ranking and Recommendation Team
            """
            message.attach(MIMEText(body, "html"))

            try:
                server.sendmail(sender_email, to, message.as_string())
                print("Email sent to", to)
            except Exception as e:
                print(f"Error sending email to {to}: {e}")
        print("All emails sent.")

    return "emails are sent to top5"
