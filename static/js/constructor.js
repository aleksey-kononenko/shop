$(document).ready(function () {
    const frame = document.getElementById("figure");
    const picture = $('#picture');
    const root = document.querySelector(':root');
    $(window).bind('resize load', function () {
        update_frame();
    }); // end resize load

    $(document).on('click', '.product', function (e) {
        var name = $(this).data('name');
        var width_fr = $(this).data('width');
        $('.corner').each(function () {
            var corner = document.createElement("img");
            corner.src = '/media/catalog/'+name+'/c.png';
            $(this).children('img').replaceWith(corner);
        });
        $('.side').each(function () {
            var side = document.createElement("img");
            side.src = '/media/catalog/'+name+'/h.png';
            $(this).empty();
            $(this).append(side);
        });
        $('#figure').data('baguette_width', width_fr);
        setTimeout( function(){
            update_frame();
        }, 100);
    });

    function update_frame () {
        // var frame_width = parseInt($('#width').val());
        // var frame_height = parseInt($('#height').val());
        // var frame_border = $('#figure').data('baguette_width');

        // var k = width/(2*frame_border+frame_width);
        // var size = frame_border * k + 'px';
        // console.log(size);
        // const root = document.querySelector(':root');
        // root.style.setProperty('--frame_width', size);
        // root.style.setProperty('--overal_scale', k);
        var k = calcScale();
        var width = parseInt(getComputedStyle(root).getPropertyValue('--figure_width'));  //Ширина элемента окна
        var height = parseInt(getComputedStyle(root).getPropertyValue('--figure_height'));  //Высота элемента окна
        // frame.style.height = height +'px';
        var side = frame.getElementsByClassName('side');
        var img_top = side[0].children;
        // console.log(img_top[0].clientWidth);
        var img_left = side[3].children;
        var img_width = img_top[0].clientWidth;
        var top_num = width/img_width;
        var left_num = height/img_width;
        url = img_top[0].src;
        // console.log(img_width);
        if (img_width > 0) {
            for (var i = img_top.length; i <= top_num; i++) {
                var top_img = document.createElement("img");
                top_img.src = url;
                var bottom_img = document.createElement("img");
                bottom_img.src = url;
                side[0].appendChild(top_img);
                side[2].appendChild(bottom_img);
            }
            for (var i = img_left.length; i <= left_num; i++) {
                var left_img = document.createElement("img");
                left_img.src = url;
                var right_img = document.createElement("img");
                right_img.src = url;
                side[1].appendChild(left_img);
                side[3].appendChild(right_img);
            }
        }
    }

    $('#constructor').on('change', '.empty_frame input[type="file"]', function (){
        // console.log('loadImg')
        if(this.files[0].size > 20000000){
            $(this).val('');
            alert('Максимальний розмір файлу - 20 МБ')
        } else {
            let img = picture.find('img');
            readURL(this, img);

            $('.empty_frame').css('display', 'none');
            $('figure').removeClass('empty');
            //
            // update_frame()
        }
    });

    $('#filterFrame').on('change', 'input[type="number"]', function (){
        update_frame();
        update_paspartu();
    });

    // Image upload
    function readURL(input, img){
        if(input.files && input.files[0]){
            var reader = new FileReader();
            reader.onload = function (e){
                img.attr('src', e.target.result).show()
            }
            reader.readAsDataURL(input.files[0]);
        }
    };

    $('#single_p').on('click', '.paspartu_list img', function () {
        if ($(this).hasClass('active')){
             $(this).removeClass('active');
             $('#paspartu').removeAttr('style');
             $('#dpaspartu_tab').addClass('hidden');
             $('#d_paspartu_list').children('img').removeClass('active');
             $('#dpaspartu').removeAttr('style');
             $('#paspartu_type').data('paspartu', "remove");
        } else {
            $(this).addClass('active').siblings('img').removeClass('active');
            // console.log($(this).attr('src'));
            let paspartu_bg = $(this).attr('src');
            // let paspartu_width = parseInt($('#p1_width').val());
            // const root = document.querySelector(':root');
            // let k = root.style.getPropertyValue('--overal_scale');
            // let width = paspartu_width*k + 'px';
            $('#paspartu').css('background', 'url(' + paspartu_bg + ')');
            $('#dpaspartu_tab').removeClass('hidden');
            let type_paspartu = $('#paspartu_type').data('paspartu');
            if (type_paspartu === 'remove'){
                $('#paspartu_type').data('paspartu', "one");
            }
        };
        update_paspartu();
        update_frame();
    });

    $('#double_p').on('click', '.paspartu_list img', function () {
        if ($(this).hasClass('active')){
             $(this).removeClass('active');
             $('#dpaspartu').removeAttr('style');
             $('#paspartu_type').data('paspartu', "one");
        } else {
            $(this).addClass('active').siblings('img').removeClass('active');
            let paspartu_bg = $(this).attr('src');
            // let paspartu_width = parseInt($('#p2_width').val());
            // const root = document.querySelector(':root');
            // let k = root.style.getPropertyValue('--overal_scale');
            // let width = paspartu_width*k + 'px';
            $('#dpaspartu').css('background', 'url(' + paspartu_bg + ')');
            let type_paspartu = $('#paspartu_type').data('paspartu');
            if (type_paspartu === 'one'){
                $('#paspartu_type').data('paspartu', "double");
            }
        };
        update_paspartu();
        update_frame();
    });

    function update_paspartu() {
        var k = calcScale();
        let type_paspartu = $('#paspartu_type').data('paspartu');
        if (type_paspartu === 'one'){
            p1_width = parseInt($('#p1_width').val());
        }if (type_paspartu === 'double'){
            p1_width = parseInt($('#p1_width').val());
            p2_width = parseInt($('#p2_width').val());
        }
    };

    function calcScale() {
        var frame_width = parseInt($('#width').val());
        var frame_height = parseInt($('#height').val());
        var frame_border = $('#figure').data('baguette_width');
        let type_paspartu = $('#paspartu_type').data('paspartu');
        var p1_width = 0;
        var p2_width = 0;
        if (type_paspartu === 'one'){
            p1_width = parseInt($('#p1_width').val());
        }if (type_paspartu === 'double'){
            p1_width = parseInt($('#p1_width').val());
            p2_width = parseInt($('#p2_width').val());
        }
        var width = frame.clientWidth;  //Ширина элемента окна
        var k = width/(2*frame_border+frame_width+2*p1_width+2*p2_width);
        var height = (frame_height+2*frame_border+2*p1_width+2*p2_width)*k;   //Высота элемента окна
        var size = frame_border * k + 'px';
        var p1_size = p1_width*k + 'px';
        var p2_size = p2_width*k + 'px';
        root.style.setProperty('--frame_width', size);
        root.style.setProperty('--figure_width', width+'px');
        root.style.setProperty('--figure_height', height+'px');
        root.style.setProperty('--spaspartu_width', p1_size);
        root.style.setProperty('--dpaspartu_width', p2_size);
        return k;
    };

    //For stylish input check box
    $('input').iCheck({
        // checkboxClass: 'icheckbox_minimal-green',
        // radioClass: 'iradio_minimal-green'

        checkboxClass: 'icheckbox_square-green iCheck-margin',
        radioClass: 'iradio_square-green iChk iCheck-margin'
    });

    $("input[type=checkbox]").change(function () {
        filter();
    });

    $("input[type=radio]").change(function () {
        if ($(this).is(':checked')){
            filter();
        }
    });

    function filter() {
        var data = {};
        var colors = [];
        var materials = [];
        var width = '0';
        $(".panel-group").find("input:checked").each(function () {
            var id = $(this).data('id');
            switch ($(this).attr('name')) {
                case 'material':
                    materials.push(id);
                    break
                case 'color':
                    colors.push(id);
                    break
                case 'width':
                    width = $(this).val();
                    break
            }
        })
        var page = $('.pagination').find('ul li.active').text();
        console.log('Current page');
        console.log(page);
        data['colors'] = colors;
        data['materials'] = materials;
        data['range_width'] = width;
        data['current_page'] = page;
        console.log(data);
        var url = "/constructor_filter";
        $.ajax({
            url: url,
            type: 'GET',
            data: data,
            cache: true,
            success: function (data) {
                console.log(data);
                var c_page = data.current_page;
                var template = document.getElementById("template-baguette");
                // Get the contents of the template
                var templateHtml = template.innerHTML;
                // Final HTML variable as empty string
                var listHtml = "";
                var origin   = window.location.origin;
                for (var item = 0; item < data.baguette.length; item++) {
                    var prodHtml = "";
                    prodHtml = templateHtml.replace(new RegExp('{{url}}', 'g'), origin+'/media/catalog/'+data.baguette[item].name+'/img-1000x1000.png')
                                           .replace(new RegExp('{{name}}', 'g'), data.baguette[item].name)
                                           .replace(new RegExp('{{width}}', 'g'), data.baguette[item].width)
                                           .replace(new RegExp('{{price}}', 'g'), data.baguette[item].price);
                    listHtml += prodHtml;
                }
                document.getElementsByClassName("category-top")[0].innerHTML = listHtml;
                var footerHtml = "";
                footerHtml += '<li><a href="#">«</a></li>';
                for (var i = 0; i < data.page_total_nmb.length; i++) {
                    if (data.page_total_nmb[i] == data.current_page){
                        footerHtml += '<li class="active"><a href="#">'+data.page_total_nmb[i]+'</a></li>';
                    } else {
                        footerHtml += '<li><a href="#">'+data.page_total_nmb[i]+'</a></li>';
                    }
                }
                footerHtml += '<li><a href="#">»</a></li>';
                document.getElementById("pagination").innerHTML = footerHtml;
            },
            error: function () {
                console.log("error")
            }
        })
    }

    $('.pagination').on('click', 'ul li', function () {
        if ($(this).text() != '...') {
            $(this).addClass('active').siblings('li').removeClass('active');
            filter();
        };
    })

    // document.body.onclick=e=>document.querySelector("#tag").textContent = 'Tag: '+e.target;
    // window.onclick = e => {
    //     console.dir(e.target);  // use this in chrome
    //     console.log(e.target);  // use this in firefox - click on tag name to view
    // }
})