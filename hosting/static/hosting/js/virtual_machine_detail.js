function changeButtonState(state) {
    var btnConfirmCancel = $("#btn-confirm-cancel");
    if (state) {
        btnConfirmCancel.removeAttr('disabled');
        btnConfirmCancel.html(terminate_vm_text);
    } else {
        btnConfirmCancel.attr('disabled', 'disabled');
        btnConfirmCancel.html(terminating_vm_text + ' <i class="fa fa-cog fa-spin fa-fw" aria-hidden="true"></i>');
    }
}

if (typeof vm_id !== 'undefined') {
    // variable is undefined or null or empty
    var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host + '/hosting/' + vm_id + '/';
    console.log("Connecting to " + ws_path);
    var socket = new WebSocket(ws_path);

    $(document).ready(function () {
        socket.onopen = function open() {
            console.log('WebSockets connection opened');
            var message = {
                action: "get_vm_state"
            };
            console.log('sending get_vm_state');
            socket.send(JSON.stringify(message));
            console.log('sent get_vm_state');
        };

        if (socket.readyState === WebSocket.OPEN) {
            socket.onopen();
        }

        socket.onmessage = function (message) {
            console.log("Got message: " + message.data);
            var data = JSON.parse(message.data);
            var btnConfirmCancel = $("#btn-confirm-cancel");
            // if action is started, add new item to table
            if (data.state === "none") {
                if (btnConfirmCancel.prop('disabled')) {
                    changeButtonState(true);
                }
            }
            // if action is completed, just update the status
            else if (data.action === "TERMINATE_VM") {
                if (data.result === "SUCCESS") {
                    window.location.replace(home_url);
                } else if (data.result === "FAILURE") {
                    alert("Could not delete VM. Please contact support.");
                    if (btnConfirmCancel.prop('disabled')) {
                        changeButtonState(true);
                    }
                } else {
                    if (!btnConfirmCancel.prop('disabled')) {
                        changeButtonState(false);
                    }
                }
            }
        }
    });


    $('#confirm-cancel').on('click', '.btn-ok', function (e) {
        //$('#virtual_machine_cancel_form').trigger('submit');
        changeButtonState(false);
        $('#confirm-cancel').modal('hide');
        var message = {
            action: "terminate_vm"
        };
        console.log('sending terminate_vm');
        if (socket !== null)
            socket.send(JSON.stringify(message));
        console.log('sent terminate_vm');

    });
}


var hash = window.location.hash;
hash && $('ul.nav a[href="' + hash + '"]').tab('show');

$('.nav-tabs a').click(function (e) {
    $(this).tab('show');
    var scrollmem = $('body').scrollTop() || $('html').scrollTop();
    window.location.hash = this.hash;
    $('html,body').scrollTop(scrollmem);
});