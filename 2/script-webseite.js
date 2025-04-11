<script>
    function changePage(pageId) {
        const loader = document.getElementById('loader');
        loader.classList.add('active');
        
        setTimeout(function() {
            // Hide all pages
            document.querySelectorAll('.page').forEach(function(page) {
                page.classList.remove('active');
                page.classList.add('inactive');
            });
            
            // Show the requested page
            const newPage = document.getElementById(pageId);
            if (newPage) {
                newPage.classList.remove('inactive');
                newPage.classList.add('active');
                window.scrollTo(0, 0);
            }
            
            loader.classList.remove('active');
        }, 300);
    }
    
    document.addEventListener('DOMContentLoaded', function() {
        // Initialize all pages except home as inactive
        document.querySelectorAll('.page').forEach(function(page) {
            if (page.id !== 'home-page') {
                page.classList.add('inactive');
                page.classList.remove('active');
            }
        });
    });
</script>