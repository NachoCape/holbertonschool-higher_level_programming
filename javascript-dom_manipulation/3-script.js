const header_class = document.querySelector('header');
document.getElementById('toggle_header').onclick = function() {
  if (header_class.classList.value.includes('red')) {
    header_class.classList.remove('red');
    header_class.classList.add('green');
  } else if (header_class.classList.value.includes('green')) {
    header_class.classList.remove('green');
    header_class.classList.add('red');
  }
}
