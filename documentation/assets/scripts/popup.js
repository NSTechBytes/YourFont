const query = localStorage.getItem('searchQuery');
const results = JSON.parse(localStorage.getItem('searchResults'));

// Display the search query
document.querySelector('.bold-text').textContent = `Search Results for "${query}"`;

// Display the results
const resultsContainer = document.getElementById('results-container');
if (results && results.length > 0) {
    results.forEach(item => {
        const resultDiv = document.createElement('div');
        resultDiv.classList.add('result-box');
        resultDiv.innerHTML = `
            <div class="icon-container">
                <i class="yf ${item['html-code']}"></i> <!-- Dynamically apply the icon class -->
            </div>
            <p class="icon-name">${item.name}</p>
        `;
        resultDiv.addEventListener('click', () => openPopup(item));
        resultsContainer.appendChild(resultDiv);
    });
} else {
    resultsContainer.innerHTML = '<p>No results found.</p>';
}

// Open Popup Function
async function openPopup(item) {
    const popupBox = document.getElementById('popup-box');
    const popupIcon = document.getElementById('popup-icon');
    const popupUnicode = document.getElementById('popup-unicode');
    const popupHtmlCode = document.getElementById('popup-html-code');
    const popupSvgContent = document.getElementById('popup-svg-content');

    // Update popup content
    popupIcon.className = ''; // Clear previous icon
    popupIcon.classList.add(`yf`, item['html-code']); // Apply the CSS class for the icon
    popupUnicode.textContent = item.code; // Unicode value
    popupHtmlCode.textContent = `<i class="yf ${item['html-code']}"></i>`; // HTML code

    // Fetch and display SVG content
    try {
        const svgFileName = `${item.name.toLowerCase()}.svg`; // e.g., home.svg
        const response = await fetch(`assets/svg/${svgFileName}`);
        if (response.ok) {
            const svgContent = await response.text();
            popupSvgContent.textContent = svgContent;
        } else {
            popupSvgContent.textContent = 'SVG file not found.';
        }
    } catch (error) {
        console.error('Error fetching SVG:', error);
        popupSvgContent.textContent = 'Error loading SVG content.';
    }

    // Show popup
    popupBox.classList.remove('hidden');
}

// Close Popup Function
function closePopup() {
    const popupBox = document.getElementById('popup-box');
    popupBox.classList.add('hidden');
}

// Custom Notification Function
function showNotification(message) {
    const notification = document.getElementById('custom-notification');
    const notificationMessage = document.getElementById('notification-message');
    notificationMessage.textContent = message;

    // Show notification
    notification.classList.remove('hidden');

    // Hide notification after 3 seconds
    setTimeout(() => {
        notification.classList.add('hidden');
    }, 3000);
}

// Copy Unicode Function
function copyUnicode() {
    const unicode = document.getElementById('popup-unicode').textContent;
    navigator.clipboard.writeText(unicode).then(() => {
        showNotification('Unicode copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy text: ', err);
        showNotification('Failed to copy Unicode.');
    });
}

// Copy HTML Code Function
function copyHtmlCode() {
    const htmlCode = document.getElementById('popup-html-code').textContent;
    navigator.clipboard.writeText(htmlCode).then(() => {
        showNotification('HTML Code copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy text: ', err);
        showNotification('Failed to copy HTML code.');
    });
}

// Copy SVG Content Function
function copySvgContent() {
    const svgContent = document.getElementById('popup-svg-content').textContent;
    navigator.clipboard.writeText(svgContent).then(() => {
        showNotification('SVG Content copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy text: ', err);
        showNotification('Failed to copy SVG content.');
    });
}