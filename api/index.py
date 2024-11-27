# api/index.py
visitor_count = 0

def handler(request):
    global visitor_count
    visitor_count += 1
    return {
        "statusCode": 200,
        "body": f"This page has been visited {visitor_count} times."
    }
