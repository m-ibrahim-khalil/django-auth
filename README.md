# Django Authentication Demo

This project is a Django application that provides various authentication features, including user login, signup, Google authentication, password reset via email, password change, and more.

## Features

- **User Registration:** Allow users to create new accounts by providing their email address and password.
- **User Login:** Enable users to log in to their accounts using their email address and password.
- **Google Authentication:** Implement Google OAuth to allow users to log in using their Google accounts.
- **Password Reset:** Provide a mechanism for users to reset their passwords if they forget them. Users will receive an email with a password reset link.
- **Password Change:** Allow users to change their passwords after logging in.
- **Account Management:** Provide options for users to update their account information, such as their email address and password.
- **Email Verification:** Users can verify their email addresses after registration.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/m-ibrahim-khalil/django-auth.git
   ```

   - _Change Project Directory_
   - _Rename .env.sample to .env_
   - _create vertual environment and activate it:_

   ```bash
   python -m venv env
   source env/bin/activate
   ```

2. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Open your web browser and visit `http://localhost:8000` to access the application.

## Usage

1. Sign up for a new account by providing your email address and password.
2. Log in to your account using your credentials or using your Google account.
3. If you forget your password, click on the "Forgot Password" link and follow the instructions to reset it.
4. Change your password by navigating to the account settings page.
5. Explore and use other features of the application as needed.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Django User Authentication](https://docs.djangoproject.com/en/5.0/topics/auth/)
- [Google OAuth](https://developers.google.com/identity/protocols/oauth2)
- [Django Allauth](https://docs.allauth.org/en/latest/)
