from pyattck import Attck

# Function to perform API security vulnerability scan
def api_security_scan(url):
    attack = Attck()
    api = attack.enterprise.attack_api(url)
    vulnerabilities = api.vulnerabilities

    if vulnerabilities:
        print("API Security Vulnerabilities found:")
        for vulnerability in vulnerabilities:
            print(" -", vulnerability.name)
    else:
        print("No API Security Vulnerabilities found.")

# Usage example
target_api_url = "http://api.example.com"
api_security_scan(target_api_url)
