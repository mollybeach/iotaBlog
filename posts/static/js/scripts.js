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
/**************GET USERS****************/
function getUsers(response) {
    let Json = JSON.parse(response)
    textlist = ""
    for (let i = 0; i < Json.length; i++) {
        textlist += "<input type='radio'  name='user' id=" + Json[i].pk + ">" + Json[i].fields['firstname'] + " " + Json[i].fields['lastname'] + "<br>"
    }
    $('#firstname').val("firstname")
    $('#lastname').val("lastname")
    $('#email').val("email")
    $('#service').val("service")
    $('telephone').val("telephone")
    $('#appointmentdate').val("appointmentdate")
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
/**************ADD****************/
$("#add").click(function(e) {
    let firstname = $('input[name=firstname]').val()
    let lastname = $("input[name=lastname]").val()
    let email = $("input[name=email]").val()
    let service = $("input[name=service]").val()
    let telephone = $("input[name=telephone]").val()
    let appointmentdate = $("input[name=appointmentdate]").val()
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
            'appointmentdate': appointmentdate
        }),
        success: getUsers
    });
});
/**************DETAILS****************/
$("#details").click(function(e) {
    let id = $("input[name=user]:checked").attr('id');
    $.ajax({
        type: "GET",
        url: 'users/',
        dataType: 'json',
        success: function(response) {
            let Json = JSON.parse(response)
            for (let i = Json.length - 1; i >= 0; i--) {
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

/**************DELETE****************/
$("#delete").click(function(e) {
    let id = $("input[name=user]:checked").attr('id');
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
/**************UPDATE****************/    
$("#update").click(function() {
    let id = $("input[name=user]:checked").attr('id');
    let firstname = $('input[name=firstname]').val()
    let lastname = $("input[name=lastname]").val()
    let email = $("input[name=email]").val()
    let service = $("input[name=service]").val()
    let telephone = $("input[name=telephone]").val()
    let appointmentdate = $("input[name=appointmentdate]").val()

    $.ajax({
        url: 'userupdated/',
        type: 'PUT',
        dataType: 'json',
        data: JSON.stringify({
            'pk': id,
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'service': service,
            'telephone': telephone,
            'appointmentdate': appointmentdate
        }),
        success: getUsers,
    });

});
