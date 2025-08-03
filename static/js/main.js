// Tool Management System JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Make messages dismissible
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        // Add close button
        const closeBtn = document.createElement('span');
        closeBtn.innerHTML = '&times;';
        closeBtn.className = 'close-message';
        closeBtn.style.float = 'right';
        closeBtn.style.cursor = 'pointer';
        closeBtn.style.fontWeight = 'bold';
        closeBtn.onclick = function() {
            message.style.display = 'none';
        };
        message.prepend(closeBtn);

        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            message.style.display = 'none';
        }, 5000);
    });

    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.delete-btn, button[type="submit"][value="delete"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
});
