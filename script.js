// Selecionar os elementos do menu hambúrguer
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("nav-links");

// Adicionar evento de clique
hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});
