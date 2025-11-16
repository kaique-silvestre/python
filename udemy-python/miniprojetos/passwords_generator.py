import secrets
import string 

def password(
        password_length: int | None = None,
        digits: bool = True,
        lower_letters: bool = True,
        upper_letters: bool = True,
        punctuation: bool = True 
        ) -> str:
    
    sec = secrets.SystemRandom()
   
    all_symbols = '' 

    if password_length == None:
        password_length = sec.randint(6, 24) 

    check(password_length, digits, lower_letters, upper_letters, punctuation)


    if digits:
        all_symbols += string.digits
    if lower_letters:
        all_symbols += string.ascii_lowercase
    if upper_letters:
        all_symbols += string.ascii_uppercase
    if punctuation:
        all_symbols += string.punctuation
    


    list_random_symbols = sec.choices(all_symbols, k=password_length)
    string_random_symbols = ''.join(list_random_symbols)
    return string_random_symbols

def check(password_lenght, digits, lower_letters, upper_letters, punctuation):
        if not isinstance(digits, bool) or not isinstance(lower_letters, bool) or not \
        isinstance(upper_letters, bool) or not isinstance(punctuation, bool):
            raise Exception("You must to write a bool")
        if not digits and not lower_letters and not upper_letters and not punctuation:
             raise Exception("You cannot let every optinion to be false") 
