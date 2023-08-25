const link = document.querySelector('#contact');

// Añadir un escuchador de eventos para el clic
link.addEventListener('click', (event) => {
  // Prevenir la acción predeterminada del enlace
  event.preventDefault();

  // Obtener la posición del elemento a donde se desea hacer scroll
  const target = document.querySelector('#foot');
  const targetPosition = target.getBoundingClientRect().top;

  // Hacer scroll suavemente hacia abajo
  window.scrollTo({
    top: targetPosition,
    behavior: 'smooth'
  });
});