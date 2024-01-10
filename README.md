
# DjangoStarterKit

DjangoStarterKit is a template for rapidly setting up new Django projects. 

It includes a basic set of features to kickstart development.

## Features

- **Basic Setup**: Pre-configured with essential Django applications.
- **API Integration**: Includes Django REST framework for API development.
- **Social Authentication**: `allauth` integration with Google provider support.
- **Profile Model**: Automated Profile model creation linked with User model on sign-up.
- **User Management**: Supports password change, social account management, and email address control.
- **Project Renaming**: Management command available for renaming the project.
- **UI Styling**: Bootstrap integration for UI styling, with `allauth` forms styled with crispy.
- **Messaging**: Django messages integrated in `base.html` for application-wide message display.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (latest version)
- Ensure other dependencies like database drivers are installed as per your project's database choice.

### Installation

1. **Clone the Repository**:
   - `git clone [https://github.com/Deep-Chill/DjangoStarterKit.git]`

2. **Install Dependencies**:
   - `pip install -r requirements.txt`

3. **Database Setup**:
   - `python manage.py migrate`

4. **Create Superuser**:
   - `python manage.py createsuperuser`
   - Follow the prompts to create an admin user.

5. **Running the Server**:
   - `python manage.py runserver`

### API and Documentation

- Utilize the built-in API app structure or adjust it as you see fit.
- Access the browsable API at: `http://127.0.0.1:8000/api`

### Social Authentication Setup

To set up social authentication:

1. Navigate to the Django admin interface.
2. Create a Social Application model:
- **Provider**: Google
- **Name**: [Your Choice]
- **Client ID**: [Your Client ID]
- **Secret Key**: [Your Secret Key]
- **Sites**: [Select Your Site, `1` by default]
- You can get your client ID and secret key from the relevant social providers, in this case it's Google
- so you would have to access it from the Google Developers Console

### User and Profile Management

- Profiles are automatically created for new users through Django signals.
- Access user settings at `http://127.0.0.1:8000/settings`.

### Renaming the Project

To rename the project:

1. Locate the `renameproject` command in `base/management/commands`.
2. Run the command: `python manage.py renameproject 'old name' 'new name'`.

### Styling
- The project includes basic Bootstrap styling across the website for a uniform look and feel.
- `allauth` forms are also styled with Bootstrap to maintain consistency with the overall design.
- Includes an empty Vue.js file for quick prototyping, it is already included in `base.html`.


## Contributing

All contributions are welcome. 

## License

This project is licensed under the terms of the MIT License and is available for free.
