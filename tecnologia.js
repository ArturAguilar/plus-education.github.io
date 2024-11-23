const data = [
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
    data.forEach(e => {
        cardContainer.innerHTML += `
        <article class="card-article">
                <img src="${e.image}" alt="${e.title}" class="card-img"> <!-- Usando a imagem correspondente -->

                <div class="card-data">
                    <span class="card-description">${e.description}</span>
                    <h2 class="card-title">${e.title}</h2>
                    <a href="" class="card-button">Leia Mais</a>
                </div>
        </article>
        
        `;
    });
};

searchInput.addEventListener("keyup", (e) => {
    const search = data.filter(i => i.title.toLowerCase().includes(e.target.value.toLowerCase()));
    displayData(search);
});

window.addEventListener("load", () => displayData(data));