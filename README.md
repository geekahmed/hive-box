# Project: Hive Box
## Introduction


[DevOps Hive](https://devopshive.net/) master plan for **roadmap**, **mentorship**, and **bootcamp** to start a DevOps Engineer career in the Agile way!


Me, Ahmed Moustafa, a Junior DevOps Engineer will start implementing this project based on the [Roadmap](https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap/tree/main/projects/hivebox#approach).


The implementation will be as clean as possible and I will try to add more features and approaches more than in the project description.

<!-- omit in toc -->
## ToC

- [Approach](#approach)
- [Goal](#goal)
- [Phase 1](#phase-1)
- [Phase 2](#phase-2)
  - [2.1 Tools](#21-tools)
  - [2.2 Code](#22-code)
  - [2.3 Containers](#23-containers)
  - [2.4 Testing](#24-testing)
- [Phase 3](#phase-3)
  - [3.1 Tools](#31-tools)
  - [3.2 Code](#32-code)
  - [3.3 Containers](#33-containers)
  - [3.4 Continuous Integration](#34-continuous-integration)
  - [3.5 Testing](#35-testing)
- [Phase 4](#phase-4)
  - [4.1 Tools](#41-tools)
  - [4.2 Code](#42-code)
  - [4.3 Containers](#43-containers)
  - [4.4 Continuous Integration](#44-continuous-integration)
  - [4.5 Continuous Delivery](#45-continuous-delivery)
- [Phase 5](#phase-5)
  - [5.1 Tools](#51-tools)
  - [5.2 Code](#52-code)
  - [5.3 Containers](#53-containers)
  - [5.4 Infrastructure as Code](#54-infrastructure-as-code)
  - [5.5 Continuous Integration](#55-continuous-integration)
  - [5.6 Continuous Delivery](#56-continuous-delivery)
- [Phase 6](#phase-6)

## Approach

This project follows the same Dynamic MVP-style mindset used in the [roadmap](../../). Which aims to cover the whole Software Development Life Cycle (SDLC). That mean each phase of this project will cover all aspects of the DevOps areas like planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

This project works the best in `Peering` mode where you have another person helps you whenever you stuck (like a mentor or so). But in case you don't have that, always back to the `Related Module` where it has more details could help you in the project.




## Goal

The goal of this project is to build a scalable RESTful API around [openSenseMap](https://opensensemap.org/) but customized to help beekeeper with their chores. The API output should be in JSON. You will start with a basic implementation, then extend the whole system to handles thousands of requests per second. But always remember, every decision has a cost.

You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use this one [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786) as starting point). Just copy the IDs, you will need them in the next steps.

---

## Phase 1

- Understand your role in this project and how you work with other teams.

> In this project, my role is to apply an Agile approach to learning DevOps strategies and tools, aligning with the dynamic DevOps roadmap. The MVP methodology, widely used in business and startups, is adopted here, enhancing the learning experience. This iterative approach accelerates knowledge absorption and enables learners to connect information seamlessly. By welcoming enthusiastic team members, we foster a collaborative and competitive environment, making the learning process more effective and enjoyable.


- Brush up on your knowledge about Software Project management (Hint: [What is agile project management?](https://www.apm.org.uk/resources/find-a-resource/agile-project-management/) And [Introduction to Software Product Management](https://www.coursera.org/learn/introduction-to-software-product-management)).

> Agile Software Management is a flexible approach to overseeing software projects. It emphasizes collaboration, adaptability, and breaking tasks into manageable parts. This method encourages regular feedback and open communication, promoting efficient development and high-quality results. 


- Decide which Agile methodology you will use. (Scrum, Kanban, Scrumban, etc.).

> As a solo developer for the Hive Box project, I've chosen Kanban for its simplicity and adaptability. Utilizing the Kanban board on [YouTrack software](https://hivebox-geekahmed.youtrack.cloud) from IntelliJ allows me to efficiently manage tasks, visualize workflow stages, and maintain a clear overview of project progress. This streamlined approach enhances productivity and flexibility, crucial for solo development endeavors.


- Document as you go. Always assume that someone else will read your project at any phase.

> I am committed to meticulously documenting every aspect of my work on the Hive Box project within the Github ReadMe main file. This will not only serve as the primary documentation source but also stand as a comprehensive record of the project's evolution. While I have the option to leverage the Knowledge Base feature in YouTrack, I deliberately opt for tools universally accessible to maintain a tool-neutral and inclusive approach for everyone involved. This choice reflects my dedication to transparency and collaboration in the project's development journey. 



---

## Phase 2

- This phase mainly concentrate on learning or brushing up the basic concepts about the following topics:

  - Python Fundamentals
  - Common Development Tools
  - Git Basics
  - Operating System - Linux Fundamentals
  - Operating System - Common Tools and Commands
  - Operating System - Bash Scripting Basics
  - Containers - Docker Fundamentals
  - Containers - Docker CLI Basics

- As experienced developer, I have brushed up Linux basic commands and Docker.
- Regarding Git, I have used the [GitFlow pattern](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) you can learn more from here: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
- My recommendations in learning those concepts for non-experienced developers:
  - Linux: Linux in Action book by David Clinton.
  - Docker: Docker Deep Dive.
    - Ahmed Samy YouTube Video: https://www.youtube.com/watch?v=PrusdhS2lmo
  - Git: Ahmed Samy YouTube Course: https://www.youtube.com/watch?v=Q6G-J54vgKc
  - Python: Ahmed Samy Youtube Videos
    - Part 1: https://www.youtube.com/watch?v=XKQaCF_Om8o
    - Part 2: https://www.youtube.com/watch?v=mlbe7Vxr7yA

- I would like to note that I have used FastAPI with this application.
  - I used FastAPI as it has modern features like Pydantic models, Dependency injection ease, etc.
  - Many developers will use Flask, so why not change?
- We have in this phase two releases:
  - release with tag 0.0.1: This is considered the first half of the project
    - Structuring folders and files
    - Implementing the basic code for running FastAPI.
  - release with tag 0.0.2: This contains the code for the Dockerfile

