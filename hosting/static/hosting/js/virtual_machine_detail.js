function VMTerminateStatus($container, url) {
    $.get(url)
        .done(function(data) {
            setTimeout(function(){
                VMTerminateStatus($container, url);
            }, 4000);
        })
        .fail(function(data) {
            VMTerminateSuccess($container, data)
            window.location.reload(true);
        });
}

function VMTerminateActive($container, altText) {
    $container.find('.alert-danger').addClass('hide');
    $container.addClass('processing')
        .find('.vm-item-lg').attr('class', '')
        .addClass('vm-item-lg vm-color-failed')
        .text(altText);
    $container.find('.btn').prop('disabled', true);
    $('#confirm-cancel').modal('hide');
}

function VMTerminateSuccess($container, data) {
    $container.addClass('terminate-success')
        .find('.vm-item-lg').text(data.text);
    $container.find('.btn').remove();
}

function VMTerminateFail($container, data, text) {
    $container.addClass('terminate-fail')
        .find('.vm-item-lg').text(text);
    $container.find('.btn').prop('disabled', false);
    $container.find('.alert-danger').text(data.text).removeClass('hide');
    $container.removeClass('processing');
}


$(document).ready(function() {

    $('#confirm-cancel').on('click', '.btn-ok', function(e) {
        var url = $('#virtual_machine_cancel_form').attr('action');
        var $container = $('#terminate-VM');
        var text = $container.find('.vm-item-lg').text();
        var altText = $container.attr('data-alt');
        VMTerminateActive($container, altText);

        $.post(url)
            .done(function(data) {
                console.log("success", data);
                if (data.status == true) {
                    VMTerminateSuccess($container, data);
                    window.location = data.redirect;
                } else {
                    if ('text' in data) {
                        VMTerminateFail($container, data, text);
                    } else {
                        VMTerminateStatus($container, url);
                    }
                }
            })
            .fail(function(data) {
                console.log(data)
                if (data.status==504) {
                    VMTerminateStatus($container, url);
                } else {
                    VMTerminateFail($container, data, text);
                }
            })
    });

    var hash = window.location.hash;
    hash && $('ul.nav a[href="' + hash + '"]').tab('show');

    $('.nav-tabs a').click(function(e) {
        $(this).tab('show');
        var scrollmem = $('body').scrollTop() || $('html').scrollTop();
        window.location.hash = this.hash;
        $('html,body').scrollTop(scrollmem);
    });

});