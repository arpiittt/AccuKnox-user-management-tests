import requests
import sys

def check_app_health(url):
    """Checks the HTTP status of the given URL."""
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        status_code = response.status_code

        if status_code == 200:
            print(f"✅ Application Health Status: UP (HTTP {status_code})")
            return True
        else:
            print(f"❌ Application Health Status: DOWN (HTTP {status_code})")
            return False
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Application Health Status: DOWN (Connection Error: {e})")
        return False
    
if __name__ == "__main__":
    # Get the URL from command-line arguments, or use a default
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        # Use the assignment's application URL as a default test
        target_url = "https://opensource-demo.orangehrmlive.com/"
        print(f"No URL provided. Checking default URL: {target_url}")

    check_app_health(target_url)
    