#!/usr/bin/env python3

#!/usr/bin/env python3

def is_palindrome(phrase):

  if len(phrase) == 1:
    return True
  if len(phrase) == 2:
    if phrase[0] == phrase[1]:
      return True
    return False
  length = len(phrase)
  if phrase[0] == phrase[length - 1]:
    return is_palindrome(phrase[1:length - 1])
  return False
    