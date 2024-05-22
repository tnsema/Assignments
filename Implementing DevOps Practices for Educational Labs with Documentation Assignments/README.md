# Implementing DevOps Practices for Educational Labs with Documentation

![Terraform](https://img.shields.io/badge/Terraform-v1.1-blue.svg)
![Docker](https://img.shields.io/badge/Docker-v20.10-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-blue.svg)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-blue.svg)

![DevOps Graphic](https://www.devopsschool.com/blog/wp-content/uploads/2021/02/DevOps-Tools.png)

## Overview

This assignment involves setting up a virtual lab environment using DevOps tools and practices and creating a detailed tutorial and lab guide. The objective is to demonstrate technical proficiency and the ability to communicate complex information effectively.

## Objectives

1. **Set up a fully automated lab environment** using modern Infrastructure as Code (IaC) practices.
2. **Document the process** thoroughly to create a comprehensive lab guide for other learners.

## Tools and Technologies

- **Terraform**
- **cloud-init**
- **Docker**
- **CI/CD tools** (e.g., GitHub Actions or Jenkins)

## Assignment Details

### Part 1: Infrastructure and Container Setup

#### Task 1: Terraform Infrastructure
- Provision a VM with appropriate networking and security configurations.
- Ensure the VM is set up with the necessary permissions and access controls.

#### Task 2: VM Customization with cloud-init
- Prepare the VM by installing Docker, setting up user accounts, and installing necessary software packages.
- Configure cloud-init scripts to automate the setup process.

#### Task 3: Docker Container Configuration
- Develop Dockerfiles for at least three different containers.
- Ensure the containers are configured correctly and can communicate with each other.

### Part 2: Automation with CI/CD

#### Task
- Automate the building, testing, and deployment of Docker images using CI/CD pipelines.
- Implement the CI/CD pipeline using tools like GitHub Actions or Jenkins.

### Part 3: Documentation and Tutorial Creation

#### Task 1: Documentation
- Document every step, tool, and decision made during the setup process with explanations and justifications.
- Use markdown to maintain a clear structure.
- Include code snippets, configuration files, and CLI commands used.
- Provide diagrams and flowcharts to visualize processes and architecture.

#### Task 2: Lab Guide/Tutorial
- Create a separate document that acts as a tutorial for future students to replicate the lab setup.
- Include step-by-step instructions that are clear and beginner-friendly.
- Highlight troubleshooting tips and explain common issues that may arise.
- Incorporate screenshots and links to additional resources.

## Submission Guidelines

- Submit all code and documentation through a GitHub repository.
- The README.md file should detail the project and include links to the tutorial/lab guide.
- If applicable, include video demonstrations or a live demo link.

## Evaluation Criteria

### Category 1: Technical Setup and Innovation

| Criteria                      | Description                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------|
| **Accuracy and Functionality**| Terraform setup and cloud-init scripts must be accurate and functional.                       |
| **Efficiency and Security**   | Docker configurations should be efficient and secure, ensuring seamless interconnectivity.    |
| **CI/CD Pipeline**            | The pipeline should be reliable and robust.                                                   |
| **Innovative Solutions**      | Implement innovative solutions and optimizations in the design.                               |

### Category 2: Documentation Quality and Usability

| Criteria                      | Description                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------|
| **Clarity and Thoroughness**  | Documentation should be clear, thorough, and technically accurate.                            |
| **Organization and Readability**| The tutorial/lab guide should be well-organized, readable, and visually appealing.           |
| **Beginner-Friendly**         | The tutorial should be useful for beginners, making it easy to understand and follow the steps.|
| **Instructional Materials**   | Include high-quality diagrams, flowcharts, and videos.                                        |

## Example Project Structure

```plaintext
project-root/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfstate
├── cloud-init/
│   └── cloud-init.yaml
├── docker/
│   ├── Dockerfile1
│   ├── Dockerfile2
│   └── Dockerfile3
├── ci-cd/
│   ├── .github/
│   │   └── workflows/
│   │       └── ci-cd-pipeline.yml
│   └── Jenkinsfile
├── docs/
│   ├── tutorial.md
│   └── lab-guide.md
├── README.md
└── demo/
    ├── demo-video.mp4
    └── demo-link.txt
```

---

![DevOps Background](https://www.agileconnection.com/sites/default/files/DXC_Tra_DevOps_Fig02.jpg)

This assignment is designed to develop both technical skills in DevOps and cloud technologies and the ability to produce educational content. These skills are crucial for future roles as educators, developers, or IT professionals.
