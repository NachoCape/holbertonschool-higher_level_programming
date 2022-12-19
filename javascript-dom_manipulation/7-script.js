const list = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    for (let title of data.results) {
      const li = document.createElement('li');
      li.textContent = title.title;
      list.append(li);
    }
  });
