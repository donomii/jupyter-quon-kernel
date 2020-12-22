FROM jupyter/minimal-notebook
MAINTAINER Brendan Rius <ping@brendan-rius.com>

USER root

WORKDIR /tmp

COPY ./ jupyter_quon_kernel/

RUN pip install --no-cache-dir jupyter_quon_kernel/
RUN cd jupyter_quon_kernel && install_quon_kernel --user

WORKDIR /home/$NB_USER/

USER $NB_USER
