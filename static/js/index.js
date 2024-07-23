darkReader = document.getElementsByClassName('darkreader');

for (let i = 0; i < darkReader.length; i++ ){
  darkReader[i].classList.add('hidden') 
}

const textarea = document.getElementById('paste');

textarea.addEventListener('keydown', function(event) {
  if (event)
  event.preventDefault();

  
}

