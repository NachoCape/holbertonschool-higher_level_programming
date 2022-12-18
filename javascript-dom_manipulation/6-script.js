const character_name = document.querySelector('#character');
fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then ((response) => response.json())
  .then((data) => {
    character_name.textContent = data.name; 
  });
