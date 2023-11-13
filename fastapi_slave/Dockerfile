FROM python

WORKDIR /appmain

COPY ./requirements.txt /appmain/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /appmain/requirements.txt
RUN python3 -m textblob.download_corpora

COPY ./app /appmain/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]