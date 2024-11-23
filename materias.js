const data = [
    {
        title: "Língua Portuguesa",
        description: "Domine as palavras e abra portas para o mundo.",
        image: "img/portugues.png" // Caminho da imagem para o primeiro card
    },
    {
        title: "Inglês",
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