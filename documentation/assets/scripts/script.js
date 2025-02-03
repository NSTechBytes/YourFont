
function showNotification(message) {
    const notification = document.getElementById('custom-notification');
    const notificationMessage = document.getElementById('notification-message');
    notificationMessage.textContent = message;


    notification.classList.remove('hidden');


    setTimeout(() => {
        notification.classList.add('hidden');
    }, 3000);
}


