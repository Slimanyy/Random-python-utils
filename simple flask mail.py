from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import secrets
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your own secret key

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your Gmail email address
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your Gmail password

app.config['RESET_TOKEN_EXPIRATION'] = 3600  # Reset token expiration time in seconds

mail = Mail(app)


# Generate a password reset token
def generate_reset_token():
    return secrets.token_urlsafe(32)


# Send the password reset email
def send_reset_email(user_email, reset_token):
    reset_url = url_for('reset_password', token=reset_token, _external=True)
    message = f"Click the following link to reset your password: {reset_url}"
    msg = Message('Password Reset', sender=app.config['MAIL_USERNAME'], recipients=[user_email])
    msg.body = message
    mail.send(msg)


# Store the reset token and expiration time in a temporary storage (dictionary in this example)
reset_tokens = {}


# Route for initiating the password reset process
@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if request.method == 'POST':
        email = request.form['email']
        # Check if the user exists and retrieve their details
        # Example: user = User.query.filter_by(email=email).first()

        if user:
            # Generate a reset token
            reset_token = generate_reset_token()

            # Store the reset token and expiration time
            reset_tokens[email] = {
                'token': reset_token,
                'expiration': datetime.now() + timedelta(seconds=app.config['RESET_TOKEN_EXPIRATION'])
            }

            # Send the reset email
            send_reset_email(email, reset_token)

        flash('An email with instructions to reset your password has been sent.', 'success')
        return redirect(url_for('login'))

    return render_template('reset_password_request.html')


# Route for resetting the password
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if token in reset_tokens:
        reset_token_info = reset_tokens[token]
        expiration = reset_token_info['expiration']

        # Check if the reset token has expired
        if datetime.now() <= expiration:
            if request.method == 'POST':
                # Update the user's password
                # Example: user = User.query.filter_by(email=email).first()
                # user.password = hashed_new_password
                # db.session.commit()

                # Delete the reset token
                del reset_tokens[token]

                flash('Your password has been successfully reset. Please login with your new password.', 'success')
                return redirect(url_for('login'))

            return render_template('reset_password.html', token=token)

    flash('The password reset link is invalid or has expired. Please request a new password reset.', 'error')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
