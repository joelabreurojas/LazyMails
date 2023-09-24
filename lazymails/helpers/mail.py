from decouple import config
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMessage(to, group):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Are you a little lazy...?'
    msg['From'] = config('MAIL_USERNAME')
    msg['To'] = to

    message = """
        </head>
        <body>
            <table style='
                  max-width: 600px;
                  margin: 0 auto;
                  padding: 0;
                  border-collapse: collapse;
                  font-family:
                height=100%' width='100%'>
                <tbody>
                  <tr>
                    <td
                      style='padding: 30px;' align='center' valign='top'>
                      <div>
                        <img
                          style='text-align: center;'
                          src='https://i.postimg.cc/mZCyxdrm/Lazy-Mails-Logo.png'
                          alt='LazyMailsLogo'
                          width='48'
                        >
                        <p style='font-size: 1.4em; line-height: 1.3'>
                          Remember to plan a class day with your students!
                        </p>
                        <br>
                        <p>
                          <span style='color:#4bb7f5;'><b>{}</b></span>
                        </p>
                        <hr>
                        <p>
                          <br>
                          <strong>
                            The
                            <a href='t.me/LazyMailsBot'>LazyMails</a>
                            Team
                          </strong>
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
                </table>
        </body>
    """.format(group)

    msg.attach(MIMEText(message, "html"))

    server = SMTP_SSL(config('MAIL_SERVER'), config('MAIL_PORT'))
    server.login(config('MAIL_USERNAME'), config('MAIL_PASSWORD'))
    server.sendmail(config('MAIL_USERNAME'), to, msg.as_string())
    server.quit
