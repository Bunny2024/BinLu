def is_valid_zip_code(zip_code):
    if len(zip_code) == 6 and zip_code.isalnum():
        return True
    else:
        return False
    
    # if len(zip_code) == 6 and zip_code.isalnum():
    #     return True
    # return False

if __name__ =="__main__":
    zip_code = "H1B1B2"
    print(is_valid_zip_code(zip_code)) # Output: True

    zip_code = "H1B 1B2"
    print(is_valid_zip_code(zip_code)) # Output: False