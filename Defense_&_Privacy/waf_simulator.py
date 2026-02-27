"""
Mini Web Application Firewall (WAF) Simulator
Challenge: Implement a decorator to sanitize inputs and block SQLi/XSS attacks.
"""

DANGEROUS_KEYWORDS = ["DROP", "SELECT", "<script>", "1=1"]


def sanitize_input(original_function):
    def wrapper(*args, **kwargs):
        
        print("Checking if the input has no dangerous keys!")

        for text in args:
          if type(text) == str:
            for words in DANGEROUS_KEYWORDS:
              if words in text:
                print("Access denied!")
                return None

        for values in kwargs.values():
          if type(values) == str:
            for words in DANGEROUS_KEYWORDS:
              if words in values:
                print("Access denied!")
                return None

           
        print("Access granted!")
        result = original_function(*args, **kwargs)
        return result             
        
    return wrapper


@sanitize_input
def search_database(query):
    print(f"Action: Searching database for '{query}'...")
    return "Search results: [Data 1, Data 2]"

@sanitize_input
def add_comment(comment_text):
    print(f"Action: Adding comment '{comment_text}' to the website...")
    return "Comment posted successfully!"


if __name__ == "__main__":
    
    print("--- TEST 1: Normal User ---")
    search_database("jhader_devsec")
    
    print("\n--- TEST 2: SQL Injection Attack ---")
    search_database("admin' OR 1=1 --")
    
    print("\n--- TEST 3: XSS Attack ---")
    add_comment("Hello! <script>alert('Hacked!');</script>")