"""A function to abbreviate strings."""

__author__ = "730004269"

def abbreviate(question: str) -> str:
    newstring = ""
    i = 0
    while i < len(question):
       if question[i].isupper():
           newstring += question[i]
       i += 1
    return newstring  

def main() -> None:
    question: str = str(input("Wrtie some text with some uppercase letters:  "))
    print(f"The abbreviation is a {abbreviate}")

    # for new in question:
    #   if new.isupper():
    #      newstring += new
    #return newstring
    
   

if __name__ == "__main__":
    main()