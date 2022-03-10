// меняет цвет (черный или серый) при клике (каталог - бренды)
$(document).on('click', '.js-badge' , function(){ 
    this.classList.toggle('badge-dark');
    this.classList.toggle('badge-amlight'); 
    var userChoice = collectChoice();
    myFilter(userChoice);
});


// меняет текст (жирный или обычный) при клике (каталог - категории)
$(document).on('click', '.js-category' , function(){ 
    this.classList.toggle('active');
    var userChoice = collectChoice();
    myFilter(userChoice);
});

function myFilter(userChoice) {
    // Функция отправляет фильтры которые включил пользователь и получает список с продуктами (они уже отфильтрованы во вьюхе)

    $.ajax({
        type: "GET",
        data: userChoice,
        url: "/filterproducts",
        dataType: 'json',
        success: function(data){
            console.log('Успешно получены обьекты. Начинаем создание Div');
            createObjects(data);
        }
    });
}

function collectChoice() {
    // Функция собирает значения для "бренды" и "категории", которые активны на странице "Каталог"

    var brands_node = [];
    var cotegories_node = [];

    // Собрать нажатые значения для брендов // (4) ['agm', 'boston_dynamics', 'jouav', 'geoscan']
    $('.badge-dark').each(function() {
        brand = $(this).attr('brand_html');
        brands_node.push(brand);
    });

    // Собрать активные значения для категорий // (4) ['air', 'terra', 'mobile', 'radars']
    $('.js-category.active').each(function() {
        category = $(this).attr('category_html');
        cotegories_node.push(category);
    });

    // Словарь для отправки во views

    var choice = {
        'brands': brands_node, 
        'categories': cotegories_node
    };

    return choice;
}

function createObjects(productList) {
    // Функция создаёт объекты в HTML (получает список словарей, в списках все данные о продуктах)


    // Удаляет существующие div'ы с продуктами
    var parent_div = document.getElementById("products-section");

    while (parent_div.firstChild) {
        parent_div.firstChild.remove();
    }

    // Создаёт новые div'ы с продуктами
    for (var elem in productList) {
        selected = productList[elem];

        var product_node = document.createElement("div");
        product_node.className = "col-sm-4";
        product_node.innerHTML = `
                                    <article class="post post-medium border-0 pb-0 mb-5">
    
                                        <div class="post-image">
                                            <a href="/product/${selected.url_dop}">
                                                <img src="media/${selected.img_product}" class="img-fluid img-thumbnail img-thumbnail-no-borders rounded-0" alt="" />
                                            </a>
                                        </div>
    
                                        <div class="post-content">
                                            <h2 class="font-weight-semibold text-5 line-height-6 mt-3 mb-2"><a href="/product/${selected.url_dop}">${selected.name}</a></h2>
    
                                            <p>${selected.description_short}</p>
    
                                            <div class="post-meta">
                                                <span><i class="far fa-user"></i> by <a href="/brandpage/${selected.manufacturer_url}">${selected.manufacturer_name}</a> </span>
                                                <span class="d-block mt-2"><a href="/product/${selected.url_dop}" class="btn btn-xs btn-light text-1 text-uppercase">Подробнее</a></span>
                                            </div>
    
                                        </div>
    
                                    </article>
        `;
    
        parent_div.append(product_node);
    
    }

    
}