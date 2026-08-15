function displayHello () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      const hello = document.querySelector('#hello');
      hello.textContent = data.hello;
    });
}

document.addEventListener('DOMContentLoaded', displayHello);
