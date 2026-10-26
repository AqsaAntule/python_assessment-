def reverse_string(text: str) -> str:
    result = ""
    for i in range(len(text) - 1, -1, -1):
         result = result + text[i]
    return result


def count_vowels(text: str) -> int:
    vowels = "aeiou"
    count = 0

    for ch in text:    
        if ch.lower() in vowels:
            count += 1


if __name__ == "__main__":
    print(reverse_string("hello"))      
    print(reverse_string(""))            
    print(reverse_string("Python"))      

    print(count_vowels("Hello World"))   
    print(count_vowels(""))              
    print(count_vowels("AEIOU"))         
    print(count_vowels("rhythm"))  