

let cardsPage = document.querySelector(".cards-page"),
    homePage = document.querySelector(".home-page"),
    chatPage = document.querySelector(".chat-page"),
    cardsBtm = document.querySelector(".cards-btm"),
    homeBtm = document.querySelector(".home-btm"),
    chatBtm = document.querySelector(".chat-btm");

    cardsBtm.onclick = showGamecards;
    homeBtm.onclick = showGameHome;
    chatBtm.onclick = showGameChat;

function showGamecards(){
    console.log("-1");
    cardsPage.style.left = 0;
    homePage.style.left = "100vw";
    chatPage.style.left = "200vw";

    cardsBtm.style.background = "#ffe652";
    cardsBtm.style.transform = "scale(1.05)";
    homeBtm.style.background = "transparent";
    homeBtm.style.transform = "scale(1)";
    chatBtm.style.background = "transparent";
    chatBtm.style.transform = "scale(1)";
}
function showGameHome(){
    console.log("0");
    cardsPage.style.left = "-100vw";
    homePage.style.left = 0;
    chatPage.style.left = "100vw";

    cardsBtm.style.background = "transparent";
    cardsBtm.style.transform = "scale(1)";
    homeBtm.style.background = "#ffe652";
    homeBtm.style.transform = "scale(1.05)";
    chatBtm.style.background = "transparent";
    chatBtm.style.transform = "scale(1)";
}
function showGameChat(){
    console.log("1");
    cardsPage.style.left = "-200vw";
    homePage.style.left = "-100vw";
    chatPage.style.left = 0;

    cardsBtm.style.background = "transparent";
    cardsBtm.style.transform = "scale(1)";
    homeBtm.style.background = "transparent";
    homeBtm.style.transform = "scale(1)";
    chatBtm.style.background = "#ffe652";
    chatBtm.style.transform = "scale(1.05)";
}