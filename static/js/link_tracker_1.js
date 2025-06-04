const TOTAL_LINK = document.querySelectorAll(".point_1").length;
const STORAGE_KEY = "clicked_link";
const PROGRESS_BAR = document.getElementById("progress_bar_1");

document.addEventListener("DOMContentLoaded", () => {
    updateProgressBar();
});


// отслеживание ссылок из левого списка (???)
document.querySelectorAll(".point_1").forEach(link => {
    link.addEventListener("click", async function (e) {
        
        const linkId = this.dataset.id;
        const href = this.getAttribute("href")

        if (isAlreadyClicked(linkId)) {
            return;
        };

        e.preventDefault();

        const success = await sendClickToServer(linkId);

        if (success) {
            saveClickedLink(linkId);
            updateProgressBar();

            window.open(href,"_blank")
        };
    });
});

function isAlreadyClicked(linkId) {
    const clicked = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
    return clicked.includes(linkId);
};

function saveClickedLink(linkId) {
    const clicked = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
    clicked.push(linkId);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(clicked));
};

function updateProgressBar () {
    const clicked = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
    const persent = Math.round((clicked.length / TOTAL_LINK) * 100);

    PROGRESS_BAR.style.width = `${persent}%`;
    PROGRESS_BAR.textContent = `${persent}% просмотренных видео`;
    PROGRESS_BAR.setAttribute("aria-valuenow", persent);
};

async function sendClickToServer(linkId) {
    try {
        // const csrfToken = document.querySelector("meta[name='csrf-token']").textContent;

        const responce = await fetch("/track_link_left", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                link_id : linkId,
                action: "count_and_redirect"
            })
        });
        return responce.ok;
    } catch (error) {
        console.error("Ошибка",error);
        return false;
    }
}