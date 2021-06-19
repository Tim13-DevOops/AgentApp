FROM node:slim
RUN apt-get update && apt-get install -y dos2unix


WORKDIR /work/frontend

COPY package.json /work/frontend/

RUN npm i npm@latest -g && \
    npm install -g @angular/cli@7.3.9


RUN npm install --force

COPY . /work/frontend/

RUN dos2unix /work/frontend/entrypoint.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*


ENTRYPOINT ["sh", "/work/frontend/entrypoint.sh"]