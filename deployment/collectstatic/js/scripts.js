/*!
* Start Bootstrap - Clean Blog v6.0.4 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})
function getUsers(response) {
    var Json = JSON.parse(response)
    textlist = ""
    for (var i = 0; i < Json.length; i++) {
        textlist += "<input type='radio'  name='user' id=" + Json[i].pk + ">" + Json[i].fields['firstname'] + "<br>"
    }
    $('#firstname').val("firstname")
    $('#lastname').val("lastname")
    $('#email').val("email")
    $('#service').val("service")
    $('#telephone').val("telephone")
    $('appointmentdate').val("appointmentdate")
    if (textlist == "")
        $("#userlist").html("No users available, add one below please")
    else
        $("#userlist").html(textlist)

}

$("#userlist").ready(function() {
    $.ajax({
        url: 'users/',
        type: 'GET',
        success: getUsers,
    });
});

$("#details").click(function(e) {
    var id = $("input[name=user]:checked").attr('id');
    $.ajax({
        type: "GET",
        url: 'users/',
        dataType: 'json',
        success: function(response) {
            var Json = JSON.parse(response)
            for (var i = Json.length - 1; i >= 0; i--) {
                if (id == Json[i].pk) {
                    $('#firstname').val(Json[i].fields['firstname'])
                    $('#lastname').val(Json[i].fields['lastname'])
                    $('#email').val(Json[i].fields['email'])
                    $('#service').val(Json[i].fields['service'])
                    $('#telephone').val(Json[i].fields['telephone'])
                    $('#appointmentdate').val(Json[i].fields['appointmentdate'])
                    break;
                }
            }
        },
    });

});


$("#add").click(function(e) {
    var firstname = $('input[name=firstname]').val()
    var lastname = $("input[name=lastname]").val()
    var email = $("input[name=email]").val()
    var service = $("input[name=service]").val()
    var telephone = $("input[name=telephone]").val()
    var appointmentdate = $("input[name=appointmentdate]").val()
    $.ajax({
        type: "POST",
        url: '/useradded/',
        dataType: 'json',
        data: JSON.stringify({
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'service': service,
            'telephone': telephone,
            'appointmentdate': appointmentdate,
        }),
        success: getUsers
    });
});



$("#delete").click(function(e) {
    var id = $("input[name=user]:checked").attr('id');
    $.ajax({
        type: 'DELETE',
        url: '/userremoved/',
        dataType: 'json',
        data: JSON.stringify({
            'pk': id
        }),
        success: getUsers
    });

});

$("#update").click(function() {
    var id = $("input[name=user]:checked").attr('id');
    var firstname = $('input[name=firstname]').val()
    var lastname = $("input[name=lastname]").val()
    var email = $("input[name=email]").val()
    var service = $("input[name=service]").val()
    var telephone = $("input[name=telephone]").val()
    var appointmentdate = $("input[name=appointmentdate]").val()
    $.ajax({
        url: 'productupdated/',
        type: 'PUT',
        dataType: 'json',
        data: JSON.stringify({
            'pk': id,
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'service': service,
            'telephone': telephone,
            'appointmentdate': Appointment_date,
        }),
        success: getUsers,
    });

});