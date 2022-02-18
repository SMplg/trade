// меняет цвет при клике (каталог - бренды)
$(document).on('click', '.js-badge' , function(){ 
    this.classList.toggle('badge-dark');
    this.classList.toggle('badge-amlight'); 
});


// меняет текст (жирный или обычный) при клике (каталог - категории)
$(document).on('click', '.js-category' , function(){ 
    this.classList.toggle('active');
});