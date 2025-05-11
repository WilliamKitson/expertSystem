# Expert System
## Who 
I developed this project during my 2025 Software Engineering degree’s Introduction to AI module, using my student GitHub credentials (4kitsw10). I am the sole contributor and maintainer of this project. 

## What 
This project contains the source code for a basic expert system that plays 20-Questions to guess a video game based off its associated characteristics. It was written in object-oriented Python. Were I to extend this project, I would develop and implement a database of video game titles and their rules to enhance the systems complexity and remove the need to manually define them upon initialisation of the expert system. 
### main.py
This source file contains a basic implementation of the expert system, initialising an instance of the system, defining a few basic questions and answers, and launching the core loop of the program. The program should be launched from this file.

### expert.py
This source file defines the expert class, the implementation object that coordinates domain rule and questions objects into fulfil the requirements of the program. The investigate function loops through and asks questions, using the users answers to calculate the likely video game. 

### rule.py
The Rule data class contains an array of conditions and a singular conclusion variable, this is used by the expert system to questions with the conclusion of the rule.

### question.py
The question data class is used by the expert system to record if a rules condition has been queried and the answer thereof. The expert system uses questions to ensure that rules are only queried once. 

## When 
I developed this project in the first semester of my second year of my Software Engineering course, September to December of 2024. 

## Where 
This project was developed at Solent University. 

## Why
This project was useful as it allowed me space to develop my understanding of how Expert Systems are designed and utilised throughout larger software systems. This project was a fundamental building block in my larger AI assessment project (4kitsw10_COM526_1).
