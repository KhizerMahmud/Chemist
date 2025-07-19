const timerInterval = setInterval(function() {
    const timer = document.getElementById('timer');
    if (!timer) return;
    const gameOver = timer.getAttribute('data-game-over') === 'true';
    if (gameOver) {
        clearInterval(timerInterval);
        return;
    }

    let current = parseInt(timer.innerText, 10);
    if (current > 0) {
        timer.innerText = current - 1;
    } else {
        timer.innerText = 0;
        // Optionally, you can reload or show a message here
        // window.location.reload();
    }
}, 1000);