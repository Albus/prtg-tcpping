FROM astral/uv
ENV TZ=Europe/Moscow
WORKDIR /app

ENTRYPOINT ["/uv"]
CMD ["run", "--script", "https://raw.githubusercontent.com/Albus/prtg-tcpping/refs/heads/master/main.py"]