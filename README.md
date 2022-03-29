# Api_LOL

Docker Build: Executar o comando para buildar a imagem -> docker image build -t oauthintegration:latest .

Executar o comando para iniciar a imagem no container -> docker container run -it -v ${pwd}:/usr/src/app --env-file .env -p 81:80 --name oauthintegration oauthintegration:latest



Documentação -> https://developer.riotgames.com/apis#summoner-v4/GET_getByAccessToken