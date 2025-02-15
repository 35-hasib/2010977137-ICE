**I. Introduction to Python**

* **What is Python?** (Brief overview, applications, advantages)  
* **Setting up your environment** (Installing Python, choosing an IDE or text editor)

**II. Basic Syntax and Data Types**

**Printing to the console:**  
Python  
print("Hello, world\!")   
print("This is my first Python program.")

1. 

**Variables and data types:**  
Python  
name \= "Alice"  \# String  
age \= 30       \# Integer  
height \= 5.8   \# Float  
is\_student \= True \# Boolean  
print(name, age, height, is\_student)

2. 

**Basic operators:**  
Python  
a \= 10  
b \= 5  
print(a \+ b)  \# Addition  
print(a \- b)  \# Subtraction  
print(a \* b)  \# Multiplication  
print(a / b)  \# Division  
print(a // b) \# Floor division  
print(a % b)  \# Modulus (remainder)  
print(a \*\* b) \# Exponentiation

3. 

**III. Control Flow**

**Conditional statements (if-else):**  
Python  
age \= 20  
if age \>= 18:  
    print("You are an adult.")  
else:  
    print("You are a minor.")

1. 

**Loops (for and while):**  
Python  
\# For loop  
for i in range(5):  \# Prints numbers from 0 to 4  
    print(i)

\# While loop  
count \= 0  
while count \< 5:  
    print(count)  
    count \+= 1

2. 

**IV. Data Structures**

**Lists:**  
Python  
my\_list \= \[1, 2, 3, "apple", "banana"\]  
print(my\_list\[0\])   \# Accessing elements  
my\_list.append(4)  \# Adding elements  
my\_list.remove("apple")  \# Removing elements  
print(my\_list)

1. 

**Tuples:**  
Python  
my\_tuple \= (1, 2, 3\)  
print(my\_tuple\[0\])  \# Accessing elements (tuples are immutable)

2. 

**Dictionaries:**  
Python  
my\_dict \= {"name": "Bob", "age": 25, "city": "New York"}  
print(my\_dict\["name"\])  \# Accessing values by key  
my\_dict\["country"\] \= "USA"  \# Adding key-value pairs

3. 

**V. Functions**

**Defining and calling functions:**  
Python  
def greet(name):  
    """This function greets the person passed in as a parameter."""  
    print("Hello, " \+ name \+ "\!")

greet("Alice")  \# Calling the function

1. 

**Returning values:**  
Python  
def add(x, y):  
    return x \+ y

result \= add(5, 3\)  
print(result)  \# Output: 8

2. 

**VI. Working with Files**

**Reading from a CSV file:**  
Python  
import csv

with open('data.csv', 'r') as file:  
    reader \= csv.reader(file)  
    for row in reader:  
        print(row)

1. 

**Writing to a CSV file:**  
Python  
import csv

data \= \[\['Name', 'Age', 'City'\], \['Alice', 30, 'New York'\], \['Bob', 25, 'Los Angeles'\]\]

with open('output.csv', 'w', newline='') as file:  
    writer \= csv.writer(file)  
    writer.writerows(data) 

2. 

**VII. Object-Oriented Programming (OOP)**

1. **Classes and objects:**

class Car: def **init**(self, make, model): self.make \= make self.model \= model

  def drive(self):  
       print("The car is driving.")

my\_car \= Car("Toyota", "Camry") my\_car.drive()  

2\. \*\*Inheritance:\*\*  
\`\`\`python  
class ElectricCar(Car):  
    def charge(self):  
        print("The car is charging.")

my\_electric\_car \= ElectricCar("Tesla", "Model S")  
my\_electric\_car.drive()  
my\_electric\_car.charge()

3. **Encapsulation:** (Example already provided above)

**VIII. Functional Programming**

**Lambda functions:**  
Python  
square \= lambda x: x \* x  
print(square(5))  \# Output: 25

1.   
2. **Map, filter, reduce:** (Examples with `map` and `filter` provided above. You can add `reduce` from the `functools` library if needed)

**IX. Modules and Packages**

**Importing modules:**  
Python  
import math  
print(math.sqrt(25))  \# Output: 5.0

*   
* **Using external packages:** (Explain how to install packages using `pip`)

**Generating the .doc file:**

I can't directly create and save a .doc file for you. However, I can give you all of this content in a well-formatted way that you can easily copy and paste into a Word document:

* **Code blocks:** I'll use Markdown code blocks (`python ...`) to format the code.  
* **Explanations:** I'll provide clear explanations for each concept and code example.  
* **Structure:** I'll use headings and subheadings to organize the content logically.

Once you have the content, you can:

1. **Create a new Word document.**  
2. **Paste the content.**  
3. **Adjust formatting:** Apply headings, font styles, and code highlighting as needed.  
4. **Save as .doc or .docx:** Choose your preferred Word document format.

I'm ready to start creating this Python crash course content for you. Just let me know if you have any specific preferences or if you want to add or remove any topics\!

![profile picture][image1]

yes create it

Okay, I'm creating the Python crash course content for you. Here it is, formatted and ready for you to copy and paste into a Word document:

# **Python Crash Course**

## **I. Introduction to Python**

**What is Python?**

Python is a high-level, interpreted, general-purpose programming language. It's known for its clear syntax and readability, making it a great language for beginners and experienced programmers alike. Python is used in a wide range of applications, including:

* Web development  
* Data science and machine learning    
*   
* Scripting and automation  
* Desktop applications  
* Game development

**Advantages of Python:**

* **Easy to learn:** Python has a simple and straightforward syntax.  
* **Versatile:** It can be used for a wide variety of tasks.  
* **Large community:** There's a huge and supportive Python community, making it easy to find help and resources.  
* **Extensive libraries:** Python has a vast collection of libraries for various purposes.

**Setting up your environment**

1. **Install Python:** Download the latest version of Python from the official website (python.org) and follow the installation instructions for your operating system.    
2.   
3. **Choose an IDE or text editor:** An Integrated Development Environment (IDE) provides tools for writing, debugging, and running code. Popular Python IDEs include PyCharm, VS Code, and Spyder. Alternatively, you can use a simple text editor like Sublime Text or Atom.

## **II. Basic Syntax and Data Types**

### **1\. Printing to the console:**

Python  
print("Hello, world\!")   
print("This is my first Python program.")

This code uses the `print()` function to display text on the console.

### **2\. Variables and data types:**

Python  
name \= "Alice"  \# String  
age \= 30       \# Integer  
height \= 5.8   \# Float  
is\_student \= True \# Boolean  
print(name, age, height, is\_student)

* **Variables** are used to store data. In Python, you create a variable by assigning a value to a name (e.g., `name = "Alice"`).  
* **Data types** represent the kind of value a variable holds. Common data types include:  
  * **String:** Text enclosed in single or double quotes (e.g., "Hello").  
  * **Integer:** Whole numbers (e.g., 10, \-5).  
  * **Float:** Numbers with decimal points (e.g., 3.14).  
  * **Boolean:** Represents truth values (`True` or `False`).

### **3\. Basic operators:**

Python  
a \= 10  
b \= 5  
print(a \+ b)  \# Addition  
print(a \- b)  \# Subtraction  
print(a \* b)  \# Multiplication  
print(a / b)  \# Division  
print(a // b) \# Floor division (result is an integer)  
print(a % b)  \# Modulus (remainder)  
print(a \*\* b) \# Exponentiation

Python provides various operators for performing arithmetic and other operations.

## **III. Control Flow**

### **1\. Conditional statements (if-else):**

Python  
age \= 20  
if age \>= 18:  
    print("You are an adult.")  
else:  
    print("You are a minor.")

* `if-else` statements allow you to execute different blocks of code based on a condition.  
* The code inside the `if` block will run if the condition is `True`, otherwise the code inside the `else` block will run.

### **2\. Loops (for and while):**

Python  
\# For loop  
for i in range(5):  \# Prints numbers from 0 to 4  
    print(i)

\# While loop  
count \= 0  
while count \< 5:  
    print(count)  
    count \+= 1

* **Loops** are used to repeat a block of code multiple times.  
* **`for` loop:** Iterates over a sequence (like a list or range of numbers).  
* **`while` loop:** Repeats as long as a condition is `True`.

## **IV. Data Structures**

### **1\. Lists:**

Python  
my\_list \= \[1, 2, 3, "apple", "banana"\]  
print(my\_list\[0\])   \# Accessing elements (index starts from 0\)  
my\_list.append(4)  \# Adding elements to the end  
my\_list.remove("apple")  \# Removing elements  
print(my\_list)

* **Lists** are ordered collections of items. They can store different data types.  
* Lists are mutable, meaning you can change their contents after creation.

### **2\. Tuples:**

Python  
my\_tuple \= (1, 2, 3\)  
print(my\_tuple\[0\])  \# Accessing elements

* **Tuples** are similar to lists but are immutable (cannot be changed after creation).

### **3\. Dictionaries:**

Python  
my\_dict \= {"name": "Bob", "age": 25, "city": "New York"}  
print(my\_dict\["name"\])  \# Accessing values by key  
my\_dict\["country"\] \= "USA"  \# Adding key-value pairs

* **Dictionaries** store key-value pairs. You can access values using their corresponding keys.

## **V. Functions**

### **1\. Defining and calling functions:**

Python  
def greet(name):  
    """This function greets the person passed in as a parameter."""  
    print("Hello, " \+ name \+ "\!")

greet("Alice")  \# Calling the function

* **Functions** are blocks of reusable code.  
* The `def` keyword is used to define a function.  
* Functions can take parameters (input values).

### **2\. Returning values:**

Python  
def add(x, y):  
    return x \+ y

result \= add(5, 3\)  
print(result)  \# Output: 8

* Functions can return values using the `return` statement.

## **VI. Working with Files**

### **1\. Reading from a CSV file:**

Python  
import csv

with open('data.csv', 'r') as file:  
    reader \= csv.reader(file)  
    for row in reader:  
        print(row)

* This code reads data from a CSV (Comma Separated Values) file.  
* The `csv` module provides functions for working with CSV files.

### **2\. Writing to a CSV file:**

Python  
import csv

data \= \[\['Name', 'Age', 'City'\], \['Alice', 30, 'New York'\], \['Bob', 25, 'Los Angeles'\]\]

with open('output.csv', 'w', newline='') as file:  
    writer \= csv.writer(file)  
    writer.writerows(data)

* This code writes data to a CSV file.

## **VII. Object-Oriented Programming (OOP)**

### **1\. Classes and objects:**

Python  
class Car:  
    def \_\_init\_\_(self, make, model):  
        self.make \= make  
        self.model \= model

    def drive(self):  
        print("The car is driving.")

my\_car \= Car("Toyota", "Camry")  
my\_car.drive()

* **Classes** are blueprints for creating objects.  
* **Objects** are instances of a class.  
* The `__init__` method is a special method (constructor) that is called when an object is created.

### **2\. Inheritance:**

Python  
class ElectricCar(Car):  \# ElectricCar inherits from Car  
    def charge(self):  
        print("The car is charging.")

my\_electric\_car \= ElectricCar("Tesla", "Model S")  
my\_electric\_car.drive()  \# Inherited method  
my\_electric\_car.charge()

* **Inheritance** allows you to create new classes that inherit properties and methods from existing classes.

### **3\. Encapsulation:**

Python  
class BankAccount:  
    def \_\_init\_\_(self, initial\_balance):  
        self.\_\_balance \= initial\_balance  \# Private attribute

    def deposit(self, amount):  
        self.\_\_balance \+= amount

    def withdraw(self, amount):  
        if amount \<= self.\_\_balance:  
            self.\_\_balance \-= amount  
        else:  
            print("Insufficient funds")

    def get\_balance(self):  
        return self.\_\_balance

account \= BankAccount(1000)  
account.deposit(500)  
account.withdraw(200)  
print(account.get\_balance())  \# Output: 1300  
\# print(account.\_\_balance)  \# This would cause an error (accessing private attribute)

* **Encapsulation** restricts access to the internal state of an object.  
* Private attributes (with names starting with `__`) cannot be accessed directly from outside the class.

## **VIII. Functional Programming**

### **1\. Lambda functions:**

Python  
square \= lambda x: x \* x  
print(square(5))  \# Output: 25

* **Lambda functions** are small, anonymous functions defined using the `lambda` keyword.

### **2\. Map and filter:**

Python  
def square(x):  
  return x \* x

numbers \= \[1, 2, 3, 4, 5\]  
squared\_numbers \= list(map(square, numbers))  \# Apply square function to each element  
print(squared\_numbers)  \# Output: \[1, 4, 9, 16, 25\]

def is\_even(x):  
  return x % 2 \== 0

even\_numbers \= list(filter(is\_even, numbers))  \# Filter even numbers  
print(even\_numbers)  \# Output: \[2, 4\]

* **`map`:** Applies a function to each element of an iterable.  
* **`filter`:** Creates a new iterable with elements that pass a certain condition.

## **IX. Modules and Packages**

### **1\. Importing modules:**

Python  
import math  
print(math.sqrt(25))  \# Output: 5.0

* **Modules** are files containing Python code.  
* The `import` statement is used to access code from modules.

### **2\. Using external packages:**

* **Packages** are collections of modules.  
* You can install packages using the `pip` package manager (e.g., `pip install requests`).  
* Once installed, you can import and use packages in your code.

**Remember:**

* Copy and paste this content into a Word document.  
* Adjust the formatting (headings, fonts, code highlighting) to your liking.  
* Save the document as a .doc or .docx file.

This crash course provides a good starting point for learning Python. Let me know if you have any other questions\!

# **Conversation with Gemini**

**![profile picture][image2]**

give me 1 example of every type of programs with python

like OOP, encapsulations

and make a doc file

**1\. Procedural Programming**

* **Concept:** Organizes code into a step-by-step set of instructions.  
* **Example:**

Python  
def calculate\_area(length, width):  
  """Calculates the area of a rectangle."""  
  area \= length \* width  
  return area

\# Get input from the user  
length \= float(input("Enter the length of the rectangle: "))  
width \= float(input("Enter the width of the rectangle: "))

\# Calculate and print the area  
area \= calculate\_area(length, width)  
print("The area of the rectangle is:", area)

**2\. Object-Oriented Programming (OOP)**

* **Concept:** Structures code around "objects" which combine data (attributes) and actions (methods).  
* **Example:**

Python  
class Dog:  
    def \_\_init\_\_(self, name, breed):  
        self.name \= name  
        self.breed \= breed

    def bark(self):  
        return "Woof\!"

my\_dog \= Dog("Buddy", "Golden Retriever")  
print(my\_dog.name)  \# Output: Buddy  
print(my\_dog.bark()) \# Output: Woof\!

**3\. Encapsulation**

* **Concept:** Bundles data and methods within a class, controlling access to the internal state of an object.  
* **Example:**

Python  
class BankAccount:  
    def \_\_init\_\_(self, initial\_balance):  
        self.\_\_balance \= initial\_balance  \# Private attribute

    def deposit(self, amount):  
        self.\_\_balance \+= amount

    def withdraw(self, amount):  
        if amount \<= self.\_\_balance:  
            self.\_\_balance \-= amount  
        else:  
            print("Insufficient funds")

    def get\_balance(self):  
        return self.\_\_balance

account \= BankAccount(1000)  
account.deposit(500)  
account.withdraw(200)  
print(account.get\_balance())  \# Output: 1300  
\# print(account.\_\_balance)  \# This would cause an error (private attribute) 

**4\. Functional Programming**

* **Concept:** Relies on functions as the primary building blocks, often avoiding changing state and mutable data.  
* **Example:**

Python  
def square(x):  
  return x \* x

numbers \= \[1, 2, 3, 4, 5\]  
squared\_numbers \= list(map(square, numbers))   
print(squared\_numbers)  \# Output: \[1, 4, 9, 16, 25\]

**Creating a .doc file**

You can create a Word document (.doc or .docx) and include these examples. Here's how you could structure it:

**Title:** Python Programming Examples

**Sections:**

* **Procedural Programming:**  
  * Explanation of procedural programming  
  * Code example (calculate\_area function)  
* **Object-Oriented Programming:**  
  * Explanation of OOP concepts (classes, objects, methods, etc.)  
  * Code example (Dog class)  
* **Encapsulation:**  
  * Explanation of encapsulation and its benefits  
  * Code example (BankAccount class)  
* **Functional Programming**  
  * Explanation of functional programming paradigms  
  * Code example (square function and map)

**To create the .doc file:**

1. **Use a Word Processor:** Open Microsoft Word, LibreOffice Writer, or a similar program.  
2. **Type in Content:** Add the title, section headings, explanations, and code examples.  
3. **Format:** Use headings, bullet points, and code formatting to make the document clear and readable.  
4. **Save:** Save the file as a .doc or .docx document.

If you want to generate the .doc file programmatically with Python, you could use libraries like `python-docx`. Let me know if you'd like help with that\!

![profile picture][image3]

no you didn't understand

i need every example step by step

like printing a statement, read csv file

like a course

and create a doc file with it

You're right, I apologize for missing that\! It seems like you want a comprehensive Python tutorial presented in a structured way, almost like a mini-course within a Word document. I can definitely help you with that.

Here's a breakdown of the topics we can cover, presented step-by-step, and how I'll organize it into a .doc file:

**Python Crash Course (.doc)**

**I. Introduction to Python**

* **What is Python?** (Brief overview, applications, advantages)  
* **Setting up your environment** (Installing Python, choosing an IDE or text editor)

**II. Basic Syntax and Data Types**

**Printing to the console:**  
Python  
print("Hello, world\!")   
print("This is my first Python program.")

1. 

**Variables and data types:**  
Python  
name \= "Alice"  \# String  
age \= 30       \# Integer  
height \= 5.8   \# Float  
is\_student \= True \# Boolean  
print(name, age, height, is\_student)

2. 

**Basic operators:**  
Python  
a \= 10  
b \= 5  
print(a \+ b)  \# Addition  
print(a \- b)  \# Subtraction  
print(a \* b)  \# Multiplication  
print(a / b)  \# Division  
print(a // b) \# Floor division  
print(a % b)  \# Modulus (remainder)  
print(a \*\* b) \# Exponentiation

3. 

**III. Control Flow**

**Conditional statements (if-else):**  
Python  
age \= 20  
if age \>= 18:  
    print("You are an adult.")  
else:  
    print("You are a minor.")

1. 

**Loops (for and while):**  
Python  
\# For loop  
for i in range(5):  \# Prints numbers from 0 to 4  
    print(i)

\# While loop  
count \= 0  
while count \< 5:  
    print(count)  
    count \+= 1

2. 

**IV. Data Structures**

**Lists:**  
Python  
my\_list \= \[1, 2, 3, "apple", "banana"\]  
print(my\_list\[0\])   \# Accessing elements  
my\_list.append(4)  \# Adding elements  
my\_list.remove("apple")  \# Removing elements  
print(my\_list)

1. 

**Tuples:**  
Python  
my\_tuple \= (1, 2, 3\)  
print(my\_tuple\[0\])  \# Accessing elements (tuples are immutable)

2. 

**Dictionaries:**  
Python  
my\_dict \= {"name": "Bob", "age": 25, "city": "New York"}  
print(my\_dict\["name"\])  \# Accessing values by key  
my\_dict\["country"\] \= "USA"  \# Adding key-value pairs

3. 

**V. Functions**

**Defining and calling functions:**  
Python  
def greet(name):  
    """This function greets the person passed in as a parameter."""  
    print("Hello, " \+ name \+ "\!")

greet("Alice")  \# Calling the function

1. 

**Returning values:**  
Python  
def add(x, y):  
    return x \+ y

result \= add(5, 3\)  
print(result)  \# Output: 8

2. 

**VI. Working with Files**

**Reading from a CSV file:**  
Python  
import csv

with open('data.csv', 'r') as file:  
    reader \= csv.reader(file)  
    for row in reader:  
        print(row)

1. 

**Writing to a CSV file:**  
Python  
import csv

data \= \[\['Name', 'Age', 'City'\], \['Alice', 30, 'New York'\], \['Bob', 25, 'Los Angeles'\]\]

with open('output.csv', 'w', newline='') as file:  
    writer \= csv.writer(file)  
    writer.writerows(data) 

2. 

**VII. Object-Oriented Programming (OOP)**

1. **Classes and objects:**

class Car: def **init**(self, make, model): self.make \= make self.model \= model

  def drive(self):  
       print("The car is driving.")

my\_car \= Car("Toyota", "Camry") my\_car.drive()  

2\. \*\*Inheritance:\*\*  
\`\`\`python  
class ElectricCar(Car):  
    def charge(self):  
        print("The car is charging.")

my\_electric\_car \= ElectricCar("Tesla", "Model S")  
my\_electric\_car.drive()  
my\_electric\_car.charge()

3. **Encapsulation:** (Example already provided above)

**VIII. Functional Programming**

**Lambda functions:**  
Python  
square \= lambda x: x \* x  
print(square(5))  \# Output: 25

1.   
2. **Map, filter, reduce:** (Examples with `map` and `filter` provided above. You can add `reduce` from the `functools` library if needed)

**IX. Modules and Packages**

**Importing modules:**  
Python  
import math  
print(math.sqrt(25))  \# Output: 5.0

*   
* **Using external packages:** (Explain how to install packages using `pip`)

**Generating the .doc file:**

I can't directly create and save a .doc file for you. However, I can give you all of this content in a well-formatted way that you can easily copy and paste into a Word document:

* **Code blocks:** I'll use Markdown code blocks (`python ...`) to format the code.  
* **Explanations:** I'll provide clear explanations for each concept and code example.  
* **Structure:** I'll use headings and subheadings to organize the content logically.

Once you have the content, you can:

1. **Create a new Word document.**  
2. **Paste the content.**  
3. **Adjust formatting:** Apply headings, font styles, and code highlighting as needed.  
4. **Save as .doc or .docx:** Choose your preferred Word document format.

I'm ready to start creating this Python crash course content for you. Just let me know if you have any specific preferences or if you want to add or remove any topics\!

![profile picture][image4]

yes create it

Okay, I'm creating the Python crash course content for you. Here it is, formatted and ready for you to copy and paste into a Word document:

# **Python Crash Course**

## **I. Introduction to Python**

**What is Python?**

Python is a high-level, interpreted, general-purpose programming language. It's known for its clear syntax and readability, making it a great language for beginners and experienced programmers alike. Python is used in a wide range of applications, including:

* Web development  
* Data science and machine learning    
*   
* Scripting and automation  
* Desktop applications  
* Game development

**Advantages of Python:**

* **Easy to learn:** Python has a simple and straightforward syntax.  
* **Versatile:** It can be used for a wide variety of tasks.  
* **Large community:** There's a huge and supportive Python community, making it easy to find help and resources.  
* **Extensive libraries:** Python has a vast collection of libraries for various purposes.

**Setting up your environment**

1. **Install Python:** Download the latest version of Python from the official website (python.org) and follow the installation instructions for your operating system.    
2.   
3. **Choose an IDE or text editor:** An Integrated Development Environment (IDE) provides tools for writing, debugging, and running code. Popular Python IDEs include PyCharm, VS Code, and Spyder. Alternatively, you can use a simple text editor like Sublime Text or Atom.

## **II. Basic Syntax and Data Types**

### **1\. Printing to the console:**

Python  
print("Hello, world\!")   
print("This is my first Python program.")

This code uses the `print()` function to display text on the console.

### **2\. Variables and data types:**

Python  
name \= "Alice"  \# String  
age \= 30       \# Integer  
height \= 5.8   \# Float  
is\_student \= True \# Boolean  
print(name, age, height, is\_student)

* **Variables** are used to store data. In Python, you create a variable by assigning a value to a name (e.g., `name = "Alice"`).  
* **Data types** represent the kind of value a variable holds. Common data types include:  
  * **String:** Text enclosed in single or double quotes (e.g., "Hello").  
  * **Integer:** Whole numbers (e.g., 10, \-5).  
  * **Float:** Numbers with decimal points (e.g., 3.14).  
  * **Boolean:** Represents truth values (`True` or `False`).

### **3\. Basic operators:**

Python  
a \= 10  
b \= 5  
print(a \+ b)  \# Addition  
print(a \- b)  \# Subtraction  
print(a \* b)  \# Multiplication  
print(a / b)  \# Division  
print(a // b) \# Floor division (result is an integer)  
print(a % b)  \# Modulus (remainder)  
print(a \*\* b) \# Exponentiation

Python provides various operators for performing arithmetic and other operations.

## **III. Control Flow**

### **1\. Conditional statements (if-else):**

Python  
age \= 20  
if age \>= 18:  
    print("You are an adult.")  
else:  
    print("You are a minor.")

* `if-else` statements allow you to execute different blocks of code based on a condition.  
* The code inside the `if` block will run if the condition is `True`, otherwise the code inside the `else` block will run.

### **2\. Loops (for and while):**

Python  
\# For loop  
for i in range(5):  \# Prints numbers from 0 to 4  
    print(i)

\# While loop  
count \= 0  
while count \< 5:  
    print(count)  
    count \+= 1

* **Loops** are used to repeat a block of code multiple times.  
* **`for` loop:** Iterates over a sequence (like a list or range of numbers).  
* **`while` loop:** Repeats as long as a condition is `True`.

## **IV. Data Structures**

### **1\. Lists:**

Python  
my\_list \= \[1, 2, 3, "apple", "banana"\]  
print(my\_list\[0\])   \# Accessing elements (index starts from 0\)  
my\_list.append(4)  \# Adding elements to the end  
my\_list.remove("apple")  \# Removing elements  
print(my\_list)

* **Lists** are ordered collections of items. They can store different data types.  
* Lists are mutable, meaning you can change their contents after creation.

### **2\. Tuples:**

Python  
my\_tuple \= (1, 2, 3\)  
print(my\_tuple\[0\])  \# Accessing elements

* **Tuples** are similar to lists but are immutable (cannot be changed after creation).

### **3\. Dictionaries:**

Python  
my\_dict \= {"name": "Bob", "age": 25, "city": "New York"}  
print(my\_dict\["name"\])  \# Accessing values by key  
my\_dict\["country"\] \= "USA"  \# Adding key-value pairs

* **Dictionaries** store key-value pairs. You can access values using their corresponding keys.

## **V. Functions**

### **1\. Defining and calling functions:**

Python  
def greet(name):  
    """This function greets the person passed in as a parameter."""  
    print("Hello, " \+ name \+ "\!")

greet("Alice")  \# Calling the function

* **Functions** are blocks of reusable code.  
* The `def` keyword is used to define a function.  
* Functions can take parameters (input values).

### **2\. Returning values:**

Python  
def add(x, y):  
    return x \+ y

result \= add(5, 3\)  
print(result)  \# Output: 8

* Functions can return values using the `return` statement.

## **VI. Working with Files**

### **1\. Reading from a CSV file:**

Python  
import csv

with open('data.csv', 'r') as file:  
    reader \= csv.reader(file)  
    for row in reader:  
        print(row)

* This code reads data from a CSV (Comma Separated Values) file.  
* The `csv` module provides functions for working with CSV files.

### **2\. Writing to a CSV file:**

Python  
import csv

data \= \[\['Name', 'Age', 'City'\], \['Alice', 30, 'New York'\], \['Bob', 25, 'Los Angeles'\]\]

with open('output.csv', 'w', newline='') as file:  
    writer \= csv.writer(file)  
    writer.writerows(data)

* This code writes data to a CSV file.

## **VII. Object-Oriented Programming (OOP)**

### **1\. Classes and objects:**

Python  
class Car:  
    def \_\_init\_\_(self, make, model):  
        self.make \= make  
        self.model \= model

    def drive(self):  
        print("The car is driving.")

my\_car \= Car("Toyota", "Camry")  
my\_car.drive()

* **Classes** are blueprints for creating objects.  
* **Objects** are instances of a class.  
* The `__init__` method is a special method (constructor) that is called when an object is created.

### **2\. Inheritance:**

Python  
class ElectricCar(Car):  \# ElectricCar inherits from Car  
    def charge(self):  
        print("The car is charging.")

my\_electric\_car \= ElectricCar("Tesla", "Model S")  
my\_electric\_car.drive()  \# Inherited method  
my\_electric\_car.charge()

* **Inheritance** allows you to create new classes that inherit properties and methods from existing classes.

### **3\. Encapsulation:**

Python  
class BankAccount:  
    def \_\_init\_\_(self, initial\_balance):  
        self.\_\_balance \= initial\_balance  \# Private attribute

    def deposit(self, amount):  
        self.\_\_balance \+= amount

    def withdraw(self, amount):  
        if amount \<= self.\_\_balance:  
            self.\_\_balance \-= amount  
        else:  
            print("Insufficient funds")

    def get\_balance(self):  
        return self.\_\_balance

account \= BankAccount(1000)  
account.deposit(500)  
account.withdraw(200)  
print(account.get\_balance())  \# Output: 1300  
\# print(account.\_\_balance)  \# This would cause an error (accessing private attribute)

* **Encapsulation** restricts access to the internal state of an object.  
* Private attributes (with names starting with `__`) cannot be accessed directly from outside the class.

## **VIII. Functional Programming**

### **1\. Lambda functions:**

Python  
square \= lambda x: x \* x  
print(square(5))  \# Output: 25

* **Lambda functions** are small, anonymous functions defined using the `lambda` keyword.

### **2\. Map and filter:**

Python  
def square(x):  
  return x \* x

numbers \= \[1, 2, 3, 4, 5\]  
squared\_numbers \= list(map(square, numbers))  \# Apply square function to each element  
print(squared\_numbers)  \# Output: \[1, 4, 9, 16, 25\]

def is\_even(x):  
  return x % 2 \== 0

even\_numbers \= list(filter(is\_even, numbers))  \# Filter even numbers  
print(even\_numbers)  \# Output: \[2, 4\]

* **`map`:** Applies a function to each element of an iterable.  
* **`filter`:** Creates a new iterable with elements that pass a certain condition.

## **IX. Modules and Packages**

### **1\. Importing modules:**

Python  
import math  
print(math.sqrt(25))  \# Output: 5.0

* **Modules** are files containing Python code.  
* The `import` statement is used to access code from modules.

### **2\. Using external packages:**

* **Packages** are collections of modules.  
* You can install packages using the `pip` package manager (e.g., `pip install requests`).  
* Once installed, you can import and use packages in your code.

**Remember:**

* Copy and paste this content into a Word document.  
* Adjust the formatting (headings, fonts, code highlighting) to your liking.  
* Save the document as a .doc or .docx file.

This crash course provides a good starting point for learning Python. Let me know if you have any other questions\!

Sources and related content  
[www.prepbytes.com](https://www.prepbytes.com/blog/infosys-company/infosys-python-language-questions/)  
[www.prepbytes.com](https://www.prepbytes.com/blog/infosys-company/infosys-python-language-questions/)  
[karsaathi.com](https://karsaathi.com/best-learning-sites-for-python/)  
[karsaathi.com](https://karsaathi.com/best-learning-sites-for-python/)  
[github.com](https://github.com/Rj1221/PythonTutorial)  
[MIT](https://github.com/Rj1221/PythonTutorial)  
[github.com](https://github.com/Rj1221/PythonTutorial)  
[github.com](https://github.com/uditbaliyan/PYTHON)  
[github.com](https://github.com/uditbaliyan/PYTHON)  
[github.com](https://github.com/Prasad8ab/Prasad_Assign)  
[github.com](https://github.com/Prasad8ab/Prasad_Assign)  
[![profile picture][image5]](https://github.com/Prasad8ab/Prasad_Assign)

want add numpy and pandas

Okay, I'll add sections on NumPy and pandas to the Python crash course.

**Python Crash Course (.doc)**

(Previous sections: I to IX as provided before)

## **X. NumPy**

**What is NumPy?**

NumPy (Numerical Python) is a powerful library for numerical computing in Python. It provides:

* **N-dimensional arrays:** Efficient data structures for storing and manipulating large arrays of numbers.  
* **Mathematical functions:** A wide range of mathematical operations for arrays.  
* **Linear algebra, Fourier transforms, and random number capabilities:** Tools for advanced mathematical computations.

**Getting started with NumPy**

**Installation:**  
Bash  
pip install numpy

1. 

**Importing NumPy:**  
Python  
import numpy as np  \# np is a common alias for numpy

2. 

**Creating arrays:**  
Python  
\# 1D array  
arr1 \= np.array(\[1, 2, 3, 4, 5\])  

\# 2D array  
arr2 \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\]) 

\# Array filled with zeros  
zeros\_arr \= np.zeros(5)  

\# Array filled with ones  
ones\_arr \= np.ones((2, 3)) 

3. 

**Array operations:**  
Python  
a \= np.array(\[1, 2, 3\])  
b \= np.array(\[4, 5, 6\])

print(a \+ b)  \# Element-wise addition  
print(a \* b)  \# Element-wise multiplication  
print(np.dot(a, b))  \# Dot product

4. 

**Array indexing and slicing:**  
Python  
arr \= np.array(\[1, 2, 3, 4, 5\])  
print(arr\[0\])    \# Accessing the first element  
print(arr\[1:4\])  \# Slicing (elements from index 1 to 3\)

5. 

## **XI. Pandas**

**What is pandas?**

pandas is a library built on top of NumPy that provides high-performance, easy-to-use data structures and data analysis tools. It's particularly useful for working with tabular data (like CSV files or spreadsheets).

**Key features of pandas:**

* **DataFrame:** A 2-dimensional labeled data structure (like a table).  
* **Series:** A 1-dimensional labeled array.  
* **Data manipulation:** Tools for cleaning, transforming, and analyzing data.  
* **Data import and export:** Functions for reading and writing data from various formats (CSV, Excel, etc.).

**Getting started with pandas**

**Installation:**  
Bash  
pip install pandas

1. 

**Importing pandas:**  
Python  
import pandas as pd  \# pd is a common alias for pandas

2. 

**Creating DataFrames:**  
Python  
\# From a dictionary  
data \= {'Name': \['Alice', 'Bob', 'Charlie'\],   
        'Age': \[25, 30, 28\],   
        'City': \['New York', 'Los Angeles', 'Chicago'\]}  
df \= pd.DataFrame(data)

\# From a CSV file  
df \= pd.read\_csv('data.csv') 

3. 

**Data exploration:**  
Python  
print(df.head())      \# Display the first few rows  
print(df.describe())  \# Summary statistics  
print(df.columns)    \# Column names

4. 

**Data manipulation:**  
Python  
print(df\['Name'\])       \# Access a column  
print(df\[df\['Age'\] \> 28\])  \# Filtering rows  
df\['Salary'\] \= \[50000, 60000, 55000\]  \# Adding a new column

5. 

**File handling in Python**

**Opening a file:**

 Python  
file \= open('my\_file.txt', 'r')  \# 'r' for reading (default mode)

1.   
   * The `open()` function opens a file and returns a file object.  
   * The second argument specifies the mode:  
     * `'r'`: Read mode.  
     * `'w'`: Write mode (creates a new file or overwrites an existing one).  
     * `'a'`: Append mode (adds data to the end of the file).  
     * `'x'`: Create mode (creates a new file, fails if the file exists).

**Reading from a file:**

 Python  
file \= open('my\_file.txt', 'r')  
content \= file.read()  \# Read the entire file content  
print(content)

file.seek(0)  \# Go back to the beginning of the file  
line \= file.readline()  \# Read a single line  
print(line)

file.seek(0)  
for line in file:  \# Iterate over lines  
    print(line, end='')   
file.close()

2. 

**Writing to a file:**

 Python  
file \= open('output.txt', 'w')  
file.write("This is some text.\\n")  \# Write a string  
file.write("This is another line.")  
file.close()

3. 

**Closing a file:**

 Python  
file.close()

4.   
   * It's important to close files after you're done with them to release resources.

**Using `with` statement (recommended):**

 Python  
with open('my\_file.txt', 'r') as file:  
    content \= file.read()  
    print(content)

5. \# File is automatically closed when you exit the 'with' block

**Using the `csv` module**

**Reading with `csv.reader`:**

 Python  
import csv

with open('data.csv', 'r') as file:  
    reader \= csv.reader(file)  
    for row in reader:  
        print(row)  \# Each row is a list of values

1. 

**Reading with `csv.DictReader`:**

 Python  
import csv

with open('data.csv', 'r') as file:  
    reader \= csv.DictReader(file)  
    for row in reader:  
        print(row)  \# Each row is a dictionary  
        print(row\['Name'\], row\['Age'\])  \# Access values by column headers

2. 

**Writing with `csv.writer`:**

 Python  
import csv

data \= \[\['Name', 'Age', 'City'\], \['Alice', 30, 'New York'\], \['Bob', 25, 'Los Angeles'\]\]

with open('output.csv', 'w', newline='') as file:  
    writer \= csv.writer(file)  
    writer.writerows(data)  \# Write multiple rows

3. 

**Writing with `csv.DictWriter`:**

 Python  
import csv

data \= \[{'Name': 'Alice', 'Age': 30, 'City': 'New York'},  
        {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'}\]

with open('output.csv', 'w', newline='') as file:  
    fieldnames \= \['Name', 'Age', 'City'\]  \# Define column headers  
    writer \= csv.DictWriter(file, fieldnames=fieldnames)  
    writer.writeheader()  \# Write header row  
    writer.writerows(data)  \# Write data rows

4. 

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAL70lEQVR4Xi1W+VeS+R7mD7i/3HPvnGlSU8sllzTN0Ukr03LLNc2VXBKEBDdEQFEWUVATAQERRVZRIVBEUEFxSZs2LW26kzN1b03N1KRpapG7vPedc+85n/Oe95f3eT7P53m+388LQSGyS9H5NDKurAjW0kRmNpJYt8i1JEwjrYJWhWLVYZpq0CUF1/KuJ924kZkFTcNX4OD5sKTEeGhWamVlCYWCbWFRf1q882nltW1vGzg43N3aBICN9dVfD7c/AvtWSFx0aMKVMGwpglqDLS7MqSWV8zl0ei2+CoukVqITLwUVZMamxoaeD/QOu3A2OioiISb+8sWw+JjorLSUvOw0bBkSiyngc+kvl+YA255tZwcAtratv//x9jGwtwrYtiBIWAYKAU29GokvR4LoNDK2oa6yiV5TVV50PSUuPMgvLiwkNjzk9EnXAF/v8AvnzweFnDnldzH4XFxk5LXEuIyUxIK8LAaNUEfFPJwZA2w7wO7a5urzV7/OAoerwMEXSBWukIBFspuphQVZGddiMcVwZiOFUF6Un5Vx1tfn/Bn/c/5+YUGBHs6OPq5uwX7+QT5+YIEv5wO+j70UdvGHwLyM1Jz0RBIBSSEUPXs4DRx83Pn8wrqxBBxuAMAOBI+F11MrkLD0W4xqfHlhDQEDohchYef8z/i6ufu4nvR0dvE76eXucMz1u+/8XF1BVj93N/+T7r6uLiB3/KXw2LDQzKQYNPwaBYemVaC/vH8OfP03AKzYbJ+t1s+QRnoFrhzGZdGg6XH02sraGjw8F+rr6X7azd39mPOxI/bf/v0bV0dnD8djXg5Hv3c74eVk/72nm88JxzMnXc75nQr29QoL9A/29UiKDinKTScgcgT1+N21JeBgGWx//wCAcNnkdn5daVG2gNuARuZUVZQF+ft6uh53d7C3++ab7/55xMnO8bj9sUAvj4hAv4yoUFhafGl+JohVeP1aXkp8anR4VHBA7IXA0O+9UyPD8hNjaCWw+YnbwOHa3t7OAQBAOGxiu6Ce3UJtqK+WdvLhudf9PU9eCAzwdjnu5uR0wsHB08Ul6JR37tUEfEE2HVvIoxNlbLqmkyNlMXr4TGEDlYEryUmMjgr2jwr0zb0SgUqLlfHqAJvVZrPtHAKQWywsm08Wy3lShUgq6Wym013tjp52cXFzOu5mb+d33OHiKbeEYD9Y3GUiIptHqezhNvd38gxSoVHWYe6RjEg7+gUcPglHREBz4y5kRAShsmIbyRXA4bYN2LOBCvjCBq7wlkjertVrelU9Am6rh/MxL2dHDydnbyen8z4emREXilLjychcHgWvFbYOdrWB0KPdXWCZlGJLj3RcKekXsOQttBJofGp4ADI9up5YBuZ1/2D7LwL1oEqpUepMhiGT0Tw5hkIjvN1PnLA74unk6GlvlxIeUgmHNpWjOmhEaTNNLWDrRHy9WPA/BWO90snb3TMDfVMahUnZ0UouuxZ25mZGTBMFBxL8X4HRbNGZRvtHRwbMwwbzcFJyvIP9t64OR72POfifOIZKT2rAotpr8V10krS5XtPOMXQJjOJ2k1wEzseikk9qlDM61awe5JANitmZkT+U5V1ta64FCQ5tu38RDA6P683jPbqB/hE9OKXMrFR3F8fjR78NdD8eE3iaVlLAJ2M7agmyplo5q2FYJjLLRJZuCTiZO7eVUxrldH/vXYPmoWngvkE1o5PDksILM6/QqzEH25s7u9bd/T1IGbbSYDb3G3TDFuP0rKWk+KaPm4u3s6O33T/yEyJIyOs5kcGh7nZXAk8lnQ8sy04fEnAn5OIJpRTUMa6ST2iV4/3KCa3iTr9iSivJTwzDFaQxaspBBXv7W/uHB5CUlFS+gGcw6S1TxsmpUWo1wdXO3svBwcfun6CxXGJZ3c3s1qpiLhmHh13H5mWJqTUgh1EkULexCPDsstz0mpICMLugB3f13dDoYDCzbHr1l08fdve+HtgOIQUwREJCnFzR1aeWTFkMYiHfy/m4p739uZOOYGxaSRX0cjSYdG4dmVaBrUIhmaVoDatxqJ2jbedyamv4DbU8BlnQSBE1UWYGldCYEFABt7HmxfPH1i+ftne3INfT8iPDoktQaH4r845lRKdROH33j1MnjhamRFMxKBGX1yWSs7miRmZbM6u9sa5JXE/pbabpBGyNSCTtlMklPXqV2ny7x6xRWXR90MRL+ZnR718/fvVy/o+3zz9//gDJzsg9G/ADo5YsFnDGh9QTBnVEiH+wh3MbCQMqAD9TSmQcFo/HFYo6ZeCR4tRU64RcXZewX9Hb1dXbJdNqNYNmvW5u0jQg7yCWwTVKPgCsP1uYBQDrv/71CHIp7DK2tITVVAeiWwaVdw1qJrEsLtBLwagUUitmB9WqznaZoE0tk+t61QphR0tV5Yikc0anmTCatQPjGv3E+Pjsj1NTBqVYzmfWVpW8+uXRxqc3T+andrZWwOUDcXNzw5QV3YRDh1RdEzrF/Jh2tl+RGODBr0C2V5cO8G4NdPKMcvG4Vj3er1V3trfiS6cVwpfTo49MIxOmySnL7NzM7MKM5cu7f4taG3578QRs/M2bnxcX79n2P+/vbEJCQ0NJRNz4qPauRXfHqJzUSu4MyAqvRggr0e0ElISK629laHlM0NJWMpFTjVcxiPcU3JejfZPdnbP6/vkJ0/Pp4aWJgZePZyxDKhAdvKVtwPb6xoe3b1/8tXBCz1+op5LMw1qzoW9qpG/kdpext4NUmMPGIFpK4VJKeS+j2ihs0XCb2UQck1AhqCyZlbb+rJffV0vGlV0PhvqWRrqXRhXzlv7/PLsP2L5adz9v7X+1bm3+9vrF4Y4VEnExMheaJRJwdBrZsE5uHJAN9HZw66sYhTeai2ECPBpsuZte3VZDaCgvvR4dhcvPUXOaeprIlu4uc690Rit/OiheMogemFTA1sry8pvVzY+/L79bW19dW36/vvIeEh8VG3Xpcn1drbJHZhweNA7rBvVabV93Q2lxIxrGLYPzMAXo+Evw2EhUcnLkaf9KBAKWEM+rJoC3qUWtmOztfHhbuDAoGR3o2d5e//3DH592tjf39/YBADxof3kATU7Jgeb36ycGxx+rRufBGn/0OiT8WnpcMqP4ZiM8jQKNhUdeQFyJIWZlMwsQ3WS8rJ4qZzaoW+ldpMKx9rr7fcK5MUNjR7flyYt3O8AqAHzYB5Z3d99/WX29+hYCzUYJJQPmu78MTv4yNveO2qqpYfaevZxx6Ww4IT+XmpPMRmcTspJLkq8SMjO5pcVCfLGqhQEuBgEFw8XmTkuZMyrRgEJZTO5EkTuSkfWc3slHr62fAODjLrBuAyAdqh9HH7wf+vFd9+gv0FJus3Q6JKGkkiH39wohwBF0ZDYxK74yO62u8CanAiOuIQyyGXph67BcaJLztJzqEdGth0YdpYqOJqsQNT1Ich+pbTyP0EG4pbq/tPmHFYCMLGwPzX0xLez0313rm3qnHHsjHX5BaFDZHz2deeUqNj2FhoBSELlNmGIuvry5uKCx6IayhT6pEpsk7AkZ645azKRSk1NvkviT2h/XNPdXdfOf2nSLzJ67+GYVTaCHDC3sGxf2huasunvrmjsfwBq8t1bdYnD1iAzyDi5Iis+PCcfdyCAi8ypzM1pxKDG9StN2a1TGtchZk3L2kExw+lRgQlZ5i+re/Apw7z3waAVY3AAWV4F7r7Ymnq1AjIs75qfbI4/Xh+9/HHm4MjDzp+HhBolj8gpI9XYNgiUlI1PiMiLPJYcFwRPCcNC4WnQOuBp72RRDO+02u0bBY7l5BKcgaTSJ8dHy4YPlnbm17cWNw7k/v86923r65wEEHD1owOTjlekny+DTNPfROLfGVS0ccY728bp4OSCoPDezAgZFZyWhrkWWZcZgspOrEOl8ElrLIY6IGktgN86EJKWWtMBI/IVV27MvwE/Ww5829hZX90D0n0ACqeGJXD+nGX1qnFwae/B24snqAGi4+be/Hbno5xt17pR/ZuRF8H+NWY1Rsqg9rJq+tiadhDUqZ45JGGJaqf9Jt/jM0gKKLL6A9KsVeAsAr2zAs82Dp6uHP38EXq4C/wWIP6F3tg8nyQAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,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>