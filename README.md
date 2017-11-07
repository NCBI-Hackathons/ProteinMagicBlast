# Super Magic Blast
![Workflow](/bc073254-b7d4-4648-912f-a346c63b585f.png?raw=true "logo.png")
## Website (if applicable)

## Introduction
    We are adding the functionalities to the existing Magic Blast which makes it Super Magic Blast.These functionalities will make the       Magic Blast run faster. The results will be displayed in same fashion but delivered faster. 
    New Translated Magic Blast allows user to find changes and relationship for the given genome with interested protein.  

## What's the problem?
    There is no problem with Magic Blast but optimizing it to deliver results fast. 
    New Translated Magic Blast solves the problem of user. User has some genome(s) and it is interestred in specific proteins. 
    User wants to know if in the new genome are there any significant changes related with given protein? 
    Has the amino acid changed at any of the positions?  

## Why should we solve it?
   Faster Magic Blast will save lots of time and resources thus giving user opportunity to do better research. 
   Amino acid point mutations (nsSNPs) may change protein structure and function. The second approach lets us identify the changes and      the magnitude may vary depending on how similar or dissimilar the replaced amino acids are, as well as on their position in the          sequence or the structure.  
   
# What is <this software>?

Overview Diagram

# How to use <this software>

## Installation options:

We provide two options for installing <this software>: Docker or directly from Github.

### Docker

The Docker image contains <this software> as well as a webserver and FTP server in case you want to deploy the FTP server. It does also contain a web server for testing the <this software> main website (but should only be used for debug purposes).

1. `docker pull ncbihackathons/<this software>` command to pull the image from the DockerHub
2. `docker run ncbihackathons/<this software>` Run the docker image from the master shell script
3. Edit the configuration files as below

### Installing <this software> from Github

1. `git clone https://github.com/NCBI-Hackathons/<this software>.git`
2. Edit the configuration files as below
3. `sh server/<this software>.sh` to test
4. Add cron job as required (to execute <this software>.sh script)

### Configuration

```Examples here```

# Testing

We tested four different tools with <this software>. They can be found in [server/tools/](server/tools/) . v

# Additional Functionality

### DockerFile

<this software> comes with a Dockerfile which can be used to build the Docker image.

  1. `git clone https://github.com/NCBI-Hackathons/<this software>.git`
  2. `cd server`
  3. `docker build --rm -t <this software>/<this software> .`
  4. `docker run -t -i <this software>/<this software>`
  
### Website

There is also a Docker image for hosting the main website. This should only be used for debug purposes.

  1. `git clone https://github.com/NCBI-Hackathons/<this software>.git`
  2. `cd Website`
  3. `docker build --rm -t <this software>/website .`
  4. `docker run -t -i <this software>/website`
  
