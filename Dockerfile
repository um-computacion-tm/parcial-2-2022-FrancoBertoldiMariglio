FROM python:3
RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-FrancoBertoldiMariglio.git
WORKDIR /parcial-2-2022-FrancoBertoldiMariglio
CMD ["python3",  "-m", "unittest"]
