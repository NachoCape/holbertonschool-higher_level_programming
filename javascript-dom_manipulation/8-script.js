fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
  .then(response => response.json())
  .then(data => {
    const hi = document.querySelector('#hello');
    hi.textContent = data.hello;
  });
  