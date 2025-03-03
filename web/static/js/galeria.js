// document.addEventListener('DOMContentLoaded', function() {
//     // Variables
//     const filterBtns = document.querySelectorAll('.filter-btn');
//     const galleryItems = document.querySelectorAll('.gallery-item');
//     const lightbox = document.querySelector('.lightbox');
//     const lightboxImg = document.querySelector('.lightbox-img');
//     const lightboxTitle = document.querySelector('.lightbox-title');
//     const lightboxCategory = document.querySelector('.lightbox-category');
//     const lightboxClose = document.querySelector('.lightbox-close');
//     const lightboxPrev = document.querySelector('.lightbox-prev');
//     const lightboxNext = document.querySelector('.lightbox-next');
    
//     let currentIndex = 0;
//     let filteredItems = [...galleryItems];
    
//     // Filtrar imágenes por categoría
//     filterBtns.forEach(btn => {
//         btn.addEventListener('click', function() {
//             // Eliminar clase active de todos los botones
//             filterBtns.forEach(btn => btn.classList.remove('active'));
            
//             // Añadir clase active al botón actual
//             this.classList.add('active');
            
//             const filter = this.getAttribute('data-filter');
            
//             // Mostrar/ocultar elementos según el filtro
//             galleryItems.forEach(item => {
//                 if (filter === 'all' || item.getAttribute('data-category') === filter) {
//                     item.style.display = 'block';
                    
//                     // Aplicar animación de entrada
//                     item.style.animation = 'none';
//                     void item.offsetWidth; // Forzar reflow
//                     item.style.animation = 'fadeIn 0.5s ease forwards';
//                 } else {
//                     item.style.display = 'none';
//                 }
//             });
            
//             // Actualizar los items filtrados
//             filteredItems = [...galleryItems].filter(item => 
//                 filter === 'all' || item.getAttribute('data-category') === filter
//             );
//         });
//     });
    
//     // Abrir lightbox al hacer clic en una imagen
//     galleryItems.forEach((item, index) => {
//         item.addEventListener('click', function() {
//             const img = this.querySelector('img');
//             const title = this.querySelector('.item-title').textContent;
//             const category = this.querySelector('.item-category').textContent;
            
//             lightboxImg.src = img.src;
//             lightboxTitle.textContent = title;
//             lightboxCategory.textContent = category;
//             lightbox.classList.add('active');
            
//             // Guardar el índice actual
//             currentIndex = filteredItems.indexOf(this);
//         });
//     });
    
//     // Cerrar lightbox
//     lightboxClose.addEventListener('click', () => {
//         lightbox.classList.remove('active');
//     });
    
//     // Cerrar lightbox con tecla ESC
//     document.addEventListener('keydown', (e) => {
//         if (e.key === 'Escape') {
//             lightbox.classList.remove('active');
//         }
//     });
    
//     // Navegar al anterior
//     lightboxPrev.addEventListener('click', () => {
//         if (currentIndex > 0) {
//             currentIndex--;
//         } else {
//             currentIndex = filteredItems.length - 1;
//         }
//         updateLightbox();
//     });
    
//     // Navegar al siguiente
//     lightboxNext.addEventListener('click', () => {
//         if (currentIndex < filteredItems.length - 1) {
//             currentIndex++;
//         } else {
//             currentIndex = 0;
//         }
//         updateLightbox();
//     });
    
//     // Navegar con teclado
//     document.addEventListener('keydown', (e) => {
//         if (lightbox.classList.contains('active')) {
//             if (e.key === 'ArrowLeft') {
//                 lightboxPrev.click();
//             } else if (e.key === 'ArrowRight') {
//                 lightboxNext.click();
//             }
//         }
//     });
    
//     // Actualizar lightbox con la imagen actual
//     function updateLightbox() {
//         const currentItem = filteredItems[currentIndex];
//         const img = currentItem.querySelector('img');
//         const title = currentItem.querySelector('.item-title').textContent;
//         const category = currentItem.querySelector('.item-category').textContent;
        
//         lightboxImg.src = img.src;
//         lightboxTitle.textContent = title;
//         lightboxCategory.textContent = category;
//     }
    
//     // Efecto de entrada escalonado para los elementos de la galería
//     galleryItems.forEach((item, index) => {
//         item.style.animationDelay = `${index * 0.1}s`;
//     });



// });


const images = [
  {
      src: "{ static 'img/1.jpg' }",
      title: "ensalada fitness",
      description: "Hermosas vistas de montañas cubiertas de nieve y vegetación"
  },
  {
      src: "/api/placeholder/800/600",
      title: "Playa tropical",
      description: "Arena blanca y aguas cristalinas en un paraíso tropical"
  },
  {
      src: "/api/placeholder/800/600",
      title: "Ciudad moderna",
      description: "Rascacielos y arquitectura urbana contemporánea"
  },
  {
      src: "/api/placeholder/800/600",
      title: "Bosque denso",
      description: "Naturaleza verde y exuberante con árboles centenarios"
  },
  {
      src: "/api/placeholder/800/600",
      title: "Desierto árido",
      description: "Extensiones de arena y dunas bajo el sol intenso"
  },
  {
      src: "/api/placeholder/800/600",
      title: "Lago tranquilo",
      description: "Aguas calmas rodeadas de vegetación exuberante"
  }
];

const modal = document.getElementById('imageModal');
const modalImage = document.getElementById('modalImage');
const modalTitle = document.getElementById('modalTitle');
const modalDescription = document.getElementById('modalDescription');

// Función para abrir el modal
function openModal(index) {
  const image = images[index];
  modalImage.src = image.src;
  modalTitle.textContent = image.title;
  modalDescription.textContent = image.description;
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

// Función para cerrar el modal
function closeModal() {
  modal.classList.remove('active');
  document.body.style.overflow = '';
}

// Cerrar modal al hacer clic fuera de la imagen
modal.addEventListener('click', function(event) {
  if (event.target === modal) {
      closeModal();
  }
});

// Cerrar modal con la tecla Escape
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
  }
});