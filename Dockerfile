FROM astral/uv
ENV TZ=Europe/Moscow

ENTRYPOINT ["uv"]
CMD ["run", "--script", "main.py"]