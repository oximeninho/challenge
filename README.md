Sobre o projeto

Acredito que tenha sido um grande desafio para mim, utilizei pela primeira vez algumas ferramentas que não estava habituado, como o docker, github e o postgresql;

É um projeto embrionário que atinge os requisitos do que foi solicitado, está longe da versão final e talvez eu continue aprimorando como um projeto pessoal próprio.

Para o futuro desse projeto, listei algumas possíveis melhorias:
    1. Pedido de autenticação automática, sem precisar relogar pelo localhost:8000/start-session manualmente toda vez;
    2. Alguma ferramenta que eu pudesse digitar o nome do grupo ao invés de "mocar" o ID no main.py;
    3. Outra forma de visualizar a base de dados sem utilizar o DBEAVER;
    4. Adicionar mais funcionalidades na aplicação (existe hoje uma tentativa de envio de mensagem automática).

Acredito que essas foram as funcionalidades que eu pensei nesse primeiro momento para a aplicação.

Sobre essa semana de desenvolvimento:
    Comecei de maneira muito crua, na verdade, um pouco perdido, eu diria, sem saber por onde começar. Procurei em videos na internet e artigos referência sobre as ferramentas que eu iria utilizar. Graças a alguns vídeos no youtube, consegui ter o mínimo de conhecimento de Docker, Waha, entre outros que deixarei nas referências deste documento.
    Após começar com Docker, baixei a aplicação e depois fui procurar mais sobre o WAHA, não havia conhecido a ferramenta até então, li a documentação inteira para ter um norte de onde começar. Por sorte, é bem fácil instalar a imagem via docker e utilizar o dashboard. Depois, me programei sobre como iria funcionar dentro do Python, quais seriam os imports a serem feitos. No mesmo dia eu já conseguia colocar todos os textos que eu recebi em um doc txt no meu computador, não era o que havia sido pedido, mas já era um começo.
    Admito que meus anos de Petrobrás, planilhas de EXCEL e automação em web não foram muito educativos para esse challenge, aprendi mais em 2 semanas do que nos últimos 6 meses no meu emprego e esse desafio me ajudou bastante. Logo após já conseguir inserir algumas mensagens em um arquivo txt, dava-se início ao próximo passo, adicionar os dados recebidos via webhook para a base de dados, ao invés de um documento TXT. Demorei 1 dia inteiro para entender melhor como fazer, por onde começar, sempre que eu tentava, algo dava errado, mas no final, consegui (demorei até entender que só por um milagre o aplicativo colocaria uma mensagem numa tabela que não havia sido criada ainda, algo trivial parando para pensar agora).
    Depois de me livrar do problema trivial, eu já tinha maior parte das coisas, eu fazia a aplicação rodar sem problemas, adicionava as mensagens num banco de dados, tudo local, estava na hora utilizar o docker pra valer.
    Comecei pelo requirements, que não tem grande mistério, só um amontado de necessidades pro docker instalar.
    Então, fui para o DockerFile, que instalaria os requirements.
    Por fim, o docker-compose, a maior dificuldade até então, não pelo o que está escrito nele em si, mas como ele modificava o main, as portas, a relação com as imagens. No começo pareceu muito complicado, mas depois, realmente entendi como o docker é um grande facilitador no dia a dia.
    E então, consegui fazer tudo ser executado em um único container, sem depender do meu computador e que possívelmente rodaria em qualquer máquina, uma maravilha moderna.

    Enfim, aqui está um pouco da minha experiência na última semana, li alguns (centenas) de artigos e páginas de fórum de pessoas que enfrentaram um milhão de problemas assim como eu. Tive um grande desafio, mas com grandes desafios também vêm grandes aprendizados.
    
PRINCIPAIS REFERENCIAS:
    https://www.youtube.com/watch?v=0TFWtfFY87U
    https://www.youtube.com/watch?v=DM65_JyGxCo
    https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/
    https://www.youtube.com/watch?v=n2Fluyr3lbc
    https://www.youtube.com/watch?v=XfO3TRvESBo
    https://www.youtube.com/watch?v=SIpY5PZ9PBQ
    https://www.youtube.com/watch?v=ntbpIfS44Gw
    https://www.youtube.com/watch?v=UBAX-13g8OM
    https://www.youtube.com/watch?v=DqTITcMq68k

    "Todo o mundo está contido num container docker" - Átila.