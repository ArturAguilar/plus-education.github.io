const data = [
    {
        title: "Língua Portuguesa",
        description: "Domine as palavras e abra portas para o mundo.",
        image: "img/portugues.png" // Caminho da imagem para o primeiro card
    },
    {
        title: "Lingua Inglesa",
        description: "Aprenda inglês e abra as portas para o mundo e novas oportunidades.",
        image: "img/ingles.png" // Caminho da imagem para o segundo card
    },
    {
        title: "Matemática",
        description: "Desvende os segredos do universo com a lógica dos números.",
        image: "img/mat.png" // Caminho da imagem para o segundo card
    },
    {
        title: "Biologia",
        description: "Descubra os segredos da vida e como ela se adapta ao mundo.",
        image: "img/bio.png", // Caminho da imagem para o terceiro card
    },
    {
        title: "Química",
        description: "Desvende as reações que transformam a matéria e fazem o mundo funcionar.",
        image: "img/qui.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Física",
        description: "Compreenda as forças do universo e a ciência por trás de cada movimento.",
        image: "img/fisica.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Geografia",
        description: "Explorando o mundo e suas maravilhas.",
        image: "img/geografia.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "História",
        description: "Conheça o passado para entender o presente e construir o futuro.",
        image: "img/historia.png" // Caminho da imagem para o terceiro
    },
    {
        title: "Filosofia",
        description: "Pense e questione o mundo ao seu redor.",
        image: "img/filosofia.png" // Caminho da imagem para o terce
    },
    {
        title: "Sociologia",
        description: "Entenda a sociedade para transformar o mundo ao seu redor.",
        image: "img/sociologia.png" // Caminho da imagem para o terceiro
    }, 
    {
        title: "Inglês",
        description: "Aprenda inglês e abra as portas para o mundo e novas oportunidades.",
        image: "img/eua.png", //Caminho da imagem para o primeiro card
    },
    {
        title: "Francês",
        description: "Domine o francês e conecte-se com a língua da arte e da diplomacia.",
        image: "img/franca.png", // Caminho da imagem para o segundo card
    },
    {
        title: "Italiano",
        description: "Descubra a beleza do italiano e viva a cultura da moda e do design.",
        image: "img/italia.png", // Caminho da imagem para o segundo card
    },
    {
        title: "Espanhol",
        description: "Fale espanhol e conecte-se com milhões de pessoas ao redor do mundo.",
        image: "img/espanha.png", // Caminho da imagem para o terceiro card
    },
    {
        title: "Coreano",
        description: "Aprenda coreano e mergulhe na cultura vibrante e tecnológica da Coreia.",
        image: "img/coreia.png", // Caminho da imagem para o terceiro card
    },
    {
        title: "Japonês",
        description: "Desvende o japonês e explore a tradição e inovação de um país fascinante.",
        image: "img/japao.png", // Caminho da imagem para o terceiro card
    },
    {
        title: "Alemão",
        description: "Domine o alemão e abra caminho para a ciência, a tecnologia e a indústria.",
        image: "img/alemanha.png", // Caminho da imagem para o terceiro card
    },
    {
        title: "Chinês",
        description: "Aprenda chinês e conecte-se com a língua do futuro e a cultura milenar.",
        image: "img/china.png", // Caminho da imagem para o terceiro
    },  
    {
        title: "HTML 5",
        description: "Construa a estrutura da web e dê vida às suas ideias online.",
        image: "img/html.png" //Caminho da imagem para o primeiro card
    },
    {
        title: "CSS",
        description: "Estilize a web e crie experiências visuais incríveis.",
        image: "img/css.png" // Caminho da imagem para o segundo card
    },
    {
        title: "JavaScript",
        description: "Transforme a web com interatividade e dinâmica em cada página.",
        image: "img/javascript.png" // Caminho da imagem para o segundo card
    },
    {
        title: "React",
        description: "Desenvolva interfaces modernas e escaláveis com facilidade.",
        image: "img/react.png", // Caminho da imagem para o terceiro card
    },
    {
        title: "Python",
        description: "Programe com simplicidade e conquiste o mundo da ciência de dados e automação.",
        image: "img/python.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Designer Gráfico",
        description: "Transforme ideias em arte e crie interfaces que encantam.",
        image: "img/designer.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Linguagem C",
        description: "Controle o hardware e programe com uma das linguagens mais poderosas.",
        image: "img/c.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Banco de Dados",
        description: "Organize dados e construa sistemas robustos e inteligentes.",
        image: "img/bd.png" // Caminho da imagem para o terceiro
    },  
    {
        title: "MySQL",
        description: "Gerencie grandes volumes de dados de forma eficiente e confiável.",
        image: "img/mysql.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Ruby",
        description: "Desenvolva aplicações elegantes e produtivas com uma linguagem dinâmica.",
        image: "img/ruby.png", // Caminho da imagem para o terceiro card
    },
    {
        title: "Linguagem C#",
        description: "Crie soluções robustas para plataformas diversas com facilidade.",
        image: "img/c..png" // Caminho da imagem para o terceiro
    }, 
    {
        title: "SQL",
        description: "Domine o SQL e controle o fluxo de dados de forma eficaz.",
        image: "img/sql.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "PHP",
        description: "Desenvolva websites dinâmicos e poderosos com simplicidade.",
        image: "img/php.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Java",
        description: "CrConstrua aplicações seguras e escaláveis para qualquer plataforma.",
        image: "img/java.png" // Caminho da imagem para o terceiro
    },    
];

const cardContainer = document.querySelector(".card-container");
const searchInput = document.querySelector("#searchInput");

const displayData = data => {
    cardContainer.innerHTML = "";
    
    // Se houver resultados, mostra os cards
    if (data.length > 0) {
        data.forEach(e => {
            cardContainer.innerHTML += `
            <article class="card-article">
                    <img src="${e.image}" alt="${e.title}" class="card-img">

                    <div class="card-data">
                        <span class="card-description">${e.description}</span>
                        <h2 class="card-title">${e.title}</h2>
                        <a href="" class="card-button">Leia Mais</a>
                    </div>
            </article>
            `;
        });
    } else {
        // Se não houver resultados, não mostra nada
        cardContainer.innerHTML = "<p>Nenhum resultado encontrado.</p>";
    }
};

searchInput.addEventListener("keyup", (e) => {
    const search = data.filter(i => i.title.toLowerCase().includes(e.target.value.toLowerCase()));
    
    // Só exibe os resultados da pesquisa
    if (e.target.value.trim() !== "") {
        displayData(search);
    } else {
        // Limpa a área se não houver busca
        cardContainer.innerHTML = "";
    }
});

window.addEventListener("load", () => {
    // Deixa a área dos cards vazia quando carregar a página
    cardContainer.innerHTML = "";
});
