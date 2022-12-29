# TINY LIBRARY MANAGEMENT SYSTEM
#### Description: 
<p>
This is a library management system called Tiny Library or TinyLib in short. The project is written in Python as the main programming language, using MySQL as database system, I also use HTML and CSS to design the web page. The system is designed for library staffs to manage the library. System main functions include adding new authors, categories, publishers, member and books, searching for books by title or members by their name, issuing books for members, and finally returing borrowed books back to the library.
</p>
<p>
The project is written using Django framework. The project includes some automatically created files through Django and some self-made files. The "manage.py" file is the main file to run the system. The "templates" folder contains all the HTML files for the web. The "static" folder contains the main CSS file and inside static, there is the "img" folder containing all the images used for this project. The "TinyLib" folder is the project folder. The "home" folder is where I created the functions and database for this project.
</p>

#### Database design:
<p>Below is my designed Entity Relationship diagram in order to build a database model for this project.</p>

![ER diagram](static/img/testing/ER.png)
#### Testing:
Home page
<p> By clicking to the "STAFF" we can be directed to the Signup or Login page. </p>

![Home](static/img/testing/Home.jpg)

Signup or Login page

![Signup or login](static/img/testing/signupAndLogin.jpg)

Signup page

![signup](static/img/testing/Signup.jpg)

Login page

![login](static/img/testing/login.jpg)

Dashboard
<p>We will be directed to dashboard after logging in. We can see and edit books information here, we can also delete and search for books here. </p>

![dashboard](static/img/testing/dashboard.jpg)

Add new author

![author](static/img/testing/addAuthor.jpg)

Add new book type

![category](static/img/testing/addType.jpg)

Add new publisher

![publisher](static/img/testing/addPublisher.jpg)

Add book
<p>Before adding a new book, we have to make sure that the new book's author, type and publisher information are already inserted into the database.</p>

![newbook](static/img/testing/addBook.jpg)

Search book
<p>We can search for a book by its title in the dashboard.</p>

![searchbook](static/img/testing/searchBook.jpg)

Add member

![addmember](static/img/testing/addMember.jpg)

View member

![viewmember](static/img/testing/viewMember.jpg)

Search member

![searchmember](static/img/testing/searchMember.jpg)

Issue book

![issuebook](static/img/testing/issue.jpg)

View issued books

![viewissue](static/img/testing/viewIssueBook.jpg)

Return books

![return](static/img/testing/return.jpg)

#### Reference:
<p>Part of the project code is consulted from the TechVidvanLibrary project. Refer to: https://techvidvan.com/tutorials/python-library-management-system/ </p>
