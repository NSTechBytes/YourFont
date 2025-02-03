let allIcons = [];

// Fetch and display all icons from content.json
async function loadAllIcons() {
    try {
        const response = await fetch('../assets/content.json');
        allIcons = await response.json();

        // Display all icons initially
        displayIcons(allIcons);

        // Add event listeners to tabs
        document.querySelectorAll('.tab-button').forEach(tab => {
            tab.addEventListener('click', () => handleTabClick(tab));
        });
    } catch (error) {
        console.error('Error loading content.json:', error);
        document.getElementById('all-icons-container').innerHTML = '<p>Error loading icons.</p>';
    }
}

// Display icons based on category
function displayIcons(filteredIcons) {
    const container = document.getElementById('all-icons-container');
    container.innerHTML = ''; // Clear previous content

    Object.values(filteredIcons).forEach(item => {
        const iconDiv = document.createElement('div');
        iconDiv.classList.add('result-box');
        iconDiv.innerHTML = `
            <div class="icon-container">
                <i class="yf ${item['html-code']}"></i> <!-- Dynamically apply the icon class -->
            </div>
            <p class="icon-name">${item.name}</p>
        `;
        iconDiv.addEventListener('click', () => openPopup(item));
        container.appendChild(iconDiv);
    });
}

// Handle tab clicks
function handleTabClick(tab) {
    // Remove 'active' class from all tabs
    document.querySelectorAll('.tab-button').forEach(t => t.classList.remove('active'));

    // Add 'active' class to the clicked tab
    tab.classList.add('active');

    // Get the selected category
    const category = tab.dataset.category;

    // Filter icons based on the selected category
    if (category === 'all') {
        displayIcons(allIcons);
    } else {
        const filteredIcons = Object.values(allIcons).filter(icon => icon.category === category);
        displayIcons(filteredIcons);
    }
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
        const svgFileName = `${item.name.toLowerCase().replace(/ /g, '-')}.svg`; // e.g., arrow-up.svg
        const response = await fetch(`../assets/svg/${svgFileName}`);
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

// Load all icons on page load
window.onload = loadAllIcons;