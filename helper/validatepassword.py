def validate_password(password):
    l, u, p, d = 0, 0, 0, 0
    s = "R@m@_f0rtu9e$"
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnopqrstuvwxyz"
    specialchar="$@_"
    digits="0123456789"
    if (len(s) >= 8):
        for i in s:
    
            # counting lowercase alphabets
            if (i in smallalphabets):
                l+=1           
    
            # counting uppercase alphabets
            if (i in capitalalphabets):
                u+=1           
    
            # counting digits
            if (i in digits):
                d+=1           
    
            # counting the mentioned special characters
            if(i in specialchar):
                p+=1       

    if(l<=1):
        return "should contain atleast 2 samll letters"
    if(u<=1):
        return "should contain atleast 2 samll letters"
    if(p<=1):
        return "should contain atleast 2 samll letters"
    if(d<=1):
        return "should contain atleast 2 samll letters"
    else:
        return "strong password"