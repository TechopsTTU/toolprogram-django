// Database Connection Check Utility

document.addEventListener('DOMContentLoaded', function() {
    // Add database connection status indicator
    const statusIndicator = document.createElement('div');
    statusIndicator.id = 'db-status';
    statusIndicator.className = 'status-indicator';
    statusIndicator.innerHTML = `
        <span class="status-dot pending"></span>
        <span class="status-text">Checking database connection...</span>
    `;
    document.querySelector('header').appendChild(statusIndicator);

    // Function to check database connection
    function checkDatabaseConnection() {
        fetch('/api/db-status/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Database connection failed');
                }
                return response.json();
            })
            .then(data => {
                const statusDot = document.querySelector('.status-dot');
                const statusText = document.querySelector('.status-text');

                if (data.status === 'connected') {
                    statusDot.className = 'status-dot connected';
                    statusText.textContent = 'Database connected';
                    console.log('Database connection verified:', data);
                } else {
                    statusDot.className = 'status-dot error';
                    statusText.textContent = 'Database connection error';
                    console.error('Database connection issue:', data.message);
                }
            })
            .catch(error => {
                const statusDot = document.querySelector('.status-dot');
                const statusText = document.querySelector('.status-text');
                statusDot.className = 'status-dot error';
                statusText.textContent = 'Database connection error';
                console.error('Database connection check failed:', error);
            });
    }

    // Check database connection on page load
    checkDatabaseConnection();

    // Add connection verification button to admin pages
    if (window.location.pathname.includes('/admin/')) {
        const adminToolbar = document.querySelector('#header');
        if (adminToolbar) {
            const verifyButton = document.createElement('button');
            verifyButton.id = 'verify-db';
            verifyButton.className = 'btn';
            verifyButton.textContent = 'Verify DB Connections';
            verifyButton.onclick = function() {
                checkDatabaseConnection();
                return false;
            };
            adminToolbar.appendChild(verifyButton);
        }
    }
});
