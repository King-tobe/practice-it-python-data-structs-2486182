from collections import deque 
#function to check the word if its Palindrome
def palindrome_checker(word):
    #creating a deque stack
    d = deque(word)
    #while len is greater than 1
    while len(d) > 1:
        # check the word from left to right if they're equal
        if d.pop() != d.popleft():
            return False
    return True

def main():
    w = "age"
    print(palindrome_checker(w))
    #add code here
    return

if __name__ == "__main__":
    main()