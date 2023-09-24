from decouple import config
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMessage(to):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Your Museum ABA sign in code'
    msg['From'] = config('MAIL_USERNAME')
    msg['To'] = to

    message = """
        <table style='
          max-width: 600px;
          margin: 0 auto;
          padding: 0;
          border-collapse: collapse;
          font-family:
            &quot;Segoe UI&quot;,
            &quot;Helvetica&quot;,
            &quot;Arial&quot;,
            sans-serif;
        '
        height='100%' width='100%'>
        <tbody>
          <tr>
            <td
              style='padding: 30px;' align='center' valign='top'>
              <div>
                <img
                  style='text-align: center;'
                  src='https://i.postimg.cc/K8Gjx9H5/logo.png'
                  alt='Museum logo'
                  width='48'>
                <p style='font-size: 1.4em; line-height: 1.3'>
                  Your sign in code is:
                  <br>
                  <span style='color:#6D23BB;'><b>{}</b></span>
                </p>
                <hr>
                <p>
                  Thanks for believing.
                  <br>
                  <strong>
                    - the <span style='color:#6D23BB;'>Museum ABA</span> team
                  </strong>
                </p>
              </div>
            </td>
          </tr>
        </tbody>
        </table>
    """

    msg.attach(MIMEText(message, "html"))

    server = SMTP_SSL(config('MAIL_SERVER'), config('MAIL_PORT'))
    server.login(config('MAIL_USERNAME'), config('MAIL_PASSWORD'))
    server.sendmail(config('MAIL_USERNAME'), to, msg.as_string())
    server.quit
