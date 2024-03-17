def pattern_search(text, pattern, replacement, case_sensitive=True):
    fixed_text = ""
    num_skips = 0
    
    for index in range(len(text)):
        if num_skips > 0:
            num_skips -= 1
            continue
        
        match_count = 0
        if index + len(pattern) <= len(text):  
            for char in range(len(pattern)):
                if case_sensitive and pattern[char] == text[index + char]:
                    match_count += 1
                elif not case_sensitive and pattern[char].lower() == text[index + char].lower():
                    match_count += 1
                else:
                    break
        
        if match_count == len(pattern):
            fixed_text += replacement
            num_skips = len(pattern) - 1
        else:
            fixed_text += text[index]
    
    return fixed_text

# Example usage
friends_intro = "Python is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than ideal, by properly zzz utilizing built-in libraries and other language features, Python's performance zzz can approach that of C."
print(pattern_search(friends_intro, "Language", "language"))
print(pattern_search(friends_intro, "pylhon", "Python", False))
print(pattern_search(friends_intro, "idil", "ideal", False))
print(pattern_search(friends_intro, "zzz ", ""))
print(pattern_search(friends_intro, "syntacs", "syntax"))
print(pattern_search(friends_intro, "languuUuage", "language"))
