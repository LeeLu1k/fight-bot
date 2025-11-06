let playerHP = 100;
let botHP = 100;

function attack() {
    const playerDamage = Math.floor(Math.random() * 20) + 5;
    const botDamage = Math.floor(Math.random() * 15) + 5;
    botHP -= playerDamage;
    playerHP -= botDamage;
    updateStatus();
}

function heal() {
    const healAmount = Math.floor(Math.random() * 20) + 5;
    playerHP += healAmount;
    const botDamage = Math.floor(Math.random() * 15) + 5;
    playerHP -= botDamage;
    updateStatus();
}

function updateStatus() {
    if(playerHP <= 0 && botHP <= 0){
        document.getElementById("status").innerText = "Ничья!";
    } else if(playerHP <= 0){
        document.getElementById("status").innerText = "Вы проиграли!";
    } else if(botHP <= 0){
        document.getElementById("status").innerText = "Вы победили!";
    } else {
        document.getElementById("status").innerText = `Ваше HP: ${playerHP} | Бот HP: ${botHP}`;
    }
}
