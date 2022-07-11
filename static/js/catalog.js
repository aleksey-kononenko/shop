$(document).ready(function () {
    $("input[type=checkbox]").change(function () {
        console.log('chekbox');
        filter();
    });

    $(document).on('click', '.clearFilter', function () {
        console.log('Очистить')
        var min_price = $('#min_price').data('min_price');
        var max_price = $('#max_price').data('max_price');
        $('#min_price').val(min_price);
        $('#max_price').val(max_price);
        filter();
        console.log(min_price);
        console.log(max_price);
    });

    $(document).on('click', '#submit-range', function (e) {
        var form = $('#price-range');
        form.on('submit', function (e) {
            e.preventDefault();
            console.log('set range');
            filter();
        });
    });

    function filter() {
        var data = {};
        var types = [];
        var categories = [];
        var is_discount = 0;
        var is_new = 0;
        $(".panel-group").find("input:checked").each(function () {
            var id = $(this).data('id');
            switch ($(this).attr('name')) {
                case 'type':
                    types.push(id);
                    break
                case 'category':
                    categories.push(id);
                    break
                case 'promo':
                    if (id == 1){ is_discount = 1};
                    if (id == 2){ is_new = 1};
                    break
            }
        })
        var min_price = $("#min_price").val();
        var max_price = $("#max_price").val();
        data['types'] = types;
        data['categories'] = categories;
        data['is_discount'] = is_discount;
        data['is_new'] = is_new;
        data['min_price'] = min_price;
        data['max_price'] = max_price;
        console.log(data);
        var url = "/shop_filter";
        $.ajax({
            url: url,
            type: 'GET',
            data: data,
            cache: true,
            success: function (data) {
                // console.log(data);
                var template = document.getElementById("template-product");
                // Get the contents of the template
                var templateHtml = template.innerHTML;
                // Final HTML variable as empty string
                var listHtml = "";
                var origin   = window.location.origin;
                for (var item = 0; item < data.catalog_total_nmb; item++) {
                    var description = truncateString(data.catalog[item].description, 120);
                    var prodHtml = "";
                    prodHtml = templateHtml.replace(new RegExp('{{url}}', 'g'), origin+'/item/'+data.catalog[item].id)
                                           .replace(new RegExp('{{url_img}}', 'g'), origin+data.catalog[item].img)
                                           .replace(new RegExp('{{name}}', 'g'), data.catalog[item].name)
                                           .replace(new RegExp('{{description}}', 'g'), description)
                                           .replace(new RegExp('{{price}}', 'g'), data.catalog[item].price)
                                           .replace(new RegExp('{{id}}', 'g'), data.catalog[item].id);
                    if (data.catalog[item].is_new) {
                        prodHtml = prodHtml.replace(new RegExp('{{new}}', 'g'), '<span class="new-product">NEW</span>');
                    } else {
                        prodHtml = prodHtml.replace(new RegExp('{{new}}', 'g'), '')
                    }
                    if (data.catalog[item].discount) {
                        prodHtml = prodHtml.replace(new RegExp('{{discount}}', 'g'), '<div class="discount"><span>'+data.catalog[item].discount+'%</span></div>');
                    } else {
                        prodHtml = prodHtml.replace(new RegExp('{{discount}}', 'g'), '')
                    }
                    listHtml += prodHtml;
                }

                $('#c_nmb').text(data.catalog_total_nmb);
                document.getElementsByClassName("categoryProduct")[0].innerHTML = listHtml;
                // console.log(cat_div);
            },
            error: function () {
                console.log("error")
            }
        })
    }

    function truncateString(str, num) {
        if (str.length > num) {
                return str.slice(0, num-1) + "...";
            } else {
                return str;
        }
    }


    //For stylish input check box
    $('input').iCheck({
        // checkboxClass: 'icheckbox_minimal-green',
        // radioClass: 'iradio_minimal-green'

        checkboxClass: 'icheckbox_square-green iCheck-margin',
        radioClass: 'iradio_square-green iChk iCheck-margin'
    });

    $(window).bind('resize load', function () {
        if ($(this).width() < 767) {
            $("#accordionNo .panel-collapse:not(#collapseCategory)").collapse('hide');
        }
    }); // end resize load

    $("#accordionNo .panel-collapse").each(function () {
        $(this).on('hidden.bs.collapse', function () {
            // do something…
            $(this).parent().find('.collapseWill').removeClass('active').addClass('hasPlus');
        });
        $(this).on('show.bs.collapse', function () {
            // do something…
            $(this).parent().find('.collapseWill').removeClass('hasPlus').addClass('active');
        });
    });
})


