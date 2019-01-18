# Conduct effective QA interviews using this web application as a backdrop

This simple web application is an ideal 'product' for interviewing QA. Think of it as the '[fizz-buzz](https://www.hackerrank.com/challenges/fizzbuzz/problem)' equivalent for QA. We recommend reserving one round (between 30-60 minutes) of the interview for testing this application. 

This application was designed by [Qxf2 Services](https://www.qxf2.com/?utm_source=qa-interview&utm_medium=click&utm_campaign=From%20QA%20Interview). Qxf2 provides QA for startups.

For convenience, this app has been hosted at: [http://qainterview.pythonanywhere.com](http://qainterview.pythonanywhere.com). 


## Features of the 'Fizz buzz for QA' application

1. The app has been seeded with a variety of bugs:

* a major functional bug
* a data limit bug
* a usability bug
* a typo
* a bug to test if the QA is reading the page content
* a slightly weird wording 
* a cross-browser bug 

2. The app also has several workflows which will work well and that the QA being interviewed should check. 

* E.g.: Entering an integer followed by a string followed by an integer (does the form validation clear?)

3. You can use this app to conduct more technical interviews too. You can ask the candidate to: 

* write a locator (CSS selector/XPath) for the red form validation styling
* find the console message printed
* write a Selenium script to test that the factorial of 5 is 120
* figure out the API call being made along with the headers and parameters sent 
* write a bug report
* document a test case


## Setup

This app has been hosted at: [http://qainterview.pythonanywhere.com](http://qainterview.pythonanywhere.com). Follow this setup only if you want to use a local copy of this application. 

1. `pip install requirements.txt`


## How to run the QA interview application

To start the application, run `python qa_interview.py` and visit `localhost:6464` in your browser.


## What the application does

The application calculates the factorial of a given number. We have exactly one page with:

* one text box 
* one submit button
* a page title 
* three hyperlinks 
* a copyright message

By keeping the application this simple, we are increasing the likelihood of the interviewer and the candidate agreeing upon what is important. You can also reasonably expect QA to be able to verbalize their testing for such limited functionality.


## Tips when interviewing QA engineers

Apart from technical skills, you can also pick up on several characteristics. Here are some tips:

* Verify if the QA is able to check functional correctness for 0,1 and a few more integers
* Watch the body language of the QA as they discover bugs - good QA are happy when they are discovering bugs
* Make sure the QA tries to reproduce any bug they discover!
* Are they keeping notes or screenshots of what they see?
* Are they continuously trying to discover bugs through the entire time allotted?
* Do they ask good questions about context (why am I even testing this? who is going to use this? etc.)

For general advice on interviewing QA engineers effectively, refer to [A better way to interview QA engineers](https://qxf2.com/a-better-way-to-interview-qa).

## Solutions

We haven't really documented our test strategy and the bugs anywhere. For now, just write to Arun (mak@qxf2.com) if you want a quick overview of all the bugs and how a typical interview will look like.