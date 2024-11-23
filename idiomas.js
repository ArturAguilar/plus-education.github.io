const data = [
    {
        title: "Inglês",
        description: "Aprenda inglês e abra as portas para o mundo e novas oportunidades.",
        image: "img/eua.png" //Caminho da imagem para o primeiro card
    },
    {
        title: "Francês",
        description: "Domine o francês e conecte-se com a língua da arte e da diplomacia.",
        image: "img/franca.png" // Caminho da imagem para o segundo card
    },
    {
        title: "Italiano",
        description: "Descubra a beleza do italiano e viva a cultura da moda e do design.",
        image: "img/italia.png" // Caminho da imagem para o segundo card
    },
    {
        title: "Espanhol",
        description: "Fale espanhol e conecte-se com milhões de pessoas ao redor do mundo.",
        image: "img/espanha.png", // Caminho da imagem para o terceiro card
    },
    {
        title: "Coreano",
        description: "Aprenda coreano e mergulhe na cultura vibrante e tecnológica da Coreia.",
        image: "img/coreia.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Japonês",
        description: "Desvende o japonês e explore a tradição e inovação de um país fascinante.",
        image: "img/japao.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Alemão",
        description: "Domine o alemão e abra caminho para a ciência, a tecnologia e a indústria.",
        image: "img/alemanha.png" // Caminho da imagem para o terceiro card
    },
    {
        title: "Chinês",
        description: "Aprenda chinês e conecte-se com a língua do futuro e a cultura milenar.",
        image: "img/china.png" // Caminho da imagem para o terceiro
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