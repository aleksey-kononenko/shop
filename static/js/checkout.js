$(document).ready(function () {
    // Подключение автодополнения по городу
    $('#city').autocomplete({
        source: '/search',
        minLength: 2,
        select: function (event, ui) {
            console.log('select');
            $("#city").val(ui.item.DescriptionRu);
            $("#city_ref").val(ui.item.Ref);
            document.getElementById("form-search").submit();
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

    // For stylish input check box
    $('input').iCheck({
        // checkboxClass: 'icheckbox_minimal-green',
        // radioClass: 'iradio_minimal-green'

        checkboxClass: 'icheckbox_square-green iCheck-margin',
        radioClass: 'iradio_square-green iChk iCheck-margin'
    });

})