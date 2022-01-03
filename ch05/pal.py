def is_palindrome(word):
    imsi = word[::-1]
    return imsi == word
print("racecar :",is_palindrome("racecar"))
print("stars :",is_palindrome("stars"))
print("토마토 :",is_palindrome("토마토"))
print("kayak :", is_palindrome("kayak"))
print("hello :",is_palindrome("hello"))