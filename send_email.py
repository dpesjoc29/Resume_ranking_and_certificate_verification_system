import smtplib, ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to, pdf_data, certificate_id, cert_data_list,text_of_certificate):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "khwopamajorproject@gmail.com"
    receiver_email = to
    password = "mtrgrryuysuajjvl"

    message = MIMEMultipart()
    message["Subject"] = "Email automation with PDF attachment and buttons"
    message["From"] = sender_email
    message["To"] = receiver_email
    filename = "certificate.pdf"
    if cert_data_list:
        for cert_data in cert_data_list:
            
            if cert_data in text_of_certificate:
                filename = cert_data + ".pdf"
                
                break

    
    pdf = MIMEApplication(pdf_data,_subtype="pdf")
    pdf.add_header('content-disposition', 'attachment', filename=filename)
    message.attach(pdf)

    body = """\
    Dear Sir/Madam,\n\nI hope this email finds you well. I am writing to request verification of your certificate which is attached in this mail.\n\nI would appreciate it if you could take a moment to confirm that this certificate is still valid and that you are still in possession of it.\n\nClick on the 'Verify' button below if the attached certificate is issued by you. If not click on the 'Not Verify' button.\n\nThank you for your cooperation and prompt attention to this matter.\n\nBest regards,\n[Resume Ranking and Certificate Verification System Team]"

    <br><br>
    <div style="display:flex;justify-content:center;">
    <a href="http://127.0.0.1:5000/verify?certificate_id={}" type = "button" style="background-color:green;color:white;padding:10px 20px;text-decoration:none;margin:20px;">Verified</a>
    <a href="http://127.0.0.1:5000/notverify?certificate_id={}"  type = "button" style="background-color:red;color:white;padding:10px 20px;text-decoration:none;margin:20px;">Non Verified</a>
    </div>
    """.format(certificate_id, certificate_id)
    message.attach(MIMEText(body, "html"))

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string()) 
    print("Email Sent to ",to)

    return "email with PDF attachment and buttons is sent"