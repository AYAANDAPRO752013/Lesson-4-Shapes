Books={"Physics":150,
       "English":250,
       "Ethics":200,
       "Biologics":500,
       "Chemistry":1055}

Books["Physics"]=200

print(Books)

Books["Maths"]=140
Books["Arts"]=775

print(Books.keys())
print(Books.values())

print(Books["English"])

print(Books)

def gbc():
    bookname=input("Enter the books name")
    cost=Books.get(bookname)
    if cost:
        print(f"the cost of {bookname}is{cost}")
        
    else:
        print("We dont have that book in our store")

def bookgallery():
    print("The books avalible are:")
    for book,cost in Books.items():
     print(f"{book};{cost}")        

gbc()
bookgallery()
