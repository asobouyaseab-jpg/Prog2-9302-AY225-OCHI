
const draggable = document.getElementById('draggable');
const dropzone = document.getElementById('dropzone');

draggable.addEventListener('dragstart', (e) => {
    
    e.dataTransfer.setData('text/plain', draggable.id);
    e.dataTransfer.effectAllowed = 'move'; 
});


dropzone.addEventListener('dragover', (e) => {
    e.preventDefault(); 
    dropzone.classList.add('dragover'); 
    e.dataTransfer.dropEffect = 'move';
});


dropzone.addEventListener('dragleave', () => {
    dropzone.classList.remove('dragover');
});


dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.classList.remove('dragover');
    
    
    const draggedId = e.dataTransfer.getData('text/plain');
    const draggedElement = document.getElementById(draggedId);
    
    
    dropzone.appendChild(draggedElement);
    
    console.log('ドロップ完了！'); 
});