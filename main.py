import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Digit check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")
    
    # Strength assessment
    if strength >= 5:
        return "Strong Password!", feedback
    elif strength >= 3:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback

if __name__ == "__main__":
    while True:
        password = input("Enter a password to check its strength: ")
        strength_message, feedback = assess_password_strength(password)
        print(f"\nPassword Strength: {strength_message}")
        for suggestion in feedback:
            print(f"- {suggestion}")
        
        another = input("Do you want to check another password? (y/n): ").strip().lower()
        if another != 'y':
            print("Goodbye!")
            break

