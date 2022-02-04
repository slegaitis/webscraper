# Webpage analysis tool

## Starting a project

- Docker: Run ``docker-compose up`` App accessible through http://127.0.0.1:8000/
- Standard way: ``pip3 install -r requirements.txt`` then ``flask run`` App accessible through http://127.0.0.1:5000/

- Running tests: ``python -m unittest test_web_scraper.py``

## Task
Write a web page or HTML analysis tool to extract specific insights about the webpage or a simple XML file.
## Technical requirements
-   Use any technology or programming language of your preference, however it has to be opensource and you must provide detailed instructions on how to launch the code.
-   You can use additional libraries for the document parsing but the statistics and insights should be collected by your algorithm.
-   Include some tests for your code, 100% coverage is not required, focus on some key functionalities.
## Functional requirements
-   The webpage URL has to be provided as a parameter.
-   Find all unique tags used in the document.
-   Find the most commonly used tag.
-   Find the longest path starting from root node to the descendent.
-   Find the longest path starting from root node where the most popular tag is used the most times.
-   All 4 insights can be presented in your preferred way.
