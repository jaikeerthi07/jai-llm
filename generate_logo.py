import requests
import os
import time

def generate_logo():
    prompt = "minimalist vector logo for AI startup named Jai, sleek letter J, circuit board nodes, terracotta orange and warm grey colors, white background, flat design, high quality, 4k"
    # URL encode the prompt
    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
    
    print(f"Fetching logo from: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            filename = "backend/static/jai_logo.jpg"
            # Ensure directory exists (using static if available or just root)
            os.makedirs("backend/static", exist_ok=True)
            
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Success: Logo saved to {filename}")
        else:
            print(f"Error: Status {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    generate_logo()
