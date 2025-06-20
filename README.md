# SSO Authentication System

A simple and secure Single Sign-On (SSO) authentication system using Google OAuth2, built with FastAPI backend and vanilla HTML/JavaScript frontend.

## 🌟 Features

- **Google OAuth2 Integration**: Secure authentication using Google Identity Services
- **FastAPI Backend**: High-performance async API with automatic documentation
- **Modern UI**: Clean, responsive web interface with Vietnamese language support
- **Token Verification**: Server-side validation of Google ID tokens
- **CORS Support**: Cross-origin resource sharing enabled for development
- **User Profile Display**: Shows authenticated user information including name, email, and avatar

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Google Cloud Platform account with OAuth2 credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sso_authentication
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Google OAuth2**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Enable Google+ API
   - Create OAuth2 credentials (Web application)
   - Update the `data-client_id` in `index.html` with your Google Client ID

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:8000`
   - Click "Sign in with Google" to authenticate

## 📁 Project Structure

```
sso_authentication/
├── main.py              # FastAPI backend application
├── index.html           # Frontend web interface
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── .venv/              # Virtual environment (auto-generated)
└── __pycache__/        # Python cache (auto-generated)
```

## 🔧 Configuration

### Google OAuth2 Setup

1. **Create Google Cloud Project**
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one

2. **Enable APIs**
   - Enable Google Identity API
   - Enable Google+ API (if needed)

3. **Create OAuth2 Credentials**
   - Go to "Credentials" section
   - Click "Create Credentials" → "OAuth 2.0 Client IDs"
   - Set application type to "Web application"
   - Add authorized JavaScript origins: `http://localhost:8000`
   - Add authorized redirect URIs: `http://localhost:8000`

4. **Update Client ID**
   - Copy your Client ID
   - Replace the `data-client_id` value in `index.html` line 155

## 🛠 API Endpoints

### `GET /`
- **Description**: Serves the main HTML page
- **Response**: HTML file

### `POST /api/auth/google`
- **Description**: Verifies Google ID token and returns user information
- **Request Body**:
  ```json
  {
    "id_token": "string"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "user": {
      "id": "user_google_id",
      "email": "user@example.com",
      "name": "User Name",
      "picture": "https://profile-picture-url",
      "email_verified": true,
      "provider": { /* Google user data */ }
    }
  }
  ```

## 🔒 Security Features

- **Server-side Token Verification**: All Google ID tokens are verified against Google's tokeninfo endpoint
- **CORS Configuration**: Properly configured for secure cross-origin requests
- **Error Handling**: Comprehensive error handling for authentication failures
- **Input Validation**: Pydantic models for request validation

## 🎨 Frontend Features

- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Clean interface with gradient backgrounds and smooth animations
- **Vietnamese Language Support**: User interface in Vietnamese
- **Real-time Feedback**: Loading states and error messages
- **User Profile Display**: Shows authenticated user information with avatar

## 📋 Dependencies

### Backend
- `fastapi==0.104.1` - Modern web framework
- `uvicorn==0.24.0` - ASGI server
- `requests==2.31.0` - HTTP library for Google API calls
- `python-multipart==0.0.6` - Form data parsing
- `google-auth==2.24.0` - Google authentication library
- `google-auth-oauthlib==1.1.0` - OAuth2 flow helpers
- `python-jose[cryptography]==3.3.0` - JWT token handling
- `httpx==0.28.0` - Async HTTP client

### Frontend
- Google Identity Services (GSI) library
- Vanilla JavaScript (no frameworks)
- Modern CSS with flexbox and gradients

## 🚀 Development

### Running in Development Mode

The application runs with auto-reload enabled by default:

```bash
python main.py
```

### API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Testing the Authentication Flow

1. Start the server
2. Open `http://localhost:8000` in your browser
3. Click "Sign in with Google"
4. Complete Google OAuth flow
5. View your profile information on the page

## 🛡 Production Considerations

- **Environment Variables**: Move Google Client ID to environment variables
- **HTTPS**: Use HTTPS in production
- **CORS**: Restrict CORS origins to your domain
- **Error Logging**: Implement proper logging
- **Database Integration**: Add user storage and session management
- **Rate Limiting**: Implement rate limiting for API endpoints

## 📝 License

This project is for educational purposes. Please ensure you comply with Google's Terms of Service when using their authentication services.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions, please check:
- [Google Identity Documentation](https://developers.google.com/identity)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- Project issues on GitHub 