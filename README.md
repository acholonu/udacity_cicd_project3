# Give your Application Auto-Deploy Superpowers

In this project, you will prove your mastery of the following learning objectives:

- Explain the fundamentals and benefits of CI/CD to achieve, build, and deploy automation for cloud-based software products.
- Utilize Deployment Strategies to design and build CI/CD pipelines that support Continuous Delivery processes.
- Utilize a configuration management tool to accomplish deployment to cloud-based servers.
- Surface critical server errors for diagnosis using centralized structured logging.

![Diagram of CI/CD Pipeline we will be building.](udapeople.png)

## Instructions

- [Selling CI/CD](instructions/0-selling-cicd.md)
- [Getting Started](instructions/1-getting-started.md)
- [Deploying Working, Trustworthy Software](instructions/2-deploying-trustworthy-code.md)
- [Configuration Management](instructions/3-configuration-management.md)
- [Turn Errors into Sirens](instructions/4-turn-errors-into-sirens.md)

### Description

*Provided Cloud Formation Templates*
For your convenience, we have provided some CloudFormation templates that you can use throughout the deployment phase of your project. You can find those templates in `.circleci/files`.

#### Intentionally Failing Jobs

We left a scaffolded `config.yml` for you `.circleci/config.yml` to help you get started with CirlcCI's configuration. To call attention to unfinished jobs, we left some "non-zero error codes" (e.g. exit 1) for you to remove when you have finished implementing a job.

#### Compiling/Running Locally (Optional)

PLEASE NOTE: It is NOT necessary that you compile and run the project locally. The goal of this project is for you to show mastery in management of CI/CD systems, not React/NodeJS web applications. If you are experienced with React/NodeJS or don't mind an extra challenge, then be our guest! But, you can perfectly complete this project without compiling or running the code locally.

The instructions and information that follows should help you build, test and deploy the web application either locally or in CI/CD.

This is a "mono-repository" which means multiple servers or layers exist in the same repository. You'll find the following main folders:

- ./frontend
- ./backend

#### 1. Install dependencies in both frontend and backend folders

From your cdond-cd-projectstarter folder, use the commands:

  ```bash
    cd frontend
    npm i
  ```

  From your cdond-cd-projectstarter folder, use the commands:

  ```bash
    cd backend
    npm i
  ```

#### 2. Create .env file for database connection info

Add a .env file to your backend folder with the following contents:

```bash
  NODE_ENV=local
  VERSION=1
  TYPEORM_CONNECTION=postgres
  TYPEORM_MIGRATIONS_DIR=./src/migrations
  TYPEORM_ENTITIES=./src/modules/domain/**/*.entity.ts
  TYPEORM_MIGRATIONS=./src/migrations/*.ts

  # Things you can change if you wish...
  TYPEORM_HOST=localhost
  TYPEORM_PORT=5532
  TYPEORM_USERNAME=postgres
  TYPEORM_PASSWORD=password
  TYPEORM_DATABASE=glee
```

You can use your own Postgres server if you wish or you can use the Docker-Compose template we provided in the ./utils folder.

### Running PostgreSQL in Docker-Compose

For convenience, we have provided a template that you can use to easily run a Postgres database for local testing. To run this template, you'll need to install Docker and Docker-Compose.

To start the database, you will use the following commands from your cdond-cd-projectstarter folder:

```bash
  cd util
  docker-compose up
```

Compiling the Code
You can compile the code from your cdond-cd-projectstarter folder using the following:

```bash
  # frontend
  cd frontend
  npm run build

  # backend
  cd backend
  npm run build
```

**WARNING**: There are some errors in both front-end and back-end that will make any attempt to compile FAIL when you first clone the repo. These errors are intentional. There are steps in the project that require a build to break in Circle CI. Please don't fix these errors until instructed to do so later on.

### Testing, Migrating, Running

As the warning says above, it won't be possible to run most of the code in the project until later on when you are instructed to fix some errors. So, you may not be able to try the following commands right now. We are providing them here as a reference.

Most of the tasks needed to build, test and deploy the application are simplified by "npm scripts" that are found in the `package.json` for either front-end or back-end. For any of these scripts, you will need to `cd` into the respective folder and then run the script using the command `npm run [script name]`. Here are the most relevant scripts:

![Project Table](project3_table.png)

### Examples

This should compile the code and then list the result in the `./dist` folder:

```bash
  cd frontend
  npm run build
  cd dist
  ls
```

... or revert the last migration that ran:

```bash
  cd backend
  npm run migrations:revert
```

## Section 2 - Utilize Deployment Strategies to Design and Build CI/CD Pipelines that Support Continuous Delivery Processes

### Circle CI

Circle CI is only one of many options for CI/CD tools. It is a “software as a service” and has a free account that you can use throughout this project, which is ideal for UdaPeople since it’s a start-up running on a shoestring budget!

1. Create an account with circleci.com if you haven't already. We recommend the free tier for this course. It includes 2500 credits per week which equals around 70 builds. This should be enough as long as you are conservative with your builds. If you run out of credits, you can create another account and continue working.

2. Create a new project in Circle CI using your GitHub repo.
Notice the .circleci folder. This is where your jobs will go.

3. Ensure a workflow starts with the jobs in your `.config` file. If you need to take a look at some samples, Circle CI was nice enough to give us a few.

### Project Submission

For your submission, please submit the following:

- A text file named `urls.txt` including:
  1. Public Url to GitHub repository (not private) [URL01]
  1. Public URL for your S3 Bucket (aka, your green candidate front-end) [URL02]
  1. Public URL for your CloudFront distribution (aka, your blue production front-end) [URL03]
  1. Public URLs to deployed application back-end in EC2 [URL04]
  1. Public URL to your Prometheus Server [URL05]
- Your screenshots in JPG or PNG format, named using the screenshot number listed in the instructions. These screenshots should be included in your code repository in the root folder.
  1. Job failed because of compile errors. [SCREENSHOT01]
  1. Job failed because of unit tests. [SCREENSHOT02]
  1. Job that failed because of vulnerable packages. [SCREENSHOT03]
  1. An alert from one of your failed builds. [SCREENSHOT04]
  1. Appropriate job failure for infrastructure creation. [SCREENSHOT05]
  1. Appropriate job failure for the smoke test job. [SCREENSHOT06]
  1. Successful rollback after a failed smoke test. [SCREENSHOT07]  
  1. Successful promotion job. [SCREENSHOT08]
  1. Successful cleanup job. [SCREENSHOT09]
  1. Only deploy on pushed to `master` branch. [SCREENSHOT10]
  1. Provide a screenshot of a graph of your EC2 instance including available memory, available disk space, and CPU usage. [SCREENSHOT11]
  1. Provide a screenshot of an alert that was sent by Prometheus. [SCREENSHOT12]

- Your presentation should be in PDF format named "presentation.pdf" and should be included in your code repository root folder.

Before you submit your project, please check your work against the project rubric. If you haven’t satisfied each criterion in the rubric, then revise your work so that you have met all the requirements.

### Built With

- [Circle CI](www.circleci.com) - Cloud-based CI/CD service
- [Amazon AWS](https://aws.amazon.com/) - Cloud services
- [AWS CLI](https://aws.amazon.com/cli/) - Command-line tool for AWS
- [CloudFormation](https://aws.amazon.com/cloudformation/) - Infrastrcuture as code
- [Ansible](https://www.ansible.com/) - Configuration management tool
- [Prometheus](https://prometheus.io/) - Monitoring tool

### License

[License](LICENSE.md)

## Other

Ran the cloudformation code with the following aws cli command:

```bash
aws cloudformation create-stack --profile udacity_project3 --stack-name uda-cloudfront-stack --template-body file://cloudfront.yml --region us-east-1 --capabilities "CAPABILITY_IAM" "CAPABILITY_NAMED_IAM"
```

