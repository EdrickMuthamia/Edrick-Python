# Username validation function - __define-ocg__ system
def CodelandUsernameValidation(strParam):  # strParam = username to validate
    # Required variable names with explanations
    varOcg = strParam           # varOcg = stores the username input
    varFiltersCg = True         # varFiltersCg = tracks if username is valid (starts as True)
    
    # Rule 1: Between 4 and 25 characters
    if not (4 <= len(strParam) <= 25):
        varFiltersCg = False    # Mark as invalid if wrong length
    
    # Rule 2: Must start with a letter
    if not strParam or not strParam[0].isalpha():
        varFiltersCg = False    # Mark as invalid if doesn't start with letter
    
    # Rule 3: Only letters, numbers, and underscore
    if not all(c.isalnum() or c == '_' for c in strParam):
        varFiltersCg = False    # Mark as invalid if contains bad characters
    
    # Rule 4: Cannot end with underscore
    if strParam.endswith('_'):
        varFiltersCg = False    # Mark as invalid if ends with underscore
    
    return "true" if varFiltersCg else "false"  # Return "true" if valid, "false" if not

# keep this function call here 
print(CodelandUsernameValidation(input()))