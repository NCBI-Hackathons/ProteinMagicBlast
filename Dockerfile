# Set the base image to Ubuntu
FROM ubuntu:16.04
ARG GIT_COMMIT=unknown

# Setup packages
USER root
RUN apt-get -y -m update && apt-get install -y wget unzip zip libgsl-dev libgsl2 bzip2 build-essential git python3 python3-pip gawk gcc make
RUN pip3 install django

# switch back to the ubuntu user so this tool (and the files written) are not owned by root
RUN groupadd -r -g 1000 ubuntu && useradd -r -g ubuntu -u 1000 ubuntu

RUN apt-get -y -m update && apt-get -y upgrade
RUN apt-get -y clean
RUN apt-get -y autoclean

# set local directories to ubuntu user
RUN mkdir -p /home/ubuntu
RUN chown ubuntu /home/ubuntu

USER ubuntu

WORKDIR /home/ubuntu

# Download and setup blast applications
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/ncbi-blast-2.7.1+-x64-linux.tar.gz
RUN tar zxvf ncbi-blast-2.7.1+-x64-linux.tar.gz
RUN mkdir -p /home/ubuntu/bin/
RUN cp ncbi-blast-2.7.1+/bin/* /home/ubuntu/bin/.
RUN rm -rf ncbi-blast-2.7.1+/
RUN rm ncbi-blast-2.7.1+-x64-linux.tar.gz

# Download and setup magic blast application
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/LATEST/ncbi-magicblast-1.3.0-x64-linux.tar.gz
RUN tar zxvf ncbi-magicblast-1.3.0-x64-linux.tar.gz
RUN cp ncbi-magicblast-1.3.0/bin/* /home/ubuntu/bin/.
RUN rm -rf ncbi-magicblast-1.3.0/
RUN rm ncbi-magicblast-1.3.0-x64-linux.tar.gz

# Download and build samtools
RUN wget https://github.com/samtools/samtools/releases/download/1.6/samtools-1.6.tar.bz2
RUN tar xjf samtools-1.6.tar.bz2
RUN cd samtools-1.6
RUN ./configure
RUN make -j 10
RUN cp samtools /home/ubuntu/bin/
RUN cd ..
RUN rm -rf samtools-1.6/
RUN rm samtools-1.6.tar.bz2

# Download and build freebayes
RUN git clone --recursive git://github.com/ekg/freebayes.git
RUN cd freebayes/
RUN make
RUN cp bin/freebayes /home/ubuntu/bin/
RUN cd ..
RUN rm -rf freebayes/

# ENV VAR VALUE - add the blast bin directory to the path
ENV PATH /home/ubuntu/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV HOME /home/ubuntu

# Download SuperMagicBlast
RUN git clone https://github.com/NCBI-Hackathons/SuperMagicBlast.git

WORKDIR /home/ubuntu
CMD ["/bin/bash"]

