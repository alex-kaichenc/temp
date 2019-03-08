FROM docker.lappsgrid.org/deiis/base

COPY . /root/

WORKDIR /root

ENV HOST '127.0.0.3'

# RUN ./start.sh
# RUN python pipeline.py data/train.json
# RUN python save.py

# ENTRYPOINT ["python", "save.py"]
# ENTRYPOINT ["./start.sh"]
