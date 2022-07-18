$(document).ready(function () {
    // Подключение автодополнения по городу
    $('#city').autocomplete({
        source: '/search',
        minLength: 3,
        select: function (event, ui) {
            console.log('select');
            $("#city").val(ui.item.DescriptionRu);
            $("#city_ref").val(ui.item.Ref);
            // document.getElementById("form-search").submit();
            var data = {};
            data['ref'] = ui.item.Ref;
            data['city'] = ui.item.DescriptionRu;
            console.log(data);
            var url = "/search_wh";
            $.ajax({
                url: url,
                type: 'GET',
                data: data,
                cache: true,
                success: function (data) {
                    console.log('success');
                    console.log(data);
                    var select = document.getElementById('wh');
                    var wh = data.warehouse;
                    for (var i=0; i<wh.length; i++){
                        var opt_wh = document.createElement('option');
                        opt_wh.value = wh[i].DescriptionRu_wh;
                        opt_wh.innerHTML = wh[i].DescriptionRu_wh;
                        opt_wh.dataset.ref = wh[i].Ref_wh;
                        select.appendChild(opt_wh);
                    }
                },
                error: function () {
                    console.log("error")
                }
            });
            return false;
        }
    })

    .autocomplete( "instance" )._renderItem = function( ul, item ) {
        console.log('autocomplete');
        return $( "<li>" )
        .append( "<div>" + item.DescriptionRu + "</div>" )
        .appendTo( ul );
    };

    //Panel
    $(window).bind('resize load', function () {
        console.log('Resize');
        if ($(this).width() < 767) {
            $('#accordion.panel-group .panel-collapse').collapse('hide');
            $('#accordion.panel-group .panel-heading ').find('span').removeClass('hasMinus').addClass('hasPlus');
        } else {
            $('#accordion.panel-group .panel-collapse').removeClass('out').addClass('in').css('height', 'auto');
            $('#accordion.panel-group .panel-heading ').find('span').removeClass('hasPlus').addClass('hasMinus');
        }
    });

    $('[data-toggle="collapse"]').click(function (e) {
        console.log('Collapse click');
        $('#accordion.panel-group').on('show.bs.collapse', function (e) {
            console.log('show');
            $(e.target).prev().addClass('active').find('span').removeClass('hasPlus').addClass('hasMinus');
        })
        $('#accordion.panel-group').on('hide.bs.collapse', function (e) {
            console.log('hide');
            $(e.target).prev().addClass('active').find('span').addClass('hasPlus').removeClass('hasMinus');
        })
    });

    $('#creditCard').change(function () {
        if ($(this).is(':checked')) {
            $("#creditCardCollapse").addClass('in')
        } else {
            $("#creditCardCollapse").removeClass('in')
        }
    });


    // For stylish input check box
    $('input').iCheck({
        // checkboxClass: 'icheckbox_minimal-green',
        // radioClass: 'iradio_minimal-green'

        checkboxClass: 'icheckbox_square-green iCheck-margin',
        radioClass: 'iradio_square-green iChk iCheck-margin'
    });

    var year_now = new Date().getFullYear(),
        select = document.getElementById('year');
    for (var i=0; i<10; i++){
        var opt_year = document.createElement('option');
        opt_year.value = year_now + i;
        opt_year.innerHTML = year_now + i;
        select.appendChild(opt_year);
    }

    document.getElementById('CardNumber').addEventListener('input', function (e) {
        e.target.value = e.target.value.replace(/[^\dA-Z]/g, '').replace(/(.{4})/g, '$1 ').trim();
    });

})