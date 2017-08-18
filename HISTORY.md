Decisões que foram tomadas:

Utilização de tecnologias que facilitaram o desenvolvimento.

-Python e Django

Descrição: Foi utilizado Python e Django pelo fato do desenvolvimento ser fácil e, além disso, o Django fornece um admin completo para a resolução do meu problema que era cadastrar menus e seus respectivos itens.

-Gulp(Bônus)

Descrição: Foi utilizado Gulp para automatizar as tarefas do front-end minificando arquivos css,js e img, particularmente não utilizaria o Gulp em um projeto tão pequeno pelo fato de ser mais uma configuração a ser feita e não haver a necessidade em um projeto desse porte.

Foi utilizado uma serie de libs do Gulp para um exemplo rapido de como funciona a sua utilização

imagemin- Minificar Imagens
mincss - Para minificar css
clean - Apaga um diretorio

-NPM(Bônus)

Descrição: Foi utilizado o gerenciador de pacotes do Node pelo fato de ele ser bem conhecido e ser de extrema
facilidade no uso,particularmente tambem não utilizaria o NPM por não haver necessidades neste projeto.

-SQLite

Descrição: O Banco de dados utilizado foi o SQLite por ser integrado com o Django e não havendo necessidade em um exemplo desse nivel a utilização de um outro banco que seja de grande porte.

-MPTT

Descrição: O MPTT é uma lib que foi integrada no projeto para facilitar o trabalho com a estrutura de arvores,ele é muito interessante pelo fato de fornecer métodos de extrema importância já prontos para fazer o percurso na arvore.

Em relação ao desenvolvimento do projeto a principio eu pensei em desenvolver utilizando três classes (Menu,Item e Subitem) mas eu notei que dessa forma eu não teria êxito na criação da estrutura sucessiva de filhos, então pensei em fazer com 2 classes(Menu e Item) e fazer recursivamente onde a classe item chamava ela mesma assim me dando a liberdade de criar a quantidade de itens que eu quiser. Caso tivesse mais tempo para o desenvolvimento eu utilizaria o Sass para desenvolver um CSS de forma mais proveitosa e produtiva.
