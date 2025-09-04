def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"]
    
    def two_digits(num):
        if num < 10:
            return ones[num]
        elif 10 <= num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + (" " + ones[num % 10] if (num % 10 != 0) else "")
    
    def three_digits(num):
        if num < 100:
            return two_digits(num)
        else:
            return ones[num // 100] + " Hundred" + (" " + two_digits(num % 100) if (num % 100 != 0) else "")
    
    
    if n == 0:
        return "Zero"
    
    
    result = ""
    if n >= 1000:
        result += three_digits(n // 1000) + " Thousand "
        n = n % 1000
    
    result += three_digits(n)
    
    return result.strip()



num = int(input("Enter a number (0-9999): "))
print("In words:", number_to_words(num))