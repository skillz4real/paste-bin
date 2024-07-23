darkReader = document.getElementsByClassName('darkreader');

for (let i = 0; i < darkReader.length; i++ ){
  darkReader[i].classList.add('hidden') 
}
 const textarea = document.getElementById('paste');

textarea.addEventListener('keydown', function(event) {
  if (event.key === 'Tab') {
    event.preventDefault(); // Prevent default tab behavior (move to next element)
    const { selectionStart, selectionEnd, value } = textarea;
    const start = selectionStart;
    const end = selectionEnd;

    // Insert tab character at current cursor position
    textarea.value = value.substring(0, start) + '\t' + value.substring(end);
    
    // Move cursor to after the inserted tab
    textarea.selectionStart = textarea.selectionEnd = start + 1;
  }
}); 


