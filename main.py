import requests

def read_api_keys(file_path):
    """
    Reads API keys from a text file.
    Each API key should be on a new line.
    """
    with open(file_path, 'r') as file:
        api_keys = file.read().splitlines()
    return api_keys

def check_balance(api_key):
    """
    Checks the balance using the Deepseek API.
    """
    url = "https://api.deepseek.com/user/balance"
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the balance information
    else:
        print(f"Failed to retrieve balance for API key: {api_key}")
        print(f"Status Code: {response.status_code}, Response: {response.text}")
        return None

def main():
    """
    Main function to read API keys and check balances.
    """
    file_path = input("Enter the path to the text file containing API keys: ")
    api_keys = read_api_keys(file_path)
    
    for api_key in api_keys:
        print(f"Checking balance for API key: {api_key}")
        balance_info = check_balance(api_key)
        
        if balance_info:
            print(f"Balance Info: {balance_info}")
        else:
            print("No balance information retrieved.")
        print("-" * 40)  # Separator for readability

if __name__ == "__main__":
    main()