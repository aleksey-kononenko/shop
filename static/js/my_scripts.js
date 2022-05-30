$(document).ready(function () {

    make_input_field();

    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
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
        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK")
                console.log(data.products_total_nmb)
                console.log(data.order_total_price)
                if (data.products_total_nmb) {
                    $('#cart_total_nmb').text('Корзина ('+data.products_total_nmb+')');
                    $('#cart_subtotal').text('Subtotal: '+data.order_total_price+' UAH');
                    console.log(data.products)
                    var Table = document.getElementById("mCSB_tbody");
                    Table.innerHTML = "";

                    for(var row = 0; row < data.products_total_nmb; row++) {
                        var mycurrent_row = document.createElement("tr");
                        mycurrent_row.className = "miniCartProduct";
                        var description_cell = document.createElement("td");
                        description_cell.style.cssText="width:60%";
                        var description_div = document.createElement('div');
                        description_div.className = "mCPDescription";
                        var description_h5 = document.createElement("h5")
                        var description_a = document.createElement("a")
                        description_a.setAttribute('href', '/item/'+data.products[row].id )
                        description_a.textContent = data.products[row].name;
                        description_h5.appendChild(description_a)
                        var price_div = document.createElement('div');
                        price_div.className = "price";
                        price_div.innerHTML = '<span>'+data.products[row].price+'UAH </span>';
                        description_div.appendChild(description_h5);
                        description_div.appendChild(price_div);
                        description_cell.appendChild(description_div);
                        mycurrent_row.appendChild(description_cell);
                        var quantity_cell = document.createElement("td");
                        quantity_cell.style.cssText="width:20%";
                        quantity_cell.className="mCPQuantity";
                        quantity_cell.innerHTML='<a> X '+data.products[row].nmb+'</a>';
                        mycurrent_row.appendChild(quantity_cell);
                        var subtotal_cell = document.createElement("td");
                        subtotal_cell.style.cssText="width:20%";
                        subtotal_cell.className="mCPSubtotal";
                        subtotal_cell.innerHTML='<span>'+data.products[row].total+'UAH </span>';
                        mycurrent_row.appendChild(subtotal_cell);
                        Table.appendChild(mycurrent_row);
                    }
                }
            },
            error: function () {
                console.log("error")
            }
        })

    })
    // var form_cart = $('#form_cart');
    // console.log(form_cart);
    // form_cart.on('submit', function (e) {
    //     e.preventDefault();
    //     console.log(product_id);
    // })
    // $('.cartMenu').on('click',function () {
    //     $('.dropdown-menu-cart').removeClass('hidden');
    // })
    $('.cartMenu').mouseover(function () {
        $('.dropdown-menu-cart').removeClass('hidden');
    })

    $(document).on('click', '.delete', function (e) {
        e.preventDefault();
        $(this).closest('tr').remove();
        
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



    // $(document).on('click', '.update', function (e) {
    //     e.preventDefault();
    //     console.log("Увеличение количества")
    //     var id = $(this).closest().find('.quanitySniper').data('product_id');
    //     console.log(id);
    // })

    // $('.cartMenu').mouseout(function () {
    //     $('.dropdown-menu-cart').addClass('hidden');
    // })

    // $(document).on('click', '.mCPDelete', function (e) {
    //     e.preventDefault();
    //     $(this).closest('tr').remove();
    // })
})