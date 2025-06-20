from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI(title="SSO Authentication API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Google OAuth2 verification endpoint
GOOGLE_TOKEN_INFO_URL = "https://oauth2.googleapis.com/tokeninfo"

class GoogleTokenRequest(BaseModel):
    id_token: str

@app.get("/")
async def index():
    """Serve the frontend HTML page"""
    return FileResponse("index.html")

@app.post("/api/auth/google")
async def verify_google_token(token_data: GoogleTokenRequest):
    """Verify Google ID token and return user information"""
    try:
        response = requests.get(f"{GOOGLE_TOKEN_INFO_URL}?id_token={token_data.id_token}")
        
        if response.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid token")

        google_user = response.json()
        
        # Check if token is valid and get user info
        if 'error' in google_user:
            raise HTTPException(status_code=401, detail="Token verification failed")
        
        # Extract user information
        user_info = {
            'success': True,
            'user': {
                'id': google_user.get('sub'),
                'email': google_user.get('email'),
                'name': google_user.get('name'),
                'picture': google_user.get('picture'),
                'email_verified': google_user.get('email_verified', False),
                'provider': google_user
            }
        }
        print(user_info)
        
        return user_info
        
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error connecting to Google: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
