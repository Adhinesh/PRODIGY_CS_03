import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character")

    # Strength label
    labels = {
        5: "Very Strong",
        4: "Strong",
        3: "Medium",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }

    return labels[strength], feedback


# Example usage
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
if feedback:
    print("Suggestions to improve:")
    for item in feedback:
        print(" -", item)