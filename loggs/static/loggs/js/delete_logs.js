document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default form submission

        if (confirm("Are you sure you want to delete this?")) {
            const form = this.closest('form');
            const formData = new FormData(form);

            fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                },
                body: formData
            })
            .then(response => response.json()) // Parse JSON response
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url; // Redirect to the URL provided by the server
                } else {
                    alert('An error occurred while deleting.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An unexpected error occurred.');
            });
        }
    });
});
