const TOTAL_LINK_2 = document.querySelectorAll(".point_2").length;
const STORAGE_KEY_2 = "clicked_link_2";
const PROGRESS_BAR_2 = document.getElementById("progress_bar_2");

document.addEventListener("DOMContentLoaded", () => {
    updateProgressBar_2();
});


// отслеживание ссылок из левого списка (???)
document.querySelectorAll(".point_2").forEach(link => {
    link.addEventListener("click", async function (e) {
        
        const linkId_2 = this.dataset.id;
        const href_2 = this.getAttribute("href")

        if (isAlreadyClicked_2(linkId_2)) {
            return;
        };

        e.preventDefault();

        const success = await sendClickToServer_2(linkId_2);

        if (success) {
            saveClickedLink_2(linkId_2);
            updateProgressBar_2();

            window.open(href_2,"_blank")
        };
    });
});

function isAlreadyClicked_2(linkId_2) {
    const clicked = JSON.parse(localStorage.getItem(STORAGE_KEY_2)) || [];
    return clicked.includes(linkId_2);
};

function saveClickedLink_2(linkId_2) {
    const clicked = JSON.parse(localStorage.getItem(STORAGE_KEY_2)) || [];
    clicked.push(linkId_2);
    localStorage.setItem(STORAGE_KEY_2, JSON.stringify(clicked));
};

function updateProgressBar_2 () {
    const clicked = JSON.parse(localStorage.getItem(STORAGE_KEY_2)) || [];
    const persent = Math.round((clicked.length / TOTAL_LINK_2) * 100);

    PROGRESS_BAR_2.style.width = `${persent}%`;
    PROGRESS_BAR_2.textContent = `${persent}% решёных тестов`;
    PROGRESS_BAR_2.setAttribute("aria-valuenow", persent);
};

async function sendClickToServer_2(linkId_2) {
    try {
        // const csrfToken = document.querySelector("meta[name='csrf-token']").textContent;

        const responce = await fetch("/track_link_right", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                link_id_2 : linkId_2,
                action: "count_and_redirect"
            })
        });
        return responce.ok;
    } catch (error) {
        console.error("Ошибка",error);
        return false;
    }
}