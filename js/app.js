document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("comicForm");

    const loading = document.getElementById("loading");

    const result = document.getElementById("result");

    const generateButton =
        document.getElementById("generateButton");


    // Panel selection
    const panelOptions =
        document.querySelectorAll(".panel-option");

    panelOptions.forEach(option => {

        option.addEventListener("click", () => {

            panelOptions.forEach(item => {
                item.classList.remove("active");
            });

            option.classList.add("active");

            const radio =
                option.querySelector("input");

            if (radio) {
                radio.checked = true;
            }
        });

    });


    // Form
    form.addEventListener("submit", async (event) => {

        event.preventDefault();


        const story =
            document.getElementById("story").value.trim();

        const characters =
            document.getElementById("characters").value.trim();

        const style =
            document.getElementById("style").value;

        const panels =
            document.querySelector(
                'input[name="panels"]:checked'
            ).value;


        if (!story) {

            alert("Please describe your story first.");

            return;
        }


        // Loading state
        form.style.display = "none";

        loading.style.display = "block";

        result.style.display = "none";


        try {

            const response = await fetch("/generate", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    story: story,

                    characters: characters,

                    style: style,

                    panels: Number(panels)

                })

            });


            if (!response.ok) {

                throw new Error(
                    "Comic generation failed"
                );

            }


            const data = await response.json();


            loading.style.display = "none";

            result.style.display = "block";


            const comicResult =
                document.getElementById("comicResult");


            if (data.image_url) {

                comicResult.innerHTML = `

                    <div class="generated-comic">

                        <img
                            src="${data.image_url}"
                            alt="Generated Comic"
                            style="
                                width:100%;
                                border-radius:15px;
                            "
                        >

                    </div>

                `;

            } else {

                comicResult.innerHTML = `

                    <div style="
                        padding:30px;
                        background:#fff8f3;
                        border-radius:15px;
                        text-align:center;
                    ">

                        <h3>Comic generated successfully!</h3>

                        <p>
                            ${data.message || ""}
                        </p>

                    </div>

                `;

            }


        } catch (error) {

            console.error(error);

            loading.style.display = "none";

            form.style.display = "block";

            alert(
                "Something went wrong while generating your comic."
            );

        }

    });

});


function scrollToCreate() {

    document
        .getElementById("create")
        .scrollIntoView({
            behavior: "smooth"
        });

}