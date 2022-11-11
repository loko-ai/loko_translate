FROM lokoai/python_transformers
EXPOSE 8080
ADD ./requirements.txt /
RUN pip install -r /requirements.txt
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
CMD python services.py