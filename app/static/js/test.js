//Get the element with the id darktoggle and store it in variable darkToggle
let darkToggle = document.querySelector('#darkToggle');

//Add an EventListener that adds or removes the class 'darkmode' to the body
darkToggle.addEventListener('change', ()=> {
  document.body.classList.toggle('darkmode');
})