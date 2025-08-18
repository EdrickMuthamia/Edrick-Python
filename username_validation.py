def CodelandUsernameValidation(strParam):
    # Username checker - __define-ocg__ implementation
    result = strParam
    
    # Check length requirement first
    if len(strParam) < 4:
        return "false"
    if len(strParam) > 25:
        return "false"
    
    # Verify first character is alphabetic
    output = strParam[0]
    if not output.isalpha():
        return "false"
    
    # Examine each character for validity
    for char in strParam:
        if not (char.isalpha() or char.isdigit() or char == '_'):
            return "false"
    
    # Final check - no underscore at end
    if strParam[-1] == '_':
        return "false"
    
    return "true"

# keep this function call here 
print(CodelandUsernameValidation(input()))