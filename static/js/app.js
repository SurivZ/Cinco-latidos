const hora = document.querySelector("#hora");
const fecha = document.querySelector("#fecha");

setInterval(() => {
  const $hora = new Date().toLocaleTimeString();

  const $fecha = {
    dia: new Date().getDate(),
    mes: new Date().getMonth(),
    anio: new Date().getFullYear(),
  };

  hora.innerHTML = $hora;
  fecha.innerHTML = `${$fecha.dia}/${$fecha.mes}/${$fecha.anio}`;
}, 1000);


document.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}, false);