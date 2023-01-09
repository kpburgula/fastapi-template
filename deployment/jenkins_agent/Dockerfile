FROM jenkins/agent
USER root
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libffi-dev python3 python3-pip python3-venv python3-dev && \
    pip install requests fastapi uvicorn[standard]
USER jenkins