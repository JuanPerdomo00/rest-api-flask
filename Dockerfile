# descargamos el sistem alpine de docker hub
FROM alpine:3.10

# descargamos python3 y pip en alpine
RUN apk add python3-dev \
    && pip3  install --upgrade pip 

# creamaos la carpeta donde estara el codigo
WORKDIR /app 

# copiamos todo el codigo a la carpeta creada llamada app
COPY . /app

# descargamamos las librerias para que funcione la aplicacion
RUN pip3 --no-cache-dir install -r requirements.txt

# ejecutamos la aplicacion
CMD [ "python3", "src/app.py" ]