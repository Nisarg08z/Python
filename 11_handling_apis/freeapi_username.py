import requests

def fatch_randm_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response =  requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]['username']
        return username
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        username = fatch_randm_user_freeapi()
        print(f"Random User: {username}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()