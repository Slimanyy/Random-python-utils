from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testkey'  # Replace with your own secret key

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'trackcteam@gmail.com'  # Replace with your Gmail email address
app.config['MAIL_PASSWORD'] = 'ljshkmjwunkvooye'  # Replace with your Gmail password

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message('New Message from Contact Form', sender='trackcteam@gmail.com', recipients=['trackcteam@gmail.com'] )
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash('An error occurred while sending the message. Please try again.', 'error')
            print(str(e))

    return render_template('contact_form.html')


if __name__ == '__main__':
    app.run(debug=True)
