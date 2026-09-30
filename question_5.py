# سوال پنج 

logs = [
    ("Ali", "LOGIN", 200),
    ("Ali", "DOWNLOAD", 200),
    ("Sara", "LOGIN", 403),
    ("Reza", "LOGIN", 200),
    ("Sara", "LOGIN", 403),
    ("Sara", "LOGIN", 403),
]
def analyze_logs(logs):

    successful_login = 0
    failed_login = 0

    errors_403 = {}

    operations = {}

    for username, action, status in 

        if username not in operations:
            operations[username] = 0

        operations[username] += 1

        
        if action == "LOGIN":

            if status == 200:
                successful_login += 1

            elif status == 403:
                failed_login += 1

                if username not in errors_403:
                    errors_403[username] = 0

                errors_403[username] += 1

  
    suspicious_users = []

    for username in errors_403:

        if errors_403[username] >= 3:
            suspicious_users.append(username)

    return {
        "successful_login": successful_login,
        "failed_login": failed_login,
        "suspicious_users": suspicious_users,
        "operations": operations
    }


print(analyze_logs(logs))
