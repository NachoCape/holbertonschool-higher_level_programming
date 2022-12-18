const header_class = document.querySelector('ul');
document.getElementById('add_item').onclick = function() {
  const elem = document.createElement('li');
  elem.textContent = 'Item';
  header_class.append(elem)
}
