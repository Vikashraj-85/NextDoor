
//   for profile toggle
const leftBox = document.querySelector(' #drop-down-toggle');
const rightBox = document.querySelector(' #profile-drop-down-1');


leftBox.addEventListener('mouseenter', () => {
    rightBox.style.display = 'block';
  
});


window.addEventListener('click', () => {

    if(rightBox.style.display === 'block'){
        rightBox.style.display = 'none';
    }
    
    

});