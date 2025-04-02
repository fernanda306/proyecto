
// productos.js - Check login before adding to cart

document.addEventListener('DOMContentLoaded', function() {
    // Select all "Add to cart" forms
    const addToCartForms = document.querySelectorAll('.producto-card form');
    
    // Add event listener to each form
    addToCartForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            // Check if user is logged in
            // This assumes you have a way to determine if user is logged in
            // For Django, you can pass this information in the template context
            const isLoggedIn = checkUserLoginStatus();
            
            if (!isLoggedIn) {
                // Prevent form submission
                event.preventDefault();
                
                // Redirect to login page
                // Get the current URL to redirect back after login
                const currentPage = window.location.href;
                
                // Redirect to login with next parameter
                window.location.href = '/login/?next=' + encodeURIComponent(currentPage);
                
                // Optionally show a message
                alert('Debes iniciar sesión para agregar productos al carrito');
            }
            // If user is logged in, form submits normally
        });
    });
    
    // Function to check if user is logged in
    // This function needs to be implemented based on how your app tracks login status
    function checkUserLoginStatus() {
        // For Django templates, you would pass this information and access it like:
        // return userIsAuthenticated; // This would be a variable set in your template
        
        // Since we don't have direct access to Django's authentication in JS,
        // we'll use a data attribute approach
        
        // Check for a data attribute on the body or another element
        const body = document.body;
        return body.getAttribute('data-user-authenticated') === 'true';
    }
});