
var isMobile = function () {
    return /(iphone|ipod|ipad|android|blackberry|windows ce|palm|symbian)/i.test(navigator.userAgent);
};
var productContainer = $('.equalHeightCategoryProduct');

$(document).ready(function () {

    make_input_field();

    function updateCart(data){
        console.log("OK");
        console.log(data);
        console.log(data.products_total_nmb);
        console.log(data.order_total_price);
        if (data.products_total_nmb) {
            $('.cartRespons').text('Корзина (' + data.order_total_price + 'UAH) ');
            $('.subtotal').text('Subtotal: ' + data.order_total_price + ' UAH');
            console.log(data.products)
            var Table = document.getElementById("mCSB_tbody");
            console.log(Table);
            Table.innerHTML = "";
            for (var row = 0; row < data.products_total_nmb; row++) {
                var mycurrent_row = document.createElement("tr");
                mycurrent_row.className = "miniCartProduct";
                var thumb_cell = document.createElement("td");
                //Cell image
                thumb_cell.style.cssText = "width:20%";
                thumb_cell.className = "miniCartProductThumb";
                var thumb_cell_div = document.createElement('div');
                var thumb_cell_a = document.createElement("a");
                thumb_cell_a.setAttribute('href', '/item/' + data.products[row].id);
                var thumb_cell_img = document.createElement("img");
                thumb_cell_img.alt = "img";
                thumb_cell_img.src = data.products[row].img;
                thumb_cell_a.appendChild(thumb_cell_img);
                thumb_cell_div.appendChild(thumb_cell_a);
                thumb_cell.appendChild(thumb_cell_div);
                mycurrent_row.appendChild(thumb_cell);
                //Cell description + price
                //description
                var description_cell = document.createElement("td");
                description_cell.style.cssText = "width:40%";
                var description_div = document.createElement('div');
                description_div.className = "miniCartDescription";
                var description_h4 = document.createElement("h4")
                var description_a = document.createElement("a")
                description_a.setAttribute('href', '/item/' + data.products[row].id)
                description_a.textContent = data.products[row].name;
                description_h4.appendChild(description_a)
                //price
                var price_div = document.createElement('div');
                price_div.className = "price";
                price_div.innerHTML = '<span> ' + data.products[row].price + 'UAH </span>';
                description_div.appendChild(description_h4);
                description_div.appendChild(price_div);
                description_cell.appendChild(description_div);
                mycurrent_row.appendChild(description_cell);
                //Cell quantity
                var quantity_cell = document.createElement("td");
                quantity_cell.style.cssText = "width:20%";
                quantity_cell.className = "miniCartQuantity";
                quantity_cell.innerHTML = '<a> x' + data.products[row].nmb + ' </a>';
                mycurrent_row.appendChild(quantity_cell);
                //Cell subtotal
                var subtotal_cell = document.createElement("td");
                subtotal_cell.style.cssText = "width:20%";
                subtotal_cell.className = "miniCartSubtotal";
                subtotal_cell.innerHTML = '<span> ' + data.products[row].total + 'UAH </span>';
                mycurrent_row.appendChild(subtotal_cell);
                Table.appendChild(mycurrent_row);
            }
        }
    }

    $(document).on('click', '.btn-cart', function (e) {
        var form = $('#form_buying_product');
        form.on('submit', function (e) {
            e.preventDefault();
            console.log('From item page');
            var nmb = $('#number').val();
            console.log(nmb);
            var submit_btn = $('#submit_btn');
            var product_id = submit_btn.data("product_id");
            var product_name = submit_btn.data("name");
            console.log(product_id);
            console.log(product_name);

            var data = {};
            data.product_id = product_id;
            data.nmb = nmb;
            var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
            console.log(data);
            var url = form.attr("action");
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    updateCart(data);
                },
                error: function () {
                    console.log("error")
                }
            })

        })
    })


    $('.cartMenu').mouseover(function () {
        $('.dropdown-menu-cart').removeClass('hidden');
    })

    function updateTotalAmount(){
        var total_order_amount = 0;
        $('.total-price').each(function () {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log(total_order_amount);
        $('#total-price').text(total_order_amount.toFixed(2));
    };

    $(document).on('change', ".quanitySniper", function () {
        var current_qty = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.price-per-item').text().split("UAH")[0]).toFixed(2);
        var total_price = parseFloat(current_qty * current_price).toFixed(2);
        current_tr.find('.total-price').text(total_price);
        // updateTotalAmount();
    });

    $(document).on('click', "#updateCart", function (e) {
        e.preventDefault();
        updateTotalAmount();
    })

    $(document).on('click', '.add2cart', function (e) {
        var product_id = $(this).data("product_id");
        console.log('From main page');
        var nmb = "1";
        var data1 = {};
        data1.product_id = product_id;
        data1.nmb = nmb;
        var csrf_token = $('#form_add2cart [name="csrfmiddlewaretoken"]').val();
        data1["csrfmiddlewaretoken"] = csrf_token;
        console.log(data1);
        var form1 = $('#form_add2cart');
        var url = form1.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data1,
            cache: true,
            success: function (data1) {
                updateCart(data1);
            },
            error: function () {
                console.log("error")
            }
        })
    })
        $(document).on('click', '#btn-login', function (e) {
            console.log('Вход в личный кабинет');
        })

    function make_input_field() {
        var table = document.getElementById("cart_Table");
        if (table!=null){
            var rowCount = table.rows.length;
            var data = document.getElementsByClassName("quanitySniper");
            for (i=0; i<data.length; i++){
                var name = data[i].getAttribute('name');
                $("input[name='"+name+"']").TouchSpin({
                    min: 0,
                    max: 100,
                    buttondown_class: "btn btn-link",
                    buttonup_class: "btn btn-link"
                });
            }
        }
    }

    /*==================================
     Delete item in cart
     ====================================*/
    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        $(this).closest('tr').hide();
        $(this).closest('tr').find('.quanitySniper').val(0);
        document.getElementById("form_update").submit();
        console.log('Form update');
    });

    /*==================================
     Custom Scrollbar for Dropdown Cart
     ====================================*/
    $(".scroll-pane").mCustomScrollbar({
        advanced: {
            updateOnContentResize: true
        },
        scrollButtons: {
            enable: false
        },
        mouseWheelPixels: "200",
        theme: "dark-2"
    });

    $(".smoothscroll").mCustomScrollbar({
        advanced: {
            updateOnContentResize: true
        },
        scrollButtons: {
            enable: false
        },
        mouseWheelPixels: "100",
        theme: "dark-2"
    });

    /*=======================================================================================
     Code for equal height - // your div will never broken if text get overflow
     ========================================================================================*/


    function equalHeightDivs() {
        $('.subCategoryList > div').matchHeight({byRow: false})
        $('.featuredImgLook2 .inner').matchHeight({byRow: false})
        $('.featuredImageLook3 .inner').matchHeight({byRow: false})
    };
    equalHeightDivs();


    /* testing page code only, you wont need this! */

    productContainer.each(function () {
        $(this).children('.item').matchHeight({
            byRaw: true
        });
    });


    var equalHeightUpdate = function () {
        // equal height reload function

        productContainer.each(function () {
            $(this).children('.item').matchHeight({
                remove: true
            });
        });

        setTimeout(function () {
                //  reload function after 0.5 second
                productContainer.each(function () {
                    $(this).children('.item').matchHeight({
                        byRaw: true
                    });
                });
            }
            , 500);
        // update all heights
        $.fn.matchHeight._update();
    };


    window.addEventListener("orientationchange", function () {
        // ipad, tab orientation
        equalHeightUpdate();
    }, false);


    if (!isMobile()) {
        // avoid touch event issue on resize
        $(window).resize(function () {
            equalHeightUpdate();
            console.log('resized')
        });
    }

    //if you need to call it at page load to resize elements etc.

    (function () {
        /* matchHeight category baguette  */
        $(function () {
            // apply matchHeight to each item container's items
            $('.equalheightItem').each(function () {
                $(this).children('.item').matchHeight({
                    byRow: true
                });
            });

        });

    })();

     // NEW ARRIVALS Carousel

    function customPager() {

        $.each(this.owl.userItems, function (i) {
            var pagination1 = $('.owl-controls .owl-pagination > div:first-child');
            var pagination = $('.owl-controls .owl-pagination');
            $(pagination[i]).append("<div class=' owl-has-nav owl-next'><i class='fa fa-angle-right'></i>  </div>");
            $(pagination1[i]).before("<div class=' owl-has-nav owl-prev'><i class='fa fa-angle-left'></i> </div>");
        });

    }

    // top navbar IE & Mobile Device fix
    if (isMobile()) {
        // For  mobile , ipad, tab
        $('.introContent').addClass('ismobile');
    } else {
        $(function () {
            //Keep track of last scroll
            var tshopScroll = 0;
            $(window).scroll(function (event) {
                //Sets the current scroll position
                var ts = $(this).scrollTop();
                //Determines up-or-down scrolling
                if (ts > tshopScroll) {
                    // downward-scrolling
                    $('.navbar').addClass('stuck');
                } else {
                    // upward-scrolling
                    $('.navbar').removeClass('stuck');
                }
                if (ts < 600) {
                    // downward-scrolling
                    $('.navbar').removeClass('stuck');
                    //alert()
                }
                tshopScroll = ts;
                //Updates scroll position
            });
        });
    } // end Desktop else

    //active navbar for current page
    $(function(){
        $('.nav li a').each(function(){
            if ($(this).prop('href') == window.location.href) {
                $(this).parents('li').addClass('active');
            }
        });
    });
})