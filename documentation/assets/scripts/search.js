document.getElementById('search-input').addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        performSearch();
    }
});

async function performSearch() {
    const query = document.getElementById('search-input').value.trim().toLowerCase();

    if (!query) {
        alert('Please enter a search term.');
        showNotification('Please enter a search term.');
        return;
    }

    try {
        // Fetch the JSON file
        const response = await fetch('assets/content.json');
        const data = await response.json();

        // Filter the data based on the search query
        const results = Object.values(data).filter(item =>
            item.name.toLowerCase().includes(query) ||
            item.code.toLowerCase().includes(query) ||
            item['html-code'].toLowerCase().includes(query)
        );

        // Store the query and results in localStorage
        localStorage.setItem('searchQuery', query);
        localStorage.setItem('searchResults', JSON.stringify(results));

        // Redirect to the search results page
        window.location.href = 'content/search-results.html';
    } catch (error) {
        console.error('Error fetching or processing data:', error);
        alert('An error occurred while searching. Please try again.');
    }
}
