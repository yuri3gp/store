const formulario = document.querySelector('#formulario');
formulario.addEventListener("submit", async (event) => {
    event.preventDefault();
    const dados = new FormData(formulario);
    try {
        const response = await fetch('/enviar', {
            method: 'POST',
            body: dados
        });
        const data = await response.text();
        console.log(data);
        location.reload()
    } catch (error) {
        console.error(error);
    }
});