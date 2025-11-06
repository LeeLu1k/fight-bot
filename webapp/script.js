let playerHealth = 100;
let botHealth = 100;

function playerMove(action) {
    let log = document.getElementById("log");
    let botAction = ["attack", "defense", "heal"][Math.floor(Math.random() * 3)];

    // --- Действие игрока ---
    if (action === "attack") {
        if (botAction !== "defense") {
            botHealth -= 20;
            log.innerHTML += `<p>Вы атаковали, бот получил 20 урона!</p>`;
        } else {
            log.innerHTML += `<p>Вы атаковали, но бот защитился!</p>`;
        }
    } else if (action === "defense") {
        log.innerHTML += `<p>Вы защитились!</p>`;
    } else if (action === "heal") {
        playerHealth += 15;
        if (playerHealth > 100) playerHealth = 100;
        log.innerHTML += `<p>Вы исцелились на 15 HP!</p>`;
    }

    // --- Действие бота ---
    if (botAction === "attack") {
        if (action !== "defense") {
            playerHealth -= 20;
            log.innerHTML += `<p>Бот атаковал, вы получили 20 урона!</p>`;
        } else {
            log.innerHTML += `<p>Бот атаковал, но вы защитились!</p>`;
        }
    } else if (botAction === "heal") {
        botHealth += 15;
        if (botHealth > 100) botHealth = 100;
        log.innerHTML += `<p>Бот исцелился на 15 HP!</p>`;
    } else {
        log.innerHTML += `<p>Бот защитился!</p>`;
    }

    document.getElementById("playerHealth").innerText = playerHealth;
    document.getElementById("botHealth").innerText = botHealth;

    // --- Проверка конца игры ---
    if (playerHealth <= 0 || botHealth <= 0) {
        if (playerHealth <= 0 && botHealth <= 0) alert("Ничья!");
        else if (playerHealth <= 0) alert("Вы проиграли!");
        else alert("Вы выиграли!");
        playerHealth = 100;
        botHealth = 100;
        log.innerHTML = "";
        document.getElementById("playerHealth").innerText = playerHealth;
        document.getElementById("botHealth").innerText = botHealth;
    }
}
